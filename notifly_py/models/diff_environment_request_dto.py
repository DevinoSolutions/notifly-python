from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffEnvironmentRequestDto")


@_attrs_define
class DiffEnvironmentRequestDto:
    """
    Attributes:
        source_environment_id (str | Unset): Source environment ID to compare from. Defaults to the Development
            environment if not provided. Example: 507f1f77bcf86cd799439011.
    """

    source_environment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_environment_id = self.source_environment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_environment_id is not UNSET:
            field_dict["sourceEnvironmentId"] = source_environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_environment_id = d.pop("sourceEnvironmentId", UNSET)

        diff_environment_request_dto = cls(
            source_environment_id=source_environment_id,
        )

        diff_environment_request_dto.additional_properties = d
        return diff_environment_request_dto

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
