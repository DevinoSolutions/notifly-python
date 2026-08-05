from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_topic_subscriber_identifier_dto import DeleteTopicSubscriberIdentifierDto


T = TypeVar("T", bound="DeleteTopicSubscriptionsRequestDto")


@_attrs_define
class DeleteTopicSubscriptionsRequestDto:
    """
    Attributes:
        subscriber_ids (list[str] | Unset): List of subscriber identifiers to unsubscribe from the topic (max: 100).
            @deprecated Use the "subscriptions" property instead. Example: ['subscriberId1', 'subscriberId2'].
        subscriptions (list[DeleteTopicSubscriberIdentifierDto | str] | Unset): List of subscriptions to unsubscribe
            from the topic (max: 100). Can be either a string array of subscriber IDs or an array of objects with identifier
            and/or subscriberId. If only subscriberId is provided, all subscriptions for that subscriber within the topic
            will be deleted. Example: [{'identifier': 'subscriber-123-subscription-a', 'subscriberId': 'subscriber-123'},
            {'subscriberId': 'subscriber-456'}, {'identifier': 'subscriber-789-subscription-b'}].
    """

    subscriber_ids: list[str] | Unset = UNSET
    subscriptions: list[DeleteTopicSubscriberIdentifierDto | str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_topic_subscriber_identifier_dto import DeleteTopicSubscriberIdentifierDto

        subscriber_ids: list[str] | Unset = UNSET
        if not isinstance(self.subscriber_ids, Unset):
            subscriber_ids = self.subscriber_ids

        subscriptions: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item: dict[str, Any] | str
                if isinstance(subscriptions_item_data, DeleteTopicSubscriberIdentifierDto):
                    subscriptions_item = subscriptions_item_data.to_dict()
                else:
                    subscriptions_item = subscriptions_item_data
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriber_ids is not UNSET:
            field_dict["subscriberIds"] = subscriber_ids
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_topic_subscriber_identifier_dto import DeleteTopicSubscriberIdentifierDto

        d = dict(src_dict)
        subscriber_ids = cast(list[str], d.pop("subscriberIds", UNSET))

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[DeleteTopicSubscriberIdentifierDto | str] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:

                def _parse_subscriptions_item(data: object) -> DeleteTopicSubscriberIdentifierDto | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        subscriptions_item_type_1 = DeleteTopicSubscriberIdentifierDto.from_dict(data)

                        return subscriptions_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(DeleteTopicSubscriberIdentifierDto | str, data)

                subscriptions_item = _parse_subscriptions_item(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        delete_topic_subscriptions_request_dto = cls(
            subscriber_ids=subscriber_ids,
            subscriptions=subscriptions,
        )

        delete_topic_subscriptions_request_dto.additional_properties = d
        return delete_topic_subscriptions_request_dto

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
