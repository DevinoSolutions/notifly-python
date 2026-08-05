from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateWorkflowDto")


@_attrs_define
class DuplicateWorkflowDto:
    """
    Attributes:
        name (str | Unset): Name of the workflow
        workflow_id (str | Unset): Custom workflow identifier for the duplicated workflow
        tags (list[str] | Unset): Tags associated with the workflow
        description (str | Unset): Description of the workflow
        is_translation_enabled (bool | Unset): Enable or disable translations for this workflow Default: False.
    """

    name: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    is_translation_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        workflow_id = self.workflow_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        description = self.description

        is_translation_enabled = self.is_translation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if description is not UNSET:
            field_dict["description"] = description
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        description = d.pop("description", UNSET)

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        duplicate_workflow_dto = cls(
            name=name,
            workflow_id=workflow_id,
            tags=tags,
            description=description,
            is_translation_enabled=is_translation_enabled,
        )

        duplicate_workflow_dto.additional_properties = d
        return duplicate_workflow_dto

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
