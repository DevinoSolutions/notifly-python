from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_run_dto_status import StepRunDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_metadata_dto import DigestMetadataDto
    from ..models.step_execution_detail_dto import StepExecutionDetailDto


T = TypeVar("T", bound="StepRunDto")


@_attrs_define
class StepRunDto:
    """
    Attributes:
        step_run_id (str): Step run identifier
        step_id (str): Step identifier
        step_type (str): Step type
        status (StepRunDtoStatus): Step status
        created_at (datetime.datetime): Creation timestamp
        updated_at (datetime.datetime): Update timestamp
        execution_details (list[StepExecutionDetailDto]): Execution details
        provider_id (str | Unset): Provider identifier
        digest (DigestMetadataDto | Unset):
        schedule_extensions_count (float | Unset): The number of times the digest/delay job has been extended to align
            with the subscribers schedule
    """

    step_run_id: str
    step_id: str
    step_type: str
    status: StepRunDtoStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    execution_details: list[StepExecutionDetailDto]
    provider_id: str | Unset = UNSET
    digest: DigestMetadataDto | Unset = UNSET
    schedule_extensions_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_run_id = self.step_run_id

        step_id = self.step_id

        step_type = self.step_type

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        execution_details = []
        for execution_details_item_data in self.execution_details:
            execution_details_item = execution_details_item_data.to_dict()
            execution_details.append(execution_details_item)

        provider_id = self.provider_id

        digest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.digest, Unset):
            digest = self.digest.to_dict()

        schedule_extensions_count = self.schedule_extensions_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stepRunId": step_run_id,
                "stepId": step_id,
                "stepType": step_type,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "executionDetails": execution_details,
            }
        )
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if digest is not UNSET:
            field_dict["digest"] = digest
        if schedule_extensions_count is not UNSET:
            field_dict["scheduleExtensionsCount"] = schedule_extensions_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_metadata_dto import DigestMetadataDto
        from ..models.step_execution_detail_dto import StepExecutionDetailDto

        d = dict(src_dict)
        step_run_id = d.pop("stepRunId")

        step_id = d.pop("stepId")

        step_type = d.pop("stepType")

        status = StepRunDtoStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        execution_details = []
        _execution_details = d.pop("executionDetails")
        for execution_details_item_data in _execution_details:
            execution_details_item = StepExecutionDetailDto.from_dict(execution_details_item_data)

            execution_details.append(execution_details_item)

        provider_id = d.pop("providerId", UNSET)

        _digest = d.pop("digest", UNSET)
        digest: DigestMetadataDto | Unset
        if isinstance(_digest, Unset):
            digest = UNSET
        else:
            digest = DigestMetadataDto.from_dict(_digest)

        schedule_extensions_count = d.pop("scheduleExtensionsCount", UNSET)

        step_run_dto = cls(
            step_run_id=step_run_id,
            step_id=step_id,
            step_type=step_type,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            execution_details=execution_details,
            provider_id=provider_id,
            digest=digest,
            schedule_extensions_count=schedule_extensions_count,
        )

        step_run_dto.additional_properties = d
        return step_run_dto

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
