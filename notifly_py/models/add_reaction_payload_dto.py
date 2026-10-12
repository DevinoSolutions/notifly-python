from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddReactionPayloadDto")


@_attrs_define
class AddReactionPayloadDto:
    """
    Attributes:
        message_id (str): Platform message id to react to. Example: 1712345678.123456.
        emoji_name (str): Well-known cross-platform emoji name (e.g. `white_check_mark`, `thumbsup`). Example:
            white_check_mark.
    """

    message_id: str
    emoji_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        emoji_name = self.emoji_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "emojiName": emoji_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        emoji_name = d.pop("emojiName")

        add_reaction_payload_dto = cls(
            message_id=message_id,
            emoji_name=emoji_name,
        )

        add_reaction_payload_dto.additional_properties = d
        return add_reaction_payload_dto

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
