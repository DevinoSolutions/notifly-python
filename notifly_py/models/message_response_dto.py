from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..models.message_status_enum import MessageStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_block import EmailBlock
    from ..models.message_cta import MessageCTA
    from ..models.message_response_dto_overrides import MessageResponseDtoOverrides
    from ..models.message_response_dto_payload import MessageResponseDtoPayload
    from ..models.subscriber_response_dto import SubscriberResponseDto
    from ..models.workflow_response import WorkflowResponse


T = TypeVar("T", bound="MessageResponseDto")


@_attrs_define
class MessageResponseDto:
    """
    Attributes:
        field_environment_id (str): Environment ID where the message is sent
        field_organization_id (str): Organization ID associated with the message
        field_notification_id (str): Notification ID associated with the message
        field_subscriber_id (str): Subscriber ID associated with the message
        created_at (str): Creation date of the message
        transaction_id (str): Transaction ID associated with the message
        channel (ChannelTypeEnum): Channel type through which the message is sent
        read (bool): Indicates if the message has been read
        seen (bool): Indicates if the message has been seen
        cta (MessageCTA):
        status (MessageStatusEnum): Status of the message
        field_id (str | Unset): Unique identifier for the message
        field_template_id (None | str | Unset): Template ID associated with the message
        field_message_template_id (None | str | Unset): Message template ID
        subscriber (SubscriberResponseDto | Unset):
        template (WorkflowResponse | Unset):
        template_identifier (str | Unset): Identifier for the message template
        delivered_at (list[str] | Unset): Array of delivery dates for the message, if the message has multiple delivery
            dates, for example after being snoozed
        last_seen_date (str | Unset): Last seen date of the message, if available
        last_read_date (str | Unset): Last read date of the message, if available
        content (list[EmailBlock] | None | str | Unset): Content of the message, can be an email block or a string
        subject (str | Unset): Subject of the message, if applicable
        snoozed_until (str | Unset): Date when the message will be unsnoozed
        email (str | Unset): Email address associated with the message, if applicable
        phone (str | Unset): Phone number associated with the message, if applicable
        direct_webhook_url (str | Unset): Direct webhook URL for the message, if applicable
        provider_id (str | Unset): Provider ID associated with the message, if applicable
        device_tokens (list[str] | Unset): Device tokens associated with the message, if applicable
        title (str | Unset): Title of the message, if applicable
        field_feed_id (None | str | Unset): Feed ID associated with the message, if applicable
        error_id (str | Unset): Error ID if the message has an error
        error_text (str | Unset): Error text if the message has an error
        payload (MessageResponseDtoPayload | Unset): The payload that was used to send the notification trigger
        overrides (MessageResponseDtoOverrides | Unset): Provider specific overrides used when triggering the
            notification
        context_keys (list[str] | Unset): Context (single or multi) in which the message was sent Example:
            ['tenant:org-123', 'region:us-east-1'].
    """

    field_environment_id: str
    field_organization_id: str
    field_notification_id: str
    field_subscriber_id: str
    created_at: str
    transaction_id: str
    channel: ChannelTypeEnum
    read: bool
    seen: bool
    cta: MessageCTA
    status: MessageStatusEnum
    field_id: str | Unset = UNSET
    field_template_id: None | str | Unset = UNSET
    field_message_template_id: None | str | Unset = UNSET
    subscriber: SubscriberResponseDto | Unset = UNSET
    template: WorkflowResponse | Unset = UNSET
    template_identifier: str | Unset = UNSET
    delivered_at: list[str] | Unset = UNSET
    last_seen_date: str | Unset = UNSET
    last_read_date: str | Unset = UNSET
    content: list[EmailBlock] | None | str | Unset = UNSET
    subject: str | Unset = UNSET
    snoozed_until: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    direct_webhook_url: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    device_tokens: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    field_feed_id: None | str | Unset = UNSET
    error_id: str | Unset = UNSET
    error_text: str | Unset = UNSET
    payload: MessageResponseDtoPayload | Unset = UNSET
    overrides: MessageResponseDtoOverrides | Unset = UNSET
    context_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        field_notification_id = self.field_notification_id

        field_subscriber_id = self.field_subscriber_id

        created_at = self.created_at

        transaction_id = self.transaction_id

        channel = self.channel.value

        read = self.read

        seen = self.seen

        cta = self.cta.to_dict()

        status = self.status.value

        field_id = self.field_id

        field_template_id: None | str | Unset
        if isinstance(self.field_template_id, Unset):
            field_template_id = UNSET
        else:
            field_template_id = self.field_template_id

        field_message_template_id: None | str | Unset
        if isinstance(self.field_message_template_id, Unset):
            field_message_template_id = UNSET
        else:
            field_message_template_id = self.field_message_template_id

        subscriber: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        template_identifier = self.template_identifier

        delivered_at: list[str] | Unset = UNSET
        if not isinstance(self.delivered_at, Unset):
            delivered_at = self.delivered_at

        last_seen_date = self.last_seen_date

        last_read_date = self.last_read_date

        content: list[dict[str, Any]] | None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, list):
            content = []
            for content_type_0_item_data in self.content:
                content_type_0_item = content_type_0_item_data.to_dict()
                content.append(content_type_0_item)

        else:
            content = self.content

        subject = self.subject

        snoozed_until = self.snoozed_until

        email = self.email

        phone = self.phone

        direct_webhook_url = self.direct_webhook_url

        provider_id = self.provider_id

        device_tokens: list[str] | Unset = UNSET
        if not isinstance(self.device_tokens, Unset):
            device_tokens = self.device_tokens

        title = self.title

        field_feed_id: None | str | Unset
        if isinstance(self.field_feed_id, Unset):
            field_feed_id = UNSET
        else:
            field_feed_id = self.field_feed_id

        error_id = self.error_id

        error_text = self.error_text

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "_notificationId": field_notification_id,
                "_subscriberId": field_subscriber_id,
                "createdAt": created_at,
                "transactionId": transaction_id,
                "channel": channel,
                "read": read,
                "seen": seen,
                "cta": cta,
                "status": status,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if field_template_id is not UNSET:
            field_dict["_templateId"] = field_template_id
        if field_message_template_id is not UNSET:
            field_dict["_messageTemplateId"] = field_message_template_id
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber
        if template is not UNSET:
            field_dict["template"] = template
        if template_identifier is not UNSET:
            field_dict["templateIdentifier"] = template_identifier
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if last_seen_date is not UNSET:
            field_dict["lastSeenDate"] = last_seen_date
        if last_read_date is not UNSET:
            field_dict["lastReadDate"] = last_read_date
        if content is not UNSET:
            field_dict["content"] = content
        if subject is not UNSET:
            field_dict["subject"] = subject
        if snoozed_until is not UNSET:
            field_dict["snoozedUntil"] = snoozed_until
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if direct_webhook_url is not UNSET:
            field_dict["directWebhookUrl"] = direct_webhook_url
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if device_tokens is not UNSET:
            field_dict["deviceTokens"] = device_tokens
        if title is not UNSET:
            field_dict["title"] = title
        if field_feed_id is not UNSET:
            field_dict["_feedId"] = field_feed_id
        if error_id is not UNSET:
            field_dict["errorId"] = error_id
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if payload is not UNSET:
            field_dict["payload"] = payload
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_block import EmailBlock
        from ..models.message_cta import MessageCTA
        from ..models.message_response_dto_overrides import MessageResponseDtoOverrides
        from ..models.message_response_dto_payload import MessageResponseDtoPayload
        from ..models.subscriber_response_dto import SubscriberResponseDto
        from ..models.workflow_response import WorkflowResponse

        d = dict(src_dict)
        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        field_notification_id = d.pop("_notificationId")

        field_subscriber_id = d.pop("_subscriberId")

        created_at = d.pop("createdAt")

        transaction_id = d.pop("transactionId")

        channel = ChannelTypeEnum(d.pop("channel"))

        read = d.pop("read")

        seen = d.pop("seen")

        cta = MessageCTA.from_dict(d.pop("cta"))

        status = MessageStatusEnum(d.pop("status"))

        field_id = d.pop("_id", UNSET)

        def _parse_field_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_template_id = _parse_field_template_id(d.pop("_templateId", UNSET))

        def _parse_field_message_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_message_template_id = _parse_field_message_template_id(d.pop("_messageTemplateId", UNSET))

        _subscriber = d.pop("subscriber", UNSET)
        subscriber: SubscriberResponseDto | Unset
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = SubscriberResponseDto.from_dict(_subscriber)

        _template = d.pop("template", UNSET)
        template: WorkflowResponse | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = WorkflowResponse.from_dict(_template)

        template_identifier = d.pop("templateIdentifier", UNSET)

        delivered_at = cast(list[str], d.pop("deliveredAt", UNSET))

        last_seen_date = d.pop("lastSeenDate", UNSET)

        last_read_date = d.pop("lastReadDate", UNSET)

        def _parse_content(data: object) -> list[EmailBlock] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_0 = []
                _content_type_0 = data
                for content_type_0_item_data in _content_type_0:
                    content_type_0_item = EmailBlock.from_dict(content_type_0_item_data)

                    content_type_0.append(content_type_0_item)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmailBlock] | None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        subject = d.pop("subject", UNSET)

        snoozed_until = d.pop("snoozedUntil", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        direct_webhook_url = d.pop("directWebhookUrl", UNSET)

        provider_id = d.pop("providerId", UNSET)

        device_tokens = cast(list[str], d.pop("deviceTokens", UNSET))

        title = d.pop("title", UNSET)

        def _parse_field_feed_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_feed_id = _parse_field_feed_id(d.pop("_feedId", UNSET))

        error_id = d.pop("errorId", UNSET)

        error_text = d.pop("errorText", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: MessageResponseDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = MessageResponseDtoPayload.from_dict(_payload)

        _overrides = d.pop("overrides", UNSET)
        overrides: MessageResponseDtoOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = MessageResponseDtoOverrides.from_dict(_overrides)

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        message_response_dto = cls(
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            field_notification_id=field_notification_id,
            field_subscriber_id=field_subscriber_id,
            created_at=created_at,
            transaction_id=transaction_id,
            channel=channel,
            read=read,
            seen=seen,
            cta=cta,
            status=status,
            field_id=field_id,
            field_template_id=field_template_id,
            field_message_template_id=field_message_template_id,
            subscriber=subscriber,
            template=template,
            template_identifier=template_identifier,
            delivered_at=delivered_at,
            last_seen_date=last_seen_date,
            last_read_date=last_read_date,
            content=content,
            subject=subject,
            snoozed_until=snoozed_until,
            email=email,
            phone=phone,
            direct_webhook_url=direct_webhook_url,
            provider_id=provider_id,
            device_tokens=device_tokens,
            title=title,
            field_feed_id=field_feed_id,
            error_id=error_id,
            error_text=error_text,
            payload=payload,
            overrides=overrides,
            context_keys=context_keys,
        )

        message_response_dto.additional_properties = d
        return message_response_dto

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
