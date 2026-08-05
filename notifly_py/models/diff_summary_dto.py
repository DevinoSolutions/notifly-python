from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DiffSummaryDto")


@_attrs_define
class DiffSummaryDto:
    """
    Attributes:
        added (float): Number of added resources (workflows and steps)
        modified (float): Number of modified resources (workflows and steps)
        deleted (float): Number of deleted resources (workflows and steps)
        unchanged (float): Number of unchanged resources (workflows and steps)
    """

    added: float
    modified: float
    deleted: float
    unchanged: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        modified = self.modified

        deleted = self.deleted

        unchanged = self.unchanged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "modified": modified,
                "deleted": deleted,
                "unchanged": unchanged,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = d.pop("added")

        modified = d.pop("modified")

        deleted = d.pop("deleted")

        unchanged = d.pop("unchanged")

        diff_summary_dto = cls(
            added=added,
            modified=modified,
            deleted=deleted,
            unchanged=unchanged,
        )

        diff_summary_dto.additional_properties = d
        return diff_summary_dto

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
