from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_filter_part_dto_on import FieldFilterPartDtoOn
from ..models.field_filter_part_dto_operator import FieldFilterPartDtoOperator

T = TypeVar("T", bound="FieldFilterPartDto")


@_attrs_define
class FieldFilterPartDto:
    """
    Attributes:
        field (str):
        value (str):
        operator (FieldFilterPartDtoOperator):
        on (FieldFilterPartDtoOn):
    """

    field: str
    value: str
    operator: FieldFilterPartDtoOperator
    on: FieldFilterPartDtoOn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        value = self.value

        operator = self.operator.value

        on = self.on.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "value": value,
                "operator": operator,
                "on": on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        value = d.pop("value")

        operator = FieldFilterPartDtoOperator(d.pop("operator"))

        on = FieldFilterPartDtoOn(d.pop("on"))

        field_filter_part_dto = cls(
            field=field,
            value=value,
            operator=operator,
            on=on,
        )

        field_filter_part_dto.additional_properties = d
        return field_filter_part_dto

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
