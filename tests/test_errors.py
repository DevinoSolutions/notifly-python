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


def test_raw_generated_functions_still_return_unions_instead_of_raising(client_factory: Any) -> None:
    """The escape hatch is unchanged: only the facade raises."""
    from notifly_py.api.subscribers import subscribers_controller_get_subscriber

    client, _ = client_factory(json_response(404, error_dto(404, "Subscriber not found")))

    parsed = subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert parsed is not None
    assert parsed.message == "Subscriber not found"
