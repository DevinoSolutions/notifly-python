from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EnvironmentVariableValueResponseDto")


@_attrs_define
class EnvironmentVariableValueResponseDto:
    """
    Attributes:
        field_environment_id (str):
        value (str): Value is masked (••••••••) for secret variables
    """

    field_environment_id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_environment_id = self.field_environment_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_environmentId": field_environment_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_environment_id = d.pop("_environmentId")

        value = d.pop("value")

        environment_variable_value_response_dto = cls(
            field_environment_id=field_environment_id,
            value=value,
        )

        environment_variable_value_response_dto.additional_properties = d
        return environment_variable_value_response_dto

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
