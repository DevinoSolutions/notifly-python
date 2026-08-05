from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelCredentialsDto")


@_attrs_define
class ChannelCredentialsDto:
    """
    Attributes:
        webhook_url (str | Unset): The URL for the webhook associated with the channel.
        device_tokens (list[str] | Unset): An array of device tokens for push notifications.
    """

    webhook_url: str | Unset = UNSET
    device_tokens: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        device_tokens: list[str] | Unset = UNSET
        if not isinstance(self.device_tokens, Unset):
            device_tokens = self.device_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if device_tokens is not UNSET:
            field_dict["deviceTokens"] = device_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl", UNSET)

        device_tokens = cast(list[str], d.pop("deviceTokens", UNSET))

        channel_credentials_dto = cls(
            webhook_url=webhook_url,
            device_tokens=device_tokens,
        )

        channel_credentials_dto.additional_properties = d
        return channel_credentials_dto

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
