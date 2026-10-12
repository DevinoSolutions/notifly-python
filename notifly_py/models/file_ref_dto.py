from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileRefDto")


@_attrs_define
class FileRefDto:
    """
    Attributes:
        filename (str): Filename shown to the end user, including extension. Example: report.pdf.
        mime_type (str | Unset): IANA MIME type of the file. Example: application/pdf.
        data (str | Unset): Base64-encoded inline file bytes. Mutually exclusive with `url`. Decoded size must be ≤ 5
            MB. Prefer `url` for larger files. Example: JVBERi0xLjQK....
        url (str | Unset): Publicly accessible HTTP(S) URL. Mutually exclusive with `data`. Server-side limits: 25 MB
            per file, 15 files per message, 50 MB aggregate. Example: https://example.com/files/report.pdf.
    """

    filename: str
    mime_type: str | Unset = UNSET
    data: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        mime_type = self.mime_type

        data = self.data

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
            }
        )
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if data is not UNSET:
            field_dict["data"] = data
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        mime_type = d.pop("mimeType", UNSET)

        data = d.pop("data", UNSET)

        url = d.pop("url", UNSET)

        file_ref_dto = cls(
            filename=filename,
            mime_type=mime_type,
            data=data,
            url=url,
        )

        file_ref_dto.additional_properties = d
        return file_ref_dto

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
