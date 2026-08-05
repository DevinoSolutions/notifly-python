from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..models.preference_override_source_enum import PreferenceOverrideSourceEnum

T = TypeVar("T", bound="SubscriberPreferenceOverrideDto")


@_attrs_define
class SubscriberPreferenceOverrideDto:
    """
    Attributes:
        channel (ChannelTypeEnum): Channel type through which the message is sent
        source (PreferenceOverrideSourceEnum): The source of overrides
    """

    channel: ChannelTypeEnum
    source: PreferenceOverrideSourceEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = ChannelTypeEnum(d.pop("channel"))

        source = PreferenceOverrideSourceEnum(d.pop("source"))

        subscriber_preference_override_dto = cls(
            channel=channel,
            source=source,
        )

        subscriber_preference_override_dto.additional_properties = d
        return subscriber_preference_override_dto

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
