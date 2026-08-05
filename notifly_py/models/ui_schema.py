from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ui_schema_group_enum import UiSchemaGroupEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_schema_properties import UiSchemaProperties


T = TypeVar("T", bound="UiSchema")


@_attrs_define
class UiSchema:
    """
    Attributes:
        group (UiSchemaGroupEnum | Unset): Group of the UI Schema
        properties (UiSchemaProperties | Unset): Properties of the UI Schema
    """

    group: UiSchemaGroupEnum | Unset = UNSET
    properties: UiSchemaProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: str | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.value

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_schema_properties import UiSchemaProperties

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: UiSchemaGroupEnum | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = UiSchemaGroupEnum(_group)

        _properties = d.pop("properties", UNSET)
        properties: UiSchemaProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = UiSchemaProperties.from_dict(_properties)

        ui_schema = cls(
            group=group,
            properties=properties,
        )

        ui_schema.additional_properties = d
        return ui_schema

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
