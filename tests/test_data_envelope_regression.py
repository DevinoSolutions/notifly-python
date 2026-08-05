"""THE regression suite for the ``{"data": ...}`` envelope ship-blocker (PRD G1/D5).

Background: the API wraps single entities as ``{"data": {...}}`` at runtime, while the
OpenAPI document the SDK is generated from describes the *unwrapped* payload. Without the
unwrap layer the generated ``from_dict`` receives the envelope and either

* silently returns the envelope itself wherever the generated code uses ``cast()`` — a
  ``cast(bool, response.json())`` hands the caller ``{"data": True}`` and every type checker
  agrees it is a ``bool``; or
* raises ``KeyError`` on the first required field, wherever the response maps to a model
  (``TriggerEventResponseDto``, ``SubscriberResponseDto``, ...).

Both failure modes are asserted below against a client with the fix disabled, so if the
unwrap layer is ever removed these tests fail loudly instead of shipping empty models.
"""

from __future__ import annotations

from typing import Any

import pytest

from notifly_py.api.events import events_controller_trigger
from notifly_py.api.subscribers import subscribers_controller_get_subscriber
from notifly_py.models.trigger_event_request_dto import TriggerEventRequestDto

from .conftest import json_response

SUBSCRIBER_ENTITY = {
    "_id": "6650f0a1c1a2b3d4e5f60001",
    "subscriberId": "subscriber_123",
    "firstName": "Ada",
    "lastName": "Lovelace",
    "email": "ada@example.com",
    "_organizationId": "org_1",
    "_environmentId": "env_1",
    "deleted": False,
    "createdAt": "2026-08-05T10:00:00.000Z",
    "updatedAt": "2026-08-05T10:00:00.000Z",
}


def _trigger_body() -> TriggerEventRequestDto:
    return TriggerEventRequestDto(name="welcome", to="subscriber_123")


def test_trigger_returns_a_populated_model_through_the_generated_module(
    client_factory: Any, trigger_payload: dict[str, Any]
) -> None:
    client, _ = client_factory(json_response(201, trigger_payload))

    parsed = events_controller_trigger.sync(client=client, body=_trigger_body())

    assert parsed is not None
    assert parsed.acknowledged is True
    assert parsed.status.value == "processed"
    assert parsed.transaction_id == "txn_01HZY"
    assert parsed.additional_properties == {}, "the envelope must not survive into additional_properties"


async def test_trigger_returns_a_populated_model_asynchronously(
    client_factory: Any, trigger_payload: dict[str, Any]
) -> None:
    client, _ = client_factory(json_response(201, trigger_payload))

    parsed = await events_controller_trigger.asyncio(client=client, body=_trigger_body())

    assert parsed is not None
    assert parsed.acknowledged is True
    assert parsed.transaction_id == "txn_01HZY"


def test_trigger_through_the_facade_returns_a_populated_model(
    notifly_factory: Any, trigger_payload: dict[str, Any]
) -> None:
    notifly, recorder = notifly_factory(json_response(201, trigger_payload))

    result = notifly.events.trigger(workflow="welcome", to="subscriber_123", payload={"name": "Ada"})

    assert result.acknowledged is True
    assert result.transaction_id == "txn_01HZY"
    assert recorder.request.url.path == "/v1/events/trigger"


def test_reverting_the_fix_raises_on_models_with_required_fields(
    client_factory: Any, trigger_payload: dict[str, Any]
) -> None:
    """Proof of the blocker: with unwrapping off, the envelope reaches ``from_dict``."""
    client, _ = client_factory(json_response(201, trigger_payload), unwrap_data_envelope=False)

    with pytest.raises(KeyError, match="acknowledged"):
        events_controller_trigger.sync(client=client, body=_trigger_body())


def test_read_endpoint_returns_populated_fields(client_factory: Any) -> None:
    client, _ = client_factory(json_response(200, {"data": SUBSCRIBER_ENTITY}))

    parsed = subscribers_controller_get_subscriber.sync(client=client, subscriber_id="subscriber_123")

    assert parsed is not None
    assert parsed.subscriber_id == "subscriber_123"
    assert parsed.email == "ada@example.com"
    assert parsed.first_name == "Ada"
    assert parsed.additional_properties == {}


def test_reverting_the_fix_raises_on_read_endpoints_too(client_factory: Any) -> None:
    client, _ = client_factory(json_response(200, {"data": SUBSCRIBER_ENTITY}), unwrap_data_envelope=False)

    with pytest.raises(KeyError, match="subscriberId"):
        subscribers_controller_get_subscriber.sync(client=client, subscriber_id="subscriber_123")


def test_cast_typed_responses_are_unwrapped_to_the_documented_scalar(client_factory: Any) -> None:
    """``EventsController_cancel`` is documented as returning a bare ``bool``."""
    from notifly_py.api.events import events_controller_cancel

    client, _ = client_factory(json_response(200, {"data": True}))

    assert events_controller_cancel.sync(client=client, transaction_id="txn_1") is True


def test_reverting_the_fix_silently_returns_the_envelope_for_cast_typed_responses(
    client_factory: Any,
) -> None:
    """The quiet failure mode: ``cast()`` does nothing at runtime, so nobody notices."""
    from notifly_py.api.events import events_controller_cancel

    client, _ = client_factory(json_response(200, {"data": True}), unwrap_data_envelope=False)

    parsed = events_controller_cancel.sync(client=client, transaction_id="txn_1")

    assert parsed == {"data": True}, "type-clean, silently wrong — this is the bug being fixed"
    assert parsed is not True


def test_paginated_responses_keep_their_data_wrapper(client_factory: Any) -> None:
    """``returnWholeObject()`` keeps paginated bodies multi-key — they must not be unwrapped."""
    page = {
        "data": [SUBSCRIBER_ENTITY],
        "next": "cursor_2",
        "previous": None,
        "totalCount": 1,
        "totalCountCapped": False,
    }
    client, _ = client_factory(json_response(200, page))

    from notifly_py.api.subscribers import subscribers_controller_search_subscribers

    parsed = subscribers_controller_search_subscribers.sync(client=client)

    assert parsed is not None
    assert parsed.total_count == 1
    assert parsed.next_ == "cursor_2"
    assert len(parsed.data) == 1
    assert parsed.data[0].subscriber_id == "subscriber_123"


def test_no_content_responses_still_parse(client_factory: Any) -> None:
    from notifly_py.api.workflows import workflow_controller_remove_workflow

    client, _ = client_factory(json_response(204, None))
    assert workflow_controller_remove_workflow.sync(client=client, workflow_id="wf_1") is None
