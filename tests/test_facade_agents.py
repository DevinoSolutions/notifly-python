"""``notifly.agents``: every Agents operation through the facade, sync and async, under ``respx``.

``tests/test_agents_operations.py`` pins the generated modules. These cases pin what the facade adds on
top: method, path, query, headers and JSON body for each of the eleven operations, the pagination
helpers, and that update calls send only what the caller passed.
"""

from __future__ import annotations

import inspect
import json
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from notifly_py import AsyncNotifly, Notifly, NotiflyClient, RetryConfig
from notifly_py.exceptions import NotFoundError
from notifly_py.facade import AGENTS_ANALYTICS_SOURCE
from notifly_py.models import (
    AddAgentIntegrationRequestDto,
    AgentBehaviorDto,
    AgentBehaviorDtoSubscriberAccess,
    AgentIntegrationResponseDto,
    AgentResponseDto,
    CreateAgentRequestDto,
    CreateAgentRequestDtoRuntime,
    ListAgentsResponseDto,
    SentMessageInfoDto,
    UpdateAgentRequestDto,
)

from .test_agents_operations import AGENT, AGENT_INTEGRATION, page

BASE_URL = "https://api.notifly.test"
INTEGRATION_ID = AGENT_INTEGRATION["_id"]


def _notifly() -> Notifly:
    return Notifly(client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0)))


def _async_notifly() -> AsyncNotifly:
    return AsyncNotifly(
        client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0))
    )


@dataclass
class Case:
    """One facade call and what it must put on the wire."""

    operation_id: str
    call: Callable[[Any], Any]
    method: str
    path: str
    status: int
    response: Any
    query: dict[str, str] = field(default_factory=dict)
    body: dict[str, Any] | None = None
    headers: dict[str, str] = field(default_factory=dict)
    parsed_type: type | None = None


CASES = [
    Case(
        "AgentsController_createAgent",
        lambda n: n.agents.create(name="Support bot", identifier="support-bot"),
        "POST",
        "/v1/agents",
        201,
        {"data": AGENT},
        body={"name": "Support bot", "identifier": "support-bot", "active": True},
        headers={"novu-analytics-source": AGENTS_ANALYTICS_SOURCE},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_listAgents",
        lambda n: n.agents.list(limit=5, identifier="support-bot"),
        "GET",
        "/v1/agents",
        200,
        {"data": page([AGENT])},
        query={"limit": "5", "identifier": "support-bot"},
        parsed_type=ListAgentsResponseDto,
    ),
    Case(
        "AgentsController_getAgent",
        lambda n: n.agents.get("support-bot"),
        "GET",
        "/v1/agents/support-bot",
        200,
        {"data": AGENT},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_updateAgent",
        lambda n: n.agents.update("support-bot", name="Support bot v2"),
        "PATCH",
        "/v1/agents/support-bot",
        200,
        {"data": AGENT},
        body={"name": "Support bot v2"},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_deleteAgent",
        lambda n: n.agents.delete("support-bot"),
        "DELETE",
        "/v1/agents/support-bot",
        204,
        None,
        query={"deleteFromProvider": "false"},
    ),
    Case(
        "AgentsController_updateAgentBridge",
        lambda n: n.agents.update_bridge("support-bot", bridge_url="https://bot.example.com/api/notifly"),
        "PUT",
        "/v1/agents/support-bot/bridge",
        200,
        {"data": AGENT},
        body={"bridgeUrl": "https://bot.example.com/api/notifly"},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentIntegrationsController_addAgentIntegration",
        lambda n: n.agents.add_integration("support-bot", "slack-prod"),
        "POST",
        "/v1/agents/support-bot/integrations",
        201,
        {"data": AGENT_INTEGRATION},
        body={"integrationIdentifier": "slack-prod"},
        parsed_type=AgentIntegrationResponseDto,
    ),
    Case(
        "AgentIntegrationsController_listAgentIntegrations",
        lambda n: n.agents.list_integrations("support-bot", integration_identifier="slack-prod", include_cursor=True),
        "GET",
        "/v1/agents/support-bot/integrations",
        200,
        {"data": page([AGENT_INTEGRATION])},
        query={"integrationIdentifier": "slack-prod", "includeCursor": "true"},
    ),
    Case(
        "AgentIntegrationsController_updateAgentIntegration",
        lambda n: n.agents.update_integration("support-bot", INTEGRATION_ID, "slack-staging"),
        "PATCH",
        f"/v1/agents/support-bot/integrations/{INTEGRATION_ID}",
        200,
        {"data": AGENT_INTEGRATION},
        body={"integrationIdentifier": "slack-staging"},
        parsed_type=AgentIntegrationResponseDto,
    ),
    Case(
        "AgentIntegrationsController_removeAgentIntegration",
        lambda n: n.agents.remove_integration("support-bot", INTEGRATION_ID),
        "DELETE",
        f"/v1/agents/support-bot/integrations/{INTEGRATION_ID}",
        204,
        None,
    ),
    Case(
        "AgentReplyController_handleAgentReplyHandler",
        lambda n: n.agents.reply(AGENT["_id"], conversation_id="conv_1", integration_identifier="slack-prod"),
        "POST",
        f"/v1/agents/{AGENT['_id']}/reply",
        200,
        {"data": {"messageId": "msg_1", "platformThreadId": "thread_1"}},
        body={"conversationId": "conv_1", "integrationIdentifier": "slack-prod"},
        parsed_type=SentMessageInfoDto,
    ),
]


def _mock_route(case: Case) -> respx.Route:
    response = httpx.Response(case.status, json=case.response) if case.response is not None else httpx.Response(
        case.status
    )
    return respx.route(method=case.method, url=f"{BASE_URL}{case.path}").mock(return_value=response)


def _assert_wire(case: Case, route: respx.Route) -> None:
    assert route.call_count == 1
    request = route.calls.last.request
    assert request.method == case.method
    assert request.url.path == case.path
    assert dict(request.url.params) == case.query
    assert request.headers["authorization"] == "ApiKey sk_test"
    for name, value in case.headers.items():
        assert request.headers[name] == value
    if case.body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == case.body


def test_the_table_covers_every_agents_operation_in_the_spec() -> None:
    spec = json.loads((Path(__file__).parent.parent / "openapi.json").read_text(encoding="utf-8"))
    agents_operations = {
        operation["operationId"]
        for path_item in spec["paths"].values()
        for operation in path_item.values()
        if isinstance(operation, dict) and "Agents" in operation.get("tags", [])
    }

    assert len(CASES) == len(agents_operations) == 11
    assert {case.operation_id for case in CASES} == agents_operations


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.operation_id)
@respx.mock
def test_sync_call_reaches_the_wire_and_parses_the_response(case: Case) -> None:
    route = _mock_route(case)

    result = case.call(_notifly())

    _assert_wire(case, route)
    if case.parsed_type is not None:
        assert isinstance(result, case.parsed_type)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.operation_id)
@respx.mock
async def test_async_call_reaches_the_wire_and_parses_the_response(case: Case) -> None:
    route = _mock_route(case)

    awaited = case.call(_async_notifly())
    assert inspect.isawaitable(awaited)
    result = await awaited

    _assert_wire(case, route)
    if case.parsed_type is not None:
        assert isinstance(result, case.parsed_type)


def test_the_async_agents_resource_mirrors_the_sync_one() -> None:
    sync_methods = {name for name in dir(_notifly().agents) if not name.startswith("_")}
    async_methods = {name for name in dir(_async_notifly().agents) if not name.startswith("_")}

    assert sync_methods == async_methods
    assert {"create", "get", "update", "delete", "list", "iter_all", "update_bridge", "reply"} <= sync_methods
    assert {"add_integration", "list_integrations", "iter_integrations", "update_integration"} <= sync_methods
    assert "remove_integration" in sync_methods


@respx.mock
def test_idempotency_key_is_sent_when_supplied() -> None:
    route = respx.patch(f"{BASE_URL}/v1/agents/support-bot").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )

    _notifly().agents.update("support-bot", name="Support bot v2", idempotency_key="idem_1")

    assert route.calls.last.request.headers["idempotency-key"] == "idem_1"


@respx.mock
def test_an_unknown_agent_raises_a_typed_error() -> None:
    respx.get(f"{BASE_URL}/v1/agents/missing").mock(
        return_value=httpx.Response(
            404,
            json={
                "statusCode": 404,
                "timestamp": "2026-10-12T10:00:00.000Z",
                "path": "/v1/agents/missing",
                "message": "Agent not found",
            },
        )
    )

    with pytest.raises(NotFoundError):
        _notifly().agents.get("missing")


# --------------------------------------------------------------------------------------
# create
# --------------------------------------------------------------------------------------
@respx.mock
def test_create_accepts_a_prebuilt_dto_and_a_mapping() -> None:
    route = respx.post(f"{BASE_URL}/v1/agents").mock(return_value=httpx.Response(201, json={"data": AGENT}))
    notifly = _notifly()

    notifly.agents.create(CreateAgentRequestDto(name="A", identifier="a", active=False))
    notifly.agents.create({"name": "B", "identifier": "b", "description": "second"})

    first, second = (json.loads(call.request.content) for call in route.calls)
    assert first == {"name": "A", "identifier": "a", "active": False}
    assert second == {"name": "B", "identifier": "b", "description": "second"}


@respx.mock
def test_create_overrides_the_analytics_source_header() -> None:
    route = respx.post(f"{BASE_URL}/v1/agents").mock(return_value=httpx.Response(201, json={"data": AGENT}))

    _notifly().agents.create(name="A", identifier="a", analytics_source="my-integration")

    assert route.calls.last.request.headers["novu-analytics-source"] == "my-integration"


@respx.mock
def test_create_builds_nested_runtime_fields_from_plain_values() -> None:
    route = respx.post(f"{BASE_URL}/v1/agents").mock(return_value=httpx.Response(201, json={"data": AGENT}))

    _notifly().agents.create(
        name="A",
        identifier="a",
        runtime="managed",
        managed_runtime={"providerId": "anthropic", "integrationId": "int_1"},
    )

    body = json.loads(route.calls.last.request.content)
    assert body["runtime"] == CreateAgentRequestDtoRuntime.MANAGED.value
    assert body["managedRuntime"] == {"providerId": "anthropic", "integrationId": "int_1"}


def test_create_without_the_required_fields_fails_fast() -> None:
    with pytest.raises(TypeError):
        _notifly().agents.create(name="A")


# --------------------------------------------------------------------------------------
# update: only what the caller passed
# --------------------------------------------------------------------------------------
@respx.mock
def test_update_sends_only_the_fields_the_caller_passed() -> None:
    route = respx.patch(f"{BASE_URL}/v1/agents/support-bot").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )

    _notifly().agents.update("support-bot", description="Answers support questions")

    assert json.loads(route.calls.last.request.content) == {"description": "Answers support questions"}


@respx.mock
def test_update_keeps_an_explicit_false() -> None:
    route = respx.patch(f"{BASE_URL}/v1/agents/support-bot").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )

    _notifly().agents.update("support-bot", active=False)

    assert json.loads(route.calls.last.request.content) == {"active": False}


@respx.mock
def test_update_builds_the_behavior_from_a_mapping_without_resending_its_defaults() -> None:
    route = respx.patch(f"{BASE_URL}/v1/agents/support-bot").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )

    _notifly().agents.update("support-bot", behavior={"subscriberAccess": "restricted"})

    assert json.loads(route.calls.last.request.content) == {"behavior": {"subscriberAccess": "restricted"}}


@respx.mock
def test_update_with_a_behavior_model_sends_only_its_set_fields_and_null_still_disables_the_reaction() -> None:
    route = respx.patch(f"{BASE_URL}/v1/agents/support-bot").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )
    notifly = _notifly()

    notifly.agents.update(
        "support-bot",
        behavior=AgentBehaviorDto(subscriber_access=AgentBehaviorDtoSubscriberAccess.OPEN),
    )
    notifly.agents.update("support-bot", UpdateAgentRequestDto(behavior=AgentBehaviorDto(reaction_on_resolved=None)))

    first, second = (json.loads(call.request.content) for call in route.calls)
    assert first == {"behavior": {"subscriberAccess": "open"}}
    assert second == {"behavior": {"reactionOnResolved": None}}


@respx.mock
def test_update_bridge_sends_only_the_fields_the_caller_passed() -> None:
    route = respx.put(f"{BASE_URL}/v1/agents/support-bot/bridge").mock(
        return_value=httpx.Response(200, json={"data": AGENT})
    )

    _notifly().agents.update_bridge("support-bot", dev_bridge_active=False)

    assert json.loads(route.calls.last.request.content) == {"devBridgeActive": False}


# --------------------------------------------------------------------------------------
# delete / integrations
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("value", "expected"), [(True, "true"), (False, "false"), ("true", "true"), ("false", "false")]
)
@respx.mock
def test_delete_sends_delete_from_provider_as_the_string_the_api_expects(value: bool | str, expected: str) -> None:
    route = respx.delete(f"{BASE_URL}/v1/agents/support-bot").mock(return_value=httpx.Response(204))

    _notifly().agents.delete("support-bot", delete_from_provider=value)

    assert route.calls.last.request.url.params["deleteFromProvider"] == expected


@respx.mock
def test_add_integration_accepts_a_dto_and_the_provider_id_form() -> None:
    route = respx.post(f"{BASE_URL}/v1/agents/support-bot/integrations").mock(
        return_value=httpx.Response(201, json={"data": AGENT_INTEGRATION})
    )
    notifly = _notifly()

    notifly.agents.add_integration(
        "support-bot", body=AddAgentIntegrationRequestDto(integration_identifier="slack-prod")
    )
    notifly.agents.add_integration("support-bot", provider_id="novu-agent-email")

    first, second = (json.loads(call.request.content) for call in route.calls)
    assert first == {"integrationIdentifier": "slack-prod"}
    assert second == {"providerId": "novu-agent-email"}


@respx.mock
def test_reply_accepts_a_mapping_body() -> None:
    route = respx.post(f"{BASE_URL}/v1/agents/{AGENT['_id']}/reply").mock(
        return_value=httpx.Response(200, json={"data": {"messageId": "msg_1", "platformThreadId": "t_1"}})
    )

    _notifly().agents.reply(AGENT["_id"], {"conversationId": "conv_1", "integrationIdentifier": "slack-prod"})

    assert json.loads(route.calls.last.request.content) == {
        "conversationId": "conv_1",
        "integrationIdentifier": "slack-prod",
    }


# --------------------------------------------------------------------------------------
# pagination
# --------------------------------------------------------------------------------------
def _cursor_page(items: list[dict[str, Any]], next_cursor: str | None) -> dict[str, Any]:
    return {"data": {**page(items), "next": next_cursor}}


@respx.mock
def test_iter_all_follows_the_next_cursor_across_pages() -> None:
    route = respx.get(f"{BASE_URL}/v1/agents").mock(
        side_effect=[
            httpx.Response(200, json=_cursor_page([AGENT], "cursor_2")),
            httpx.Response(200, json=_cursor_page([{**AGENT, "identifier": "billing-bot"}], None)),
        ]
    )

    agents = list(_notifly().agents.iter_all(limit=1))

    assert [agent.identifier for agent in agents] == ["support-bot", "billing-bot"]
    assert [dict(call.request.url.params) for call in route.calls] == [
        {"limit": "1"},
        {"limit": "1", "after": "cursor_2"},
    ]


@respx.mock
async def test_async_iter_all_follows_the_next_cursor_across_pages() -> None:
    route = respx.get(f"{BASE_URL}/v1/agents").mock(
        side_effect=[
            httpx.Response(200, json=_cursor_page([AGENT], "cursor_2")),
            httpx.Response(200, json=_cursor_page([{**AGENT, "identifier": "billing-bot"}], None)),
        ]
    )

    agents = [agent async for agent in _async_notifly().agents.iter_all(limit=1)]

    assert [agent.identifier for agent in agents] == ["support-bot", "billing-bot"]
    assert route.call_count == 2


@respx.mock
def test_iter_integrations_follows_the_next_cursor_and_keeps_the_filters() -> None:
    other = {**AGENT_INTEGRATION, "_id": "6650f0a1c1a2b3d4e5f60bb2"}
    route = respx.get(f"{BASE_URL}/v1/agents/support-bot/integrations").mock(
        side_effect=[
            httpx.Response(200, json=_cursor_page([AGENT_INTEGRATION], "cursor_2")),
            httpx.Response(200, json=_cursor_page([other], None)),
        ]
    )

    integrations = list(
        _notifly().agents.iter_integrations("support-bot", limit=1, integration_identifier="slack-prod")
    )

    assert [item.field_id for item in integrations] == [
        AGENT_INTEGRATION["_id"],
        other["_id"],
    ]
    assert [dict(call.request.url.params) for call in route.calls] == [
        {"limit": "1", "integrationIdentifier": "slack-prod"},
        {"limit": "1", "integrationIdentifier": "slack-prod", "after": "cursor_2"},
    ]
