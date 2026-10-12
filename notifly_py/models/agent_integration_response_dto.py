from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_integration_response_dto_connected_at_type_0 import AgentIntegrationResponseDtoConnectedAtType0
    from ..models.agent_integration_response_integration_dto import AgentIntegrationResponseIntegrationDto


T = TypeVar("T", bound="AgentIntegrationResponseDto")


@_attrs_define
class AgentIntegrationResponseDto:
    """
    Attributes:
        field_id (str): Agent–integration link document id.
        field_agent_id (str):
        integration (AgentIntegrationResponseIntegrationDto):
        field_environment_id (str):
        field_organization_id (str):
        created_at (str):
        updated_at (str):
        connected_at (AgentIntegrationResponseDtoConnectedAtType0 | None | Unset): Set when the agent–integration link
            received its first inbound webhook delivery.
        exceeds_plan_limit (bool | Unset): Cloud only. `true` when this channel type (provider) falls outside the
            organization plan active-channel limit (by connection order). Active channels are counted per channel type, so
            multiple integrations of the same provider (e.g. several Slack workspaces) count as a single active channel.
            Over-limit channels keep their configuration but the agent will not respond on them until the plan is upgraded
            or older channel types are disconnected.
    """

    field_id: str
    field_agent_id: str
    integration: AgentIntegrationResponseIntegrationDto
    field_environment_id: str
    field_organization_id: str
    created_at: str
    updated_at: str
    connected_at: AgentIntegrationResponseDtoConnectedAtType0 | None | Unset = UNSET
    exceeds_plan_limit: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_integration_response_dto_connected_at_type_0 import (
            AgentIntegrationResponseDtoConnectedAtType0,
        )

        field_id = self.field_id

        field_agent_id = self.field_agent_id

        integration = self.integration.to_dict()

        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        created_at = self.created_at

        updated_at = self.updated_at

        connected_at: dict[str, Any] | None | Unset
        if isinstance(self.connected_at, Unset):
            connected_at = UNSET
        elif isinstance(self.connected_at, AgentIntegrationResponseDtoConnectedAtType0):
            connected_at = self.connected_at.to_dict()
        else:
            connected_at = self.connected_at

        exceeds_plan_limit = self.exceeds_plan_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "_agentId": field_agent_id,
                "integration": integration,
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if exceeds_plan_limit is not UNSET:
            field_dict["exceedsPlanLimit"] = exceeds_plan_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_integration_response_dto_connected_at_type_0 import (
            AgentIntegrationResponseDtoConnectedAtType0,
        )
        from ..models.agent_integration_response_integration_dto import AgentIntegrationResponseIntegrationDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        field_agent_id = d.pop("_agentId")

        integration = AgentIntegrationResponseIntegrationDto.from_dict(d.pop("integration"))

        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_connected_at(data: object) -> AgentIntegrationResponseDtoConnectedAtType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connected_at_type_0 = AgentIntegrationResponseDtoConnectedAtType0.from_dict(data)

                return connected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentIntegrationResponseDtoConnectedAtType0 | None | Unset, data)

        connected_at = _parse_connected_at(d.pop("connectedAt", UNSET))

        exceeds_plan_limit = d.pop("exceedsPlanLimit", UNSET)

        agent_integration_response_dto = cls(
            field_id=field_id,
            field_agent_id=field_agent_id,
            integration=integration,
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            created_at=created_at,
            updated_at=updated_at,
            connected_at=connected_at,
            exceeds_plan_limit=exceeds_plan_limit,
        )

        agent_integration_response_dto.additional_properties = d
        return agent_integration_response_dto

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
