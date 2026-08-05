from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.environment_variable_workflow_info_dto import EnvironmentVariableWorkflowInfoDto


T = TypeVar("T", bound="GetEnvironmentVariableUsageResponseDto")


@_attrs_define
class GetEnvironmentVariableUsageResponseDto:
    """
    Attributes:
        workflows (list[EnvironmentVariableWorkflowInfoDto]): Array of workflows that reference this environment
            variable
    """

    workflows: list[EnvironmentVariableWorkflowInfoDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()
            workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflows": workflows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_variable_workflow_info_dto import EnvironmentVariableWorkflowInfoDto

        d = dict(src_dict)
        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in _workflows:
            workflows_item = EnvironmentVariableWorkflowInfoDto.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        get_environment_variable_usage_response_dto = cls(
            workflows=workflows,
        )

        get_environment_variable_usage_response_dto.additional_properties = d
        return get_environment_variable_usage_response_dto

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
