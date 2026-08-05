from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_level_enum import SeverityLevelEnum
from ..models.step_type_enum import StepTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_notification_job_response_dto import ActivityNotificationJobResponseDto
    from ..models.activity_notification_response_dto_controls import ActivityNotificationResponseDtoControls
    from ..models.activity_notification_response_dto_payload import ActivityNotificationResponseDtoPayload
    from ..models.activity_notification_response_dto_to import ActivityNotificationResponseDtoTo
    from ..models.activity_notification_subscriber_response_dto import ActivityNotificationSubscriberResponseDto
    from ..models.activity_notification_template_response_dto import ActivityNotificationTemplateResponseDto
    from ..models.activity_topic_dto import ActivityTopicDto


T = TypeVar("T", bound="ActivityNotificationResponseDto")


@_attrs_define
class ActivityNotificationResponseDto:
    """
    Attributes:
        field_environment_id (str): Environment ID of the notification
        field_organization_id (str): Organization ID of the notification
        field_subscriber_id (str): Subscriber ID of the notification
        transaction_id (str): Transaction ID of the notification
        field_id (str | Unset): Unique identifier of the notification
        field_template_id (str | Unset): Template ID of the notification
        field_digested_notification_id (str | Unset): Digested Notification ID
        created_at (str | Unset): Creation time of the notification
        updated_at (str | Unset): Last updated time of the notification
        channels (list[StepTypeEnum] | Unset):
        subscriber (ActivityNotificationSubscriberResponseDto | Unset):
        template (ActivityNotificationTemplateResponseDto | Unset):
        jobs (list[ActivityNotificationJobResponseDto] | Unset): Jobs of the notification
        payload (ActivityNotificationResponseDtoPayload | Unset): Payload of the notification
        tags (list[str] | Unset): Tags associated with the notification
        controls (ActivityNotificationResponseDtoControls | Unset): Controls associated with the notification
        to (ActivityNotificationResponseDtoTo | Unset): To field for subscriber definition
        topics (list[ActivityTopicDto] | Unset): Topics of the notification
        severity (SeverityLevelEnum | Unset): Severity of the workflow
        critical (bool | Unset): Criticality of the notification
        context_keys (list[str] | Unset): Context (single or multi) in which the notification was sent
    """

    field_environment_id: str
    field_organization_id: str
    field_subscriber_id: str
    transaction_id: str
    field_id: str | Unset = UNSET
    field_template_id: str | Unset = UNSET
    field_digested_notification_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    channels: list[StepTypeEnum] | Unset = UNSET
    subscriber: ActivityNotificationSubscriberResponseDto | Unset = UNSET
    template: ActivityNotificationTemplateResponseDto | Unset = UNSET
    jobs: list[ActivityNotificationJobResponseDto] | Unset = UNSET
    payload: ActivityNotificationResponseDtoPayload | Unset = UNSET
    tags: list[str] | Unset = UNSET
    controls: ActivityNotificationResponseDtoControls | Unset = UNSET
    to: ActivityNotificationResponseDtoTo | Unset = UNSET
    topics: list[ActivityTopicDto] | Unset = UNSET
    severity: SeverityLevelEnum | Unset = UNSET
    critical: bool | Unset = UNSET
    context_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        field_subscriber_id = self.field_subscriber_id

        transaction_id = self.transaction_id

        field_id = self.field_id

        field_template_id = self.field_template_id

        field_digested_notification_id = self.field_digested_notification_id

        created_at = self.created_at

        updated_at = self.updated_at

        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.value
                channels.append(channels_item)

        subscriber: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        controls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.controls, Unset):
            controls = self.controls.to_dict()

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        critical = self.critical

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "_subscriberId": field_subscriber_id,
                "transactionId": transaction_id,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if field_template_id is not UNSET:
            field_dict["_templateId"] = field_template_id
        if field_digested_notification_id is not UNSET:
            field_dict["_digestedNotificationId"] = field_digested_notification_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if channels is not UNSET:
            field_dict["channels"] = channels
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber
        if template is not UNSET:
            field_dict["template"] = template
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if payload is not UNSET:
            field_dict["payload"] = payload
        if tags is not UNSET:
            field_dict["tags"] = tags
        if controls is not UNSET:
            field_dict["controls"] = controls
        if to is not UNSET:
            field_dict["to"] = to
        if topics is not UNSET:
            field_dict["topics"] = topics
        if severity is not UNSET:
            field_dict["severity"] = severity
        if critical is not UNSET:
            field_dict["critical"] = critical
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_notification_job_response_dto import ActivityNotificationJobResponseDto
        from ..models.activity_notification_response_dto_controls import ActivityNotificationResponseDtoControls
        from ..models.activity_notification_response_dto_payload import ActivityNotificationResponseDtoPayload
        from ..models.activity_notification_response_dto_to import ActivityNotificationResponseDtoTo
        from ..models.activity_notification_subscriber_response_dto import ActivityNotificationSubscriberResponseDto
        from ..models.activity_notification_template_response_dto import ActivityNotificationTemplateResponseDto
        from ..models.activity_topic_dto import ActivityTopicDto

        d = dict(src_dict)
        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        field_subscriber_id = d.pop("_subscriberId")

        transaction_id = d.pop("transactionId")

        field_id = d.pop("_id", UNSET)

        field_template_id = d.pop("_templateId", UNSET)

        field_digested_notification_id = d.pop("_digestedNotificationId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        _channels = d.pop("channels", UNSET)
        channels: list[StepTypeEnum] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = StepTypeEnum(channels_item_data)

                channels.append(channels_item)

        _subscriber = d.pop("subscriber", UNSET)
        subscriber: ActivityNotificationSubscriberResponseDto | Unset
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = ActivityNotificationSubscriberResponseDto.from_dict(_subscriber)

        _template = d.pop("template", UNSET)
        template: ActivityNotificationTemplateResponseDto | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = ActivityNotificationTemplateResponseDto.from_dict(_template)

        _jobs = d.pop("jobs", UNSET)
        jobs: list[ActivityNotificationJobResponseDto] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = ActivityNotificationJobResponseDto.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        _payload = d.pop("payload", UNSET)
        payload: ActivityNotificationResponseDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ActivityNotificationResponseDtoPayload.from_dict(_payload)

        tags = cast(list[str], d.pop("tags", UNSET))

        _controls = d.pop("controls", UNSET)
        controls: ActivityNotificationResponseDtoControls | Unset
        if isinstance(_controls, Unset):
            controls = UNSET
        else:
            controls = ActivityNotificationResponseDtoControls.from_dict(_controls)

        _to = d.pop("to", UNSET)
        to: ActivityNotificationResponseDtoTo | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ActivityNotificationResponseDtoTo.from_dict(_to)

        _topics = d.pop("topics", UNSET)
        topics: list[ActivityTopicDto] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = ActivityTopicDto.from_dict(topics_item_data)

                topics.append(topics_item)

        _severity = d.pop("severity", UNSET)
        severity: SeverityLevelEnum | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityLevelEnum(_severity)

        critical = d.pop("critical", UNSET)

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        activity_notification_response_dto = cls(
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            field_subscriber_id=field_subscriber_id,
            transaction_id=transaction_id,
            field_id=field_id,
            field_template_id=field_template_id,
            field_digested_notification_id=field_digested_notification_id,
            created_at=created_at,
            updated_at=updated_at,
            channels=channels,
            subscriber=subscriber,
            template=template,
            jobs=jobs,
            payload=payload,
            tags=tags,
            controls=controls,
            to=to,
            topics=topics,
            severity=severity,
            critical=critical,
            context_keys=context_keys,
        )

        activity_notification_response_dto.additional_properties = d
        return activity_notification_response_dto

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
