from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mark_subscriber_notifications_as_seen_dto_tags import MarkSubscriberNotificationsAsSeenDtoTags


T = TypeVar("T", bound="MarkSubscriberNotificationsAsSeenDto")


@_attrs_define
class MarkSubscriberNotificationsAsSeenDto:
    """
    Attributes:
        notification_ids (list[str] | Unset): Specific notification IDs to mark as seen
        tags (MarkSubscriberNotificationsAsSeenDtoTags | Unset): Filter notifications by workflow tags (OR for string[],
            or { and: [{ or: string[] }, ...] } for AND of OR-groups).
        data (str | Unset): Filter notifications by data attributes (JSON string)
        context_keys (list[str] | Unset): Context keys for filtering notifications
    """

    notification_ids: list[str] | Unset = UNSET
    tags: MarkSubscriberNotificationsAsSeenDtoTags | Unset = UNSET
    data: str | Unset = UNSET
    context_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_ids: list[str] | Unset = UNSET
        if not isinstance(self.notification_ids, Unset):
            notification_ids = self.notification_ids

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        data = self.data

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_ids is not UNSET:
            field_dict["notificationIds"] = notification_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if data is not UNSET:
            field_dict["data"] = data
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mark_subscriber_notifications_as_seen_dto_tags import MarkSubscriberNotificationsAsSeenDtoTags

        d = dict(src_dict)
        notification_ids = cast(list[str], d.pop("notificationIds", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: MarkSubscriberNotificationsAsSeenDtoTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = MarkSubscriberNotificationsAsSeenDtoTags.from_dict(_tags)

        data = d.pop("data", UNSET)

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        mark_subscriber_notifications_as_seen_dto = cls(
            notification_ids=notification_ids,
            tags=tags,
            data=data,
            context_keys=context_keys,
        )

        mark_subscriber_notifications_as_seen_dto.additional_properties = d
        return mark_subscriber_notifications_as_seen_dto

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
