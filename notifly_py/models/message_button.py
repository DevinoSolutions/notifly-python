from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.button_type_enum import ButtonTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageButton")


@_attrs_define
class MessageButton:
    """
    Attributes:
        type_ (ButtonTypeEnum): Type of button for the action result
        content (str): Content of the button
        result_content (str | Unset): Content of the result when the button is clicked
    """

    type_: ButtonTypeEnum
    content: str
    result_content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        content = self.content

        result_content = self.result_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "content": content,
            }
        )
        if result_content is not UNSET:
            field_dict["resultContent"] = result_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ButtonTypeEnum(d.pop("type"))

        content = d.pop("content")

        result_content = d.pop("resultContent", UNSET)

        message_button = cls(
            type_=type_,
            content=content,
            result_content=result_content,
        )

        message_button.additional_properties = d
        return message_button

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
