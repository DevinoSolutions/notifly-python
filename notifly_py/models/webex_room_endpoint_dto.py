from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebexRoomEndpointDto")


@_attrs_define
class WebexRoomEndpointDto:
    """
    Attributes:
        room_id (str): Webex room ID Example: Y2lzY29zcGFyazovL3VzL1JPT00v....
        parent_id (str | Unset): Optional Webex parent message ID for threaded replies Example:
            Y2lzY29zcGFyazovL3VzL01FU1NBR0Uv....
    """

    room_id: str
    parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roomId": room_id,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("roomId")

        parent_id = d.pop("parentId", UNSET)

        webex_room_endpoint_dto = cls(
            room_id=room_id,
            parent_id=parent_id,
        )

        webex_room_endpoint_dto.additional_properties = d
        return webex_room_endpoint_dto

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
