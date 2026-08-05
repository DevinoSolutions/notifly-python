from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.digest_control_dto_type import DigestControlDtoType
from ..models.digest_control_dto_unit import DigestControlDtoUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_control_dto_skip import DigestControlDtoSkip
    from ..models.look_back_window_dto import LookBackWindowDto


T = TypeVar("T", bound="DigestControlDto")


@_attrs_define
class DigestControlDto:
    """
    Attributes:
        skip (DigestControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        type_ (DigestControlDtoType | Unset): The type of digest strategy. Determines which fields are applicable.
        amount (float | Unset): The amount of time for the digest interval (for REGULAR type). Min 1.
        unit (DigestControlDtoUnit | Unset): The unit of time for the digest interval (for REGULAR type).
        look_back_window (LookBackWindowDto | Unset):
        cron (str | Unset): Cron expression for TIMED digest. Min length 1.
        digest_key (str | Unset): Specify a custom key for digesting events instead of the default event key.
    """

    skip: DigestControlDtoSkip | Unset = UNSET
    type_: DigestControlDtoType | Unset = UNSET
    amount: float | Unset = UNSET
    unit: DigestControlDtoUnit | Unset = UNSET
    look_back_window: LookBackWindowDto | Unset = UNSET
    cron: str | Unset = UNSET
    digest_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        look_back_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.look_back_window, Unset):
            look_back_window = self.look_back_window.to_dict()

        cron = self.cron

        digest_key = self.digest_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip is not UNSET:
            field_dict["skip"] = skip
        if type_ is not UNSET:
            field_dict["type"] = type_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit
        if look_back_window is not UNSET:
            field_dict["lookBackWindow"] = look_back_window
        if cron is not UNSET:
            field_dict["cron"] = cron
        if digest_key is not UNSET:
            field_dict["digestKey"] = digest_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_control_dto_skip import DigestControlDtoSkip
        from ..models.look_back_window_dto import LookBackWindowDto

        d = dict(src_dict)
        _skip = d.pop("skip", UNSET)
        skip: DigestControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = DigestControlDtoSkip.from_dict(_skip)

        _type_ = d.pop("type", UNSET)
        type_: DigestControlDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DigestControlDtoType(_type_)

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DigestControlDtoUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DigestControlDtoUnit(_unit)

        _look_back_window = d.pop("lookBackWindow", UNSET)
        look_back_window: LookBackWindowDto | Unset
        if isinstance(_look_back_window, Unset):
            look_back_window = UNSET
        else:
            look_back_window = LookBackWindowDto.from_dict(_look_back_window)

        cron = d.pop("cron", UNSET)

        digest_key = d.pop("digestKey", UNSET)

        digest_control_dto = cls(
            skip=skip,
            type_=type_,
            amount=amount,
            unit=unit,
            look_back_window=look_back_window,
            cron=cron,
            digest_key=digest_key,
        )

        digest_control_dto.additional_properties = d
        return digest_control_dto

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
