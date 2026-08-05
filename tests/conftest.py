"""Shared fixtures: an in-process transport so tests exercise the real client stack.

Nothing here talks to the network. Requests travel through the exact transport chain the
SDK installs in production (retries -> envelope unwrap -> transport), with the bottom layer
swapped for a recorder, so a regression in that chain fails these tests.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Iterator
from typing import Any

import httpx
import pytest

from notifly_py import Notifly, NotiflyClient
from notifly_py._transport import RetryConfig
from notifly_py.facade import AsyncNotifly

BASE_URL = "https://api.notifly.test"
SECRET_KEY = "sk_test_notifly"


def _clone(response: httpx.Response) -> httpx.Response:
    """Return a fresh response so a scripted one can be replayed across retries."""
    return httpx.Response(response.status_code, content=response.content, headers=response.headers)


class Recorder:
    """Records requests and replays a scripted sequence of responses."""

    def __init__(self, responses: list[httpx.Response]) -> None:
        self._responses = list(responses)
        self.requests: list[httpx.Request] = []
        self.sleeps: list[float] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if not self._responses:
            raise AssertionError(f"unexpected extra request: {request.method} {request.url}")
        scripted = self._responses.pop(0) if len(self._responses) > 1 else self._responses[0]
        return _clone(scripted)

    @property
    def request(self) -> httpx.Request:
        assert self.requests, "no request was made"
        return self.requests[-1]

    @property
    def call_count(self) -> int:
        return len(self.requests)

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)


def json_response(status_code: int, payload: Any, headers: dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(
        status_code,
        content=json.dumps(payload).encode(),
        headers={"content-type": "application/json", **(headers or {})},
    )


def make_client(
    responses: list[httpx.Response] | httpx.Response,
    *,
    max_retries: int = 0,
    unwrap_data_envelope: bool = True,
    prefix: str | None = None,
) -> tuple[NotiflyClient, Recorder]:
    """Build a :class:`NotiflyClient` whose bottom transport is a scripted recorder."""
    recorder = Recorder(responses if isinstance(responses, list) else [responses])
    kwargs: dict[str, Any] = {}
    if prefix is not None:
        kwargs["prefix"] = prefix
    client = NotiflyClient(
        base_url=BASE_URL,
        token=SECRET_KEY,
        retry_config=RetryConfig(max_retries=max_retries, backoff_factor=0.01, jitter=False),
        unwrap_data_envelope=unwrap_data_envelope,
        httpx_args={"transport": httpx.MockTransport(recorder)},
        **kwargs,
    )
    return client, recorder


@pytest.fixture
def client_factory() -> Callable[..., tuple[NotiflyClient, Recorder]]:
    return make_client


@pytest.fixture
def notifly_factory() -> Callable[..., tuple[Notifly, Recorder]]:
    def factory(responses: list[httpx.Response] | httpx.Response, **kwargs: Any) -> tuple[Notifly, Recorder]:
        client, recorder = make_client(responses, **kwargs)
        return Notifly(client=client), recorder

    return factory


@pytest.fixture
def async_notifly_factory() -> Callable[..., tuple[AsyncNotifly, Recorder]]:
    def factory(responses: list[httpx.Response] | httpx.Response, **kwargs: Any) -> tuple[AsyncNotifly, Recorder]:
        client, recorder = make_client(responses, **kwargs)
        return AsyncNotifly(client=client), recorder

    return factory


def subscriber_entity(subscriber_id: str = "subscriber_123", **overrides: Any) -> dict[str, Any]:
    """A complete ``SubscriberResponseDto`` body — the generated model has required fields."""
    return {
        "_id": f"6650f0a1c1a2b3d4e5f6{abs(hash(subscriber_id)) % 10000:04d}",
        "subscriberId": subscriber_id,
        "_organizationId": "org_1",
        "_environmentId": "env_1",
        "deleted": False,
        "createdAt": "2026-08-05T10:00:00.000Z",
        "updatedAt": "2026-08-05T10:00:00.000Z",
        **overrides,
    }


def topic_entity(key: str = "product-updates", **overrides: Any) -> dict[str, Any]:
    return {"_id": f"topic_{key}", "key": key, "name": key.title(), **overrides}


@pytest.fixture
def trigger_payload() -> dict[str, Any]:
    """A realistic single-entity response body, exactly as the API puts it on the wire."""
    return {
        "data": {
            "acknowledged": True,
            "status": "processed",
            "transactionId": "txn_01HZY",
            "activityFeedLink": "https://dashboard.notifly.io/activity/txn_01HZY",
        }
    }


@pytest.fixture(autouse=True)
def _no_real_network(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Fail loudly if a non-e2e test ever tries to open a real connection."""
    if request.node.get_closest_marker("e2e"):
        yield
        return

    original_sync = httpx.HTTPTransport.handle_request
    original_async = httpx.AsyncHTTPTransport.handle_async_request

    def _respx_is_active() -> bool:
        # respx patches httpcore, one layer below httpx transports, so its requests still
        # travel through the guard. Let them through instead of failing the test.
        from respx.mocks import Mocker

        return any(mocker._patches for mocker in Mocker.registry.values())

    def guard(self: Any, request: httpx.Request) -> Any:
        if _respx_is_active():
            return original_sync(self, request)
        raise AssertionError(f"a test attempted a real network connection: {request.method} {request.url}")

    async def async_guard(self: Any, request: httpx.Request) -> Any:
        if _respx_is_active():
            return await original_async(self, request)
        raise AssertionError(f"a test attempted a real network connection: {request.method} {request.url}")

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", guard)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", async_guard)
    yield
