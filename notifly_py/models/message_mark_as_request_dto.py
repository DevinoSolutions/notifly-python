from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_mark_as_request_dto_mark_as import MessageMarkAsRequestDtoMarkAs

T = TypeVar("T", bound="MessageMarkAsRequestDto")


@_attrs_define
class MessageMarkAsRequestDto:
    """
    Attributes:
        message_id (list[str] | str):
        mark_as (MessageMarkAsRequestDtoMarkAs):
    """

    message_id: list[str] | str
    mark_as: MessageMarkAsRequestDtoMarkAs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id: list[str] | str
        if isinstance(self.message_id, list):
            message_id = self.message_id

        else:
            message_id = self.message_id

        mark_as = self.mark_as.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "markAs": mark_as,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_message_id(data: object) -> list[str] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                message_id_type_1 = cast(list[str], data)

                return message_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str, data)

        message_id = _parse_message_id(d.pop("messageId"))

        mark_as = MessageMarkAsRequestDtoMarkAs(d.pop("markAs"))

        message_mark_as_request_dto = cls(
            message_id=message_id,
            mark_as=mark_as,
        )

        message_mark_as_request_dto.additional_properties = d
        return message_mark_as_request_dto

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
