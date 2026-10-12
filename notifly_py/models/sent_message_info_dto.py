from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SentMessageInfoDto")


@_attrs_define
class SentMessageInfoDto:
    """
    Attributes:
        message_id (str): Platform-native message id of the delivered or edited message (e.g. Slack `ts`, Teams activity
            id). Example: 1712345678.123456.
        platform_thread_id (str): Platform-native thread / conversation id where the message was delivered. Example:
            C0123456789.
    """

    message_id: str
    platform_thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        platform_thread_id = self.platform_thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "platformThreadId": platform_thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        platform_thread_id = d.pop("platformThreadId")

        sent_message_info_dto = cls(
            message_id=message_id,
            platform_thread_id=platform_thread_id,
        )

        sent_message_info_dto.additional_properties = d
        return sent_message_info_dto

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
