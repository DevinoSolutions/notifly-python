from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timed_config_monthly_type import TimedConfigMonthlyType
from ..models.timed_config_ordinal import TimedConfigOrdinal
from ..models.timed_config_ordinal_value import TimedConfigOrdinalValue
from ..models.timed_config_week_days_item import TimedConfigWeekDaysItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimedConfig")


@_attrs_define
class TimedConfig:
    """
    Attributes:
        at_time (str | Unset):
        week_days (list[TimedConfigWeekDaysItem] | Unset):
        month_days (list[str] | Unset):
        ordinal (TimedConfigOrdinal | Unset):
        ordinal_value (TimedConfigOrdinalValue | Unset):
        monthly_type (TimedConfigMonthlyType | Unset):
    """

    at_time: str | Unset = UNSET
    week_days: list[TimedConfigWeekDaysItem] | Unset = UNSET
    month_days: list[str] | Unset = UNSET
    ordinal: TimedConfigOrdinal | Unset = UNSET
    ordinal_value: TimedConfigOrdinalValue | Unset = UNSET
    monthly_type: TimedConfigMonthlyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at_time = self.at_time

        week_days: list[str] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = []
            for week_days_item_data in self.week_days:
                week_days_item = week_days_item_data.value
                week_days.append(week_days_item)

        month_days: list[str] | Unset = UNSET
        if not isinstance(self.month_days, Unset):
            month_days = self.month_days

        ordinal: str | Unset = UNSET
        if not isinstance(self.ordinal, Unset):
            ordinal = self.ordinal.value

        ordinal_value: str | Unset = UNSET
        if not isinstance(self.ordinal_value, Unset):
            ordinal_value = self.ordinal_value.value

        monthly_type: str | Unset = UNSET
        if not isinstance(self.monthly_type, Unset):
            monthly_type = self.monthly_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at_time is not UNSET:
            field_dict["atTime"] = at_time
        if week_days is not UNSET:
            field_dict["weekDays"] = week_days
        if month_days is not UNSET:
            field_dict["monthDays"] = month_days
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if ordinal_value is not UNSET:
            field_dict["ordinalValue"] = ordinal_value
        if monthly_type is not UNSET:
            field_dict["monthlyType"] = monthly_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at_time = d.pop("atTime", UNSET)

        _week_days = d.pop("weekDays", UNSET)
        week_days: list[TimedConfigWeekDaysItem] | Unset = UNSET
        if _week_days is not UNSET:
            week_days = []
            for week_days_item_data in _week_days:
                week_days_item = TimedConfigWeekDaysItem(week_days_item_data)

                week_days.append(week_days_item)

        month_days = cast(list[str], d.pop("monthDays", UNSET))

        _ordinal = d.pop("ordinal", UNSET)
        ordinal: TimedConfigOrdinal | Unset
        if isinstance(_ordinal, Unset):
            ordinal = UNSET
        else:
            ordinal = TimedConfigOrdinal(_ordinal)

        _ordinal_value = d.pop("ordinalValue", UNSET)
        ordinal_value: TimedConfigOrdinalValue | Unset
        if isinstance(_ordinal_value, Unset):
            ordinal_value = UNSET
        else:
            ordinal_value = TimedConfigOrdinalValue(_ordinal_value)

        _monthly_type = d.pop("monthlyType", UNSET)
        monthly_type: TimedConfigMonthlyType | Unset
        if isinstance(_monthly_type, Unset):
            monthly_type = UNSET
        else:
            monthly_type = TimedConfigMonthlyType(_monthly_type)

        timed_config = cls(
            at_time=at_time,
            week_days=week_days,
            month_days=month_days,
            ordinal=ordinal,
            ordinal_value=ordinal_value,
            monthly_type=monthly_type,
        )

        timed_config.additional_properties = d
        return timed_config

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
