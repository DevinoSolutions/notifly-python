from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_schedule_dto import DayScheduleDto


T = TypeVar("T", bound="WeeklyScheduleDto")


@_attrs_define
class WeeklyScheduleDto:
    """
    Attributes:
        monday (DayScheduleDto | Unset):
        tuesday (DayScheduleDto | Unset):
        wednesday (DayScheduleDto | Unset):
        thursday (DayScheduleDto | Unset):
        friday (DayScheduleDto | Unset):
        saturday (DayScheduleDto | Unset):
        sunday (DayScheduleDto | Unset):
    """

    monday: DayScheduleDto | Unset = UNSET
    tuesday: DayScheduleDto | Unset = UNSET
    wednesday: DayScheduleDto | Unset = UNSET
    thursday: DayScheduleDto | Unset = UNSET
    friday: DayScheduleDto | Unset = UNSET
    saturday: DayScheduleDto | Unset = UNSET
    sunday: DayScheduleDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monday, Unset):
            monday = self.monday.to_dict()

        tuesday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tuesday, Unset):
            tuesday = self.tuesday.to_dict()

        wednesday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wednesday, Unset):
            wednesday = self.wednesday.to_dict()

        thursday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thursday, Unset):
            thursday = self.thursday.to_dict()

        friday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.friday, Unset):
            friday = self.friday.to_dict()

        saturday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saturday, Unset):
            saturday = self.saturday.to_dict()

        sunday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sunday, Unset):
            sunday = self.sunday.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.day_schedule_dto import DayScheduleDto

        d = dict(src_dict)
        _monday = d.pop("monday", UNSET)
        monday: DayScheduleDto | Unset
        if isinstance(_monday, Unset):
            monday = UNSET
        else:
            monday = DayScheduleDto.from_dict(_monday)

        _tuesday = d.pop("tuesday", UNSET)
        tuesday: DayScheduleDto | Unset
        if isinstance(_tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = DayScheduleDto.from_dict(_tuesday)

        _wednesday = d.pop("wednesday", UNSET)
        wednesday: DayScheduleDto | Unset
        if isinstance(_wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = DayScheduleDto.from_dict(_wednesday)

        _thursday = d.pop("thursday", UNSET)
        thursday: DayScheduleDto | Unset
        if isinstance(_thursday, Unset):
            thursday = UNSET
        else:
            thursday = DayScheduleDto.from_dict(_thursday)

        _friday = d.pop("friday", UNSET)
        friday: DayScheduleDto | Unset
        if isinstance(_friday, Unset):
            friday = UNSET
        else:
            friday = DayScheduleDto.from_dict(_friday)

        _saturday = d.pop("saturday", UNSET)
        saturday: DayScheduleDto | Unset
        if isinstance(_saturday, Unset):
            saturday = UNSET
        else:
            saturday = DayScheduleDto.from_dict(_saturday)

        _sunday = d.pop("sunday", UNSET)
        sunday: DayScheduleDto | Unset
        if isinstance(_sunday, Unset):
            sunday = UNSET
        else:
            sunday = DayScheduleDto.from_dict(_sunday)

        weekly_schedule_dto = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        weekly_schedule_dto.additional_properties = d
        return weekly_schedule_dto

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
