from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_control_values_dto import LayoutControlValuesDto


T = TypeVar("T", bound="UpdateLayoutDto")


@_attrs_define
class UpdateLayoutDto:
    """
    Attributes:
        name (str): Name of the layout
        is_translation_enabled (bool | Unset): Enable or disable translations for this layout Default: False.
        control_values (LayoutControlValuesDto | None | Unset): Control values for the layout. Omit to leave unchanged,
            or set to null to clear stored control values.
    """

    name: str
    is_translation_enabled: bool | Unset = False
    control_values: LayoutControlValuesDto | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_control_values_dto import LayoutControlValuesDto

        name = self.name

        is_translation_enabled = self.is_translation_enabled

        control_values: dict[str, Any] | None | Unset
        if isinstance(self.control_values, Unset):
            control_values = UNSET
        elif isinstance(self.control_values, LayoutControlValuesDto):
            control_values = self.control_values.to_dict()
        else:
            control_values = self.control_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled
        if control_values is not UNSET:
            field_dict["controlValues"] = control_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_control_values_dto import LayoutControlValuesDto

        d = dict(src_dict)
        name = d.pop("name")

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        def _parse_control_values(data: object) -> LayoutControlValuesDto | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_values_type_1 = LayoutControlValuesDto.from_dict(data)

                return control_values_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LayoutControlValuesDto | None | Unset, data)

        control_values = _parse_control_values(d.pop("controlValues", UNSET))

        update_layout_dto = cls(
            name=name,
            is_translation_enabled=is_translation_enabled,
            control_values=control_values,
        )

        update_layout_dto.additional_properties = d
        return update_layout_dto

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
