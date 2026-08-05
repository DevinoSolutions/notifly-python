from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadTranslationsResponseDto")


@_attrs_define
class UploadTranslationsResponseDto:
    """
    Attributes:
        total_files (float): Total number of files processed
        successful_uploads (float): Number of files successfully uploaded
        failed_uploads (float): Number of files that failed to upload
        errors (list[str]): List of error messages for failed uploads
    """

    total_files: float
    successful_uploads: float
    failed_uploads: float
    errors: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_files = self.total_files

        successful_uploads = self.successful_uploads

        failed_uploads = self.failed_uploads

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalFiles": total_files,
                "successfulUploads": successful_uploads,
                "failedUploads": failed_uploads,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_files = d.pop("totalFiles")

        successful_uploads = d.pop("successfulUploads")

        failed_uploads = d.pop("failedUploads")

        errors = cast(list[str], d.pop("errors"))

        upload_translations_response_dto = cls(
            total_files=total_files,
            successful_uploads=successful_uploads,
            failed_uploads=failed_uploads,
            errors=errors,
        )

        upload_translations_response_dto.additional_properties = d
        return upload_translations_response_dto

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
