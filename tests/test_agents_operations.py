"""The Agents API (API 3.19): request shape and response parsing for all eleven operations.

Every case drives the generated module through the real client stack from ``conftest`` (retries ->
envelope unwrap -> a recording transport), so the assertions cover what actually goes on the wire:
method, path, query string, headers and JSON body, and what ``parsed`` comes back as for the
``{"data": ...}``-wrapped bodies the API really sends.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

from notifly_py.api.agents import (
    agent_integrations_controller_add_agent_integration,
    agent_integrations_controller_list_agent_integrations,
    agent_integrations_controller_remove_agent_integration,
    agent_integrations_controller_update_agent_integration,
    agent_reply_controller_handle_agent_reply_handler,
    agents_controller_create_agent,
    agents_controller_delete_agent,
    agents_controller_get_agent,
    agents_controller_list_agents,
    agents_controller_update_agent,
    agents_controller_update_agent_bridge,
)
from notifly_py.models import (
    AddAgentIntegrationRequestDto,
    AgentBehaviorDto,
    AgentBehaviorDtoSubscriberAccess,
    AgentIntegrationResponseDto,
    AgentReplyPayloadDto,
    AgentResponseDto,
    CreateAgentRequestDto,
    ListAgentIntegrationsResponseDto,
    ListAgentsResponseDto,
    ManagedRuntimeDto,
    ManagedRuntimeDtoProviderId,
    SentMessageInfoDto,
    UpdateAgentBridgeRequestDto,
    UpdateAgentIntegrationRequestDto,
    UpdateAgentRequestDto,
)

from .conftest import SECRET_KEY, json_response

TIMESTAMP = "2026-10-12T10:00:00.000Z"

AGENT = {
    "_id": "6650f0a1c1a2b3d4e5f60aa1",
    "name": "Support bot",
    "identifier": "support-bot",
    "behavior": {"acknowledgeOnReceived": True, "reactionOnResolved": "check", "subscriberAccess": "open"},
    "active": True,
    "_environmentId": "env_1",
    "_organizationId": "org_1",
    "createdAt": TIMESTAMP,
    "updatedAt": TIMESTAMP,
}

AGENT_INTEGRATION = {
    "_id": "6650f0a1c1a2b3d4e5f60bb1",
    "_agentId": AGENT["_id"],
    "integration": {
        "_id": "6650f0a1c1a2b3d4e5f60cc1",
        "identifier": "slack-prod",
        "name": "Slack (prod)",
        "providerId": "slack",
        "active": True,
    },
    "_environmentId": "env_1",
    "_organizationId": "org_1",
    "createdAt": TIMESTAMP,
    "updatedAt": TIMESTAMP,
}


def scripted_response(case: Case) -> Any:
    """The response the recording transport replays: the case's wire body, or an empty one (204)."""
    return json_response(case.status, case.wire_response if case.wire_response is not None else {})


def page(items: list[dict[str, Any]]) -> dict[str, Any]:
    """A cursor page as the API returns it inside the ``data`` envelope."""
    return {"data": items, "next": None, "previous": None, "totalCount": len(items), "totalCountCapped": False}


@dataclass
class Case:
    """One operation: how to call it, and what must reach the wire / come back."""

    operation_id: str
    module: ModuleType
    kwargs: Callable[[], dict[str, Any]]
    method: str
    path: str
    status: int
    wire_response: Any
    query: dict[str, str] = field(default_factory=dict)
    request_body: dict[str, Any] | None = None
    headers: dict[str, str] = field(default_factory=dict)
    parsed_type: type | None = None


CASES = [
    Case(
        "AgentsController_createAgent",
        agents_controller_create_agent,
        lambda: {
            "body": CreateAgentRequestDto(name="Support bot", identifier="support-bot"),
            "novu_analytics_source": "sdk-test",
        },
        "POST",
        "/v1/agents",
        201,
        {"data": AGENT},
        request_body={"name": "Support bot", "identifier": "support-bot", "active": True},
        headers={"novu-analytics-source": "sdk-test"},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_listAgents",
        agents_controller_list_agents,
        lambda: {"limit": 5, "identifier": "support-bot"},
        "GET",
        "/v1/agents",
        200,
        {"data": page([AGENT])},
        query={"limit": "5", "identifier": "support-bot"},
        parsed_type=ListAgentsResponseDto,
    ),
    Case(
        "AgentsController_getAgent",
        agents_controller_get_agent,
        lambda: {"identifier": "support-bot"},
        "GET",
        "/v1/agents/support-bot",
        200,
        {"data": AGENT},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_updateAgent",
        agents_controller_update_agent,
        lambda: {
            "identifier": "support-bot",
            "body": UpdateAgentRequestDto(
                name="Support bot v2", behavior=AgentBehaviorDto(reaction_on_resolved="star")
            ),
        },
        "PATCH",
        "/v1/agents/support-bot",
        200,
        {"data": AGENT},
        request_body={
            "name": "Support bot v2",
            "behavior": {"acknowledgeOnReceived": True, "reactionOnResolved": "star"},
        },
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentsController_deleteAgent",
        agents_controller_delete_agent,
        lambda: {"identifier": "support-bot", "delete_from_provider": "false"},
        "DELETE",
        "/v1/agents/support-bot",
        204,
        None,
        query={"deleteFromProvider": "false"},
    ),
    Case(
        "AgentsController_updateAgentBridge",
        agents_controller_update_agent_bridge,
        lambda: {
            "identifier": "support-bot",
            "body": UpdateAgentBridgeRequestDto(bridge_url="https://bot.example.com/api/notifly", dev_bridge_active=False),
        },
        "PUT",
        "/v1/agents/support-bot/bridge",
        200,
        {"data": AGENT},
        request_body={"bridgeUrl": "https://bot.example.com/api/notifly", "devBridgeActive": False},
        parsed_type=AgentResponseDto,
    ),
    Case(
        "AgentIntegrationsController_addAgentIntegration",
        agent_integrations_controller_add_agent_integration,
        lambda: {
            "identifier": "support-bot",
            "body": AddAgentIntegrationRequestDto(integration_identifier="slack-prod"),
        },
        "POST",
        "/v1/agents/support-bot/integrations",
        201,
        {"data": AGENT_INTEGRATION},
        request_body={"integrationIdentifier": "slack-prod"},
        parsed_type=AgentIntegrationResponseDto,
    ),
    Case(
        "AgentIntegrationsController_listAgentIntegrations",
        agent_integrations_controller_list_agent_integrations,
        lambda: {"identifier": "support-bot", "integration_identifier": "slack-prod", "include_cursor": True},
        "GET",
        "/v1/agents/support-bot/integrations",
        200,
        {"data": page([AGENT_INTEGRATION])},
        query={"integrationIdentifier": "slack-prod", "includeCursor": "true"},
        parsed_type=ListAgentIntegrationsResponseDto,
    ),
    Case(
        "AgentIntegrationsController_updateAgentIntegration",
        agent_integrations_controller_update_agent_integration,
        lambda: {
            "identifier": "support-bot",
            "agent_integration_id": AGENT_INTEGRATION["_id"],
            "body": UpdateAgentIntegrationRequestDto(integration_identifier="slack-staging"),
        },
        "PATCH",
        f"/v1/agents/support-bot/integrations/{AGENT_INTEGRATION['_id']}",
        200,
        {"data": AGENT_INTEGRATION},
        request_body={"integrationIdentifier": "slack-staging"},
        parsed_type=AgentIntegrationResponseDto,
    ),
    Case(
        "AgentIntegrationsController_removeAgentIntegration",
        agent_integrations_controller_remove_agent_integration,
        lambda: {"identifier": "support-bot", "agent_integration_id": AGENT_INTEGRATION["_id"]},
        "DELETE",
        f"/v1/agents/support-bot/integrations/{AGENT_INTEGRATION['_id']}",
        204,
        None,
    ),
    Case(
        "AgentReplyController_handleAgentReplyHandler",
        agent_reply_controller_handle_agent_reply_handler,
        lambda: {
            "agent_id": AGENT["_id"],
            "body": AgentReplyPayloadDto(conversation_id="conv_1", integration_identifier="slack-prod"),
        },
        "POST",
        f"/v1/agents/{AGENT['_id']}/reply",
        200,
        {"data": {"messageId": "msg_1", "platformThreadId": "thread_1"}},
        request_body={"conversationId": "conv_1", "integrationIdentifier": "slack-prod"},
        parsed_type=SentMessageInfoDto,
    ),
]


def test_the_table_covers_every_agents_operation_in_the_spec() -> None:
    spec = json.loads((Path(__file__).parent.parent / "openapi.json").read_text(encoding="utf-8"))
    agents_operations = {
        operation["operationId"]
        for path_item in spec["paths"].values()
        for operation in path_item.values()
        if isinstance(operation, dict) and "Agents" in operation.get("tags", [])
    }

    assert len(agents_operations) == 11
    assert {case.operation_id for case in CASES} == agents_operations


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.operation_id)
def test_request_reaches_the_wire_with_the_right_method_path_query_and_body(
    case: Case, client_factory: Any
) -> None:
    client, recorder = client_factory(scripted_response(case))

    case.module.sync_detailed(client=client, **case.kwargs())

    request = recorder.request
    assert request.method == case.method
    assert request.url.path == case.path
    assert dict(request.url.params) == case.query
    assert request.headers["authorization"] == f"ApiKey {SECRET_KEY}"
    for name, value in case.headers.items():
        assert request.headers[name] == value
    if case.request_body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == case.request_body


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.operation_id)
def test_response_is_parsed_into_the_declared_model_through_the_data_envelope(
    case: Case, client_factory: Any
) -> None:
    client, _ = client_factory(scripted_response(case))

    result = case.module.sync_detailed(client=client, **case.kwargs())

    assert result.status_code == case.status
    if case.parsed_type is None:
        assert result.parsed is None
    else:
        assert isinstance(result.parsed, case.parsed_type)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.operation_id)
def test_idempotency_key_header_is_sent_when_supplied(case: Case, client_factory: Any) -> None:
    client, recorder = client_factory(scripted_response(case))

    case.module.sync_detailed(client=client, idempotency_key="idem-1", **case.kwargs())

    assert recorder.request.headers["idempotency-key"] == "idem-1"


def test_parsed_agent_exposes_the_documented_fields(client_factory: Any) -> None:
    client, _ = client_factory(json_response(200, {"data": AGENT}))

    agent = agents_controller_get_agent.sync(identifier="support-bot", client=client)

    assert isinstance(agent, AgentResponseDto)
    assert agent.identifier == "support-bot"
    assert agent.behavior.reaction_on_resolved == "check"
    assert agent.behavior.subscriber_access is AgentBehaviorDtoSubscriberAccess.OPEN
    assert agent.active is True


def test_parsed_list_exposes_cursor_fields_and_agents(client_factory: Any) -> None:
    client, _ = client_factory(json_response(200, {"data": page([AGENT, {**AGENT, "identifier": "billing-bot"}])}))

    result = agents_controller_list_agents.sync(client=client)

    assert isinstance(result, ListAgentsResponseDto)
    assert [agent.identifier for agent in result.data] == ["support-bot", "billing-bot"]
    assert result.total_count == 2


def test_an_unknown_agent_comes_back_as_an_unparsed_404_not_an_exception(client_factory: Any) -> None:
    """Generated modules never raise on HTTP errors (only the facade does) — the status is the signal."""
    client, _ = client_factory(
        json_response(
            404,
            {"statusCode": 404, "timestamp": TIMESTAMP, "path": "/v1/agents/nope", "message": "Agent not found"},
        )
    )

    result = agents_controller_get_agent.sync_detailed(identifier="nope", client=client)

    assert result.status_code == 404


async def test_async_variant_sends_the_same_request(client_factory: Any) -> None:
    client, recorder = client_factory(json_response(200, {"data": page([AGENT])}))

    result = await agents_controller_list_agents.asyncio_detailed(client=client, limit=1)

    assert recorder.request.method == "GET"
    assert recorder.request.url.path == "/v1/agents"
    assert dict(recorder.request.url.params) == {"limit": "1"}
    assert isinstance(result.parsed, ListAgentsResponseDto)


# --------------------------------------------------------------------------------------
# Models: from_dict / to_dict round trips on realistic payloads
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("model", "payload"),
    [
        (AgentResponseDto, AGENT),
        (
            AgentResponseDto,
            {**AGENT, "behavior": {"reactionOnResolved": None}, "bridgeUrl": "https://bot.example.com/api/notifly"},
        ),
        (AgentIntegrationResponseDto, AGENT_INTEGRATION),
        (ListAgentsResponseDto, page([AGENT])),
        (ListAgentIntegrationsResponseDto, page([AGENT_INTEGRATION])),
        (
            CreateAgentRequestDto,
            {
                "name": "Managed bot",
                "identifier": "managed-bot",
                "active": False,
                "managedRuntime": {"providerId": "anthropic", "integrationId": "int_1", "model": "claude-sonnet-5-5"},
            },
        ),
        (
            UpdateAgentRequestDto,
            {"behavior": {"acknowledgeOnReceived": False, "subscriberAccess": "restricted"}, "devBridgeActive": True},
        ),
        (AgentReplyPayloadDto, {"conversationId": "conv_1", "integrationIdentifier": "slack-prod", "error": False}),
        (SentMessageInfoDto, {"messageId": "msg_1", "platformThreadId": "thread_1"}),
    ],
    ids=lambda value: value.__name__ if isinstance(value, type) else "",
)
def test_models_round_trip_through_from_dict_and_to_dict(model: Any, payload: dict[str, Any]) -> None:
    parsed = model.from_dict(payload)

    assert parsed.to_dict() == payload


def test_a_null_reaction_on_resolved_survives_the_round_trip_instead_of_becoming_the_default() -> None:
    """``null`` disables the reaction; the model must not swap it for the schema default ``"check"``."""
    parsed = AgentBehaviorDto.from_dict({"reactionOnResolved": None})

    assert parsed.reaction_on_resolved is None
    assert parsed.to_dict() == {"reactionOnResolved": None}


def test_managed_runtime_nests_inside_the_create_request() -> None:
    request = CreateAgentRequestDto(
        name="Managed bot",
        identifier="managed-bot",
        managed_runtime=ManagedRuntimeDto(provider_id=ManagedRuntimeDtoProviderId.ANTHROPIC, integration_id="int_1"),
    )

    assert request.to_dict()["managedRuntime"] == {"providerId": "anthropic", "integrationId": "int_1"}
