from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_configuration_dto import BridgeConfigurationDto
    from ..models.in_bound_parse_domain_dto import InBoundParseDomainDto


T = TypeVar("T", bound="UpdateEnvironmentRequestDto")


@_attrs_define
class UpdateEnvironmentRequestDto:
    """
    Attributes:
        name (str | Unset):
        identifier (str | Unset):
        parent_id (str | Unset):
        color (str | Unset):
        dns (InBoundParseDomainDto | Unset):
        bridge (BridgeConfigurationDto | Unset):
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    color: str | Unset = UNSET
    dns: InBoundParseDomainDto | Unset = UNSET
    bridge: BridgeConfigurationDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        parent_id = self.parent_id

        color = self.color

        dns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        bridge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bridge, Unset):
            bridge = self.bridge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if color is not UNSET:
            field_dict["color"] = color
        if dns is not UNSET:
            field_dict["dns"] = dns
        if bridge is not UNSET:
            field_dict["bridge"] = bridge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_configuration_dto import BridgeConfigurationDto
        from ..models.in_bound_parse_domain_dto import InBoundParseDomainDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        parent_id = d.pop("parentId", UNSET)

        color = d.pop("color", UNSET)

        _dns = d.pop("dns", UNSET)
        dns: InBoundParseDomainDto | Unset
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = InBoundParseDomainDto.from_dict(_dns)

        _bridge = d.pop("bridge", UNSET)
        bridge: BridgeConfigurationDto | Unset
        if isinstance(_bridge, Unset):
            bridge = UNSET
        else:
            bridge = BridgeConfigurationDto.from_dict(_bridge)

        update_environment_request_dto = cls(
            name=name,
            identifier=identifier,
            parent_id=parent_id,
            color=color,
            dns=dns,
            bridge=bridge,
        )

        update_environment_request_dto.additional_properties = d
        return update_environment_request_dto

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
