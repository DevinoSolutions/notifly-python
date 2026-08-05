from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnvironmentDiffSummaryDto")


@_attrs_define
class EnvironmentDiffSummaryDto:
    """
    Attributes:
        total_entities (float): Total number of entities compared
        total_changes (float): Total number of changes detected
        has_changes (bool): Whether any changes were detected
    """

    total_entities: float
    total_changes: float
    has_changes: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entities = self.total_entities

        total_changes = self.total_changes

        has_changes = self.has_changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalEntities": total_entities,
                "totalChanges": total_changes,
                "hasChanges": has_changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_entities = d.pop("totalEntities")

        total_changes = d.pop("totalChanges")

        has_changes = d.pop("hasChanges")

        environment_diff_summary_dto = cls(
            total_entities=total_entities,
            total_changes=total_changes,
            has_changes=has_changes,
        )

        environment_diff_summary_dto.additional_properties = d
        return environment_diff_summary_dto

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
