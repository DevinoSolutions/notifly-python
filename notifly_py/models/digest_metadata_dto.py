from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.digest_metadata_dto_unit import DigestMetadataDtoUnit
from ..models.digest_type_enum import DigestTypeEnum
from ..models.digest_unit_enum import DigestUnitEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_metadata_dto_events_item import DigestMetadataDtoEventsItem
    from ..models.digest_timed_config_dto import DigestTimedConfigDto


T = TypeVar("T", bound="DigestMetadataDto")


@_attrs_define
class DigestMetadataDto:
    """
    Attributes:
        type_ (DigestTypeEnum): The Digest Type
        digest_key (str | Unset): Optional key for the digest
        amount (float | Unset): Amount for the digest
        unit (DigestMetadataDtoUnit | Unset): Unit of the digest
        events (list[DigestMetadataDtoEventsItem] | Unset): Optional array of events associated with the digest,
            represented as key-value pairs
        backoff (bool | Unset): Regular digest: Indicates if backoff is enabled for the regular digest
        backoff_amount (float | Unset): Regular digest: Amount for backoff
        backoff_unit (DigestUnitEnum | Unset): Regular digest: Unit for backoff
        update_mode (bool | Unset): Regular digest: Indicates if the digest should update
        timed (DigestTimedConfigDto | Unset):
    """

    type_: DigestTypeEnum
    digest_key: str | Unset = UNSET
    amount: float | Unset = UNSET
    unit: DigestMetadataDtoUnit | Unset = UNSET
    events: list[DigestMetadataDtoEventsItem] | Unset = UNSET
    backoff: bool | Unset = UNSET
    backoff_amount: float | Unset = UNSET
    backoff_unit: DigestUnitEnum | Unset = UNSET
    update_mode: bool | Unset = UNSET
    timed: DigestTimedConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        digest_key = self.digest_key

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        backoff = self.backoff

        backoff_amount = self.backoff_amount

        backoff_unit: str | Unset = UNSET
        if not isinstance(self.backoff_unit, Unset):
            backoff_unit = self.backoff_unit.value

        update_mode = self.update_mode

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
        if digest_key is not UNSET:
            field_dict["digestKey"] = digest_key
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit
        if events is not UNSET:
            field_dict["events"] = events
        if backoff is not UNSET:
            field_dict["backoff"] = backoff
        if backoff_amount is not UNSET:
            field_dict["backoffAmount"] = backoff_amount
        if backoff_unit is not UNSET:
            field_dict["backoffUnit"] = backoff_unit
        if update_mode is not UNSET:
            field_dict["updateMode"] = update_mode
        if timed is not UNSET:
            field_dict["timed"] = timed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_metadata_dto_events_item import DigestMetadataDtoEventsItem
        from ..models.digest_timed_config_dto import DigestTimedConfigDto

        d = dict(src_dict)
        type_ = DigestTypeEnum(d.pop("type"))

        digest_key = d.pop("digestKey", UNSET)

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DigestMetadataDtoUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = DigestMetadataDtoUnit(_unit)

        _events = d.pop("events", UNSET)
        events: list[DigestMetadataDtoEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = DigestMetadataDtoEventsItem.from_dict(events_item_data)

                events.append(events_item)

        backoff = d.pop("backoff", UNSET)

        backoff_amount = d.pop("backoffAmount", UNSET)

        _backoff_unit = d.pop("backoffUnit", UNSET)
        backoff_unit: DigestUnitEnum | Unset
        if isinstance(_backoff_unit, Unset):
            backoff_unit = UNSET
        else:
            backoff_unit = DigestUnitEnum(_backoff_unit)

        update_mode = d.pop("updateMode", UNSET)

        _timed = d.pop("timed", UNSET)
        timed: DigestTimedConfigDto | Unset
        if isinstance(_timed, Unset):
            timed = UNSET
        else:
            timed = DigestTimedConfigDto.from_dict(_timed)

        digest_metadata_dto = cls(
            type_=type_,
            digest_key=digest_key,
            amount=amount,
            unit=unit,
            events=events,
            backoff=backoff,
            backoff_amount=backoff_amount,
            backoff_unit=backoff_unit,
            update_mode=update_mode,
            timed=timed,
        )

        digest_metadata_dto.additional_properties = d
        return digest_metadata_dto

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
