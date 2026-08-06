"""Typed error mapping over ``ErrorDto`` (PRD G3).

The API does not speak RFC 9457; these tests pin the mapping from its real ``ErrorDto`` /
``ValidationErrorDto`` bodies onto the SDK exception hierarchy.
"""

from __future__ import annotations

from typing import Any

import pytest

from notifly_py.exceptions import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
    NotiflyAPIError,
    NotiflyError,
    RateLimitError,
    ServerError,
    ValidationError,
    exception_class_for_status,
)

from .conftest import json_response


def error_dto(status_code: int, message: Any = "boom", **extra: Any) -> dict[str, Any]:
    return {
        "statusCode": status_code,
        "timestamp": "2026-08-05T12:00:00.000Z",
        "path": "/v2/subscribers/s_1",
        "message": message,
        **extra,
    }


@pytest.mark.parametrize(
    ("status_code", "expected"),
    [
        (400, ValidationError),
        (401, AuthenticationError),
        (403, AuthenticationError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, ValidationError),
        (429, RateLimitError),
        (500, ServerError),
        (503, ServerError),
        (418, NotiflyAPIError),
    ],
)
def test_status_codes_map_to_exception_classes(status_code: int, expected: type[Exception]) -> None:
    assert exception_class_for_status(status_code) is expected


def test_every_api_error_is_a_notifly_error() -> None:
    assert issubclass(NotiflyAPIError, NotiflyError)
    assert issubclass(RateLimitError, NotiflyAPIError)


def test_401_raises_authentication_error_with_the_server_message(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(401, error_dto(401, "API key not found")))

    with pytest.raises(AuthenticationError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.status_code == 401
    assert excinfo.value.message == "API key not found"
    assert "[401]" in str(excinfo.value)


def test_404_raises_not_found_error(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(404, error_dto(404, "Subscriber not found")))

    with pytest.raises(NotFoundError) as excinfo:
        notifly.subscribers.get("missing")

    assert excinfo.value.message == "Subscriber not found"
    assert excinfo.value.error is not None


def test_422_raises_validation_error_carrying_field_detail(notifly_factory: Any) -> None:
    body = error_dto(
        422,
        "Validation failed",
        errors={"email": {"messages": ["email must be an email"]}},
        ctx={"field": "email"},
        errorId="err_123",
    )
    notifly, _ = notifly_factory(json_response(422, body))

    with pytest.raises(ValidationError) as excinfo:
        notifly.subscribers.create(subscriber_id="s_1", email="nope")

    assert excinfo.value.errors == {"email": {"messages": ["email must be an email"]}}
    assert excinfo.value.ctx == {"field": "email"}
    assert excinfo.value.error_id == "err_123"


def test_429_raises_rate_limit_error_exposing_retry_after(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(
        json_response(
            429,
            "Rate limit exceeded",
            headers={"retry-after": "12", "ratelimit-remaining": "0", "ratelimit-reset": "12"},
        )
    )

    with pytest.raises(RateLimitError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.retry_after == 12.0
    assert excinfo.value.rate_limit["ratelimit-remaining"] == "0"


def test_500_raises_server_error(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(500, error_dto(500, "Internal server error")))

    with pytest.raises(ServerError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.status_code == 500


def test_message_falls_back_to_the_status_phrase_when_the_body_has_none(notifly_factory: Any) -> None:
    body = {"statusCode": 404, "timestamp": "2026-08-05T12:00:00.000Z", "path": "/v2/subscribers/s_1"}
    notifly, _ = notifly_factory(json_response(404, body))

    with pytest.raises(NotFoundError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.message == "Not Found"


def test_list_messages_are_joined(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(400, error_dto(400, ["name should not be empty", "to is required"])))

    with pytest.raises(ValidationError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.message == "name should not be empty; to is required"


def test_non_json_error_bodies_do_not_break_error_construction(notifly_factory: Any) -> None:
    import httpx

    notifly, _ = notifly_factory(
        httpx.Response(502, content=b"<html>bad gateway</html>", headers={"content-type": "text/html"})
    )

    with pytest.raises(ServerError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.status_code == 502
    assert excinfo.value.body == "<html>bad gateway</html>"


def test_the_exception_keeps_the_full_response_for_escape_hatch_access(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(404, error_dto(404), headers={"x-request-id": "req_9"}))

    with pytest.raises(NotFoundError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.response is not None
    assert excinfo.value.headers["x-request-id"] == "req_9"


def test_the_real_production_401_body_maps_to_authentication_error(notifly_factory: Any) -> None:
    """Verbatim body captured from https://api.notifly.io on 2026-08-05 with a bad key.

    It is multi-key, so the envelope unwrapper correctly leaves error bodies alone — if it
    ever started stripping them, this test would fail before anyone shipped it.
    """
    live_body = {
        "error": "Unauthorized",
        "statusCode": 401,
        "timestamp": "2026-08-05T12:25:34.638Z",
        "path": "/v2/subscribers?limit=1",
        "message": "API Key not found",
        "ctx": {"error": "Unauthorized", "statusCode": 401},
    }
    notifly, _ = notifly_factory(json_response(401, live_body))

    with pytest.raises(AuthenticationError) as excinfo:
        notifly.subscribers.list(limit=1)

    assert excinfo.value.message == "API Key not found"
    assert excinfo.value.ctx == {"error": "Unauthorized", "statusCode": 401}
    assert excinfo.value.body == live_body


LIVE_400_TRIGGER_BODY: dict[str, Any] = {
    "error": "Bad Request",
    "statusCode": 400,
    "timestamp": "2026-08-06T01:20:02.503Z",
    "path": "/v1/events/trigger",
    "message": "payload is missing required key(s) and type(s): body (Value), body (Value)",
    "ctx": {"error": "Bad Request", "statusCode": 400},
}
"""Verbatim payload-validation 400 from https://api.notifly.io ``POST /v1/events/trigger``.

Captured by the live E2E run that found this bug; the same shape (no ``type``, no ``errors``)
came back from an independent probe on 2026-08-06. The spec types a 400 there as
``PayloadValidationExceptionDto``, whose generated ``from_dict`` pops both ``type`` and
``errors`` unguarded — so parsing the real body raised ``KeyError('type')`` out of the facade
instead of the :class:`ValidationError` the SDK promises.
"""


def test_the_real_production_400_without_a_type_field_maps_to_validation_error(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(400, LIVE_400_TRIGGER_BODY))

    with pytest.raises(ValidationError) as excinfo:
        notifly.events.trigger(workflow="welcome", to="subscriber_123")

    assert excinfo.value.status_code == 400
    assert excinfo.value.message == "payload is missing required key(s) and type(s): body (Value), body (Value)"
    assert excinfo.value.ctx == {"error": "Bad Request", "statusCode": 400}
    assert excinfo.value.errors is None
    assert excinfo.value.body == LIVE_400_TRIGGER_BODY


async def test_the_real_production_400_maps_to_validation_error_on_the_async_facade(
    async_notifly_factory: Any,
) -> None:
    notifly, _ = async_notifly_factory(json_response(400, LIVE_400_TRIGGER_BODY))

    with pytest.raises(ValidationError) as excinfo:
        await notifly.events.trigger(workflow="welcome", to="subscriber_123")

    assert excinfo.value.message == "payload is missing required key(s) and type(s): body (Value), body (Value)"
    assert excinfo.value.body == LIVE_400_TRIGGER_BODY


def test_a_spec_shaped_400_still_parses_into_the_payload_validation_model(notifly_factory: Any) -> None:
    """The tolerance is a fallback, not a replacement: a complete body keeps its typed model."""
    body = {
        "statusCode": 400,
        "timestamp": "2026-08-06T01:20:02.503Z",
        "path": "/v1/events/trigger",
        "type": "PAYLOAD_VALIDATION_ERROR",
        "message": "Payload validation failed",
        "errors": [
            {
                "field": "payload.name",
                "message": "must have required property 'name'",
                "value": {"age": 25},
                "schemaPath": "#/required",
            }
        ],
    }
    notifly, _ = notifly_factory(json_response(400, body))

    with pytest.raises(ValidationError) as excinfo:
        notifly.events.trigger(workflow="welcome", to="subscriber_123")

    assert excinfo.value.error is not None
    assert excinfo.value.error.type_ == "PAYLOAD_VALIDATION_ERROR"
    assert excinfo.value.errors[0].field == "payload.name"


@pytest.mark.parametrize(
    ("missing_key", "body"),
    [
        ("statusCode", {"timestamp": "2026-08-06T01:20:02.503Z", "path": "/v2/subscribers/s_1", "message": "nope"}),
        ("timestamp", {"statusCode": 404, "path": "/v2/subscribers/s_1", "message": "nope"}),
        ("path", {"statusCode": 404, "timestamp": "2026-08-06T01:20:02.503Z", "message": "nope"}),
        ("everything", {"message": "nope"}),
    ],
)
def test_error_dto_bodies_missing_a_required_key_still_raise_the_typed_error(
    notifly_factory: Any, missing_key: str, body: dict[str, Any]
) -> None:
    """``ErrorDto.from_dict`` pops ``statusCode``/``timestamp``/``path`` unguarded too."""
    notifly, _ = notifly_factory(json_response(404, body))

    with pytest.raises(NotFoundError) as excinfo:
        notifly.subscribers.get("s_1")

    assert excinfo.value.status_code == 404
    assert excinfo.value.message == "nope"
    assert excinfo.value.body == body


def test_a_422_without_the_errors_key_still_raises_validation_error(notifly_factory: Any) -> None:
    """``ValidationErrorDto.from_dict`` pops ``errors`` unguarded."""
    body = {"statusCode": 422, "timestamp": "2026-08-06T01:20:02.503Z", "path": "/v1/subscribers", "message": "boom"}
    notifly, _ = notifly_factory(json_response(422, body))

    with pytest.raises(ValidationError) as excinfo:
        notifly.subscribers.create(subscriber_id="s_1")

    assert excinfo.value.message == "boom"
    assert excinfo.value.errors is None


LIVE_422_UNKNOWN_WORKFLOW_BODY: dict[str, Any] = {
    "error": "Unprocessable Entity",
    "statusCode": 422,
    "timestamp": "2026-08-06T01:20:01.357Z",
    "path": "/v1/events/trigger",
    "message": "workflow_not_found",
    "ctx": {"error": "Unprocessable Entity", "statusCode": 422},
}
"""Verbatim 422 captured from https://api.notifly.io on 2026-08-06 by triggering an unknown workflow.

This is the everyday shape of the bug: the spec types a 422 there as ``ValidationErrorDto``,
whose ``from_dict`` pops ``errors`` unguarded, and this body has no ``errors``. Mistyping a
workflow name — the single most ordinary caller mistake — used to surface as ``KeyError('errors')``.
"""


def test_the_real_production_unknown_workflow_422_maps_to_validation_error(notifly_factory: Any) -> None:
    notifly, _ = notifly_factory(json_response(422, LIVE_422_UNKNOWN_WORKFLOW_BODY))

    with pytest.raises(ValidationError) as excinfo:
        notifly.events.trigger(workflow="no-such-workflow", to="subscriber_123")

    assert excinfo.value.message == "workflow_not_found"
    assert excinfo.value.ctx == {"error": "Unprocessable Entity", "statusCode": 422}
    assert excinfo.value.body == LIVE_422_UNKNOWN_WORKFLOW_BODY


def test_an_unparsable_success_body_still_raises_rather_than_being_swallowed(notifly_factory: Any) -> None:
    """Tolerance is scoped to failing statuses — a 2xx the SDK cannot parse is a real bug."""
    notifly, _ = notifly_factory(json_response(201, {"status": "processed"}))

    with pytest.raises(KeyError, match="acknowledged"):
        notifly.events.trigger(workflow="welcome", to="subscriber_123")


def test_the_generated_operation_modules_expose_the_helpers_the_facade_calls() -> None:
    """Drift gate: the facade builds responses from the generated private helpers."""
    from notifly_py.api.events import events_controller_trigger
    from notifly_py.api.subscribers import subscribers_controller_get_subscriber

    for module in (events_controller_trigger, subscribers_controller_get_subscriber):
        assert callable(module._get_kwargs)
        assert callable(module._parse_response)


def test_raw_generated_functions_still_return_unions_instead_of_raising(client_factory: Any) -> None:
    """The escape hatch is unchanged: only the facade raises."""
    from notifly_py.api.subscribers import subscribers_controller_get_subscriber

    client, _ = client_factory(json_response(404, error_dto(404, "Subscriber not found")))

    parsed = subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert parsed is not None
    assert parsed.message == "Subscriber not found"
