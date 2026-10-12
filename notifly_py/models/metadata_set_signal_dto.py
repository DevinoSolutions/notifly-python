from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_set_signal_dto_action import MetadataSetSignalDtoAction
from ..models.metadata_set_signal_dto_type import MetadataSetSignalDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_set_signal_dto_value import MetadataSetSignalDtoValue


T = TypeVar("T", bound="MetadataSetSignalDto")


@_attrs_define
class MetadataSetSignalDto:
    """
    Attributes:
        type_ (MetadataSetSignalDtoType):
        key (str): Metadata key (1–128 chars; letters, digits, and `-` `_` `:` separators). Example: crm:ticketId.
        value (MetadataSetSignalDtoValue): JSON-serializable value to store. Example: TCK-1001.
        action (MetadataSetSignalDtoAction | Unset): Defaults to `set` when omitted. Default:
            MetadataSetSignalDtoAction.SET.
    """

    type_: MetadataSetSignalDtoType
    key: str
    value: MetadataSetSignalDtoValue
    action: MetadataSetSignalDtoAction | Unset = MetadataSetSignalDtoAction.SET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        key = self.key

        value = self.value.to_dict()

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "key": key,
                "value": value,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_set_signal_dto_value import MetadataSetSignalDtoValue

        d = dict(src_dict)
        type_ = MetadataSetSignalDtoType(d.pop("type"))

        key = d.pop("key")

        value = MetadataSetSignalDtoValue.from_dict(d.pop("value"))

        _action = d.pop("action", UNSET)
        action: MetadataSetSignalDtoAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = MetadataSetSignalDtoAction(_action)

        metadata_set_signal_dto = cls(
            type_=type_,
            key=key,
            value=value,
            action=action,
        )

        metadata_set_signal_dto.additional_properties = d
        return metadata_set_signal_dto

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
