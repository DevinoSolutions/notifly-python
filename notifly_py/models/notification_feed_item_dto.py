from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..models.notification_feed_item_dto_status import NotificationFeedItemDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actor_feed_item_dto import ActorFeedItemDto
    from ..models.message_cta import MessageCTA
    from ..models.notification_feed_item_dto_data_type_0 import NotificationFeedItemDtoDataType0
    from ..models.notification_feed_item_dto_overrides import NotificationFeedItemDtoOverrides
    from ..models.notification_feed_item_dto_payload import NotificationFeedItemDtoPayload
    from ..models.subscriber_feed_response_dto import SubscriberFeedResponseDto


T = TypeVar("T", bound="NotificationFeedItemDto")


@_attrs_define
class NotificationFeedItemDto:
    """
    Attributes:
        field_id (str): Unique identifier for the notification. Example: 615c1f2f9b0c5b001f8e4e3b.
        field_template_id (str): Identifier for the template used to generate the notification. Example: template_12345.
        field_environment_id (str): Identifier for the environment where the notification is sent. Example: env_67890.
        field_organization_id (str): Identifier for the organization sending the notification. Example: org_98765.
        field_notification_id (str): Unique identifier for the notification instance. Example: notification_123456.
        field_subscriber_id (str): Unique identifier for the subscriber receiving the notification. Example:
            subscriber_112233.
        field_job_id (str): Identifier for the job that triggered the notification. Example: job_778899.
        transaction_id (str): Unique identifier for the transaction associated with the notification. Example:
            transaction_123456.
        content (str): The main content of the notification. Example: This is a test notification content..
        channel (ChannelTypeEnum): Channel type through which the message is sent
        read (bool): Indicates whether the notification has been read by the subscriber.
        seen (bool): Indicates whether the notification has been seen by the subscriber. Example: True.
        archived (bool): Indicates whether the notification has been archived by the subscriber.
        cta (MessageCTA):
        status (NotificationFeedItemDtoStatus): Current status of the notification. Example: sent.
        field_message_template_id (str | Unset): Identifier for the message template used. Example:
            message_template_54321.
        field_feed_id (None | str | Unset): Identifier for the feed associated with the notification. Example:
            feed_445566.
        created_at (datetime.datetime | None | Unset): Timestamp indicating when the notification was created. Example:
            2024-12-10T10:10:59.639Z.
        updated_at (datetime.datetime | None | Unset): Timestamp indicating when the notification was last updated.
            Example: 2024-12-10T10:10:59.639Z.
        actor (ActorFeedItemDto | Unset):
        subscriber (SubscriberFeedResponseDto | Unset):
        template_identifier (None | str | Unset): Identifier for the template used, if applicable. Example:
            template_abcdef.
        provider_id (None | str | Unset): Identifier for the provider that sends the notification. Example:
            provider_xyz.
        subject (None | str | Unset): The subject line for email notifications, if applicable. Example: Test
            Notification Subject.
        device_tokens (list[str] | None | Unset): Device tokens for push notifications, if applicable. Example:
            ['token1', 'token2'].
        payload (NotificationFeedItemDtoPayload | Unset): The payload that was used to send the notification trigger.
            Example: {'key': 'value'}.
        data (None | NotificationFeedItemDtoDataType0 | Unset): The data sent with the notification. Example: {'key':
            'value'}.
        overrides (NotificationFeedItemDtoOverrides | Unset): Provider-specific overrides used when triggering the
            notification. Example: {'overrideKey': 'overrideValue'}.
        tags (list[str] | None | Unset): Tags associated with the workflow that triggered the notification. Example:
            ['tag1', 'tag2'].
    """

    field_id: str
    field_template_id: str
    field_environment_id: str
    field_organization_id: str
    field_notification_id: str
    field_subscriber_id: str
    field_job_id: str
    transaction_id: str
    content: str
    channel: ChannelTypeEnum
    read: bool
    seen: bool
    archived: bool
    cta: MessageCTA
    status: NotificationFeedItemDtoStatus
    field_message_template_id: str | Unset = UNSET
    field_feed_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    actor: ActorFeedItemDto | Unset = UNSET
    subscriber: SubscriberFeedResponseDto | Unset = UNSET
    template_identifier: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    subject: None | str | Unset = UNSET
    device_tokens: list[str] | None | Unset = UNSET
    payload: NotificationFeedItemDtoPayload | Unset = UNSET
    data: None | NotificationFeedItemDtoDataType0 | Unset = UNSET
    overrides: NotificationFeedItemDtoOverrides | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_feed_item_dto_data_type_0 import NotificationFeedItemDtoDataType0

        field_id = self.field_id

        field_template_id = self.field_template_id

        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        field_notification_id = self.field_notification_id

        field_subscriber_id = self.field_subscriber_id

        field_job_id = self.field_job_id

        transaction_id = self.transaction_id

        content = self.content

        channel = self.channel.value

        read = self.read

        seen = self.seen

        archived = self.archived

        cta = self.cta.to_dict()

        status = self.status.value

        field_message_template_id = self.field_message_template_id

        field_feed_id: None | str | Unset
        if isinstance(self.field_feed_id, Unset):
            field_feed_id = UNSET
        else:
            field_feed_id = self.field_feed_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        subscriber: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        template_identifier: None | str | Unset
        if isinstance(self.template_identifier, Unset):
            template_identifier = UNSET
        else:
            template_identifier = self.template_identifier

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        device_tokens: list[str] | None | Unset
        if isinstance(self.device_tokens, Unset):
            device_tokens = UNSET
        elif isinstance(self.device_tokens, list):
            device_tokens = self.device_tokens

        else:
            device_tokens = self.device_tokens

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, NotificationFeedItemDtoDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "_templateId": field_template_id,
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "_notificationId": field_notification_id,
                "_subscriberId": field_subscriber_id,
                "_jobId": field_job_id,
                "transactionId": transaction_id,
                "content": content,
                "channel": channel,
                "read": read,
                "seen": seen,
                "archived": archived,
                "cta": cta,
                "status": status,
            }
        )
        if field_message_template_id is not UNSET:
            field_dict["_messageTemplateId"] = field_message_template_id
        if field_feed_id is not UNSET:
            field_dict["_feedId"] = field_feed_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if actor is not UNSET:
            field_dict["actor"] = actor
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber
        if template_identifier is not UNSET:
            field_dict["templateIdentifier"] = template_identifier
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if device_tokens is not UNSET:
            field_dict["deviceTokens"] = device_tokens
        if payload is not UNSET:
            field_dict["payload"] = payload
        if data is not UNSET:
            field_dict["data"] = data
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actor_feed_item_dto import ActorFeedItemDto
        from ..models.message_cta import MessageCTA
        from ..models.notification_feed_item_dto_data_type_0 import NotificationFeedItemDtoDataType0
        from ..models.notification_feed_item_dto_overrides import NotificationFeedItemDtoOverrides
        from ..models.notification_feed_item_dto_payload import NotificationFeedItemDtoPayload
        from ..models.subscriber_feed_response_dto import SubscriberFeedResponseDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        field_template_id = d.pop("_templateId")

        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        field_notification_id = d.pop("_notificationId")

        field_subscriber_id = d.pop("_subscriberId")

        field_job_id = d.pop("_jobId")

        transaction_id = d.pop("transactionId")

        content = d.pop("content")

        channel = ChannelTypeEnum(d.pop("channel"))

        read = d.pop("read")

        seen = d.pop("seen")

        archived = d.pop("archived")

        cta = MessageCTA.from_dict(d.pop("cta"))

        status = NotificationFeedItemDtoStatus(d.pop("status"))

        field_message_template_id = d.pop("_messageTemplateId", UNSET)

        def _parse_field_feed_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_feed_id = _parse_field_feed_id(d.pop("_feedId", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        _actor = d.pop("actor", UNSET)
        actor: ActorFeedItemDto | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = ActorFeedItemDto.from_dict(_actor)

        _subscriber = d.pop("subscriber", UNSET)
        subscriber: SubscriberFeedResponseDto | Unset
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = SubscriberFeedResponseDto.from_dict(_subscriber)

        def _parse_template_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_identifier = _parse_template_identifier(d.pop("templateIdentifier", UNSET))

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("providerId", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_device_tokens(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                device_tokens_type_0 = cast(list[str], data)

                return device_tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        device_tokens = _parse_device_tokens(d.pop("deviceTokens", UNSET))

        _payload = d.pop("payload", UNSET)
        payload: NotificationFeedItemDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = NotificationFeedItemDtoPayload.from_dict(_payload)

        def _parse_data(data: object) -> None | NotificationFeedItemDtoDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = NotificationFeedItemDtoDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationFeedItemDtoDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        _overrides = d.pop("overrides", UNSET)
        overrides: NotificationFeedItemDtoOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = NotificationFeedItemDtoOverrides.from_dict(_overrides)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        notification_feed_item_dto = cls(
            field_id=field_id,
            field_template_id=field_template_id,
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            field_notification_id=field_notification_id,
            field_subscriber_id=field_subscriber_id,
            field_job_id=field_job_id,
            transaction_id=transaction_id,
            content=content,
            channel=channel,
            read=read,
            seen=seen,
            archived=archived,
            cta=cta,
            status=status,
            field_message_template_id=field_message_template_id,
            field_feed_id=field_feed_id,
            created_at=created_at,
            updated_at=updated_at,
            actor=actor,
            subscriber=subscriber,
            template_identifier=template_identifier,
            provider_id=provider_id,
            subject=subject,
            device_tokens=device_tokens,
            payload=payload,
            data=data,
            overrides=overrides,
            tags=tags,
        )

        notification_feed_item_dto.additional_properties = d
        return notification_feed_item_dto

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
