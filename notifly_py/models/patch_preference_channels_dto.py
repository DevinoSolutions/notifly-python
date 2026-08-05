from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPreferenceChannelsDto")


@_attrs_define
class PatchPreferenceChannelsDto:
    """
    Attributes:
        email (bool | Unset): Email channel preference
        sms (bool | Unset): SMS channel preference
        in_app (bool | Unset): In-app channel preference
        push (bool | Unset): Push channel preference
        chat (bool | Unset): Chat channel preference
    """

    email: bool | Unset = UNSET
    sms: bool | Unset = UNSET
    in_app: bool | Unset = UNSET
    push: bool | Unset = UNSET
    chat: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        sms = self.sms

        in_app = self.in_app

        push = self.push

        chat = self.chat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if sms is not UNSET:
            field_dict["sms"] = sms
        if in_app is not UNSET:
            field_dict["in_app"] = in_app
        if push is not UNSET:
            field_dict["push"] = push
        if chat is not UNSET:
            field_dict["chat"] = chat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        sms = d.pop("sms", UNSET)

        in_app = d.pop("in_app", UNSET)

        push = d.pop("push", UNSET)

        chat = d.pop("chat", UNSET)

        patch_preference_channels_dto = cls(
            email=email,
            sms=sms,
            in_app=in_app,
            push=push,
            chat=chat,
        )

        patch_preference_channels_dto.additional_properties = d
        return patch_preference_channels_dto

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
