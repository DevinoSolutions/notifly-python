from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_subscriber_request_dto import CreateSubscriberRequestDto


T = TypeVar("T", bound="BulkSubscriberCreateDto")


@_attrs_define
class BulkSubscriberCreateDto:
    """
    Attributes:
        subscribers (list[CreateSubscriberRequestDto]): An array of subscribers to be created in bulk.
    """

    subscribers: list[CreateSubscriberRequestDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscribers = []
        for subscribers_item_data in self.subscribers:
            subscribers_item = subscribers_item_data.to_dict()
            subscribers.append(subscribers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscribers": subscribers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subscriber_request_dto import CreateSubscriberRequestDto

        d = dict(src_dict)
        subscribers = []
        _subscribers = d.pop("subscribers")
        for subscribers_item_data in _subscribers:
            subscribers_item = CreateSubscriberRequestDto.from_dict(subscribers_item_data)

            subscribers.append(subscribers_item)

        bulk_subscriber_create_dto = cls(
            subscribers=subscribers,
        )

        bulk_subscriber_create_dto.additional_properties = d
        return bulk_subscriber_create_dto

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
