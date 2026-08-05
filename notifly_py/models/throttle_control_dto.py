from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.throttle_control_dto_type import ThrottleControlDtoType
from ..models.throttle_control_dto_unit import ThrottleControlDtoUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.throttle_control_dto_skip import ThrottleControlDtoSkip


T = TypeVar("T", bound="ThrottleControlDto")


@_attrs_define
class ThrottleControlDto:
    """
    Attributes:
        type_ (ThrottleControlDtoType): The type of throttle window. Default: ThrottleControlDtoType.FIXED.
        skip (ThrottleControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step
            execution. Supports complex logical operations with AND, OR, and comparison operators. See
            https://jsonlogic.com/ for full typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']},
            {'==': [{'var': 'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        amount (float | Unset): The amount of time for the throttle window (required for fixed type).
        unit (ThrottleControlDtoUnit | Unset): The unit of time for the throttle window (required for fixed type).
        dynamic_key (str | Unset): Key path to retrieve dynamic window value (required for dynamic type). Example:
            payload.timestamp.
        threshold (float | Unset): The maximum number of executions allowed within the window. Defaults to 1. Default:
            1.0.
        throttle_key (str | Unset): Optional key for grouping throttle rules. If not provided, defaults to workflow and
            subscriber combination.
    """

    type_: ThrottleControlDtoType = ThrottleControlDtoType.FIXED
    skip: ThrottleControlDtoSkip | Unset = UNSET
    amount: float | Unset = UNSET
    unit: ThrottleControlDtoUnit | Unset = UNSET
    dynamic_key: str | Unset = UNSET
    threshold: float | Unset = 1.0
    throttle_key: str | Unset = UNSET
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

        dynamic_key = self.dynamic_key

        threshold = self.threshold

        throttle_key = self.throttle_key

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
        if dynamic_key is not UNSET:
            field_dict["dynamicKey"] = dynamic_key
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if throttle_key is not UNSET:
            field_dict["throttleKey"] = throttle_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.throttle_control_dto_skip import ThrottleControlDtoSkip

        d = dict(src_dict)
        type_ = ThrottleControlDtoType(d.pop("type"))

        _skip = d.pop("skip", UNSET)
        skip: ThrottleControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = ThrottleControlDtoSkip.from_dict(_skip)

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: ThrottleControlDtoUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = ThrottleControlDtoUnit(_unit)

        dynamic_key = d.pop("dynamicKey", UNSET)

        threshold = d.pop("threshold", UNSET)

        throttle_key = d.pop("throttleKey", UNSET)

        throttle_control_dto = cls(
            type_=type_,
            skip=skip,
            amount=amount,
            unit=unit,
            dynamic_key=dynamic_key,
            threshold=threshold,
            throttle_key=throttle_key,
        )

        throttle_control_dto.additional_properties = d
        return throttle_control_dto

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
