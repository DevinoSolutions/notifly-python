from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.environment_diff_summary_dto import EnvironmentDiffSummaryDto
    from ..models.resource_diff_result_dto import ResourceDiffResultDto


T = TypeVar("T", bound="DiffEnvironmentResponseDto")


@_attrs_define
class DiffEnvironmentResponseDto:
    """
    Attributes:
        source_environment_id (str): Source environment ID
        target_environment_id (str): Target environment ID
        resources (list[ResourceDiffResultDto]): Diff resources by resource type
        summary (EnvironmentDiffSummaryDto):
    """

    source_environment_id: str
    target_environment_id: str
    resources: list[ResourceDiffResultDto]
    summary: EnvironmentDiffSummaryDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_environment_id = self.source_environment_id

        target_environment_id = self.target_environment_id

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceEnvironmentId": source_environment_id,
                "targetEnvironmentId": target_environment_id,
                "resources": resources,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_diff_summary_dto import EnvironmentDiffSummaryDto
        from ..models.resource_diff_result_dto import ResourceDiffResultDto

        d = dict(src_dict)
        source_environment_id = d.pop("sourceEnvironmentId")

        target_environment_id = d.pop("targetEnvironmentId")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = ResourceDiffResultDto.from_dict(resources_item_data)

            resources.append(resources_item)

        summary = EnvironmentDiffSummaryDto.from_dict(d.pop("summary"))

        diff_environment_response_dto = cls(
            source_environment_id=source_environment_id,
            target_environment_id=target_environment_id,
            resources=resources,
            summary=summary,
        )

        diff_environment_response_dto.additional_properties = d
        return diff_environment_response_dto

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
