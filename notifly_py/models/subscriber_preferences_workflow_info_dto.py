from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberPreferencesWorkflowInfoDto")


@_attrs_define
class SubscriberPreferencesWorkflowInfoDto:
    """
    Attributes:
        slug (str): Workflow slug
        identifier (str): Unique identifier of the workflow
        name (str): Display name of the workflow
        updated_at (str | Unset): last updated date
    """

    slug: str
    identifier: str
    name: str
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        identifier = self.identifier

        name = self.name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "identifier": identifier,
                "name": name,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        identifier = d.pop("identifier")

        name = d.pop("name")

        updated_at = d.pop("updatedAt", UNSET)

        subscriber_preferences_workflow_info_dto = cls(
            slug=slug,
            identifier=identifier,
            name=name,
            updated_at=updated_at,
        )

        subscriber_preferences_workflow_info_dto.additional_properties = d
        return subscriber_preferences_workflow_info_dto

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
