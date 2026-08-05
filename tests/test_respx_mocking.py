"""The mocking recipe we document for users: ``respx`` in front of the real client stack.

If these break, the README's testing advice is wrong — and it also proves the SDK's transport
layers compose with the standard httpx mocking library rather than fighting it.
"""

from __future__ import annotations

import httpx
import pytest
import respx

from notifly_py import Notifly, NotiflyClient, RetryConfig
from notifly_py.exceptions import NotFoundError

BASE_URL = "https://api.notifly.test"
SUBSCRIBER = {
    "_id": "6650f0a1c1a2b3d4e5f60001",
    "subscriberId": "s_1",
    "_organizationId": "org_1",
    "_environmentId": "env_1",
    "deleted": False,
    "createdAt": "2026-08-05T10:00:00.000Z",
    "updatedAt": "2026-08-05T10:00:00.000Z",
}


@pytest.fixture
def notifly() -> Notifly:
    return Notifly(client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0)))


@respx.mock
def test_trigger_under_respx_returns_a_populated_model(notifly: Notifly) -> None:
    route = respx.post(f"{BASE_URL}/v1/events/trigger").mock(
        return_value=httpx.Response(
            201, json={"data": {"acknowledged": True, "status": "processed", "transactionId": "txn_respx"}}
        )
    )

    result = notifly.events.trigger(workflow="welcome", to="subscriber_123")

    assert route.called
    assert result.acknowledged is True
    assert result.transaction_id == "txn_respx"


@respx.mock
def test_errors_under_respx_raise_typed_exceptions(notifly: Notifly) -> None:
    respx.get(f"{BASE_URL}/v2/subscribers/missing").mock(
        return_value=httpx.Response(
            404,
            json={
                "statusCode": 404,
                "timestamp": "2026-08-05T12:00:00.000Z",
                "path": "/v2/subscribers/missing",
                "message": "Subscriber not found",
            },
        )
    )

    with pytest.raises(NotFoundError):
        notifly.subscribers.get("missing")


@respx.mock
async def test_async_trigger_under_respx() -> None:
    from notifly_py import AsyncNotifly

    respx.post(f"{BASE_URL}/v1/events/trigger").mock(
        return_value=httpx.Response(201, json={"data": {"acknowledged": True, "status": "processed"}})
    )
    notifly = AsyncNotifly(
        client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0))
    )

    result = await notifly.events.trigger(workflow="welcome", to="s_1")

    assert result.acknowledged is True


@respx.mock
def test_retries_are_visible_to_respx(notifly: Notifly) -> None:
    client = NotiflyClient(
        base_url=BASE_URL,
        token="sk_test",
        retry_config=RetryConfig(max_retries=2, backoff_factor=0.0, jitter=False),
    )
    route = respx.get(f"{BASE_URL}/v2/subscribers/s_1").mock(
        side_effect=[
            httpx.Response(503),
            httpx.Response(200, json={"data": SUBSCRIBER}),
        ]
    )

    result = Notifly(client=client).subscribers.get("s_1")

    assert route.call_count == 2
    assert result.subscriber_id == "s_1"
