from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SnoozeSubscriberNotificationDto")


@_attrs_define
class SnoozeSubscriberNotificationDto:
    """
    Attributes:
        snooze_until (datetime.datetime): The date and time until which the notification should be snoozed Example:
            2026-03-01T10:00:00Z.
    """

    snooze_until: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snooze_until = self.snooze_until.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snoozeUntil": snooze_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snooze_until = datetime.datetime.fromisoformat(d.pop("snoozeUntil"))

        snooze_subscriber_notification_dto = cls(
            snooze_until=snooze_until,
        )

        snooze_subscriber_notification_dto.additional_properties = d
        return snooze_subscriber_notification_dto

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
