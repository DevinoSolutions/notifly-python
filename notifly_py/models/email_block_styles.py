from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_align_enum import TextAlignEnum

T = TypeVar("T", bound="EmailBlockStyles")


@_attrs_define
class EmailBlockStyles:
    """
    Attributes:
        text_align (TextAlignEnum): Text alignment for the email block
    """

    text_align: TextAlignEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_align = self.text_align.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "textAlign": text_align,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_align = TextAlignEnum(d.pop("textAlign"))

        email_block_styles = cls(
            text_align=text_align,
        )

        email_block_styles.additional_properties = d
        return email_block_styles

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
