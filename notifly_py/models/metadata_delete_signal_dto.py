from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_delete_signal_dto_action import MetadataDeleteSignalDtoAction
from ..models.metadata_delete_signal_dto_type import MetadataDeleteSignalDtoType

T = TypeVar("T", bound="MetadataDeleteSignalDto")


@_attrs_define
class MetadataDeleteSignalDto:
    """
    Attributes:
        type_ (MetadataDeleteSignalDtoType):
        action (MetadataDeleteSignalDtoAction):
        key (str): Metadata key to remove. Example: crm:ticketId.
    """

    type_: MetadataDeleteSignalDtoType
    action: MetadataDeleteSignalDtoAction
    key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        action = self.action.value

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "action": action,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MetadataDeleteSignalDtoType(d.pop("type"))

        action = MetadataDeleteSignalDtoAction(d.pop("action"))

        key = d.pop("key")

        metadata_delete_signal_dto = cls(
            type_=type_,
            action=action,
            key=key,
        )

        metadata_delete_signal_dto.additional_properties = d
        return metadata_delete_signal_dto

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
