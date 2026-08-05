from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_subscriber_notifications_count_response_dto_filter import (
        GetSubscriberNotificationsCountResponseDtoFilter,
    )


T = TypeVar("T", bound="GetSubscriberNotificationsCountResponseDto")


@_attrs_define
class GetSubscriberNotificationsCountResponseDto:
    """
    Attributes:
        count (float): The count of notifications matching the filter
        filter_ (GetSubscriberNotificationsCountResponseDtoFilter): The filter applied
    """

    count: float
    filter_: GetSubscriberNotificationsCountResponseDtoFilter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_subscriber_notifications_count_response_dto_filter import (
            GetSubscriberNotificationsCountResponseDtoFilter,
        )

        d = dict(src_dict)
        count = d.pop("count")

        filter_ = GetSubscriberNotificationsCountResponseDtoFilter.from_dict(d.pop("filter"))

        get_subscriber_notifications_count_response_dto = cls(
            count=count,
            filter_=filter_,
        )

        get_subscriber_notifications_count_response_dto.additional_properties = d
        return get_subscriber_notifications_count_response_dto

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
