from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.channel_preference_dto import ChannelPreferenceDto


T = TypeVar("T", bound="WorkflowPreferencesDtoChannels")


@_attrs_define
class WorkflowPreferencesDtoChannels:
    """Preferences for different communication channels

    Example:
        {'email': {'enabled': True}, 'sms': {'enabled': False}}

    """

    additional_properties: dict[str, ChannelPreferenceDto] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_preference_dto import ChannelPreferenceDto

        d = dict(src_dict)
        workflow_preferences_dto_channels = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ChannelPreferenceDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        workflow_preferences_dto_channels.additional_properties = additional_properties
        return workflow_preferences_dto_channels

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ChannelPreferenceDto:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ChannelPreferenceDto) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
