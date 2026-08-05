from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delay_regular_metadata_type import DelayRegularMetadataType
from ..models.delay_regular_metadata_unit import DelayRegularMetadataUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="DelayRegularMetadata")


@_attrs_define
class DelayRegularMetadata:
    """
    Attributes:
        type_ (DelayRegularMetadataType):
        amount (float | Unset):
        unit (DelayRegularMetadataUnit | Unset):
    """

    type_: DelayRegularMetadataType
    amount: float | Unset = UNSET
    unit: DelayRegularMetadataUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DelayRegularMetadataType(d.pop("type"))

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DelayRegularMetadataUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DelayRegularMetadataUnit(_unit)

        delay_regular_metadata = cls(
            type_=type_,
            amount=amount,
            unit=unit,
        )

        delay_regular_metadata.additional_properties = d
        return delay_regular_metadata

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
