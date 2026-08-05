from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delay_scheduled_metadata_type import DelayScheduledMetadataType

T = TypeVar("T", bound="DelayScheduledMetadata")


@_attrs_define
class DelayScheduledMetadata:
    """
    Attributes:
        type_ (DelayScheduledMetadataType):
        delay_path (str):
    """

    type_: DelayScheduledMetadataType
    delay_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        delay_path = self.delay_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "delayPath": delay_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DelayScheduledMetadataType(d.pop("type"))

        delay_path = d.pop("delayPath")

        delay_scheduled_metadata = cls(
            type_=type_,
            delay_path=delay_path,
        )

        delay_scheduled_metadata.additional_properties = d
        return delay_scheduled_metadata

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
