from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layout_creation_source_enum import LayoutCreationSourceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLayoutDto")


@_attrs_define
class CreateLayoutDto:
    """
    Attributes:
        layout_id (str): Unique identifier for the layout
        name (str): Name of the layout
        is_translation_enabled (bool | Unset): Enable or disable translations for this layout Default: False.
        field_source (LayoutCreationSourceEnum | Unset): Source of layout creation
    """

    layout_id: str
    name: str
    is_translation_enabled: bool | Unset = False
    field_source: LayoutCreationSourceEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_id = self.layout_id

        name = self.name

        is_translation_enabled = self.is_translation_enabled

        field_source: str | Unset = UNSET
        if not isinstance(self.field_source, Unset):
            field_source = self.field_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layoutId": layout_id,
                "name": name,
            }
        )
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled
        if field_source is not UNSET:
            field_dict["__source"] = field_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layout_id = d.pop("layoutId")

        name = d.pop("name")

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        _field_source = d.pop("__source", UNSET)
        field_source: LayoutCreationSourceEnum | Unset
        if isinstance(_field_source, Unset):
            field_source = UNSET
        else:
            field_source = LayoutCreationSourceEnum(_field_source)

        create_layout_dto = cls(
            layout_id=layout_id,
            name=name,
            is_translation_enabled=is_translation_enabled,
            field_source=field_source,
        )

        create_layout_dto.additional_properties = d
        return create_layout_dto

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
