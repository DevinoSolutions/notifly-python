from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_dto import SubscriberDto
    from ..models.subscription_preference_dto import SubscriptionPreferenceDto
    from ..models.topic_response_dto import TopicResponseDto


T = TypeVar("T", bound="TopicSubscriptionResponseDto")


@_attrs_define
class TopicSubscriptionResponseDto:
    """
    Attributes:
        field_id (str): The identifier of the subscription Example: 64da692e9a94fb2e6449ad08.
        identifier (str): The identifier of the subscription Example: tk=product-updates:si=subscriber-123.
        created_at (str): The date and time the subscription was created Example: 2021-01-01T00:00:00.000Z.
        topic (TopicResponseDto):
        subscriber (SubscriberDto):
        context_keys (list[str] | Unset): Context keys that scope this subscription (e.g., tenant:org-a,
            project:proj-123) Example: ['tenant:org-a', 'project:proj-123'].
        preferences (list[SubscriptionPreferenceDto] | Unset): The preferences for workflows in this subscription
    """

    field_id: str
    identifier: str
    created_at: str
    topic: TopicResponseDto
    subscriber: SubscriberDto
    context_keys: list[str] | Unset = UNSET
    preferences: list[SubscriptionPreferenceDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        identifier = self.identifier

        created_at = self.created_at

        topic = self.topic.to_dict()

        subscriber = self.subscriber.to_dict()

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = []
            for preferences_item_data in self.preferences:
                preferences_item = preferences_item_data.to_dict()
                preferences.append(preferences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "identifier": identifier,
                "createdAt": created_at,
                "topic": topic,
                "subscriber": subscriber,
            }
        )
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_dto import SubscriberDto
        from ..models.subscription_preference_dto import SubscriptionPreferenceDto
        from ..models.topic_response_dto import TopicResponseDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        identifier = d.pop("identifier")

        created_at = d.pop("createdAt")

        topic = TopicResponseDto.from_dict(d.pop("topic"))

        subscriber = SubscriberDto.from_dict(d.pop("subscriber"))

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        _preferences = d.pop("preferences", UNSET)
        preferences: list[SubscriptionPreferenceDto] | Unset = UNSET
        if _preferences is not UNSET:
            preferences = []
            for preferences_item_data in _preferences:
                preferences_item = SubscriptionPreferenceDto.from_dict(preferences_item_data)

                preferences.append(preferences_item)

        topic_subscription_response_dto = cls(
            field_id=field_id,
            identifier=identifier,
            created_at=created_at,
            topic=topic,
            subscriber=subscriber,
            context_keys=context_keys,
            preferences=preferences,
        )

        topic_subscription_response_dto.additional_properties = d
        return topic_subscription_response_dto

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
