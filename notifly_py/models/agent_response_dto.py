from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_response_dto_runtime import AgentResponseDtoRuntime
from ..models.agent_response_dto_visibility import AgentResponseDtoVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_behavior_dto import AgentBehaviorDto
    from ..models.agent_integration_summary_dto import AgentIntegrationSummaryDto
    from ..models.managed_runtime_response_dto import ManagedRuntimeResponseDto


T = TypeVar("T", bound="AgentResponseDto")


@_attrs_define
class AgentResponseDto:
    """
    Attributes:
        field_id (str):
        name (str):
        identifier (str):
        behavior (AgentBehaviorDto):
        active (bool):
        field_environment_id (str):
        field_organization_id (str):
        created_at (str):
        updated_at (str):
        description (str | Unset):
        bridge_url (str | Unset): Production bridge URL
        dev_bridge_url (str | Unset): Development bridge URL (set by npx novu dev)
        dev_bridge_active (bool | Unset): Whether the dev bridge override is active
        runtime (AgentResponseDtoRuntime | Unset): Whether the agent brain is self-hosted (bridge) or managed by a
            third-party provider
        visibility (AgentResponseDtoVisibility | Unset): Discovery scope of the agent. Always `public` today; reserved
            for the upcoming private-agents feature.
        managed_runtime (ManagedRuntimeResponseDto | Unset):
        created_by (str | Unset): Mongo user id of the user who created the agent
        integrations (list[AgentIntegrationSummaryDto] | Unset):
        exceeds_plan_limit (bool | Unset): Cloud only. `true` when the agent falls outside the organization plan agent
            limit (by creation order among active agents — inactive agents do not consume slots). Only plan limits produce
            this flag — system-capped organizations (enterprise/unlimited tiers) are never over-limit. Over-limit agents are
            still stored but will not respond to inbound messages until the plan is upgraded or older agents are
            deactivated.
    """

    field_id: str
    name: str
    identifier: str
    behavior: AgentBehaviorDto
    active: bool
    field_environment_id: str
    field_organization_id: str
    created_at: str
    updated_at: str
    description: str | Unset = UNSET
    bridge_url: str | Unset = UNSET
    dev_bridge_url: str | Unset = UNSET
    dev_bridge_active: bool | Unset = UNSET
    runtime: AgentResponseDtoRuntime | Unset = UNSET
    visibility: AgentResponseDtoVisibility | Unset = UNSET
    managed_runtime: ManagedRuntimeResponseDto | Unset = UNSET
    created_by: str | Unset = UNSET
    integrations: list[AgentIntegrationSummaryDto] | Unset = UNSET
    exceeds_plan_limit: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        name = self.name

        identifier = self.identifier

        behavior = self.behavior.to_dict()

        active = self.active

        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        created_at = self.created_at

        updated_at = self.updated_at

        description = self.description

        bridge_url = self.bridge_url

        dev_bridge_url = self.dev_bridge_url

        dev_bridge_active = self.dev_bridge_active

        runtime: str | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.value

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        managed_runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.managed_runtime, Unset):
            managed_runtime = self.managed_runtime.to_dict()

        created_by = self.created_by

        integrations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = []
            for integrations_item_data in self.integrations:
                integrations_item = integrations_item_data.to_dict()
                integrations.append(integrations_item)

        exceeds_plan_limit = self.exceeds_plan_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "name": name,
                "identifier": identifier,
                "behavior": behavior,
                "active": active,
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if bridge_url is not UNSET:
            field_dict["bridgeUrl"] = bridge_url
        if dev_bridge_url is not UNSET:
            field_dict["devBridgeUrl"] = dev_bridge_url
        if dev_bridge_active is not UNSET:
            field_dict["devBridgeActive"] = dev_bridge_active
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if managed_runtime is not UNSET:
            field_dict["managedRuntime"] = managed_runtime
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if integrations is not UNSET:
            field_dict["integrations"] = integrations
        if exceeds_plan_limit is not UNSET:
            field_dict["exceedsPlanLimit"] = exceeds_plan_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_behavior_dto import AgentBehaviorDto
        from ..models.agent_integration_summary_dto import AgentIntegrationSummaryDto
        from ..models.managed_runtime_response_dto import ManagedRuntimeResponseDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        name = d.pop("name")

        identifier = d.pop("identifier")

        behavior = AgentBehaviorDto.from_dict(d.pop("behavior"))

        active = d.pop("active")

        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        description = d.pop("description", UNSET)

        bridge_url = d.pop("bridgeUrl", UNSET)

        dev_bridge_url = d.pop("devBridgeUrl", UNSET)

        dev_bridge_active = d.pop("devBridgeActive", UNSET)

        _runtime = d.pop("runtime", UNSET)
        runtime: AgentResponseDtoRuntime | Unset
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = AgentResponseDtoRuntime(_runtime)

        _visibility = d.pop("visibility", UNSET)
        visibility: AgentResponseDtoVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = AgentResponseDtoVisibility(_visibility)

        _managed_runtime = d.pop("managedRuntime", UNSET)
        managed_runtime: ManagedRuntimeResponseDto | Unset
        if isinstance(_managed_runtime, Unset):
            managed_runtime = UNSET
        else:
            managed_runtime = ManagedRuntimeResponseDto.from_dict(_managed_runtime)

        created_by = d.pop("createdBy", UNSET)

        _integrations = d.pop("integrations", UNSET)
        integrations: list[AgentIntegrationSummaryDto] | Unset = UNSET
        if _integrations is not UNSET:
            integrations = []
            for integrations_item_data in _integrations:
                integrations_item = AgentIntegrationSummaryDto.from_dict(integrations_item_data)

                integrations.append(integrations_item)

        exceeds_plan_limit = d.pop("exceedsPlanLimit", UNSET)

        agent_response_dto = cls(
            field_id=field_id,
            name=name,
            identifier=identifier,
            behavior=behavior,
            active=active,
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            bridge_url=bridge_url,
            dev_bridge_url=dev_bridge_url,
            dev_bridge_active=dev_bridge_active,
            runtime=runtime,
            visibility=visibility,
            managed_runtime=managed_runtime,
            created_by=created_by,
            integrations=integrations,
            exceeds_plan_limit=exceeds_plan_limit,
        )

        agent_response_dto.additional_properties = d
        return agent_response_dto

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
