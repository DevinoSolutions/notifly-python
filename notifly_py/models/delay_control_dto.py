from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delay_control_dto_type import DelayControlDtoType
from ..models.delay_control_dto_unit import DelayControlDtoUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delay_control_dto_skip import DelayControlDtoSkip


T = TypeVar("T", bound="DelayControlDto")


@_attrs_define
class DelayControlDto:
    """
    Attributes:
        type_ (DelayControlDtoType): Type of the delay. Currently only 'regular' is supported by the schema. Default:
            DelayControlDtoType.REGULAR.
        skip (DelayControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        amount (float | Unset): Amount of time to delay.
        unit (DelayControlDtoUnit | Unset): Unit of time for the delay amount.
        cron (str | Unset): Cron expression for the delay. Min length 1.
    """

    type_: DelayControlDtoType = DelayControlDtoType.REGULAR
    skip: DelayControlDtoSkip | Unset = UNSET
    amount: float | Unset = UNSET
    unit: DelayControlDtoUnit | Unset = UNSET
    cron: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        cron = self.cron

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if skip is not UNSET:
            field_dict["skip"] = skip
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit
        if cron is not UNSET:
            field_dict["cron"] = cron

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delay_control_dto_skip import DelayControlDtoSkip

        d = dict(src_dict)
        type_ = DelayControlDtoType(d.pop("type"))

        _skip = d.pop("skip", UNSET)
        skip: DelayControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = DelayControlDtoSkip.from_dict(_skip)

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DelayControlDtoUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DelayControlDtoUnit(_unit)

        cron = d.pop("cron", UNSET)

        delay_control_dto = cls(
            type_=type_,
            skip=skip,
            amount=amount,
            unit=unit,
            cron=cron,
        )

        delay_control_dto.additional_properties = d
        return delay_control_dto

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
