"""Auth prefix, User-Agent and base-URL behaviour (PRD G12 / G9).

The single most expensive footgun in the generated client is ``prefix="Bearer"``: Notifly
answers a secret key sent as ``Bearer`` with a 401. ``NotiflyClient`` defaults to ``ApiKey``.
"""

from __future__ import annotations

from typing import Any

import httpx

from notifly_py import AuthenticatedClient, NotiflyClient, __version__, from_bearer_token, from_secret_key
from notifly_py.api.subscribers import subscribers_controller_get_subscriber

from .conftest import BASE_URL, SECRET_KEY, json_response, subscriber_entity


def test_notifly_client_sends_the_apikey_authorization_scheme(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}))

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert recorder.request.headers["authorization"] == f"ApiKey {SECRET_KEY}"


def test_generated_client_still_defaults_to_bearer() -> None:
    """Documents the trap the SDK now protects against — the generated default is unchanged."""
    assert AuthenticatedClient(base_url=BASE_URL, token="x").prefix == "Bearer"
    assert NotiflyClient(base_url=BASE_URL, token="x").prefix == "ApiKey"


def test_bearer_prefix_remains_reachable_for_dashboard_tokens(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}), prefix="Bearer")

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert recorder.request.headers["authorization"] == f"Bearer {SECRET_KEY}"


def test_from_secret_key_and_from_bearer_token_pick_the_right_scheme() -> None:
    assert from_secret_key("sk_live_x").prefix == "ApiKey"
    assert from_bearer_token("jwt_x").prefix == "Bearer"


def test_default_base_url_points_at_the_production_api() -> None:
    client = from_secret_key("sk_live_x")
    assert client.get_httpx_client().base_url == httpx.URL("https://api.notifly.io")


def test_requests_carry_an_identifying_user_agent(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}))

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    user_agent = recorder.request.headers["user-agent"]
    assert user_agent.startswith("notifly-sdk/")
    assert f"notifly-sdk/{__version__}" in user_agent
    assert "python/" in user_agent


def test_user_agent_can_be_overridden(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    client.user_agent = "my-app/2.0"
    client._client = None  # rebuild the httpx client with the new agent

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert recorder.request.headers["user-agent"] == "my-app/2.0"


def test_custom_headers_survive_alongside_auth(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}))
    client._headers["x-tenant"] = "acme"
    client._client = None

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1")

    assert recorder.request.headers["x-tenant"] == "acme"
    assert recorder.request.headers["authorization"].startswith("ApiKey ")


def test_idempotency_key_is_sent_as_a_header(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": subscriber_entity("s_1")}))

    subscribers_controller_get_subscriber.sync(client=client, subscriber_id="s_1", idempotency_key="key_42")

    assert recorder.request.headers["idempotency-key"] == "key_42"
