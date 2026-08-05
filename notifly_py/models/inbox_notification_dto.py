from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..models.severity_level_enum import SeverityLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbox_action_dto import InboxActionDto
    from ..models.inbox_notification_dto_data import InboxNotificationDtoData
    from ..models.inbox_subscriber_response_dto import InboxSubscriberResponseDto
    from ..models.notification_workflow_dto import NotificationWorkflowDto
    from ..models.redirect_dto import RedirectDto


T = TypeVar("T", bound="InboxNotificationDto")


@_attrs_define
class InboxNotificationDto:
    """
    Attributes:
        id (str): Unique identifier of the notification
        transaction_id (str): Transaction identifier of the notification
        body (str): Body content of the notification
        to (InboxSubscriberResponseDto):
        is_read (bool): Whether the notification has been read
        is_seen (bool): Whether the notification has been seen
        is_archived (bool): Whether the notification has been archived
        is_snoozed (bool): Whether the notification is snoozed
        created_at (str): ISO timestamp when the notification was created
        channel_type (ChannelTypeEnum): Channel type through which the message is sent
        severity (SeverityLevelEnum): Severity of the workflow
        subject (str | Unset): Subject of the notification
        snoozed_until (None | str | Unset): ISO timestamp when the notification will be unsnoozed
        delivered_at (list[str] | Unset): Timestamps when the notification was delivered
        read_at (None | str | Unset): ISO timestamp when the notification was read
        first_seen_at (None | str | Unset): ISO timestamp when the notification was first seen
        archived_at (None | str | Unset): ISO timestamp when the notification was archived
        avatar (str | Unset): Avatar URL for the notification
        primary_action (InboxActionDto | Unset):
        secondary_action (InboxActionDto | Unset):
        tags (list[str] | Unset): Tags associated with the notification
        data (InboxNotificationDtoData | Unset): Custom data payload of the notification
        redirect (RedirectDto | Unset):
        workflow (NotificationWorkflowDto | Unset):
    """

    id: str
    transaction_id: str
    body: str
    to: InboxSubscriberResponseDto
    is_read: bool
    is_seen: bool
    is_archived: bool
    is_snoozed: bool
    created_at: str
    channel_type: ChannelTypeEnum
    severity: SeverityLevelEnum
    subject: str | Unset = UNSET
    snoozed_until: None | str | Unset = UNSET
    delivered_at: list[str] | Unset = UNSET
    read_at: None | str | Unset = UNSET
    first_seen_at: None | str | Unset = UNSET
    archived_at: None | str | Unset = UNSET
    avatar: str | Unset = UNSET
    primary_action: InboxActionDto | Unset = UNSET
    secondary_action: InboxActionDto | Unset = UNSET
    tags: list[str] | Unset = UNSET
    data: InboxNotificationDtoData | Unset = UNSET
    redirect: RedirectDto | Unset = UNSET
    workflow: NotificationWorkflowDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        transaction_id = self.transaction_id

        body = self.body

        to = self.to.to_dict()

        is_read = self.is_read

        is_seen = self.is_seen

        is_archived = self.is_archived

        is_snoozed = self.is_snoozed

        created_at = self.created_at

        channel_type = self.channel_type.value

        severity = self.severity.value

        subject = self.subject

        snoozed_until: None | str | Unset
        if isinstance(self.snoozed_until, Unset):
            snoozed_until = UNSET
        else:
            snoozed_until = self.snoozed_until

        delivered_at: list[str] | Unset = UNSET
        if not isinstance(self.delivered_at, Unset):
            delivered_at = self.delivered_at

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        else:
            read_at = self.read_at

        first_seen_at: None | str | Unset
        if isinstance(self.first_seen_at, Unset):
            first_seen_at = UNSET
        else:
            first_seen_at = self.first_seen_at

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = self.archived_at

        avatar = self.avatar

        primary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_action, Unset):
            primary_action = self.primary_action.to_dict()

        secondary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secondary_action, Unset):
            secondary_action = self.secondary_action.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        redirect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "transactionId": transaction_id,
                "body": body,
                "to": to,
                "isRead": is_read,
                "isSeen": is_seen,
                "isArchived": is_archived,
                "isSnoozed": is_snoozed,
                "createdAt": created_at,
                "channelType": channel_type,
                "severity": severity,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if snoozed_until is not UNSET:
            field_dict["snoozedUntil"] = snoozed_until
        if delivered_at is not UNSET:
            field_dict["deliveredAt"] = delivered_at
        if read_at is not UNSET:
            field_dict["readAt"] = read_at
        if first_seen_at is not UNSET:
            field_dict["firstSeenAt"] = first_seen_at
        if archived_at is not UNSET:
            field_dict["archivedAt"] = archived_at
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if primary_action is not UNSET:
            field_dict["primaryAction"] = primary_action
        if secondary_action is not UNSET:
            field_dict["secondaryAction"] = secondary_action
        if tags is not UNSET:
            field_dict["tags"] = tags
        if data is not UNSET:
            field_dict["data"] = data
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_action_dto import InboxActionDto
        from ..models.inbox_notification_dto_data import InboxNotificationDtoData
        from ..models.inbox_subscriber_response_dto import InboxSubscriberResponseDto
        from ..models.notification_workflow_dto import NotificationWorkflowDto
        from ..models.redirect_dto import RedirectDto

        d = dict(src_dict)
        id = d.pop("id")

        transaction_id = d.pop("transactionId")

        body = d.pop("body")

        to = InboxSubscriberResponseDto.from_dict(d.pop("to"))

        is_read = d.pop("isRead")

        is_seen = d.pop("isSeen")

        is_archived = d.pop("isArchived")

        is_snoozed = d.pop("isSnoozed")

        created_at = d.pop("createdAt")

        channel_type = ChannelTypeEnum(d.pop("channelType"))

        severity = SeverityLevelEnum(d.pop("severity"))

        subject = d.pop("subject", UNSET)

        def _parse_snoozed_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozedUntil", UNSET))

        delivered_at = cast(list[str], d.pop("deliveredAt", UNSET))

        def _parse_read_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_at = _parse_read_at(d.pop("readAt", UNSET))

        def _parse_first_seen_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_seen_at = _parse_first_seen_at(d.pop("firstSeenAt", UNSET))

        def _parse_archived_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archived_at = _parse_archived_at(d.pop("archivedAt", UNSET))

        avatar = d.pop("avatar", UNSET)

        _primary_action = d.pop("primaryAction", UNSET)
        primary_action: InboxActionDto | Unset
        if isinstance(_primary_action, Unset):
            primary_action = UNSET
        else:
            primary_action = InboxActionDto.from_dict(_primary_action)

        _secondary_action = d.pop("secondaryAction", UNSET)
        secondary_action: InboxActionDto | Unset
        if isinstance(_secondary_action, Unset):
            secondary_action = UNSET
        else:
            secondary_action = InboxActionDto.from_dict(_secondary_action)

        tags = cast(list[str], d.pop("tags", UNSET))

        _data = d.pop("data", UNSET)
        data: InboxNotificationDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InboxNotificationDtoData.from_dict(_data)

        _redirect = d.pop("redirect", UNSET)
        redirect: RedirectDto | Unset
        if isinstance(_redirect, Unset):
            redirect = UNSET
        else:
            redirect = RedirectDto.from_dict(_redirect)

        _workflow = d.pop("workflow", UNSET)
        workflow: NotificationWorkflowDto | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = NotificationWorkflowDto.from_dict(_workflow)

        inbox_notification_dto = cls(
            id=id,
            transaction_id=transaction_id,
            body=body,
            to=to,
            is_read=is_read,
            is_seen=is_seen,
            is_archived=is_archived,
            is_snoozed=is_snoozed,
            created_at=created_at,
            channel_type=channel_type,
            severity=severity,
            subject=subject,
            snoozed_until=snoozed_until,
            delivered_at=delivered_at,
            read_at=read_at,
            first_seen_at=first_seen_at,
            archived_at=archived_at,
            avatar=avatar,
            primary_action=primary_action,
            secondary_action=secondary_action,
            tags=tags,
            data=data,
            redirect=redirect,
            workflow=workflow,
        )

        inbox_notification_dto.additional_properties = d
        return inbox_notification_dto

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
