"""Transport-level behaviour: envelope unwrapping and retries as httpx sees them."""

from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime, timedelta

import httpx
import pytest

from notifly_py._transport import (
    AsyncEnvelopeUnwrapTransport,
    AsyncRetryTransport,
    EnvelopeUnwrapTransport,
    RetryConfig,
    RetryTransport,
    build_sync_transport,
    parse_retry_after,
)


def _mock(handler: object) -> httpx.MockTransport:
    return httpx.MockTransport(handler)  # type: ignore[arg-type]


def test_envelope_transport_unwraps_single_entity_bodies() -> None:
    transport = EnvelopeUnwrapTransport(
        _mock(lambda request: httpx.Response(200, json={"data": {"_id": "sub_1", "email": "a@b.c"}}))
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        assert client.get("/v2/subscribers/sub_1").json() == {"_id": "sub_1", "email": "a@b.c"}


def test_envelope_transport_leaves_paginated_bodies_intact() -> None:
    page = {"data": [{"_id": "1"}], "next": None, "previous": None, "totalCount": 1, "totalCountCapped": False}
    transport = EnvelopeUnwrapTransport(_mock(lambda request: httpx.Response(200, json=page)))
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        assert client.get("/v2/subscribers").json() == page


def test_envelope_transport_leaves_non_json_bodies_untouched() -> None:
    csv = b"id,action\n1,created\n"
    transport = EnvelopeUnwrapTransport(
        _mock(lambda request: httpx.Response(200, content=csv, headers={"content-type": "text/csv"}))
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        assert client.get("/v1/audit-logs/export").content == csv


def test_envelope_transport_handles_empty_204_bodies() -> None:
    transport = EnvelopeUnwrapTransport(_mock(lambda request: httpx.Response(204)))
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        response = client.delete("/v2/workflows/wf_1")
    assert response.status_code == 204
    assert response.content == b""


def test_envelope_transport_survives_gzip_encoded_bodies() -> None:
    body = gzip.compress(json.dumps({"data": {"_id": "sub_1"}}).encode())
    transport = EnvelopeUnwrapTransport(
        _mock(
            lambda request: httpx.Response(
                200, content=body, headers={"content-type": "application/json", "content-encoding": "gzip"}
            )
        )
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        assert client.get("/v2/subscribers/sub_1").json() == {"_id": "sub_1"}


def test_envelope_transport_preserves_status_and_headers() -> None:
    transport = EnvelopeUnwrapTransport(
        _mock(lambda request: httpx.Response(201, json={"data": {"ok": True}}, headers={"x-request-id": "req_1"}))
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        response = client.post("/v1/events/trigger")
    assert response.status_code == 201
    assert response.headers["x-request-id"] == "req_1"


async def test_async_envelope_transport_unwraps_single_entity_bodies() -> None:
    transport = AsyncEnvelopeUnwrapTransport(_mock(lambda request: httpx.Response(200, json={"data": {"_id": "1"}})))
    async with httpx.AsyncClient(transport=transport, base_url="https://api.notifly.test") as client:
        assert (await client.get("/v2/subscribers/1")).json() == {"_id": "1"}


def test_build_sync_transport_composes_retry_over_unwrap() -> None:
    transport = build_sync_transport(inner=_mock(lambda request: httpx.Response(200)))
    assert isinstance(transport, RetryTransport)
    assert isinstance(transport._transport, EnvelopeUnwrapTransport)


def test_build_sync_transport_can_disable_both_layers() -> None:
    inner = _mock(lambda request: httpx.Response(200))
    transport = build_sync_transport(
        inner=inner, unwrap_data_envelope=False, retry_config=RetryConfig(max_retries=0)
    )
    assert transport is inner


# --------------------------------------------------------------------------------------
# Retry-After parsing
# --------------------------------------------------------------------------------------
def test_parse_retry_after_reads_delta_seconds() -> None:
    assert parse_retry_after("42") == 42.0


def test_parse_retry_after_reads_http_dates() -> None:
    now = datetime(2026, 8, 5, 12, 0, 0, tzinfo=UTC)
    later = (now + timedelta(seconds=30)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    assert parse_retry_after(later, now=now) == pytest.approx(30.0, abs=1.0)


def test_parse_retry_after_never_returns_negative_values() -> None:
    now = datetime(2026, 8, 5, 12, 0, 0, tzinfo=UTC)
    past = (now - timedelta(seconds=30)).strftime("%a, %d %b %Y %H:%M:%S GMT")
    assert parse_retry_after(past, now=now) == 0.0


@pytest.mark.parametrize("value", [None, "", "   ", "not-a-date"])
def test_parse_retry_after_ignores_unusable_values(value: str | None) -> None:
    assert parse_retry_after(value) is None


# --------------------------------------------------------------------------------------
# Retries
# --------------------------------------------------------------------------------------
class _Script:
    def __init__(self, *responses: httpx.Response) -> None:
        self.responses = list(responses)
        self.calls = 0

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        return self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]


def test_retry_transport_retries_a_retryable_status_then_succeeds() -> None:
    script = _Script(httpx.Response(503), httpx.Response(200, json={"ok": True}))
    sleeps: list[float] = []
    transport = RetryTransport(
        _mock(script), RetryConfig(max_retries=2, backoff_factor=0.5, jitter=False), sleep=sleeps.append
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        response = client.get("/v2/subscribers")
    assert response.status_code == 200
    assert script.calls == 2
    assert sleeps == [0.5]


def test_retry_transport_honours_retry_after_over_backoff() -> None:
    script = _Script(httpx.Response(429, headers={"retry-after": "7"}), httpx.Response(200))
    sleeps: list[float] = []
    transport = RetryTransport(_mock(script), RetryConfig(max_retries=1, jitter=False), sleep=sleeps.append)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        client.get("/v2/subscribers")
    assert sleeps == [7.0]


def test_retry_transport_caps_retry_after() -> None:
    script = _Script(httpx.Response(429, headers={"retry-after": "9999"}), httpx.Response(200))
    sleeps: list[float] = []
    transport = RetryTransport(
        _mock(script), RetryConfig(max_retries=1, max_retry_after=30.0, jitter=False), sleep=sleeps.append
    )
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        client.get("/v2/subscribers")
    assert sleeps == [30.0]


def test_retry_transport_gives_up_after_the_budget_and_returns_the_last_response() -> None:
    script = _Script(httpx.Response(429))
    transport = RetryTransport(_mock(script), RetryConfig(max_retries=2, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        response = client.get("/v2/subscribers")
    assert response.status_code == 429
    assert script.calls == 3


def test_retry_transport_does_not_retry_non_idempotent_requests() -> None:
    script = _Script(httpx.Response(503))
    transport = RetryTransport(_mock(script), RetryConfig(max_retries=3, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        client.post("/v1/events/trigger", json={})
    assert script.calls == 1


def test_retry_transport_retries_posts_carrying_an_idempotency_key() -> None:
    script = _Script(httpx.Response(503), httpx.Response(201, json={"ok": True}))
    transport = RetryTransport(_mock(script), RetryConfig(max_retries=2, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        response = client.post("/v1/events/trigger", json={"a": 1}, headers={"idempotency-key": "key_1"})
    assert response.status_code == 201
    assert script.calls == 2


def test_retry_transport_replays_the_request_body_on_every_attempt() -> None:
    bodies: list[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(request.content)
        return httpx.Response(503) if len(bodies) == 1 else httpx.Response(200)

    transport = RetryTransport(_mock(handler), RetryConfig(max_retries=1, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        client.put("/v2/workflows/wf_1", json={"name": "welcome"})
    assert bodies == [b'{"name":"welcome"}', b'{"name":"welcome"}']


def test_retry_transport_does_not_retry_a_400() -> None:
    script = _Script(httpx.Response(400))
    transport = RetryTransport(_mock(script), RetryConfig(max_retries=3), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        client.get("/v2/subscribers")
    assert script.calls == 1


def test_retry_transport_retries_connection_errors() -> None:
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ConnectError("boom", request=request)
        return httpx.Response(200)

    transport = RetryTransport(_mock(handler), RetryConfig(max_retries=1, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        assert client.get("/v2/subscribers").status_code == 200
    assert calls["n"] == 2


def test_retry_transport_reraises_when_connection_errors_exhaust_the_budget() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("boom", request=request)

    transport = RetryTransport(_mock(handler), RetryConfig(max_retries=1, jitter=False), sleep=lambda _: None)
    with httpx.Client(transport=transport, base_url="https://api.notifly.test") as client:
        with pytest.raises(httpx.ConnectError):
            client.get("/v2/subscribers")


async def test_async_retry_transport_retries_then_succeeds() -> None:
    script = _Script(httpx.Response(502), httpx.Response(200, json={"ok": True}))
    sleeps: list[float] = []

    async def sleep(seconds: float) -> None:
        sleeps.append(seconds)

    transport = AsyncRetryTransport(_mock(script), RetryConfig(max_retries=2, jitter=False), sleep=sleep)
    async with httpx.AsyncClient(transport=transport, base_url="https://api.notifly.test") as client:
        response = await client.get("/v2/subscribers")
    assert response.status_code == 200
    assert script.calls == 2
    assert sleeps == [0.5]
