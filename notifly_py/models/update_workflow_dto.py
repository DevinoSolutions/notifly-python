from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..models.severity_level_enum import SeverityLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_step_upsert_dto import ChatStepUpsertDto
    from ..models.custom_step_upsert_dto import CustomStepUpsertDto
    from ..models.delay_step_upsert_dto import DelayStepUpsertDto
    from ..models.digest_step_upsert_dto import DigestStepUpsertDto
    from ..models.email_step_upsert_dto import EmailStepUpsertDto
    from ..models.http_request_step_upsert_dto import HttpRequestStepUpsertDto
    from ..models.in_app_step_upsert_dto import InAppStepUpsertDto
    from ..models.preferences_request_dto import PreferencesRequestDto
    from ..models.push_step_upsert_dto import PushStepUpsertDto
    from ..models.sms_step_upsert_dto import SmsStepUpsertDto
    from ..models.throttle_step_upsert_dto import ThrottleStepUpsertDto
    from ..models.update_workflow_dto_payload_schema_type_0 import UpdateWorkflowDtoPayloadSchemaType0


T = TypeVar("T", bound="UpdateWorkflowDto")


@_attrs_define
class UpdateWorkflowDto:
    """
    Attributes:
        name (str): Name of the workflow
        steps (list[ChatStepUpsertDto | CustomStepUpsertDto | DelayStepUpsertDto | DigestStepUpsertDto |
            EmailStepUpsertDto | HttpRequestStepUpsertDto | InAppStepUpsertDto | PushStepUpsertDto | SmsStepUpsertDto |
            ThrottleStepUpsertDto]): Steps of the workflow
        preferences (PreferencesRequestDto):
        origin (ResourceOriginEnum): Origin of the layout
        description (str | Unset): Description of the workflow
        tags (list[str] | Unset): Tags associated with the workflow
        active (bool | Unset): Whether the workflow is active Default: False.
        validate_payload (bool | Unset): Enable or disable payload schema validation
        payload_schema (None | Unset | UpdateWorkflowDtoPayloadSchemaType0): The payload JSON Schema for the workflow
        is_translation_enabled (bool | Unset): Enable or disable translations for this workflow Default: False.
        workflow_id (str | Unset): Workflow ID (allowed only for code-first workflows)
        severity (SeverityLevelEnum | Unset): Severity of the workflow
    """

    name: str
    steps: list[
        ChatStepUpsertDto
        | CustomStepUpsertDto
        | DelayStepUpsertDto
        | DigestStepUpsertDto
        | EmailStepUpsertDto
        | HttpRequestStepUpsertDto
        | InAppStepUpsertDto
        | PushStepUpsertDto
        | SmsStepUpsertDto
        | ThrottleStepUpsertDto
    ]
    preferences: PreferencesRequestDto
    origin: ResourceOriginEnum
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    active: bool | Unset = False
    validate_payload: bool | Unset = UNSET
    payload_schema: None | Unset | UpdateWorkflowDtoPayloadSchemaType0 = UNSET
    is_translation_enabled: bool | Unset = False
    workflow_id: str | Unset = UNSET
    severity: SeverityLevelEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_step_upsert_dto import ChatStepUpsertDto
        from ..models.custom_step_upsert_dto import CustomStepUpsertDto
        from ..models.delay_step_upsert_dto import DelayStepUpsertDto
        from ..models.digest_step_upsert_dto import DigestStepUpsertDto
        from ..models.email_step_upsert_dto import EmailStepUpsertDto
        from ..models.in_app_step_upsert_dto import InAppStepUpsertDto
        from ..models.push_step_upsert_dto import PushStepUpsertDto
        from ..models.sms_step_upsert_dto import SmsStepUpsertDto
        from ..models.throttle_step_upsert_dto import ThrottleStepUpsertDto
        from ..models.update_workflow_dto_payload_schema_type_0 import UpdateWorkflowDtoPayloadSchemaType0

        name = self.name

        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, InAppStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, EmailStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, SmsStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, PushStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ChatStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, DelayStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, DigestStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ThrottleStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, CustomStepUpsertDto):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        preferences = self.preferences.to_dict()

        origin = self.origin.value

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        active = self.active

        validate_payload = self.validate_payload

        payload_schema: dict[str, Any] | None | Unset
        if isinstance(self.payload_schema, Unset):
            payload_schema = UNSET
        elif isinstance(self.payload_schema, UpdateWorkflowDtoPayloadSchemaType0):
            payload_schema = self.payload_schema.to_dict()
        else:
            payload_schema = self.payload_schema

        is_translation_enabled = self.is_translation_enabled

        workflow_id = self.workflow_id

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "steps": steps,
                "preferences": preferences,
                "origin": origin,
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
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_step_upsert_dto import ChatStepUpsertDto
        from ..models.custom_step_upsert_dto import CustomStepUpsertDto
        from ..models.delay_step_upsert_dto import DelayStepUpsertDto
        from ..models.digest_step_upsert_dto import DigestStepUpsertDto
        from ..models.email_step_upsert_dto import EmailStepUpsertDto
        from ..models.http_request_step_upsert_dto import HttpRequestStepUpsertDto
        from ..models.in_app_step_upsert_dto import InAppStepUpsertDto
        from ..models.preferences_request_dto import PreferencesRequestDto
        from ..models.push_step_upsert_dto import PushStepUpsertDto
        from ..models.sms_step_upsert_dto import SmsStepUpsertDto
        from ..models.throttle_step_upsert_dto import ThrottleStepUpsertDto
        from ..models.update_workflow_dto_payload_schema_type_0 import UpdateWorkflowDtoPayloadSchemaType0

        d = dict(src_dict)
        name = d.pop("name")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:

            def _parse_steps_item(
                data: object,
            ) -> (
                ChatStepUpsertDto
                | CustomStepUpsertDto
                | DelayStepUpsertDto
                | DigestStepUpsertDto
                | EmailStepUpsertDto
                | HttpRequestStepUpsertDto
                | InAppStepUpsertDto
                | PushStepUpsertDto
                | SmsStepUpsertDto
                | ThrottleStepUpsertDto
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_0 = InAppStepUpsertDto.from_dict(data)

                    return steps_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_1 = EmailStepUpsertDto.from_dict(data)

                    return steps_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_2 = SmsStepUpsertDto.from_dict(data)

                    return steps_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_3 = PushStepUpsertDto.from_dict(data)

                    return steps_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_4 = ChatStepUpsertDto.from_dict(data)

                    return steps_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_5 = DelayStepUpsertDto.from_dict(data)

                    return steps_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_6 = DigestStepUpsertDto.from_dict(data)

                    return steps_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_7 = ThrottleStepUpsertDto.from_dict(data)

                    return steps_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_8 = CustomStepUpsertDto.from_dict(data)

                    return steps_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                steps_item_type_9 = HttpRequestStepUpsertDto.from_dict(data)

                return steps_item_type_9

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        preferences = PreferencesRequestDto.from_dict(d.pop("preferences"))

        origin = ResourceOriginEnum(d.pop("origin"))

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        active = d.pop("active", UNSET)

        validate_payload = d.pop("validatePayload", UNSET)

        def _parse_payload_schema(data: object) -> None | Unset | UpdateWorkflowDtoPayloadSchemaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_schema_type_0 = UpdateWorkflowDtoPayloadSchemaType0.from_dict(data)

                return payload_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateWorkflowDtoPayloadSchemaType0, data)

        payload_schema = _parse_payload_schema(d.pop("payloadSchema", UNSET))

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: SeverityLevelEnum | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityLevelEnum(_severity)

        update_workflow_dto = cls(
            name=name,
            steps=steps,
            preferences=preferences,
            origin=origin,
            description=description,
            tags=tags,
            active=active,
            validate_payload=validate_payload,
            payload_schema=payload_schema,
            is_translation_enabled=is_translation_enabled,
            workflow_id=workflow_id,
            severity=severity,
        )

        update_workflow_dto.additional_properties = d
        return update_workflow_dto

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
