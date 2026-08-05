from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_dto import ScheduleDto
    from ..models.subscriber_preference_channels import SubscriberPreferenceChannels


T = TypeVar("T", bound="SubscriberGlobalPreferenceDto")


@_attrs_define
class SubscriberGlobalPreferenceDto:
    """
    Attributes:
        enabled (bool): Whether notifications are enabled globally
        channels (SubscriberPreferenceChannels):
        schedule (ScheduleDto | Unset):
    """

    enabled: bool
    channels: SubscriberPreferenceChannels
    schedule: ScheduleDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        channels = self.channels.to_dict()

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "channels": channels,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_dto import ScheduleDto
        from ..models.subscriber_preference_channels import SubscriberPreferenceChannels

        d = dict(src_dict)
        enabled = d.pop("enabled")

        channels = SubscriberPreferenceChannels.from_dict(d.pop("channels"))

        _schedule = d.pop("schedule", UNSET)
        schedule: ScheduleDto | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ScheduleDto.from_dict(_schedule)

        subscriber_global_preference_dto = cls(
            enabled=enabled,
            channels=channels,
            schedule=schedule,
        )

        subscriber_global_preference_dto.additional_properties = d
        return subscriber_global_preference_dto

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
