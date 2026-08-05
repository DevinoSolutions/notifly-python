from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_notification_job_response_dto_type import ActivityNotificationJobResponseDtoType
from ..models.providers_id_enum import ProvidersIdEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_notification_execution_detail_response_dto import (
        ActivityNotificationExecutionDetailResponseDto,
    )
    from ..models.activity_notification_job_response_dto_overrides import ActivityNotificationJobResponseDtoOverrides
    from ..models.activity_notification_job_response_dto_payload import ActivityNotificationJobResponseDtoPayload
    from ..models.activity_notification_step_response_dto import ActivityNotificationStepResponseDto
    from ..models.digest_metadata_dto import DigestMetadataDto


T = TypeVar("T", bound="ActivityNotificationJobResponseDto")


@_attrs_define
class ActivityNotificationJobResponseDto:
    """
    Attributes:
        field_id (str): Unique identifier of the job
        type_ (ActivityNotificationJobResponseDtoType): Type of the job
        execution_details (list[ActivityNotificationExecutionDetailResponseDto]): Execution details of the job
        step (ActivityNotificationStepResponseDto):
        provider_id (ProvidersIdEnum): Provider ID of the job
        status (str): Status of the job
        digest (DigestMetadataDto | Unset):
        overrides (ActivityNotificationJobResponseDtoOverrides | Unset): Optional context object for additional error
            details. Example: {'workflowId': 'some_wf_id', 'stepId': 'some_wf_id'}.
        payload (ActivityNotificationJobResponseDtoPayload | Unset): Optional payload for the job
        updated_at (str | Unset): Updated time of the notification
        schedule_extensions_count (float | Unset): The number of times the digest/delay job has been extended to align
            with the subscribers schedule
    """

    field_id: str
    type_: ActivityNotificationJobResponseDtoType
    execution_details: list[ActivityNotificationExecutionDetailResponseDto]
    step: ActivityNotificationStepResponseDto
    provider_id: ProvidersIdEnum
    status: str
    digest: DigestMetadataDto | Unset = UNSET
    overrides: ActivityNotificationJobResponseDtoOverrides | Unset = UNSET
    payload: ActivityNotificationJobResponseDtoPayload | Unset = UNSET
    updated_at: str | Unset = UNSET
    schedule_extensions_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        type_ = self.type_.value

        execution_details = []
        for execution_details_item_data in self.execution_details:
            execution_details_item = execution_details_item_data.to_dict()
            execution_details.append(execution_details_item)

        step = self.step.to_dict()

        provider_id = self.provider_id.value

        status = self.status

        digest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest.to_dict()

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        updated_at = self.updated_at

        schedule_extensions_count = self.schedule_extensions_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "type": type_,
                "executionDetails": execution_details,
                "step": step,
                "providerId": provider_id,
                "status": status,
            }
        )
        if digest is not UNSET:
            field_dict["digest"] = digest
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if payload is not UNSET:
            field_dict["payload"] = payload
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if schedule_extensions_count is not UNSET:
            field_dict["scheduleExtensionsCount"] = schedule_extensions_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_notification_execution_detail_response_dto import (
            ActivityNotificationExecutionDetailResponseDto,
        )
        from ..models.activity_notification_job_response_dto_overrides import (
            ActivityNotificationJobResponseDtoOverrides,
        )
        from ..models.activity_notification_job_response_dto_payload import ActivityNotificationJobResponseDtoPayload
        from ..models.activity_notification_step_response_dto import ActivityNotificationStepResponseDto
        from ..models.digest_metadata_dto import DigestMetadataDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        type_ = ActivityNotificationJobResponseDtoType(d.pop("type"))

        execution_details = []
        _execution_details = d.pop("executionDetails")
        for execution_details_item_data in _execution_details:
            execution_details_item = ActivityNotificationExecutionDetailResponseDto.from_dict(
                execution_details_item_data
            )

            execution_details.append(execution_details_item)

        step = ActivityNotificationStepResponseDto.from_dict(d.pop("step"))

        provider_id = ProvidersIdEnum(d.pop("providerId"))

        status = d.pop("status")

        _digest = d.pop("digest", UNSET)
        digest: DigestMetadataDto | Unset
        if isinstance(_digest, Unset):
            digest = UNSET
        else:
            digest = DigestMetadataDto.from_dict(_digest)

        _overrides = d.pop("overrides", UNSET)
        overrides: ActivityNotificationJobResponseDtoOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = ActivityNotificationJobResponseDtoOverrides.from_dict(_overrides)

        _payload = d.pop("payload", UNSET)
        payload: ActivityNotificationJobResponseDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ActivityNotificationJobResponseDtoPayload.from_dict(_payload)

        updated_at = d.pop("updatedAt", UNSET)

        schedule_extensions_count = d.pop("scheduleExtensionsCount", UNSET)

        activity_notification_job_response_dto = cls(
            field_id=field_id,
            type_=type_,
            execution_details=execution_details,
            step=step,
            provider_id=provider_id,
            status=status,
            digest=digest,
            overrides=overrides,
            payload=payload,
            updated_at=updated_at,
            schedule_extensions_count=schedule_extensions_count,
        )

        activity_notification_job_response_dto.additional_properties = d
        return activity_notification_job_response_dto

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
