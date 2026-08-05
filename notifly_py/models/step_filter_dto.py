from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.builder_field_type_enum import BuilderFieldTypeEnum
from ..models.step_filter_dto_value import StepFilterDtoValue

if TYPE_CHECKING:
    from ..models.field_filter_part_dto import FieldFilterPartDto


T = TypeVar("T", bound="StepFilterDto")


@_attrs_define
class StepFilterDto:
    """
    Attributes:
        is_negated (bool):
        type_ (BuilderFieldTypeEnum):
        value (StepFilterDtoValue):
        children (list[FieldFilterPartDto]):
    """

    is_negated: bool
    type_: BuilderFieldTypeEnum
    value: StepFilterDtoValue
    children: list[FieldFilterPartDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_negated = self.is_negated

        type_ = self.type_.value

        value = self.value.value

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isNegated": is_negated,
                "type": type_,
                "value": value,
                "children": children,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_filter_part_dto import FieldFilterPartDto

        d = dict(src_dict)
        is_negated = d.pop("isNegated")

        type_ = BuilderFieldTypeEnum(d.pop("type"))

        value = StepFilterDtoValue(d.pop("value"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = FieldFilterPartDto.from_dict(children_item_data)

            children.append(children_item)

        step_filter_dto = cls(
            is_negated=is_negated,
            type_=type_,
            value=value,
            children=children,
        )

        step_filter_dto.additional_properties = d
        return step_filter_dto

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
