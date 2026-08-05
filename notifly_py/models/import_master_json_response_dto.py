from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportMasterJsonResponseDto")


@_attrs_define
class ImportMasterJsonResponseDto:
    """
    Attributes:
        success (bool): Overall success status of the import operation
        message (str): Human-readable message describing the import result
        successful (list[str] | Unset): List of resource IDs that were successfully imported
        failed (list[str] | Unset): List of resource IDs that failed to import
    """

    success: bool
    message: str
    successful: list[str] | Unset = UNSET
    failed: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        successful: list[str] | Unset = UNSET
        if not isinstance(self.successful, Unset):
            successful = self.successful

        failed: list[str] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
            }
        )
        if successful is not UNSET:
            field_dict["successful"] = successful
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        successful = cast(list[str], d.pop("successful", UNSET))

        failed = cast(list[str], d.pop("failed", UNSET))

        import_master_json_response_dto = cls(
            success=success,
            message=message,
            successful=successful,
            failed=failed,
        )

        import_master_json_response_dto.additional_properties = d
        return import_master_json_response_dto

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
