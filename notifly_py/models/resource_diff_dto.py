from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diff_action_enum import DiffActionEnum
from ..models.resource_type_enum import ResourceTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_diff_dto_diffs import ResourceDiffDtoDiffs
    from ..models.resource_info_dto import ResourceInfoDto


T = TypeVar("T", bound="ResourceDiffDto")


@_attrs_define
class ResourceDiffDto:
    """
    Attributes:
        resource_type (ResourceTypeEnum): Type of the layout
        action (DiffActionEnum): Type of change
        source_resource (None | ResourceInfoDto | Unset): Source resource information
        target_resource (None | ResourceInfoDto | Unset): Target resource information
        diffs (ResourceDiffDtoDiffs | Unset): Detailed changes (only for modified resources)
        step_type (str | Unset): Step type (only for step resources)
        previous_index (float | Unset): Previous index in steps array (for moved/deleted steps)
        new_index (float | Unset): New index in steps array (for moved/added steps)
    """

    resource_type: ResourceTypeEnum
    action: DiffActionEnum
    source_resource: None | ResourceInfoDto | Unset = UNSET
    target_resource: None | ResourceInfoDto | Unset = UNSET
    diffs: ResourceDiffDtoDiffs | Unset = UNSET
    step_type: str | Unset = UNSET
    previous_index: float | Unset = UNSET
    new_index: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_info_dto import ResourceInfoDto

        resource_type = self.resource_type.value

        action = self.action.value

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

        diffs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diffs, Unset):
            diffs = self.diffs.to_dict()

        step_type = self.step_type

        previous_index = self.previous_index

        new_index = self.new_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceType": resource_type,
                "action": action,
            }
        )
        if source_resource is not UNSET:
            field_dict["sourceResource"] = source_resource
        if target_resource is not UNSET:
            field_dict["targetResource"] = target_resource
        if diffs is not UNSET:
            field_dict["diffs"] = diffs
        if step_type is not UNSET:
            field_dict["stepType"] = step_type
        if previous_index is not UNSET:
            field_dict["previousIndex"] = previous_index
        if new_index is not UNSET:
            field_dict["newIndex"] = new_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_diff_dto_diffs import ResourceDiffDtoDiffs
        from ..models.resource_info_dto import ResourceInfoDto

        d = dict(src_dict)
        resource_type = ResourceTypeEnum(d.pop("resourceType"))

        action = DiffActionEnum(d.pop("action"))

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

        _diffs = d.pop("diffs", UNSET)
        diffs: ResourceDiffDtoDiffs | Unset
        if isinstance(_diffs, Unset):
            diffs = UNSET
        else:
            diffs = ResourceDiffDtoDiffs.from_dict(_diffs)

        step_type = d.pop("stepType", UNSET)

        previous_index = d.pop("previousIndex", UNSET)

        new_index = d.pop("newIndex", UNSET)

        resource_diff_dto = cls(
            resource_type=resource_type,
            action=action,
            source_resource=source_resource,
            target_resource=target_resource,
            diffs=diffs,
            step_type=step_type,
            previous_index=previous_index,
            new_index=new_index,
        )

        resource_diff_dto.additional_properties = d
        return resource_diff_dto

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
