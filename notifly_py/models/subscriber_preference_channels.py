from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberPreferenceChannels")


@_attrs_define
class SubscriberPreferenceChannels:
    """
    Attributes:
        email (bool | Unset): Email channel preference Example: True.
        sms (bool | Unset): SMS channel preference
        in_app (bool | Unset): In-app channel preference Example: True.
        chat (bool | Unset): Chat channel preference
        push (bool | Unset): Push notification channel preference Example: True.
    """

    email: bool | Unset = UNSET
    sms: bool | Unset = UNSET
    in_app: bool | Unset = UNSET
    chat: bool | Unset = UNSET
    push: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        sms = self.sms

        in_app = self.in_app

        chat = self.chat

        push = self.push

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if sms is not UNSET:
            field_dict["sms"] = sms
        if in_app is not UNSET:
            field_dict["in_app"] = in_app
        if chat is not UNSET:
            field_dict["chat"] = chat
        if push is not UNSET:
            field_dict["push"] = push

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        sms = d.pop("sms", UNSET)

        in_app = d.pop("in_app", UNSET)

        chat = d.pop("chat", UNSET)

        push = d.pop("push", UNSET)

        subscriber_preference_channels = cls(
            email=email,
            sms=sms,
            in_app=in_app,
            chat=chat,
            push=push,
        )

        subscriber_preference_channels.additional_properties = d
        return subscriber_preference_channels

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
