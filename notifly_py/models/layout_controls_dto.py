from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_control_values_dto import LayoutControlValuesDto
    from ..models.layout_controls_dto_data_schema import LayoutControlsDtoDataSchema
    from ..models.ui_schema import UiSchema


T = TypeVar("T", bound="LayoutControlsDto")


@_attrs_define
class LayoutControlsDto:
    """
    Attributes:
        values (LayoutControlValuesDto):
        data_schema (LayoutControlsDtoDataSchema | Unset): JSON Schema for data
        ui_schema (UiSchema | Unset):
    """

    values: LayoutControlValuesDto
    data_schema: LayoutControlsDtoDataSchema | Unset = UNSET
    ui_schema: UiSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = self.values.to_dict()

        data_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_schema, Unset):
            data_schema = self.data_schema.to_dict()

        ui_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_schema, Unset):
            ui_schema = self.ui_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )
        if data_schema is not UNSET:
            field_dict["dataSchema"] = data_schema
        if ui_schema is not UNSET:
            field_dict["uiSchema"] = ui_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_control_values_dto import LayoutControlValuesDto
        from ..models.layout_controls_dto_data_schema import LayoutControlsDtoDataSchema
        from ..models.ui_schema import UiSchema

        d = dict(src_dict)
        values = LayoutControlValuesDto.from_dict(d.pop("values"))

        _data_schema = d.pop("dataSchema", UNSET)
        data_schema: LayoutControlsDtoDataSchema | Unset
        if isinstance(_data_schema, Unset):
            data_schema = UNSET
        else:
            data_schema = LayoutControlsDtoDataSchema.from_dict(_data_schema)

        _ui_schema = d.pop("uiSchema", UNSET)
        ui_schema: UiSchema | Unset
        if isinstance(_ui_schema, Unset):
            ui_schema = UNSET
        else:
            ui_schema = UiSchema.from_dict(_ui_schema)

        layout_controls_dto = cls(
            values=values,
            data_schema=data_schema,
            ui_schema=ui_schema,
        )

        layout_controls_dto.additional_properties = d
        return layout_controls_dto

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
