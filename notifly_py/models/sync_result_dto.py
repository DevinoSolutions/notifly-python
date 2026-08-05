from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type_enum import ResourceTypeEnum

if TYPE_CHECKING:
    from ..models.failed_workflow_dto import FailedWorkflowDto
    from ..models.skipped_workflow_dto import SkippedWorkflowDto
    from ..models.synced_workflow_dto import SyncedWorkflowDto


T = TypeVar("T", bound="SyncResultDto")


@_attrs_define
class SyncResultDto:
    """
    Attributes:
        resource_type (ResourceTypeEnum): Type of the layout
        successful (list[SyncedWorkflowDto]): Successfully synced resources
        failed (list[FailedWorkflowDto]): Failed resource syncs
        skipped (list[SkippedWorkflowDto]): Skipped resources
        total_processed (float): Total number of resources processed
    """

    resource_type: ResourceTypeEnum
    successful: list[SyncedWorkflowDto]
    failed: list[FailedWorkflowDto]
    skipped: list[SkippedWorkflowDto]
    total_processed: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type = self.resource_type.value

        successful = []
        for successful_item_data in self.successful:
            successful_item = successful_item_data.to_dict()
            successful.append(successful_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        total_processed = self.total_processed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceType": resource_type,
                "successful": successful,
                "failed": failed,
                "skipped": skipped,
                "totalProcessed": total_processed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_workflow_dto import FailedWorkflowDto
        from ..models.skipped_workflow_dto import SkippedWorkflowDto
        from ..models.synced_workflow_dto import SyncedWorkflowDto

        d = dict(src_dict)
        resource_type = ResourceTypeEnum(d.pop("resourceType"))

        successful = []
        _successful = d.pop("successful")
        for successful_item_data in _successful:
            successful_item = SyncedWorkflowDto.from_dict(successful_item_data)

            successful.append(successful_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = FailedWorkflowDto.from_dict(failed_item_data)

            failed.append(failed_item)

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = SkippedWorkflowDto.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        total_processed = d.pop("totalProcessed")

        sync_result_dto = cls(
            resource_type=resource_type,
            successful=successful,
            failed=failed,
            skipped=skipped,
            total_processed=total_processed,
        )

        sync_result_dto.additional_properties = d
        return sync_result_dto

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
