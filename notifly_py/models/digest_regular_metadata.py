from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.digest_regular_metadata_backoff_unit import DigestRegularMetadataBackoffUnit
from ..models.digest_regular_metadata_type import DigestRegularMetadataType
from ..models.digest_regular_metadata_unit import DigestRegularMetadataUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="DigestRegularMetadata")


@_attrs_define
class DigestRegularMetadata:
    """
    Attributes:
        type_ (DigestRegularMetadataType):
        amount (float | Unset):
        unit (DigestRegularMetadataUnit | Unset):
        digest_key (str | Unset):
        backoff (bool | Unset):
        backoff_amount (float | Unset):
        backoff_unit (DigestRegularMetadataBackoffUnit | Unset):
        update_mode (bool | Unset):
    """

    type_: DigestRegularMetadataType
    amount: float | Unset = UNSET
    unit: DigestRegularMetadataUnit | Unset = UNSET
    digest_key: str | Unset = UNSET
    backoff: bool | Unset = UNSET
    backoff_amount: float | Unset = UNSET
    backoff_unit: DigestRegularMetadataBackoffUnit | Unset = UNSET
    update_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        digest_key = self.digest_key

        backoff = self.backoff

        backoff_amount = self.backoff_amount

        backoff_unit: str | Unset = UNSET
        if not isinstance(self.backoff_unit, Unset):
            backoff_unit = self.backoff_unit.value

        update_mode = self.update_mode

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
        if backoff is not UNSET:
            field_dict["backoff"] = backoff
        if backoff_amount is not UNSET:
            field_dict["backoffAmount"] = backoff_amount
        if backoff_unit is not UNSET:
            field_dict["backoffUnit"] = backoff_unit
        if update_mode is not UNSET:
            field_dict["updateMode"] = update_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DigestRegularMetadataType(d.pop("type"))

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DigestRegularMetadataUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DigestRegularMetadataUnit(_unit)

        digest_key = d.pop("digestKey", UNSET)

        backoff = d.pop("backoff", UNSET)

        backoff_amount = d.pop("backoffAmount", UNSET)

        _backoff_unit = d.pop("backoffUnit", UNSET)
        backoff_unit: DigestRegularMetadataBackoffUnit | Unset
        if isinstance(_backoff_unit, Unset):
            backoff_unit = UNSET
        else:
            backoff_unit = DigestRegularMetadataBackoffUnit(_backoff_unit)

        update_mode = d.pop("updateMode", UNSET)

        digest_regular_metadata = cls(
            type_=type_,
            amount=amount,
            unit=unit,
            digest_key=digest_key,
            backoff=backoff,
            backoff_amount=backoff_amount,
            backoff_unit=backoff_unit,
            update_mode=update_mode,
        )

        digest_regular_metadata.additional_properties = d
        return digest_regular_metadata

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
