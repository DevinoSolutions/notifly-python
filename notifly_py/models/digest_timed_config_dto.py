from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.digest_timed_config_dto_week_days_item import DigestTimedConfigDtoWeekDaysItem
from ..models.monthly_type_enum import MonthlyTypeEnum
from ..models.ordinal_enum import OrdinalEnum
from ..models.ordinal_value_enum import OrdinalValueEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DigestTimedConfigDto")


@_attrs_define
class DigestTimedConfigDto:
    """
    Attributes:
        at_time (str | Unset): Time at which the digest is triggered
        week_days (list[DigestTimedConfigDtoWeekDaysItem] | Unset): Days of the week for the digest
        month_days (list[float] | Unset): Specific days of the month for the digest
        ordinal (OrdinalEnum | Unset): Ordinal position for the digest
        ordinal_value (OrdinalValueEnum | Unset): Value of the ordinal
        monthly_type (MonthlyTypeEnum | Unset): Type of monthly schedule
        cron_expression (str | Unset): Cron expression for scheduling
        until_date (str | Unset): Until date for scheduling
    """

    at_time: str | Unset = UNSET
    week_days: list[DigestTimedConfigDtoWeekDaysItem] | Unset = UNSET
    month_days: list[float] | Unset = UNSET
    ordinal: OrdinalEnum | Unset = UNSET
    ordinal_value: OrdinalValueEnum | Unset = UNSET
    monthly_type: MonthlyTypeEnum | Unset = UNSET
    cron_expression: str | Unset = UNSET
    until_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at_time = self.at_time

        week_days: list[str] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = []
            for week_days_item_data in self.week_days:
                week_days_item = week_days_item_data.value
                week_days.append(week_days_item)

        month_days: list[float] | Unset = UNSET
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

        cron_expression = self.cron_expression

        until_date = self.until_date

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
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if until_date is not UNSET:
            field_dict["untilDate"] = until_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at_time = d.pop("atTime", UNSET)

        _week_days = d.pop("weekDays", UNSET)
        week_days: list[DigestTimedConfigDtoWeekDaysItem] | Unset = UNSET
        if _week_days is not UNSET:
            week_days = []
            for week_days_item_data in _week_days:
                week_days_item = DigestTimedConfigDtoWeekDaysItem(week_days_item_data)

                week_days.append(week_days_item)

        month_days = cast(list[float], d.pop("monthDays", UNSET))

        _ordinal = d.pop("ordinal", UNSET)
        ordinal: OrdinalEnum | Unset
        if isinstance(_ordinal, Unset):
            ordinal = UNSET
        else:
            ordinal = OrdinalEnum(_ordinal)

        _ordinal_value = d.pop("ordinalValue", UNSET)
        ordinal_value: OrdinalValueEnum | Unset
        if isinstance(_ordinal_value, Unset):
            ordinal_value = UNSET
        else:
            ordinal_value = OrdinalValueEnum(_ordinal_value)

        _monthly_type = d.pop("monthlyType", UNSET)
        monthly_type: MonthlyTypeEnum | Unset
        if isinstance(_monthly_type, Unset):
            monthly_type = UNSET
        else:
            monthly_type = MonthlyTypeEnum(_monthly_type)

        cron_expression = d.pop("cronExpression", UNSET)

        until_date = d.pop("untilDate", UNSET)

        digest_timed_config_dto = cls(
            at_time=at_time,
            week_days=week_days,
            month_days=month_days,
            ordinal=ordinal,
            ordinal_value=ordinal_value,
            monthly_type=monthly_type,
            cron_expression=cron_expression,
            until_date=until_date,
        )

        digest_timed_config_dto.additional_properties = d
        return digest_timed_config_dto

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
