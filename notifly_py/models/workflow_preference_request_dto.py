from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_preference_request_dto_condition import WorkflowPreferenceRequestDtoCondition


T = TypeVar("T", bound="WorkflowPreferenceRequestDto")


@_attrs_define
class WorkflowPreferenceRequestDto:
    """
    Attributes:
        workflow_id (str): The workflow identifier Example: workflow-123.
        enabled (bool | Unset): Whether the preference is enabled. Used when condition is not provided. Example: True.
        condition (WorkflowPreferenceRequestDtoCondition | Unset): Optional condition using JSON Logic rules Example:
            {'and': [{'===': [{'var': 'tier'}, 'premium']}]}.
    """

    workflow_id: str
    enabled: bool | Unset = UNSET
    condition: WorkflowPreferenceRequestDtoCondition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        enabled = self.enabled

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowId": workflow_id,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_preference_request_dto_condition import WorkflowPreferenceRequestDtoCondition

        d = dict(src_dict)
        workflow_id = d.pop("workflowId")

        enabled = d.pop("enabled", UNSET)

        _condition = d.pop("condition", UNSET)
        condition: WorkflowPreferenceRequestDtoCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = WorkflowPreferenceRequestDtoCondition.from_dict(_condition)

        workflow_preference_request_dto = cls(
            workflow_id=workflow_id,
            enabled=enabled,
            condition=condition,
        )

        workflow_preference_request_dto.additional_properties = d
        return workflow_preference_request_dto

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
