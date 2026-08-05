from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupPreferenceFilterDetailsDto")


@_attrs_define
class GroupPreferenceFilterDetailsDto:
    """
    Attributes:
        workflow_ids (list[str] | Unset): List of workflow identifiers Example: ['workflow-1', 'workflow-2'].
        tags (list[str] | Unset): List of tags Example: ['tag1', 'tag2'].
    """

    workflow_ids: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_ids: list[str] | Unset = UNSET
        if not isinstance(self.workflow_ids, Unset):
            workflow_ids = self.workflow_ids

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_ids is not UNSET:
            field_dict["workflowIds"] = workflow_ids
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_ids = cast(list[str], d.pop("workflowIds", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        group_preference_filter_details_dto = cls(
            workflow_ids=workflow_ids,
            tags=tags,
        )

        group_preference_filter_details_dto.additional_properties = d
        return group_preference_filter_details_dto

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
