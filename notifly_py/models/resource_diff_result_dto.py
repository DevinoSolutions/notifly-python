from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type_enum import ResourceTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_summary_dto import DiffSummaryDto
    from ..models.resource_dependency_dto import ResourceDependencyDto
    from ..models.resource_diff_dto import ResourceDiffDto
    from ..models.resource_info_dto import ResourceInfoDto


T = TypeVar("T", bound="ResourceDiffResultDto")


@_attrs_define
class ResourceDiffResultDto:
    """
    Attributes:
        resource_type (ResourceTypeEnum): Type of the layout
        changes (list[ResourceDiffDto]): List of specific changes for this resource
        summary (DiffSummaryDto):
        source_resource (None | ResourceInfoDto | Unset): Source resource information
        target_resource (None | ResourceInfoDto | Unset): Target resource information
        dependencies (list[ResourceDependencyDto] | Unset): Dependencies that affect this resource
    """

    resource_type: ResourceTypeEnum
    changes: list[ResourceDiffDto]
    summary: DiffSummaryDto
    source_resource: None | ResourceInfoDto | Unset = UNSET
    target_resource: None | ResourceInfoDto | Unset = UNSET
    dependencies: list[ResourceDependencyDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_info_dto import ResourceInfoDto

        resource_type = self.resource_type.value

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        summary = self.summary.to_dict()

        source_resource: dict[str, Any] | None | Unset
        if isinstance(self.source_resource, Unset):
            source_resource = UNSET
        elif isinstance(self.source_resource, ResourceInfoDto):
            source_resource = self.source_resource.to_dict()
        else:
            source_resource = self.source_resource

        target_resource: dict[str, Any] | None | Unset
        if isinstance(self.target_resource, Unset):
            target_resource = UNSET
        elif isinstance(self.target_resource, ResourceInfoDto):
            target_resource = self.target_resource.to_dict()
        else:
            target_resource = self.target_resource

        dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceType": resource_type,
                "changes": changes,
                "summary": summary,
            }
        )
        if source_resource is not UNSET:
            field_dict["sourceResource"] = source_resource
        if target_resource is not UNSET:
            field_dict["targetResource"] = target_resource
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_summary_dto import DiffSummaryDto
        from ..models.resource_dependency_dto import ResourceDependencyDto
        from ..models.resource_diff_dto import ResourceDiffDto
        from ..models.resource_info_dto import ResourceInfoDto

        d = dict(src_dict)
        resource_type = ResourceTypeEnum(d.pop("resourceType"))

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = ResourceDiffDto.from_dict(changes_item_data)

            changes.append(changes_item)

        summary = DiffSummaryDto.from_dict(d.pop("summary"))

        def _parse_source_resource(data: object) -> None | ResourceInfoDto | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_resource_type_1 = ResourceInfoDto.from_dict(data)

                return source_resource_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceInfoDto | Unset, data)

        source_resource = _parse_source_resource(d.pop("sourceResource", UNSET))

        def _parse_target_resource(data: object) -> None | ResourceInfoDto | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_resource_type_1 = ResourceInfoDto.from_dict(data)

                return target_resource_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceInfoDto | Unset, data)

        target_resource = _parse_target_resource(d.pop("targetResource", UNSET))

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[ResourceDependencyDto] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = ResourceDependencyDto.from_dict(dependencies_item_data)

                dependencies.append(dependencies_item)

        resource_diff_result_dto = cls(
            resource_type=resource_type,
            changes=changes,
            summary=summary,
            source_resource=source_resource,
            target_resource=target_resource,
            dependencies=dependencies,
        )

        resource_diff_result_dto.additional_properties = d
        return resource_diff_result_dto

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
