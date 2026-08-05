from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.button_type_enum import ButtonTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_action_result_payload import MessageActionResultPayload


T = TypeVar("T", bound="MessageActionResult")


@_attrs_define
class MessageActionResult:
    """
    Attributes:
        payload (MessageActionResultPayload | Unset): Payload of the action result
        type_ (ButtonTypeEnum | Unset): Type of button for the action result
    """

    payload: MessageActionResultPayload | Unset = UNSET
    type_: ButtonTypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_action_result_payload import MessageActionResultPayload

        d = dict(src_dict)
        _payload = d.pop("payload", UNSET)
        payload: MessageActionResultPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = MessageActionResultPayload.from_dict(_payload)

        _type_ = d.pop("type", UNSET)
        type_: ButtonTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ButtonTypeEnum(_type_)

        message_action_result = cls(
            payload=payload,
            type_=type_,
        )

        message_action_result.additional_properties = d
        return message_action_result

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
