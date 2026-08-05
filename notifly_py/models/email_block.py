from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_block_type_enum import EmailBlockTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_block_styles import EmailBlockStyles


T = TypeVar("T", bound="EmailBlock")


@_attrs_define
class EmailBlock:
    """
    Attributes:
        type_ (EmailBlockTypeEnum): Type of the email block
        content (str): Content of the email block
        url (str | Unset): URL associated with the email block, if any
        styles (EmailBlockStyles | Unset):
    """

    type_: EmailBlockTypeEnum
    content: str
    url: str | Unset = UNSET
    styles: EmailBlockStyles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        content = self.content

        url = self.url

        styles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.styles, Unset):
            styles = self.styles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "content": content,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if styles is not UNSET:
            field_dict["styles"] = styles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_block_styles import EmailBlockStyles

        d = dict(src_dict)
        type_ = EmailBlockTypeEnum(d.pop("type"))

        content = d.pop("content")

        url = d.pop("url", UNSET)

        _styles = d.pop("styles", UNSET)
        styles: EmailBlockStyles | Unset
        if isinstance(_styles, Unset):
            styles = UNSET
        else:
            styles = EmailBlockStyles.from_dict(_styles)

        email_block = cls(
            type_=type_,
            content=content,
            url=url,
            styles=styles,
        )

        email_block.additional_properties = d
        return email_block

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
