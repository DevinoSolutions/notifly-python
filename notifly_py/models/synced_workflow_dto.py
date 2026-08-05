from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type_enum import ResourceTypeEnum
from ..models.sync_action_enum import SyncActionEnum

T = TypeVar("T", bound="SyncedWorkflowDto")


@_attrs_define
class SyncedWorkflowDto:
    """
    Attributes:
        resource_type (ResourceTypeEnum): Type of the layout
        resource_id (str): Resource ID
        resource_name (str): Resource name
        action (SyncActionEnum): Sync action performed
    """

    resource_type: ResourceTypeEnum
    resource_id: str
    resource_name: str
    action: SyncActionEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        resource_id = self.resource_id

        resource_name = self.resource_name

        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceType": resource_type,
                "resourceId": resource_id,
                "resourceName": resource_name,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_type = ResourceTypeEnum(d.pop("resourceType"))

        resource_id = d.pop("resourceId")

        resource_name = d.pop("resourceName")

        action = SyncActionEnum(d.pop("action"))

        synced_workflow_dto = cls(
            resource_type=resource_type,
            resource_id=resource_id,
            resource_name=resource_name,
            action=action,
        )

        synced_workflow_dto.additional_properties = d
        return synced_workflow_dto

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
