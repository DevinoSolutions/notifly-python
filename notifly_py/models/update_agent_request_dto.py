from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_behavior_dto import AgentBehaviorDto


T = TypeVar("T", bound="UpdateAgentRequestDto")


@_attrs_define
class UpdateAgentRequestDto:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        active (bool | Unset):
        behavior (AgentBehaviorDto | Unset):
        bridge_url (str | Unset): Production bridge URL for this agent
        dev_bridge_url (str | Unset): Development bridge URL (set by npx novu dev)
        dev_bridge_active (bool | Unset): Whether the dev bridge override is active
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    active: bool | Unset = UNSET
    behavior: AgentBehaviorDto | Unset = UNSET
    bridge_url: str | Unset = UNSET
    dev_bridge_url: str | Unset = UNSET
    dev_bridge_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        active = self.active

        behavior: dict[str, Any] | Unset = UNSET
        if not isinstance(self.behavior, Unset):
            behavior = self.behavior.to_dict()

        bridge_url = self.bridge_url

        dev_bridge_url = self.dev_bridge_url

        dev_bridge_active = self.dev_bridge_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if behavior is not UNSET:
            field_dict["behavior"] = behavior
        if bridge_url is not UNSET:
            field_dict["bridgeUrl"] = bridge_url
        if dev_bridge_url is not UNSET:
            field_dict["devBridgeUrl"] = dev_bridge_url
        if dev_bridge_active is not UNSET:
            field_dict["devBridgeActive"] = dev_bridge_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_behavior_dto import AgentBehaviorDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        _behavior = d.pop("behavior", UNSET)
        behavior: AgentBehaviorDto | Unset
        if isinstance(_behavior, Unset):
            behavior = UNSET
        else:
            behavior = AgentBehaviorDto.from_dict(_behavior)

        bridge_url = d.pop("bridgeUrl", UNSET)

        dev_bridge_url = d.pop("devBridgeUrl", UNSET)

        dev_bridge_active = d.pop("devBridgeActive", UNSET)

        update_agent_request_dto = cls(
            name=name,
            description=description,
            active=active,
            behavior=behavior,
            bridge_url=bridge_url,
            dev_bridge_url=dev_bridge_url,
            dev_bridge_active=dev_bridge_active,
        )

        update_agent_request_dto.additional_properties = d
        return update_agent_request_dto

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
