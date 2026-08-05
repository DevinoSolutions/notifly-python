from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_unit_enum import TimeUnitEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_regular_output_look_back_window import DigestRegularOutputLookBackWindow


T = TypeVar("T", bound="DigestRegularOutput")


@_attrs_define
class DigestRegularOutput:
    """
    Attributes:
        amount (float): Amount of time units
        unit (TimeUnitEnum): Time unit
        digest_key (str | Unset): Optional digest key
        look_back_window (DigestRegularOutputLookBackWindow | Unset): Look back window configuration
    """

    amount: float
    unit: TimeUnitEnum
    digest_key: str | Unset = UNSET
    look_back_window: DigestRegularOutputLookBackWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        unit = self.unit.value

        digest_key = self.digest_key

        look_back_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.look_back_window, Unset):
            look_back_window = self.look_back_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "unit": unit,
            }
        )
        if digest_key is not UNSET:
            field_dict["digestKey"] = digest_key
        if look_back_window is not UNSET:
            field_dict["lookBackWindow"] = look_back_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_regular_output_look_back_window import DigestRegularOutputLookBackWindow

        d = dict(src_dict)
        amount = d.pop("amount")

        unit = TimeUnitEnum(d.pop("unit"))

        digest_key = d.pop("digestKey", UNSET)

        _look_back_window = d.pop("lookBackWindow", UNSET)
        look_back_window: DigestRegularOutputLookBackWindow | Unset
        if isinstance(_look_back_window, Unset):
            look_back_window = UNSET
        else:
            look_back_window = DigestRegularOutputLookBackWindow.from_dict(_look_back_window)

        digest_regular_output = cls(
            amount=amount,
            unit=unit,
            digest_key=digest_key,
            look_back_window=look_back_window,
        )

        digest_regular_output.additional_properties = d
        return digest_regular_output

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
