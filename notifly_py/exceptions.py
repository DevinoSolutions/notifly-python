"""Typed exceptions raised by the :class:`notifly_py.Notifly` facade.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

The Notifly API does **not** speak RFC 9457 ``application/problem+json``. Its error body is
``ErrorDto``::

    {"statusCode": 404, "timestamp": "...", "path": "/v2/subscribers/x",
     "message": "Subscriber not found", "ctx": {...}, "errorId": "..."}

``ValidationErrorDto`` adds ``errors``; ``PayloadValidationExceptionDto`` adds ``type`` and
``schema``. This module maps those onto a small Python hierarchy so callers can write
``except NotFoundError:`` instead of type-narrowing a fourteen-member union.

The raw generated functions (``notifly_py.api.*.sync`` / ``sync_detailed``) are untouched and
keep returning unions — they remain the escape hatch for anyone who prefers them.
"""

from __future__ import annotations

import json
from http import HTTPStatus
from typing import Any

from ._transport import parse_retry_after
from .types import UNSET, Response, Unset


class NotiflyError(Exception):
    """Base class for every error raised by this SDK."""


class NotiflyAPIError(NotiflyError):
    """An HTTP error response returned by the Notifly API.

    Attributes:
        status_code: HTTP status of the failing response.
        message: Best-effort human-readable message pulled from ``ErrorDto.message``.
        error: The parsed error model (``ErrorDto`` / ``ValidationErrorDto`` / ...) when the
            generated code was able to parse one, else ``None``.
        body: The decoded JSON body when available.
        response: The full :class:`notifly_py.types.Response` for escape-hatch access.
        ctx: ``ErrorDto.ctx`` as a plain dict when present.
        error_id: ``ErrorDto.errorId`` — quote this in support requests.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error: Any = None,
        body: Any = None,
        response: Response[Any] | None = None,
    ) -> None:
        super().__init__(f"[{status_code}] {message}")
        self.status_code = status_code
        self.message = message
        self.error = error
        self.body = body
        self.response = response

    @property
    def ctx(self) -> dict[str, Any] | None:
        return _as_plain(_attr(self.error, "ctx")) or _dig(self.body, "ctx")

    @property
    def error_id(self) -> str | None:
        value = _attr(self.error, "error_id") or _dig(self.body, "errorId")
        return value if isinstance(value, str) else None

    @property
    def headers(self) -> dict[str, str]:
        return dict(self.response.headers) if self.response is not None else {}


class AuthenticationError(NotiflyAPIError):
    """401 / 403 — missing, malformed or insufficiently scoped credentials.

    The most common cause is the ``Authorization`` prefix: Notifly wants
    ``Authorization: ApiKey <secret key>``. :class:`notifly_py.NotiflyClient` defaults to
    ``ApiKey``; the raw generated ``AuthenticatedClient`` defaults to ``Bearer``.
    """


class NotFoundError(NotiflyAPIError):
    """404 — the addressed resource does not exist in this environment."""


class ValidationError(NotiflyAPIError):
    """400 / 422 — the request body or query failed validation.

    ``errors`` carries the per-field detail from ``ValidationErrorDto.errors`` /
    ``PayloadValidationExceptionDto.errors`` when the server provided it.
    """

    @property
    def errors(self) -> Any:
        return _as_plain(_attr(self.error, "errors")) or _dig(self.body, "errors")


class ConflictError(NotiflyAPIError):
    """409 — the resource already exists or the request conflicts with current state."""


class RateLimitError(NotiflyAPIError):
    """429 — rate limit exceeded.

    ``retry_after`` is the parsed ``Retry-After`` header in seconds (``None`` when absent).
    Requests are retried automatically by the transport layer; this is raised only once the
    retry budget is exhausted.
    """

    @property
    def retry_after(self) -> float | None:
        return parse_retry_after(self.headers.get("retry-after"))

    @property
    def rate_limit(self) -> dict[str, str]:
        return {key: value for key, value in self.headers.items() if key.lower().startswith("ratelimit")}


class ServerError(NotiflyAPIError):
    """5xx — the API failed to handle an otherwise valid request."""


_STATUS_EXCEPTIONS: dict[int, type[NotiflyAPIError]] = {
    400: ValidationError,
    401: AuthenticationError,
    403: AuthenticationError,
    404: NotFoundError,
    409: ConflictError,
    422: ValidationError,
    429: RateLimitError,
}


def exception_class_for_status(status_code: int) -> type[NotiflyAPIError]:
    """Return the exception class used for ``status_code``."""
    if status_code in _STATUS_EXCEPTIONS:
        return _STATUS_EXCEPTIONS[status_code]
    if status_code >= 500:
        return ServerError
    return NotiflyAPIError


def raise_for_response(response: Response[Any]) -> Any:
    """Return ``response.parsed`` for 2xx responses; raise a typed error otherwise."""
    status_code = int(response.status_code)
    if status_code < 400:
        return response.parsed

    body = _decode_body(response.content)
    parsed = response.parsed
    error = parsed if _looks_like_error_model(parsed) else None
    message = _extract_message(parsed, body, status_code)
    raise exception_class_for_status(status_code)(
        message,
        status_code=status_code,
        error=error,
        body=body,
        response=response,
    )


def _looks_like_error_model(parsed: Any) -> bool:
    return parsed is not None and hasattr(parsed, "status_code") and hasattr(parsed, "path")


def _extract_message(parsed: Any, body: Any, status_code: int) -> str:
    for candidate in (_attr(parsed, "message"), _dig(body, "message")):
        text = _stringify(candidate)
        if text:
            return text
    if isinstance(parsed, str) and parsed:
        return parsed
    if isinstance(body, str) and body:
        return body
    try:
        return HTTPStatus(status_code).phrase
    except ValueError:
        return "Notifly API error"


def _stringify(value: Any) -> str | None:
    if value is None or isinstance(value, Unset) or value is UNSET:
        return None
    if isinstance(value, str):
        return value or None
    if isinstance(value, (list, tuple)):
        parts = [part for part in (_stringify(item) for item in value) if part]
        return "; ".join(parts) or None
    if isinstance(value, (int, float, bool)):
        return str(value)
    plain = _as_plain(value)
    if isinstance(plain, dict):
        nested = _stringify(plain.get("message"))
        if nested:
            return nested
        return json.dumps(plain, default=str)
    return None


def _attr(obj: Any, name: str) -> Any:
    value = getattr(obj, name, None)
    return None if isinstance(value, Unset) else value


def _dig(body: Any, key: str) -> Any:
    return body.get(key) if isinstance(body, dict) else None


def _as_plain(value: Any) -> Any:
    if value is None or isinstance(value, Unset):
        return None
    if isinstance(value, (dict, list, str, int, float, bool)):
        return value
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        try:
            return to_dict()
        except Exception:  # pragma: no cover - defensive: never fail while building an error
            return None
    return None


def _decode_body(content: bytes) -> Any:
    if not content:
        return None
    try:
        return json.loads(content)
    except (ValueError, UnicodeDecodeError):
        return content.decode("utf-8", errors="replace")


__all__ = [
    "AuthenticationError",
    "ConflictError",
    "NotFoundError",
    "NotiflyAPIError",
    "NotiflyError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
    "exception_class_for_status",
    "raise_for_response",
]
