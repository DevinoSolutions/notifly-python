from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_cta_type_enum import ChannelCTATypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_action import MessageAction
    from ..models.message_cta_data import MessageCTAData


T = TypeVar("T", bound="MessageCTA")


@_attrs_define
class MessageCTA:
    """
    Attributes:
        type_ (ChannelCTATypeEnum | Unset): Type of call to action
        data (MessageCTAData | Unset):
        action (MessageAction | Unset):
    """

    type_: ChannelCTATypeEnum | Unset = UNSET
    data: MessageCTAData | Unset = UNSET
    action: MessageAction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if data is not UNSET:
            field_dict["data"] = data
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_action import MessageAction
        from ..models.message_cta_data import MessageCTAData

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ChannelCTATypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ChannelCTATypeEnum(_type_)

        _data = d.pop("data", UNSET)
        data: MessageCTAData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = MessageCTAData.from_dict(_data)

        _action = d.pop("action", UNSET)
        action: MessageAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = MessageAction.from_dict(_action)

        message_cta = cls(
            type_=type_,
            data=data,
            action=action,
        )

        message_cta.additional_properties = d
        return message_cta

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
