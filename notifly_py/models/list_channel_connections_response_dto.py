from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_channel_connection_response_dto import GetChannelConnectionResponseDto


T = TypeVar("T", bound="ListChannelConnectionsResponseDto")


@_attrs_define
class ListChannelConnectionsResponseDto:
    """
    Attributes:
        data (list[GetChannelConnectionResponseDto]): List of returned Channel Connections
        next_ (None | str): The cursor for the next page of results, or null if there are no more pages.
        previous (None | str): The cursor for the previous page of results, or null if this is the first page.
        total_count (float): The total count of items (up to 50,000)
        total_count_capped (bool): Whether there are more than 50,000 results available
    """

    data: list[GetChannelConnectionResponseDto]
    next_: None | str
    previous: None | str
    total_count: float
    total_count_capped: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_: None | str
        next_ = self.next_

        previous: None | str
        previous = self.previous

        total_count = self.total_count

        total_count_capped = self.total_count_capped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "next": next_,
                "previous": previous,
                "totalCount": total_count,
                "totalCountCapped": total_count_capped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_channel_connection_response_dto import GetChannelConnectionResponseDto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetChannelConnectionResponseDto.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        def _parse_previous(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous = _parse_previous(d.pop("previous"))

        total_count = d.pop("totalCount")

        total_count_capped = d.pop("totalCountCapped")

        list_channel_connections_response_dto = cls(
            data=data,
            next_=next_,
            previous=previous,
            total_count=total_count,
            total_count_capped=total_count_capped,
        )

        list_channel_connections_response_dto.additional_properties = d
        return list_channel_connections_response_dto

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
