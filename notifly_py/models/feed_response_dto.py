from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_feed_item_dto import NotificationFeedItemDto


T = TypeVar("T", bound="FeedResponseDto")


@_attrs_define
class FeedResponseDto:
    """
    Attributes:
        has_more (bool): Indicates if there are more notifications to load. Example: True.
        data (list[NotificationFeedItemDto]): Array of notifications returned in the response.
        page_size (float): The number of notifications returned in this response. Example: 2.
        page (float): The current page number of the notifications. Example: 1.
        total_count (float | Unset): Total number of notifications available. Example: 5.
    """

    has_more: bool
    data: list[NotificationFeedItemDto]
    page_size: float
    page: float
    total_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        page_size = self.page_size

        page = self.page

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasMore": has_more,
                "data": data,
                "pageSize": page_size,
                "page": page,
            }
        )
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_feed_item_dto import NotificationFeedItemDto

        d = dict(src_dict)
        has_more = d.pop("hasMore")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = NotificationFeedItemDto.from_dict(data_item_data)

            data.append(data_item)

        page_size = d.pop("pageSize")

        page = d.pop("page")

        total_count = d.pop("totalCount", UNSET)

        feed_response_dto = cls(
            has_more=has_more,
            data=data,
            page_size=page_size,
            page=page,
            total_count=total_count,
        )

        feed_response_dto.additional_properties = d
        return feed_response_dto

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
