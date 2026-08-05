from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateLayoutDto")


@_attrs_define
class DuplicateLayoutDto:
    """
    Attributes:
        name (str): Name of the layout
        layout_id (str | Unset): Identifier for the duplicated layout. When omitted, it is derived from the name.
        is_translation_enabled (bool | Unset): Enable or disable translations for this layout Default: False.
    """

    name: str
    layout_id: str | Unset = UNSET
    is_translation_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        layout_id = self.layout_id

        is_translation_enabled = self.is_translation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if layout_id is not UNSET:
            field_dict["layoutId"] = layout_id
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        layout_id = d.pop("layoutId", UNSET)

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        duplicate_layout_dto = cls(
            name=name,
            layout_id=layout_id,
            is_translation_enabled=is_translation_enabled,
        )

        duplicate_layout_dto.additional_properties = d
        return duplicate_layout_dto

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
