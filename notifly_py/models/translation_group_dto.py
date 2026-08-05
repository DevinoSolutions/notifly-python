from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type import ResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranslationGroupDto")


@_attrs_define
class TranslationGroupDto:
    """
    Attributes:
        resource_id (str): Resource identifier (slugified ID)
        resource_type (ResourceType): The resource type to associate translation with
        resource_name (str): Resource name (e.g., workflow name)
        locales (list[str]): Array of available locales for this resource
        created_at (str): Creation timestamp
        updated_at (str): Last update timestamp
        outdated_locales (list[str] | Unset): Locales that are outdated compared to the default locale (only present
            when there are outdated locales)
    """

    resource_id: str
    resource_type: ResourceType
    resource_name: str
    locales: list[str]
    created_at: str
    updated_at: str
    outdated_locales: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type = self.resource_type.value

        resource_name = self.resource_name

        locales = self.locales

        created_at = self.created_at

        updated_at = self.updated_at

        outdated_locales: list[str] | Unset = UNSET
        if not isinstance(self.outdated_locales, Unset):
            outdated_locales = self.outdated_locales

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "resourceType": resource_type,
                "resourceName": resource_name,
                "locales": locales,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if outdated_locales is not UNSET:
            field_dict["outdatedLocales"] = outdated_locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        resource_type = ResourceType(d.pop("resourceType"))

        resource_name = d.pop("resourceName")

        locales = cast(list[str], d.pop("locales"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        outdated_locales = cast(list[str], d.pop("outdatedLocales", UNSET))

        translation_group_dto = cls(
            resource_id=resource_id,
            resource_type=resource_type,
            resource_name=resource_name,
            locales=locales,
            created_at=created_at,
            updated_at=updated_at,
            outdated_locales=outdated_locales,
        )

        translation_group_dto.additional_properties = d
        return translation_group_dto

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
