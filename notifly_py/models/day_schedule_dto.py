from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range_dto import TimeRangeDto


T = TypeVar("T", bound="DayScheduleDto")


@_attrs_define
class DayScheduleDto:
    """
    Attributes:
        is_enabled (bool): Day schedule enabled Example: True.
        hours (list[TimeRangeDto] | Unset): Hours Example: [{'start': '09:00 AM', 'end': '05:00 PM'}].
    """

    is_enabled: bool
    hours: list[TimeRangeDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled = self.is_enabled

        hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hours, Unset):
            hours = []
            for hours_item_data in self.hours:
                hours_item = hours_item_data.to_dict()
                hours.append(hours_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEnabled": is_enabled,
            }
        )
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range_dto import TimeRangeDto

        d = dict(src_dict)
        is_enabled = d.pop("isEnabled")

        _hours = d.pop("hours", UNSET)
        hours: list[TimeRangeDto] | Unset = UNSET
        if _hours is not UNSET:
            hours = []
            for hours_item_data in _hours:
                hours_item = TimeRangeDto.from_dict(hours_item_data)

                hours.append(hours_item)

        day_schedule_dto = cls(
            is_enabled=is_enabled,
            hours=hours,
        )

        day_schedule_dto.additional_properties = d
        return day_schedule_dto

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
