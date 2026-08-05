from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.created_subscriber_dto import CreatedSubscriberDto
    from ..models.failed_operation_dto import FailedOperationDto
    from ..models.updated_subscriber_dto import UpdatedSubscriberDto


T = TypeVar("T", bound="BulkCreateSubscriberResponseDto")


@_attrs_define
class BulkCreateSubscriberResponseDto:
    """
    Attributes:
        updated (list[UpdatedSubscriberDto]): An array of subscribers that were successfully updated.
        created (list[CreatedSubscriberDto]): An array of subscribers that were successfully created.
        failed (list[FailedOperationDto]): An array of failed operations with error messages and optional subscriber
            IDs.
    """

    updated: list[UpdatedSubscriberDto]
    created: list[CreatedSubscriberDto]
    failed: list[FailedOperationDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated = []
        for updated_item_data in self.updated:
            updated_item = updated_item_data.to_dict()
            updated.append(updated_item)

        created = []
        for created_item_data in self.created:
            created_item = created_item_data.to_dict()
            created.append(created_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated": updated,
                "created": created,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_subscriber_dto import CreatedSubscriberDto
        from ..models.failed_operation_dto import FailedOperationDto
        from ..models.updated_subscriber_dto import UpdatedSubscriberDto

        d = dict(src_dict)
        updated = []
        _updated = d.pop("updated")
        for updated_item_data in _updated:
            updated_item = UpdatedSubscriberDto.from_dict(updated_item_data)

            updated.append(updated_item)

        created = []
        _created = d.pop("created")
        for created_item_data in _created:
            created_item = CreatedSubscriberDto.from_dict(created_item_data)

            created.append(created_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = FailedOperationDto.from_dict(failed_item_data)

            failed.append(failed_item)

        bulk_create_subscriber_response_dto = cls(
            updated=updated,
            created=created,
            failed=failed,
        )

        bulk_create_subscriber_response_dto.additional_properties = d
        return bulk_create_subscriber_response_dto

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
