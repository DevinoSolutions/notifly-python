from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..models.severity_level_enum import SeverityLevelEnum
from ..models.workflow_status_enum import WorkflowStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_step_response_dto import ChatStepResponseDto
    from ..models.custom_step_response_dto import CustomStepResponseDto
    from ..models.delay_step_response_dto import DelayStepResponseDto
    from ..models.digest_step_response_dto import DigestStepResponseDto
    from ..models.email_step_response_dto import EmailStepResponseDto
    from ..models.http_request_step_response_dto import HttpRequestStepResponseDto
    from ..models.in_app_step_response_dto import InAppStepResponseDto
    from ..models.push_step_response_dto import PushStepResponseDto
    from ..models.sms_step_response_dto import SmsStepResponseDto
    from ..models.throttle_step_response_dto import ThrottleStepResponseDto
    from ..models.user_response_dto import UserResponseDto
    from ..models.workflow_preferences_response_dto import WorkflowPreferencesResponseDto
    from ..models.workflow_response_dto_issues import WorkflowResponseDtoIssues
    from ..models.workflow_response_dto_payload_example_type_0 import WorkflowResponseDtoPayloadExampleType0
    from ..models.workflow_response_dto_payload_schema_type_0 import WorkflowResponseDtoPayloadSchemaType0


T = TypeVar("T", bound="WorkflowResponseDto")


@_attrs_define
class WorkflowResponseDto:
    """
    Attributes:
        name (str): Name of the workflow
        field_id (str): Database identifier of the workflow
        workflow_id (str): Workflow identifier
        slug (str): Slug of the workflow
        updated_at (str): Last updated timestamp
        created_at (str): Creation timestamp
        steps (list[ChatStepResponseDto | CustomStepResponseDto | DelayStepResponseDto | DigestStepResponseDto |
            EmailStepResponseDto | HttpRequestStepResponseDto | InAppStepResponseDto | PushStepResponseDto |
            SmsStepResponseDto | ThrottleStepResponseDto]): Steps of the workflow
        origin (ResourceOriginEnum): Origin of the layout
        preferences (WorkflowPreferencesResponseDto):
        status (WorkflowStatusEnum): Status of the workflow
        severity (SeverityLevelEnum): Severity of the workflow
        description (str | Unset): Description of the workflow
        tags (list[str] | Unset): Tags associated with the workflow
        active (bool | Unset): Whether the workflow is active Default: False.
        validate_payload (bool | Unset): Enable or disable payload schema validation
        payload_schema (None | Unset | WorkflowResponseDtoPayloadSchemaType0): The payload JSON Schema for the workflow
        is_translation_enabled (bool | Unset): Enable or disable translations for this workflow Default: False.
        updated_by (None | Unset | UserResponseDto): User who last updated the workflow
        last_published_at (None | str | Unset): Timestamp of the last workflow publication
        last_published_by (None | Unset | UserResponseDto): User who last published the workflow
        issues (WorkflowResponseDtoIssues | Unset): Runtime issues for workflow creation and update
        last_triggered_at (None | str | Unset): Timestamp of the last workflow trigger
        payload_example (None | Unset | WorkflowResponseDtoPayloadExampleType0): Generated payload example based on the
            payload schema
    """

    name: str
    field_id: str
    workflow_id: str
    slug: str
    updated_at: str
    created_at: str
    steps: list[
        ChatStepResponseDto
        | CustomStepResponseDto
        | DelayStepResponseDto
        | DigestStepResponseDto
        | EmailStepResponseDto
        | HttpRequestStepResponseDto
        | InAppStepResponseDto
        | PushStepResponseDto
        | SmsStepResponseDto
        | ThrottleStepResponseDto
    ]
    origin: ResourceOriginEnum
    preferences: WorkflowPreferencesResponseDto
    status: WorkflowStatusEnum
    severity: SeverityLevelEnum
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    active: bool | Unset = False
    validate_payload: bool | Unset = UNSET
    payload_schema: None | Unset | WorkflowResponseDtoPayloadSchemaType0 = UNSET
    is_translation_enabled: bool | Unset = False
    updated_by: None | Unset | UserResponseDto = UNSET
    last_published_at: None | str | Unset = UNSET
    last_published_by: None | Unset | UserResponseDto = UNSET
    issues: WorkflowResponseDtoIssues | Unset = UNSET
    last_triggered_at: None | str | Unset = UNSET
    payload_example: None | Unset | WorkflowResponseDtoPayloadExampleType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_step_response_dto import ChatStepResponseDto
        from ..models.custom_step_response_dto import CustomStepResponseDto
        from ..models.delay_step_response_dto import DelayStepResponseDto
        from ..models.digest_step_response_dto import DigestStepResponseDto
        from ..models.email_step_response_dto import EmailStepResponseDto
        from ..models.in_app_step_response_dto import InAppStepResponseDto
        from ..models.push_step_response_dto import PushStepResponseDto
        from ..models.sms_step_response_dto import SmsStepResponseDto
        from ..models.throttle_step_response_dto import ThrottleStepResponseDto
        from ..models.user_response_dto import UserResponseDto
        from ..models.workflow_response_dto_payload_example_type_0 import WorkflowResponseDtoPayloadExampleType0
        from ..models.workflow_response_dto_payload_schema_type_0 import WorkflowResponseDtoPayloadSchemaType0

        name = self.name

        field_id = self.field_id

        workflow_id = self.workflow_id

        slug = self.slug

        updated_at = self.updated_at

        created_at = self.created_at

        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, InAppStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, EmailStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, SmsStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, PushStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ChatStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, DelayStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, DigestStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, CustomStepResponseDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ThrottleStepResponseDto):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        origin = self.origin.value

        preferences = self.preferences.to_dict()

        status = self.status.value

        severity = self.severity.value

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        active = self.active

        validate_payload = self.validate_payload

        payload_schema: dict[str, Any] | None | Unset
        if isinstance(self.payload_schema, Unset):
            payload_schema = UNSET
        elif isinstance(self.payload_schema, WorkflowResponseDtoPayloadSchemaType0):
            payload_schema = self.payload_schema.to_dict()
        else:
            payload_schema = self.payload_schema

        is_translation_enabled = self.is_translation_enabled

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UserResponseDto):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        last_published_at: None | str | Unset
        if isinstance(self.last_published_at, Unset):
            last_published_at = UNSET
        else:
            last_published_at = self.last_published_at

        last_published_by: dict[str, Any] | None | Unset
        if isinstance(self.last_published_by, Unset):
            last_published_by = UNSET
        elif isinstance(self.last_published_by, UserResponseDto):
            last_published_by = self.last_published_by.to_dict()
        else:
            last_published_by = self.last_published_by

        issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()

        last_triggered_at: None | str | Unset
        if isinstance(self.last_triggered_at, Unset):
            last_triggered_at = UNSET
        else:
            last_triggered_at = self.last_triggered_at

        payload_example: dict[str, Any] | None | Unset
        if isinstance(self.payload_example, Unset):
            payload_example = UNSET
        elif isinstance(self.payload_example, WorkflowResponseDtoPayloadExampleType0):
            payload_example = self.payload_example.to_dict()
        else:
            payload_example = self.payload_example

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "_id": field_id,
                "workflowId": workflow_id,
                "slug": slug,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "steps": steps,
                "origin": origin,
                "preferences": preferences,
                "status": status,
                "severity": severity,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if active is not UNSET:
            field_dict["active"] = active
        if validate_payload is not UNSET:
            field_dict["validatePayload"] = validate_payload
        if payload_schema is not UNSET:
            field_dict["payloadSchema"] = payload_schema
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if last_published_at is not UNSET:
            field_dict["lastPublishedAt"] = last_published_at
        if last_published_by is not UNSET:
            field_dict["lastPublishedBy"] = last_published_by
        if issues is not UNSET:
            field_dict["issues"] = issues
        if last_triggered_at is not UNSET:
            field_dict["lastTriggeredAt"] = last_triggered_at
        if payload_example is not UNSET:
            field_dict["payloadExample"] = payload_example

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_step_response_dto import ChatStepResponseDto
        from ..models.custom_step_response_dto import CustomStepResponseDto
        from ..models.delay_step_response_dto import DelayStepResponseDto
        from ..models.digest_step_response_dto import DigestStepResponseDto
        from ..models.email_step_response_dto import EmailStepResponseDto
        from ..models.http_request_step_response_dto import HttpRequestStepResponseDto
        from ..models.in_app_step_response_dto import InAppStepResponseDto
        from ..models.push_step_response_dto import PushStepResponseDto
        from ..models.sms_step_response_dto import SmsStepResponseDto
        from ..models.throttle_step_response_dto import ThrottleStepResponseDto
        from ..models.user_response_dto import UserResponseDto
        from ..models.workflow_preferences_response_dto import WorkflowPreferencesResponseDto
        from ..models.workflow_response_dto_issues import WorkflowResponseDtoIssues
        from ..models.workflow_response_dto_payload_example_type_0 import WorkflowResponseDtoPayloadExampleType0
        from ..models.workflow_response_dto_payload_schema_type_0 import WorkflowResponseDtoPayloadSchemaType0

        d = dict(src_dict)
        name = d.pop("name")

        field_id = d.pop("_id")

        workflow_id = d.pop("workflowId")

        slug = d.pop("slug")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:

            def _parse_steps_item(
                data: object,
            ) -> (
                ChatStepResponseDto
                | CustomStepResponseDto
                | DelayStepResponseDto
                | DigestStepResponseDto
                | EmailStepResponseDto
                | HttpRequestStepResponseDto
                | InAppStepResponseDto
                | PushStepResponseDto
                | SmsStepResponseDto
                | ThrottleStepResponseDto
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_0 = InAppStepResponseDto.from_dict(data)

                    return steps_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_1 = EmailStepResponseDto.from_dict(data)

                    return steps_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_2 = SmsStepResponseDto.from_dict(data)

                    return steps_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_3 = PushStepResponseDto.from_dict(data)

                    return steps_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_4 = ChatStepResponseDto.from_dict(data)

                    return steps_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_5 = DelayStepResponseDto.from_dict(data)

                    return steps_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_6 = DigestStepResponseDto.from_dict(data)

                    return steps_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_7 = CustomStepResponseDto.from_dict(data)

                    return steps_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_8 = ThrottleStepResponseDto.from_dict(data)

                    return steps_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                steps_item_type_9 = HttpRequestStepResponseDto.from_dict(data)

                return steps_item_type_9

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        origin = ResourceOriginEnum(d.pop("origin"))

        preferences = WorkflowPreferencesResponseDto.from_dict(d.pop("preferences"))

        status = WorkflowStatusEnum(d.pop("status"))

        severity = SeverityLevelEnum(d.pop("severity"))

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        active = d.pop("active", UNSET)

        validate_payload = d.pop("validatePayload", UNSET)

        def _parse_payload_schema(data: object) -> None | Unset | WorkflowResponseDtoPayloadSchemaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_schema_type_0 = WorkflowResponseDtoPayloadSchemaType0.from_dict(data)

                return payload_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowResponseDtoPayloadSchemaType0, data)

        payload_schema = _parse_payload_schema(d.pop("payloadSchema", UNSET))

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        def _parse_updated_by(data: object) -> None | Unset | UserResponseDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_1 = UserResponseDto.from_dict(data)

                return updated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserResponseDto, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))

        def _parse_last_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_published_at = _parse_last_published_at(d.pop("lastPublishedAt", UNSET))

        def _parse_last_published_by(data: object) -> None | Unset | UserResponseDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_published_by_type_1 = UserResponseDto.from_dict(data)

                return last_published_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserResponseDto, data)

        last_published_by = _parse_last_published_by(d.pop("lastPublishedBy", UNSET))

        _issues = d.pop("issues", UNSET)
        issues: WorkflowResponseDtoIssues | Unset
        if isinstance(_issues, Unset):
            issues = UNSET
        else:
            issues = WorkflowResponseDtoIssues.from_dict(_issues)

        def _parse_last_triggered_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("lastTriggeredAt", UNSET))

        def _parse_payload_example(data: object) -> None | Unset | WorkflowResponseDtoPayloadExampleType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_example_type_0 = WorkflowResponseDtoPayloadExampleType0.from_dict(data)

                return payload_example_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowResponseDtoPayloadExampleType0, data)

        payload_example = _parse_payload_example(d.pop("payloadExample", UNSET))

        workflow_response_dto = cls(
            name=name,
            field_id=field_id,
            workflow_id=workflow_id,
            slug=slug,
            updated_at=updated_at,
            created_at=created_at,
            steps=steps,
            origin=origin,
            preferences=preferences,
            status=status,
            severity=severity,
            description=description,
            tags=tags,
            active=active,
            validate_payload=validate_payload,
            payload_schema=payload_schema,
            is_translation_enabled=is_translation_enabled,
            updated_by=updated_by,
            last_published_at=last_published_at,
            last_published_by=last_published_by,
            issues=issues,
            last_triggered_at=last_triggered_at,
            payload_example=payload_example,
        )

        workflow_response_dto.additional_properties = d
        return workflow_response_dto

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
