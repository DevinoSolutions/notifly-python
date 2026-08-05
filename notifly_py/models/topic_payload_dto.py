from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_recipients_type_enum import TriggerRecipientsTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicPayloadDto")


@_attrs_define
class TopicPayloadDto:
    """
    Attributes:
        topic_key (str):
        type_ (TriggerRecipientsTypeEnum):
        exclude (list[str] | Unset): Optional array of subscriber IDs to exclude from the topic trigger
    """

    topic_key: str
    type_: TriggerRecipientsTypeEnum
    exclude: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic_key = self.topic_key

        type_ = self.type_.value

        exclude: list[str] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topicKey": topic_key,
                "type": type_,
            }
        )
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic_key = d.pop("topicKey")

        type_ = TriggerRecipientsTypeEnum(d.pop("type"))

        exclude = cast(list[str], d.pop("exclude", UNSET))

        topic_payload_dto = cls(
            topic_key=topic_key,
            type_=type_,
            exclude=exclude,
        )

        topic_payload_dto.additional_properties = d
        return topic_payload_dto

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
