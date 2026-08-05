"""httpx transports that add envelope unwrapping, retries and rate-limit handling.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

Everything here is installed *below* the generated code: the generated operation modules
keep calling ``client.get_httpx_client().request(...)`` and ``response.json()``, and the
transport makes sure what they see is the unwrapped, retried response. No file under
``notifly_py/api/`` or ``notifly_py/models/`` is touched, so regeneration stays lossless.
"""

from __future__ import annotations

import asyncio
import email.utils
import random
import time
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime

import httpx

from ._envelope import is_json_content_type, unwrap_body

DEFAULT_RETRY_STATUS_CODES: frozenset[int] = frozenset({408, 429, 502, 503, 504})
"""Statuses worth retrying.

``500`` is deliberately excluded: a deterministic server-side failure is not made better by
repeating it, and Notifly returns ``ErrorDto`` with a real message for those.
"""

IDEMPOTENT_METHODS: frozenset[str] = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
IDEMPOTENCY_HEADER = "idempotency-key"
_HOP_BY_HOP_ON_REWRITE = ("content-length", "content-encoding")


@dataclass(frozen=True)
class RetryConfig:
    """Retry policy for :class:`RetryTransport` / :class:`AsyncRetryTransport`.

    ``max_retries`` counts *additional* attempts, so the default of ``2`` means at most three
    requests in total. Non-idempotent methods (``POST``/``PATCH``) are only retried when the
    caller supplied an ``idempotency-key`` header — every Notifly operation accepts one.
    """

    max_retries: int = 2
    backoff_factor: float = 0.5
    max_backoff: float = 30.0
    respect_retry_after: bool = True
    max_retry_after: float = 60.0
    jitter: bool = True
    retry_status_codes: frozenset[int] = field(default=DEFAULT_RETRY_STATUS_CODES)
    retry_on_connection_errors: bool = True

    @property
    def enabled(self) -> bool:
        return self.max_retries > 0


def parse_retry_after(value: str | None, *, now: datetime | None = None) -> float | None:
    """Parse a ``Retry-After`` header value (delta-seconds or HTTP-date) into seconds."""
    if value is None:
        return None
    raw = value.strip()
    if not raw:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        pass
    try:
        parsed = email.utils.parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    reference = now or datetime.now(UTC)
    return max(0.0, (parsed - reference).total_seconds())


def _is_retryable_request(request: httpx.Request) -> bool:
    if request.method.upper() in IDEMPOTENT_METHODS:
        return True
    return IDEMPOTENCY_HEADER in request.headers


def _retry_delay(response: httpx.Response | None, attempt: int, config: RetryConfig) -> float:
    if response is not None and config.respect_retry_after:
        retry_after = parse_retry_after(response.headers.get("retry-after"))
        if retry_after is not None:
            return min(retry_after, config.max_retry_after)
    backoff = min(config.backoff_factor * (2**attempt), config.max_backoff)
    if config.jitter:
        backoff = random.uniform(backoff / 2, backoff)  # noqa: S311 - not security sensitive
    return backoff


def _rewrite_response(response: httpx.Response, content: bytes) -> httpx.Response:
    """Rebuild ``response`` with a new, already-decoded body.

    ``content-length`` and ``content-encoding`` are dropped: the body handed back is plain
    decoded bytes, so leaving the original values would make httpx try to gunzip it again.
    """
    headers = httpx.Headers(
        [(key, value) for key, value in response.headers.multi_items() if key.lower() not in _HOP_BY_HOP_ON_REWRITE]
    )
    return httpx.Response(
        status_code=response.status_code,
        headers=headers,
        content=content,
        extensions=response.extensions,
    )


class EnvelopeUnwrapTransport(httpx.BaseTransport):
    """Sync transport that strips the single-key ``{"data": ...}`` response envelope."""

    def __init__(self, transport: httpx.BaseTransport | None = None) -> None:
        self._transport = transport if transport is not None else httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        response = self._transport.handle_request(request)
        if not is_json_content_type(response.headers.get("content-type")):
            return response
        response.read()
        unwrapped = unwrap_body(response.content)
        return _rewrite_response(response, unwrapped if unwrapped is not None else response.content)

    def close(self) -> None:
        self._transport.close()


class AsyncEnvelopeUnwrapTransport(httpx.AsyncBaseTransport):
    """Async twin of :class:`EnvelopeUnwrapTransport`."""

    def __init__(self, transport: httpx.AsyncBaseTransport | None = None) -> None:
        self._transport = transport if transport is not None else httpx.AsyncHTTPTransport()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await self._transport.handle_async_request(request)
        if not is_json_content_type(response.headers.get("content-type")):
            return response
        await response.aread()
        unwrapped = unwrap_body(response.content)
        return _rewrite_response(response, unwrapped if unwrapped is not None else response.content)

    async def aclose(self) -> None:
        await self._transport.aclose()


class RetryTransport(httpx.BaseTransport):
    """Sync transport adding bounded retries with ``Retry-After`` support."""

    def __init__(
        self,
        transport: httpx.BaseTransport | None = None,
        config: RetryConfig | None = None,
        *,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._transport = transport if transport is not None else httpx.HTTPTransport()
        self._config = config or RetryConfig()
        self._sleep = sleep

    @property
    def config(self) -> RetryConfig:
        return self._config

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        config = self._config
        if not config.enabled or not _is_retryable_request(request):
            return self._transport.handle_request(request)

        request.read()  # materialize the body so it can be replayed
        last_error: Exception | None = None
        for attempt in range(config.max_retries + 1):
            response: httpx.Response | None = None
            try:
                response = self._transport.handle_request(request)
            except httpx.TransportError as exc:
                if not config.retry_on_connection_errors or attempt == config.max_retries:
                    raise
                last_error = exc
            else:
                if response.status_code not in config.retry_status_codes or attempt == config.max_retries:
                    return response
                response.read()
                response.close()
            self._sleep(_retry_delay(response, attempt, config))
        raise last_error or RuntimeError("retry loop exited without a response")  # pragma: no cover

    def close(self) -> None:
        self._transport.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async twin of :class:`RetryTransport`."""

    def __init__(
        self,
        transport: httpx.AsyncBaseTransport | None = None,
        config: RetryConfig | None = None,
        *,
        sleep: Callable[[float], object] | None = None,
    ) -> None:
        self._transport = transport if transport is not None else httpx.AsyncHTTPTransport()
        self._config = config or RetryConfig()
        self._sleep = sleep or asyncio.sleep

    @property
    def config(self) -> RetryConfig:
        return self._config

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        config = self._config
        if not config.enabled or not _is_retryable_request(request):
            return await self._transport.handle_async_request(request)

        await request.aread()
        last_error: Exception | None = None
        for attempt in range(config.max_retries + 1):
            response: httpx.Response | None = None
            try:
                response = await self._transport.handle_async_request(request)
            except httpx.TransportError as exc:
                if not config.retry_on_connection_errors or attempt == config.max_retries:
                    raise
                last_error = exc
            else:
                if response.status_code not in config.retry_status_codes or attempt == config.max_retries:
                    return response
                await response.aread()
                await response.aclose()
            await _maybe_await(self._sleep(_retry_delay(response, attempt, config)))
        raise last_error or RuntimeError("retry loop exited without a response")  # pragma: no cover

    async def aclose(self) -> None:
        await self._transport.aclose()


async def _maybe_await(value: object) -> None:
    if asyncio.iscoroutine(value):
        await value


def build_sync_transport(
    *,
    inner: httpx.BaseTransport | None = None,
    unwrap_data_envelope: bool = True,
    retry_config: RetryConfig | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> httpx.BaseTransport:
    """Compose the sync transport stack: retries **outside**, envelope unwrap **inside**."""
    transport: httpx.BaseTransport = inner if inner is not None else httpx.HTTPTransport()
    if unwrap_data_envelope:
        transport = EnvelopeUnwrapTransport(transport)
    config = retry_config or RetryConfig()
    if config.enabled:
        transport = RetryTransport(transport, config, sleep=sleep)
    return transport


def build_async_transport(
    *,
    inner: httpx.AsyncBaseTransport | None = None,
    unwrap_data_envelope: bool = True,
    retry_config: RetryConfig | None = None,
    sleep: Callable[[float], object] | None = None,
) -> httpx.AsyncBaseTransport:
    """Compose the async transport stack: retries **outside**, envelope unwrap **inside**."""
    transport: httpx.AsyncBaseTransport = inner if inner is not None else httpx.AsyncHTTPTransport()
    if unwrap_data_envelope:
        transport = AsyncEnvelopeUnwrapTransport(transport)
    config = retry_config or RetryConfig()
    if config.enabled:
        transport = AsyncRetryTransport(transport, config, sleep=sleep)
    return transport


def rate_limit_headers(headers: Iterable[tuple[str, str]] | httpx.Headers) -> dict[str, str]:
    """Extract ``RateLimit-*``/``Retry-After`` headers (case-insensitive) for diagnostics."""
    items = headers.multi_items() if isinstance(headers, httpx.Headers) else list(headers)
    return {key.lower(): value for key, value in items if key.lower().startswith("ratelimit") or key.lower() == "retry-after"}


__all__ = [
    "DEFAULT_RETRY_STATUS_CODES",
    "IDEMPOTENCY_HEADER",
    "IDEMPOTENT_METHODS",
    "AsyncEnvelopeUnwrapTransport",
    "AsyncRetryTransport",
    "EnvelopeUnwrapTransport",
    "RetryConfig",
    "RetryTransport",
    "build_async_transport",
    "build_sync_transport",
    "parse_retry_after",
    "rate_limit_headers",
]
