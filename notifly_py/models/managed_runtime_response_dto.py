from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_mcp_server_dto import AgentMcpServerDto
    from ..models.agent_tool_dto import AgentToolDto


T = TypeVar("T", bound="ManagedRuntimeResponseDto")


@_attrs_define
class ManagedRuntimeResponseDto:
    """
    Attributes:
        provider_id (str):
        integration_id (str):
        external_agent_id (str):
        external_environment_id (str | Unset): The provider-side environment that hosts this agent. Hydrated from the
            linked integration credentials. Absent when the integration has not been provisioned.
        external_workspace_id (str | Unset): The provider-side workspace id used in console deep links. Defaults to
            `'default'` (the auto-created Default Workspace). Hydrated from the linked integration credentials.
        console_url (str | Unset): Deep link to the agent in the provider console (e.g. platform.claude.com).
        tools (list[AgentToolDto] | Unset): Live tools enabled on the managed-runtime provider for this agent. Sourced
            from the provider on read; omitted when the provider is temporarily unreachable.
        mcp_servers (list[AgentMcpServerDto] | Unset): MCP servers enabled on this agent, projected onto the runtime
            catalog `{ externalId, name, url }` shape. Mongo is the source of truth; the projection matches what the
            provider sees. Omitted when the provider read fails after a managed-agent write.
        system_prompt (str | Unset): System prompt used when invoking the agent.
    """

    provider_id: str
    integration_id: str
    external_agent_id: str
    external_environment_id: str | Unset = UNSET
    external_workspace_id: str | Unset = UNSET
    console_url: str | Unset = UNSET
    tools: list[AgentToolDto] | Unset = UNSET
    mcp_servers: list[AgentMcpServerDto] | Unset = UNSET
    system_prompt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        integration_id = self.integration_id

        external_agent_id = self.external_agent_id

        external_environment_id = self.external_environment_id

        external_workspace_id = self.external_workspace_id

        console_url = self.console_url

        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        mcp_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mcp_servers, Unset):
            mcp_servers = []
            for mcp_servers_item_data in self.mcp_servers:
                mcp_servers_item = mcp_servers_item_data.to_dict()
                mcp_servers.append(mcp_servers_item)

        system_prompt = self.system_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "integrationId": integration_id,
                "externalAgentId": external_agent_id,
            }
        )
        if external_environment_id is not UNSET:
            field_dict["externalEnvironmentId"] = external_environment_id
        if external_workspace_id is not UNSET:
            field_dict["externalWorkspaceId"] = external_workspace_id
        if console_url is not UNSET:
            field_dict["consoleUrl"] = console_url
        if tools is not UNSET:
            field_dict["tools"] = tools
        if mcp_servers is not UNSET:
            field_dict["mcpServers"] = mcp_servers
        if system_prompt is not UNSET:
            field_dict["systemPrompt"] = system_prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_mcp_server_dto import AgentMcpServerDto
        from ..models.agent_tool_dto import AgentToolDto

        d = dict(src_dict)
        provider_id = d.pop("providerId")

        integration_id = d.pop("integrationId")

        external_agent_id = d.pop("externalAgentId")

        external_environment_id = d.pop("externalEnvironmentId", UNSET)

        external_workspace_id = d.pop("externalWorkspaceId", UNSET)

        console_url = d.pop("consoleUrl", UNSET)

        _tools = d.pop("tools", UNSET)
        tools: list[AgentToolDto] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = AgentToolDto.from_dict(tools_item_data)

                tools.append(tools_item)

        _mcp_servers = d.pop("mcpServers", UNSET)
        mcp_servers: list[AgentMcpServerDto] | Unset = UNSET
        if _mcp_servers is not UNSET:
            mcp_servers = []
            for mcp_servers_item_data in _mcp_servers:
                mcp_servers_item = AgentMcpServerDto.from_dict(mcp_servers_item_data)

                mcp_servers.append(mcp_servers_item)

        system_prompt = d.pop("systemPrompt", UNSET)

        managed_runtime_response_dto = cls(
            provider_id=provider_id,
            integration_id=integration_id,
            external_agent_id=external_agent_id,
            external_environment_id=external_environment_id,
            external_workspace_id=external_workspace_id,
            console_url=console_url,
            tools=tools,
            mcp_servers=mcp_servers,
            system_prompt=system_prompt,
        )

        managed_runtime_response_dto.additional_properties = d
        return managed_runtime_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
