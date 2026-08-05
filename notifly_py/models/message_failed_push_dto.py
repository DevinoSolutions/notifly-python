from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MessageFailedPushDto")


@_attrs_define
class MessageFailedPushDto:
    """
    Attributes:
        is_invalid_token (bool): Is invalid token
        device_token (str): Device token
    """

    is_invalid_token: bool
    device_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_invalid_token = self.is_invalid_token

        device_token = self.device_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isInvalidToken": is_invalid_token,
                "deviceToken": device_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_invalid_token = d.pop("isInvalidToken")

        device_token = d.pop("deviceToken")

        message_failed_push_dto = cls(
            is_invalid_token=is_invalid_token,
            device_token=device_token,
        )

        message_failed_push_dto.additional_properties = d
        return message_failed_push_dto

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
