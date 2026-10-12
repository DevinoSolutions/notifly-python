from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAgentBridgeRequestDto")


@_attrs_define
class UpdateAgentBridgeRequestDto:
    """
    Attributes:
        bridge_url (str | Unset): Production bridge URL for this agent
        dev_bridge_url (str | Unset): Development bridge URL (set by npx novu dev)
        dev_bridge_active (bool | Unset): Whether the dev bridge override is active
    """

    bridge_url: str | Unset = UNSET
    dev_bridge_url: str | Unset = UNSET
    dev_bridge_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_url = self.bridge_url

        dev_bridge_url = self.dev_bridge_url

        dev_bridge_active = self.dev_bridge_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bridge_url is not UNSET:
            field_dict["bridgeUrl"] = bridge_url
        if dev_bridge_url is not UNSET:
            field_dict["devBridgeUrl"] = dev_bridge_url
        if dev_bridge_active is not UNSET:
            field_dict["devBridgeActive"] = dev_bridge_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge_url = d.pop("bridgeUrl", UNSET)

        dev_bridge_url = d.pop("devBridgeUrl", UNSET)

        dev_bridge_active = d.pop("devBridgeActive", UNSET)

        update_agent_bridge_request_dto = cls(
            bridge_url=bridge_url,
            dev_bridge_url=dev_bridge_url,
            dev_bridge_active=dev_bridge_active,
        )

        update_agent_bridge_request_dto.additional_properties = d
        return update_agent_bridge_request_dto

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
