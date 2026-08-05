from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mark_message_action_as_seen_dto_status import MarkMessageActionAsSeenDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_message_action_as_seen_dto_payload import MarkMessageActionAsSeenDtoPayload


T = TypeVar("T", bound="MarkMessageActionAsSeenDto")


@_attrs_define
class MarkMessageActionAsSeenDto:
    """
    Attributes:
        status (MarkMessageActionAsSeenDtoStatus): Message action status
        payload (MarkMessageActionAsSeenDtoPayload | Unset): Message action payload
    """

    status: MarkMessageActionAsSeenDtoStatus
    payload: MarkMessageActionAsSeenDtoPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mark_message_action_as_seen_dto_payload import MarkMessageActionAsSeenDtoPayload

        d = dict(src_dict)
        status = MarkMessageActionAsSeenDtoStatus(d.pop("status"))

        _payload = d.pop("payload", UNSET)
        payload: MarkMessageActionAsSeenDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = MarkMessageActionAsSeenDtoPayload.from_dict(_payload)

        mark_message_action_as_seen_dto = cls(
            status=status,
            payload=payload,
        )

        mark_message_action_as_seen_dto.additional_properties = d
        return mark_message_action_as_seen_dto

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
