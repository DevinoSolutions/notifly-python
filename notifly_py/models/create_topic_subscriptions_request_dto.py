from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_topic_subscriptions_request_dto_context import CreateTopicSubscriptionsRequestDtoContext
    from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
    from ..models.topic_subscriber_identifier_dto import TopicSubscriberIdentifierDto
    from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto


T = TypeVar("T", bound="CreateTopicSubscriptionsRequestDto")


@_attrs_define
class CreateTopicSubscriptionsRequestDto:
    """
    Attributes:
        subscriber_ids (list[str] | Unset): List of subscriber IDs to subscribe to the topic (max: 100). @deprecated Use
            the "subscriptions" property instead. Example: ['subscriberId1', 'subscriberId2'].
        subscriptions (list[str | TopicSubscriberIdentifierDto] | Unset): List of subscriptions to subscribe to the
            topic (max: 100). Can be either a string array of subscriber IDs or an array of objects with identifier and
            subscriberId Example: [{'identifier': 'subscriber-123-subscription-a', 'subscriberId': 'subscriber-123'},
            {'identifier': 'subscriber-456-subscription-b', 'subscriberId': 'subscriber-456'}].
        name (str | Unset): The name of the topic Example: My Topic.
        context (CreateTopicSubscriptionsRequestDtoContext | Unset):
        preferences (list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset): The preferences of
            the topic. Can be a simple workflow ID string, workflow preference object, or group filter object Example:
            [{'workflowId': 'workflow-123', 'condition': {'===': [{'var': 'tier'}, 'premium']}}].
    """

    subscriber_ids: list[str] | Unset = UNSET
    subscriptions: list[str | TopicSubscriberIdentifierDto] | Unset = UNSET
    name: str | Unset = UNSET
    context: CreateTopicSubscriptionsRequestDtoContext | Unset = UNSET
    preferences: list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
        from ..models.topic_subscriber_identifier_dto import TopicSubscriberIdentifierDto
        from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto

        subscriber_ids: list[str] | Unset = UNSET
        if not isinstance(self.subscriber_ids, Unset):
            subscriber_ids = self.subscriber_ids

        subscriptions: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item: dict[str, Any] | str
                if isinstance(subscriptions_item_data, TopicSubscriberIdentifierDto):
                    subscriptions_item = subscriptions_item_data.to_dict()
                else:
                    subscriptions_item = subscriptions_item_data
                subscriptions.append(subscriptions_item)

        name = self.name

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        preferences: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = []
            for preferences_item_data in self.preferences:
                preferences_item: dict[str, Any] | str
                if isinstance(preferences_item_data, WorkflowPreferenceRequestDto):
                    preferences_item = preferences_item_data.to_dict()
                elif isinstance(preferences_item_data, GroupPreferenceFilterDto):
                    preferences_item = preferences_item_data.to_dict()
                else:
                    preferences_item = preferences_item_data
                preferences.append(preferences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriber_ids is not UNSET:
            field_dict["subscriberIds"] = subscriber_ids
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if name is not UNSET:
            field_dict["name"] = name
        if context is not UNSET:
            field_dict["context"] = context
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_topic_subscriptions_request_dto_context import CreateTopicSubscriptionsRequestDtoContext
        from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
        from ..models.topic_subscriber_identifier_dto import TopicSubscriberIdentifierDto
        from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto

        d = dict(src_dict)
        subscriber_ids = cast(list[str], d.pop("subscriberIds", UNSET))

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[str | TopicSubscriberIdentifierDto] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:

                def _parse_subscriptions_item(data: object) -> str | TopicSubscriberIdentifierDto:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        subscriptions_item_type_1 = TopicSubscriberIdentifierDto.from_dict(data)

                        return subscriptions_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(str | TopicSubscriberIdentifierDto, data)

                subscriptions_item = _parse_subscriptions_item(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        name = d.pop("name", UNSET)

        _context = d.pop("context", UNSET)
        context: CreateTopicSubscriptionsRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = CreateTopicSubscriptionsRequestDtoContext.from_dict(_context)

        _preferences = d.pop("preferences", UNSET)
        preferences: list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset = UNSET
        if _preferences is not UNSET:
            preferences = []
            for preferences_item_data in _preferences:

                def _parse_preferences_item(
                    data: object,
                ) -> GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        preferences_item_type_1 = WorkflowPreferenceRequestDto.from_dict(data)

                        return preferences_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        preferences_item_type_2 = GroupPreferenceFilterDto.from_dict(data)

                        return preferences_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto, data)

                preferences_item = _parse_preferences_item(preferences_item_data)

                preferences.append(preferences_item)

        create_topic_subscriptions_request_dto = cls(
            subscriber_ids=subscriber_ids,
            subscriptions=subscriptions,
            name=name,
            context=context,
            preferences=preferences,
        )

        create_topic_subscriptions_request_dto.additional_properties = d
        return create_topic_subscriptions_request_dto

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
