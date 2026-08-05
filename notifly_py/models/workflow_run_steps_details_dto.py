from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_run_steps_details_dto_status import WorkflowRunStepsDetailsDtoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRunStepsDetailsDto")


@_attrs_define
class WorkflowRunStepsDetailsDto:
    """
    Attributes:
        id (str): Step run identifier
        step_run_id (str): Step identifier
        step_id (str): Step identifier
        step_type (str): Step type
        status (WorkflowRunStepsDetailsDtoStatus): Step status
        provider_id (str | Unset): Provider identifier
    """

    id: str
    step_run_id: str
    step_id: str
    step_type: str
    status: WorkflowRunStepsDetailsDtoStatus
    provider_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        step_run_id = self.step_run_id

        step_id = self.step_id

        step_type = self.step_type

        status = self.status.value

        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "stepRunId": step_run_id,
                "stepId": step_id,
                "stepType": step_type,
                "status": status,
            }
        )
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        step_run_id = d.pop("stepRunId")

        step_id = d.pop("stepId")

        step_type = d.pop("stepType")

        status = WorkflowRunStepsDetailsDtoStatus(d.pop("status"))

        provider_id = d.pop("providerId", UNSET)

        workflow_run_steps_details_dto = cls(
            id=id,
            step_run_id=step_run_id,
            step_id=step_id,
            step_type=step_type,
            status=status,
            provider_id=provider_id,
        )

        workflow_run_steps_details_dto.additional_properties = d
        return workflow_run_steps_details_dto

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
