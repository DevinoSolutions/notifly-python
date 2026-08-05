"""The ergonomics layer: grouped access, request shaping, and the public-surface boundary."""

from __future__ import annotations

import json
from typing import Any

import pytest

from notifly_py import AsyncNotifly, Notifly
from notifly_py.internal_ops import INTERNAL_ONLY_OPERATIONS

from .conftest import SECRET_KEY, json_response, subscriber_entity, topic_entity

RESOURCE_GROUPS = ("events", "subscribers", "topics", "workflows", "messages", "notifications", "integrations")


def test_notifly_exposes_every_resource_group(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    for group in RESOURCE_GROUPS:
        assert hasattr(notifly, group), f"missing resource group: {group}"


def test_async_notifly_mirrors_the_sync_surface(async_notifly_factory: Any, notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    async_notifly, _ = async_notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    for group in RESOURCE_GROUPS:
        sync_methods = {name for name in dir(getattr(notifly, group)) if not name.startswith("_")}
        async_methods = {name for name in dir(getattr(async_notifly, group)) if not name.startswith("_")}
        assert sync_methods == async_methods, f"sync/async drift in {group}"


def test_a_secret_key_is_all_it_takes_to_build_a_client() -> None:
    notifly = Notifly(SECRET_KEY)
    assert notifly.client.token == SECRET_KEY
    assert notifly.client.prefix == "ApiKey"
    assert AsyncNotifly(SECRET_KEY).client.prefix == "ApiKey"


def test_building_without_credentials_fails_fast() -> None:
    with pytest.raises(TypeError):
        Notifly()


def test_max_retries_is_accepted_as_a_constructor_shortcut() -> None:
    assert Notifly(SECRET_KEY, max_retries=5).client.retry_config.max_retries == 5


def test_trigger_builds_the_documented_request_body(notifly_factory: Any, trigger_payload: dict[str, Any]) -> None:
    notifly, recorder = notifly_factory(json_response(201, trigger_payload))

    notifly.events.trigger(
        workflow="welcome",
        to=["subscriber_123", "subscriber_456"],
        payload={"name": "Ada", "plan": {"tier": "pro"}},
        transaction_id="txn_local_1",
        idempotency_key="idem_1",
    )

    body = json.loads(recorder.request.content)
    assert recorder.request.method == "POST"
    assert recorder.request.url.path == "/v1/events/trigger"
    assert body["name"] == "welcome"
    assert body["to"] == ["subscriber_123", "subscriber_456"]
    assert body["payload"] == {"name": "Ada", "plan": {"tier": "pro"}}
    assert body["transactionId"] == "txn_local_1"
    assert recorder.request.headers["idempotency-key"] == "idem_1"


def test_trigger_requires_either_a_body_or_workflow_and_recipient(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(201, {"data": {"acknowledged": True, "status": "processed"}}))
    with pytest.raises(TypeError, match="workflow"):
        notifly.events.trigger(payload={"a": 1})


def test_trigger_bulk_wraps_a_list_of_events(notifly_factory: Any) -> None:
    from notifly_py.models.trigger_event_request_dto import TriggerEventRequestDto

    notifly, recorder = notifly_factory(json_response(201, {"data": []}))

    notifly.events.trigger_bulk([TriggerEventRequestDto(name="welcome", to="s_1")])

    body = json.loads(recorder.request.content)
    assert body["events"][0]["name"] == "welcome"
    assert recorder.request.url.path == "/v1/events/trigger/bulk"


def test_subscribers_create_builds_the_dto_from_keyword_fields(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(201, {"data": subscriber_entity("s_1")}))

    notifly.subscribers.create(subscriber_id="s_1", email="ada@example.com", first_name="Ada")

    body = json.loads(recorder.request.content)
    assert body == {"subscriberId": "s_1", "email": "ada@example.com", "firstName": "Ada"}


def test_subscribers_update_sends_a_patch(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))

    notifly.subscribers.update("s_1", last_name="Lovelace")

    assert recorder.request.method == "PATCH"
    assert recorder.request.url.path == "/v2/subscribers/s_1"
    assert json.loads(recorder.request.content) == {"lastName": "Lovelace"}


def test_topics_subscribe_sends_subscriber_ids(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(201, {"data": {"data": [], "meta": {"totalCount": 0, "successful": 0, "failed": 0}}}))

    notifly.topics.subscribe("product-updates", ["s_1", "s_2"])

    assert recorder.request.url.path == "/v2/topics/product-updates/subscriptions"
    assert json.loads(recorder.request.content) == {"subscriberIds": ["s_1", "s_2"]}


def test_topics_unsubscribe_uses_delete(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(200, {"data": {"data": [], "meta": {"totalCount": 0, "successful": 0, "failed": 0}}}))

    notifly.topics.unsubscribe("product-updates", ["s_1"])

    assert recorder.request.method == "DELETE"
    assert json.loads(recorder.request.content) == {"subscriberIds": ["s_1"]}


def test_topics_upsert_builds_the_dto_from_keyword_fields(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(200, {"data": topic_entity()}))

    notifly.topics.upsert(key="product-updates", name="Product updates")

    assert json.loads(recorder.request.content) == {"key": "product-updates", "name": "Product updates"}


def test_query_filters_reach_the_wire(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(
        json_response(200, {"data": [], "next": None, "previous": None, "totalCount": 0, "totalCountCapped": False})
    )

    notifly.subscribers.list(limit=25, email="ada@example.com")

    assert recorder.request.url.params["limit"] == "25"
    assert recorder.request.url.params["email"] == "ada@example.com"


def test_none_valued_arguments_are_omitted_rather_than_serialized(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))

    notifly.subscribers.get("s_1", idempotency_key=None)

    assert "idempotency-key" not in recorder.request.headers


async def test_the_async_facade_performs_real_requests(
    async_notifly_factory: Any, trigger_payload: dict[str, Any]
) -> None:
    notifly, recorder = async_notifly_factory(json_response(201, trigger_payload))

    result = await notifly.events.trigger(workflow="welcome", to="s_1")

    assert result.transaction_id == "txn_01HZY"
    assert recorder.request.url.path == "/v1/events/trigger"


def test_the_facade_never_exposes_a_bearer_only_operation(notifly_factory: Any) -> None:
    """PRD G7: the sixteen dashboard-session operations stay out of the public surface."""
    notifly, _ = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    forbidden = {"duplicate", "audit_logs", "translations", "activity", "charts", "workflow_runs"}
    for group in RESOURCE_GROUPS:
        methods = {name for name in dir(getattr(notifly, group)) if not name.startswith("_")}
        assert not (methods & forbidden), f"{group} exposes an internal-only operation"
    assert len(INTERNAL_ONLY_OPERATIONS) == 16


def test_the_underlying_client_stays_reachable_as_an_escape_hatch(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    from notifly_py import NotiflyClient

    assert isinstance(notifly.client, NotiflyClient)
