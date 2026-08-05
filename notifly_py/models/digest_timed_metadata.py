from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.digest_timed_metadata_type import DigestTimedMetadataType
from ..models.digest_timed_metadata_unit import DigestTimedMetadataUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timed_config import TimedConfig


T = TypeVar("T", bound="DigestTimedMetadata")


@_attrs_define
class DigestTimedMetadata:
    """
    Attributes:
        type_ (DigestTimedMetadataType):
        amount (float | Unset):
        unit (DigestTimedMetadataUnit | Unset):
        digest_key (str | Unset):
        timed (TimedConfig | Unset):
    """

    type_: DigestTimedMetadataType
    amount: float | Unset = UNSET
    unit: DigestTimedMetadataUnit | Unset = UNSET
    digest_key: str | Unset = UNSET
    timed: TimedConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        digest_key = self.digest_key

        timed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timed, Unset):
            timed = self.timed.to_dict()

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
        if digest_key is not UNSET:
            field_dict["digestKey"] = digest_key
        if timed is not UNSET:
            field_dict["timed"] = timed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timed_config import TimedConfig

        d = dict(src_dict)
        type_ = DigestTimedMetadataType(d.pop("type"))

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DigestTimedMetadataUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DigestTimedMetadataUnit(_unit)

        digest_key = d.pop("digestKey", UNSET)

        _timed = d.pop("timed", UNSET)
        timed: TimedConfig | Unset
        if isinstance(_timed, Unset):
            timed = UNSET
        else:
            timed = TimedConfig.from_dict(_timed)

        digest_timed_metadata = cls(
            type_=type_,
            amount=amount,
            unit=unit,
            digest_key=digest_key,
            timed=timed,
        )

        digest_timed_metadata.additional_properties = d
        return digest_timed_metadata

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
