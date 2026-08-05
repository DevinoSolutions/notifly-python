from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ui_component_enum import UiComponentEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_schema_property_placeholder_type_3 import UiSchemaPropertyPlaceholderType3
    from ..models.ui_schema_property_placeholder_type_4_item_type_3 import UiSchemaPropertyPlaceholderType4ItemType3
    from ..models.ui_schema_property_properties import UiSchemaPropertyProperties


T = TypeVar("T", bound="UiSchemaProperty")


@_attrs_define
class UiSchemaProperty:
    """
    Attributes:
        component (UiComponentEnum): Component type for the UI Schema Property
        placeholder (bool | float | list[bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3] | None | str |
            UiSchemaPropertyPlaceholderType3 | Unset): Placeholder for the UI Schema Property
        properties (UiSchemaPropertyProperties | Unset): Properties of the UI Schema
    """

    component: UiComponentEnum
    placeholder: (
        bool
        | float
        | list[bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3]
        | None
        | str
        | UiSchemaPropertyPlaceholderType3
        | Unset
    ) = UNSET
    properties: UiSchemaPropertyProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_schema_property_placeholder_type_3 import UiSchemaPropertyPlaceholderType3
        from ..models.ui_schema_property_placeholder_type_4_item_type_3 import UiSchemaPropertyPlaceholderType4ItemType3

        component = self.component.value

        placeholder: bool | dict[str, Any] | float | list[bool | dict[str, Any] | float | str] | None | str | Unset
        if isinstance(self.placeholder, Unset):
            placeholder = UNSET
        elif isinstance(self.placeholder, UiSchemaPropertyPlaceholderType3):
            placeholder = self.placeholder.to_dict()
        elif isinstance(self.placeholder, list):
            placeholder = []
            for placeholder_type_4_item_data in self.placeholder:
                placeholder_type_4_item: bool | dict[str, Any] | float | str
                if isinstance(placeholder_type_4_item_data, UiSchemaPropertyPlaceholderType4ItemType3):
                    placeholder_type_4_item = placeholder_type_4_item_data.to_dict()
                else:
                    placeholder_type_4_item = placeholder_type_4_item_data
                placeholder.append(placeholder_type_4_item)

        else:
            placeholder = self.placeholder

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component": component,
            }
        )
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_schema_property_placeholder_type_3 import UiSchemaPropertyPlaceholderType3
        from ..models.ui_schema_property_placeholder_type_4_item_type_3 import UiSchemaPropertyPlaceholderType4ItemType3
        from ..models.ui_schema_property_properties import UiSchemaPropertyProperties

        d = dict(src_dict)
        component = UiComponentEnum(d.pop("component"))

        def _parse_placeholder(
            data: object,
        ) -> (
            bool
            | float
            | list[bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3]
            | None
            | str
            | UiSchemaPropertyPlaceholderType3
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                placeholder_type_3 = UiSchemaPropertyPlaceholderType3.from_dict(data)

                return placeholder_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                placeholder_type_4 = []
                _placeholder_type_4 = data
                for placeholder_type_4_item_data in _placeholder_type_4:

                    def _parse_placeholder_type_4_item(
                        data: object,
                    ) -> bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            placeholder_type_4_item_type_3 = UiSchemaPropertyPlaceholderType4ItemType3.from_dict(data)

                            return placeholder_type_4_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3, data)

                    placeholder_type_4_item = _parse_placeholder_type_4_item(placeholder_type_4_item_data)

                    placeholder_type_4.append(placeholder_type_4_item)

                return placeholder_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | list[bool | float | str | UiSchemaPropertyPlaceholderType4ItemType3]
                | None
                | str
                | UiSchemaPropertyPlaceholderType3
                | Unset,
                data,
            )

        placeholder = _parse_placeholder(d.pop("placeholder", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: UiSchemaPropertyProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = UiSchemaPropertyProperties.from_dict(_properties)

        ui_schema_property = cls(
            component=component,
            placeholder=placeholder,
            properties=properties,
        )

        ui_schema_property.additional_properties = d
        return ui_schema_property

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
