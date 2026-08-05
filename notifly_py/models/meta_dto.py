from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetaDto")


@_attrs_define
class MetaDto:
    """
    Attributes:
        total_count (float): The total count of subscriber IDs provided Example: 3.
        successful (float): The count of successfully created subscriptions Example: 2.
        failed (float): The count of failed subscription attempts Example: 1.
    """

    total_count: float
    successful: float
    failed: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        successful = self.successful

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "successful": successful,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount")

        successful = d.pop("successful")

        failed = d.pop("failed")

        meta_dto = cls(
            total_count=total_count,
            successful=successful,
            failed=failed,
        )

        meta_dto.additional_properties = d
        return meta_dto

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
