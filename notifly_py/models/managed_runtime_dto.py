from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_runtime_dto_provider_id import ManagedRuntimeDtoProviderId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_skill_input_dto import AgentSkillInputDto


T = TypeVar("T", bound="ManagedRuntimeDto")


@_attrs_define
class ManagedRuntimeDto:
    """
    Attributes:
        provider_id (ManagedRuntimeDtoProviderId):
        integration_id (str): ID of an existing Novu integration (kind: "agent") that holds the provider API key and
            provisioned environment. Create the integration first via POST /integrations.
        external_agent_id (str | Unset): ID of an existing agent on the provider platform. When set, Novu adopts the
            agent instead of creating a new one.
        external_environment_id (str | Unset): ID of an existing environment on the provider platform. When set, Novu
            adopts the environment.
        model (str | Unset):
        system_prompt (str | Unset):
        tools (list[str] | Unset):
        mcp_servers (list[str] | Unset):
        skills (list[AgentSkillInputDto] | Unset):
    """

    provider_id: ManagedRuntimeDtoProviderId
    integration_id: str
    external_agent_id: str | Unset = UNSET
    external_environment_id: str | Unset = UNSET
    model: str | Unset = UNSET
    system_prompt: str | Unset = UNSET
    tools: list[str] | Unset = UNSET
    mcp_servers: list[str] | Unset = UNSET
    skills: list[AgentSkillInputDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id.value

        integration_id = self.integration_id

        external_agent_id = self.external_agent_id

        external_environment_id = self.external_environment_id

        model = self.model

        system_prompt = self.system_prompt

        tools: list[str] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools

        mcp_servers: list[str] | Unset = UNSET
        if not isinstance(self.mcp_servers, Unset):
            mcp_servers = self.mcp_servers

        skills: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = []
            for skills_item_data in self.skills:
                skills_item = skills_item_data.to_dict()
                skills.append(skills_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "integrationId": integration_id,
            }
        )
        if external_agent_id is not UNSET:
            field_dict["externalAgentId"] = external_agent_id
        if external_environment_id is not UNSET:
            field_dict["externalEnvironmentId"] = external_environment_id
        if model is not UNSET:
            field_dict["model"] = model
        if system_prompt is not UNSET:
            field_dict["systemPrompt"] = system_prompt
        if tools is not UNSET:
            field_dict["tools"] = tools
        if mcp_servers is not UNSET:
            field_dict["mcpServers"] = mcp_servers
        if skills is not UNSET:
            field_dict["skills"] = skills

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_skill_input_dto import AgentSkillInputDto

        d = dict(src_dict)
        provider_id = ManagedRuntimeDtoProviderId(d.pop("providerId"))

        integration_id = d.pop("integrationId")

        external_agent_id = d.pop("externalAgentId", UNSET)

        external_environment_id = d.pop("externalEnvironmentId", UNSET)

        model = d.pop("model", UNSET)

        system_prompt = d.pop("systemPrompt", UNSET)

        tools = cast(list[str], d.pop("tools", UNSET))

        mcp_servers = cast(list[str], d.pop("mcpServers", UNSET))

        _skills = d.pop("skills", UNSET)
        skills: list[AgentSkillInputDto] | Unset = UNSET
        if _skills is not UNSET:
            skills = []
            for skills_item_data in _skills:
                skills_item = AgentSkillInputDto.from_dict(skills_item_data)

                skills.append(skills_item)

        managed_runtime_dto = cls(
            provider_id=provider_id,
            integration_id=integration_id,
            external_agent_id=external_agent_id,
            external_environment_id=external_environment_id,
            model=model,
            system_prompt=system_prompt,
            tools=tools,
            mcp_servers=mcp_servers,
            skills=skills,
        )

        managed_runtime_dto.additional_properties = d
        return managed_runtime_dto

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
