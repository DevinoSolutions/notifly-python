from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InBoundParseDomainDto")


@_attrs_define
class InBoundParseDomainDto:
    """
    Attributes:
        inbound_parse_domain (str | Unset):
    """

    inbound_parse_domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_parse_domain = self.inbound_parse_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_parse_domain is not UNSET:
            field_dict["inboundParseDomain"] = inbound_parse_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbound_parse_domain = d.pop("inboundParseDomain", UNSET)

        in_bound_parse_domain_dto = cls(
            inbound_parse_domain=inbound_parse_domain,
        )

        in_bound_parse_domain_dto.additional_properties = d
        return in_bound_parse_domain_dto

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
