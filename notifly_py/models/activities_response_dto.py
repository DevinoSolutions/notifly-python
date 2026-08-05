from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.activity_notification_response_dto import ActivityNotificationResponseDto


T = TypeVar("T", bound="ActivitiesResponseDto")


@_attrs_define
class ActivitiesResponseDto:
    """
    Attributes:
        has_more (bool): Indicates if there are more activities in the result set
        data (list[ActivityNotificationResponseDto]): Array of activity notifications
        page_size (float): Page size of the activities
        page (float): Current page of the activities
    """

    has_more: bool
    data: list[ActivityNotificationResponseDto]
    page_size: float
    page: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        page_size = self.page_size

        page = self.page

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_notification_response_dto import ActivityNotificationResponseDto

        d = dict(src_dict)
        has_more = d.pop("hasMore")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ActivityNotificationResponseDto.from_dict(data_item_data)

            data.append(data_item)

        page_size = d.pop("pageSize")

        page = d.pop("page")

        activities_response_dto = cls(
            has_more=has_more,
            data=data,
            page_size=page_size,
            page=page,
        )

        activities_response_dto.additional_properties = d
        return activities_response_dto

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
