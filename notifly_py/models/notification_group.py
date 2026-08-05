from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationGroup")


@_attrs_define
class NotificationGroup:
    """
    Attributes:
        name (str):
        field_environment_id (str):
        field_organization_id (str):
        field_id (str | Unset):
        field_parent_id (str | Unset):
    """

    name: str
    field_environment_id: str
    field_organization_id: str
    field_id: str | Unset = UNSET
    field_parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        field_id = self.field_id

        field_parent_id = self.field_parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if field_parent_id is not UNSET:
            field_dict["_parentId"] = field_parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        field_id = d.pop("_id", UNSET)

        field_parent_id = d.pop("_parentId", UNSET)

        notification_group = cls(
            name=name,
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            field_id=field_id,
            field_parent_id=field_parent_id,
        )

        notification_group.additional_properties = d
        return notification_group

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
