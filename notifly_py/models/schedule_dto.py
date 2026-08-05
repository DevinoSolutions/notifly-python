from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.weekly_schedule_dto import WeeklyScheduleDto


T = TypeVar("T", bound="ScheduleDto")


@_attrs_define
class ScheduleDto:
    """
    Attributes:
        is_enabled (bool): Schedule enabled Example: True.
        weekly_schedule (WeeklyScheduleDto | Unset):
    """

    is_enabled: bool
    weekly_schedule: WeeklyScheduleDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        weekly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly_schedule, Unset):
            weekly_schedule = self.weekly_schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if weekly_schedule is not UNSET:
            field_dict["weeklySchedule"] = weekly_schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.weekly_schedule_dto import WeeklyScheduleDto

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: WeeklyScheduleDto | Unset
        if isinstance(_weekly_schedule, Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = WeeklyScheduleDto.from_dict(_weekly_schedule)

        schedule_dto = cls(
            is_enabled=is_enabled,
            weekly_schedule=weekly_schedule,
        )

        schedule_dto.additional_properties = d
        return schedule_dto

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
