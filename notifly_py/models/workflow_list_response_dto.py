from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..models.step_type_enum import StepTypeEnum
from ..models.workflow_status_enum import WorkflowStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_list_response_dto import StepListResponseDto
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="WorkflowListResponseDto")


@_attrs_define
class WorkflowListResponseDto:
    """
    Attributes:
        name (str): Name of the workflow
        updated_at (str): Last updated timestamp
        created_at (str): Creation timestamp
        field_id (str): Unique database identifier
        workflow_id (str): Workflow identifier
        slug (str): Workflow slug
        status (WorkflowStatusEnum): Status of the workflow
        origin (ResourceOriginEnum): Origin of the layout
        step_type_overviews (list[StepTypeEnum]): Overview of step types in the workflow
        steps (list[StepListResponseDto]): Steps of the workflow
        tags (list[str] | Unset): Tags associated with the workflow
        updated_by (None | Unset | UserResponseDto): User who last updated the workflow
        last_published_at (None | str | Unset): Timestamp of the last workflow publication
        last_published_by (None | Unset | UserResponseDto): User who last published the workflow
        last_triggered_at (None | str | Unset): Timestamp of the last workflow trigger
        is_translation_enabled (bool | Unset): Is translation enabled for the workflow
    """

    name: str
    updated_at: str
    created_at: str
    field_id: str
    workflow_id: str
    slug: str
    status: WorkflowStatusEnum
    origin: ResourceOriginEnum
    step_type_overviews: list[StepTypeEnum]
    steps: list[StepListResponseDto]
    tags: list[str] | Unset = UNSET
    updated_by: None | Unset | UserResponseDto = UNSET
    last_published_at: None | str | Unset = UNSET
    last_published_by: None | Unset | UserResponseDto = UNSET
    last_triggered_at: None | str | Unset = UNSET
    is_translation_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_response_dto import UserResponseDto

        name = self.name

        updated_at = self.updated_at

        created_at = self.created_at

        field_id = self.field_id

        workflow_id = self.workflow_id

        slug = self.slug

        status = self.status.value

        origin = self.origin.value

        step_type_overviews = []
        for step_type_overviews_item_data in self.step_type_overviews:
            step_type_overviews_item = step_type_overviews_item_data.value
            step_type_overviews.append(step_type_overviews_item)

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UserResponseDto):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        last_published_at: None | str | Unset
        if isinstance(self.last_published_at, Unset):
            last_published_at = UNSET
        else:
            last_published_at = self.last_published_at

        last_published_by: dict[str, Any] | None | Unset
        if isinstance(self.last_published_by, Unset):
            last_published_by = UNSET
        elif isinstance(self.last_published_by, UserResponseDto):
            last_published_by = self.last_published_by.to_dict()
        else:
            last_published_by = self.last_published_by

        last_triggered_at: None | str | Unset
        if isinstance(self.last_triggered_at, Unset):
            last_triggered_at = UNSET
        else:
            last_triggered_at = self.last_triggered_at

        is_translation_enabled = self.is_translation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "_id": field_id,
                "workflowId": workflow_id,
                "slug": slug,
                "status": status,
                "origin": origin,
                "stepTypeOverviews": step_type_overviews,
                "steps": steps,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if last_published_at is not UNSET:
            field_dict["lastPublishedAt"] = last_published_at
        if last_published_by is not UNSET:
            field_dict["lastPublishedBy"] = last_published_by
        if last_triggered_at is not UNSET:
            field_dict["lastTriggeredAt"] = last_triggered_at
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_list_response_dto import StepListResponseDto
        from ..models.user_response_dto import UserResponseDto

        d = dict(src_dict)
        name = d.pop("name")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        field_id = d.pop("_id")

        workflow_id = d.pop("workflowId")

        slug = d.pop("slug")

        status = WorkflowStatusEnum(d.pop("status"))

        origin = ResourceOriginEnum(d.pop("origin"))

        step_type_overviews = []
        _step_type_overviews = d.pop("stepTypeOverviews")
        for step_type_overviews_item_data in _step_type_overviews:
            step_type_overviews_item = StepTypeEnum(step_type_overviews_item_data)

            step_type_overviews.append(step_type_overviews_item)

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepListResponseDto.from_dict(steps_item_data)

            steps.append(steps_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UserResponseDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_1 = UserResponseDto.from_dict(data)

                return updated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserResponseDto, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))

        def _parse_last_published_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_published_at = _parse_last_published_at(d.pop("lastPublishedAt", UNSET))

        def _parse_last_published_by(data: object) -> None | Unset | UserResponseDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_published_by_type_1 = UserResponseDto.from_dict(data)

                return last_published_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserResponseDto, data)

        last_published_by = _parse_last_published_by(d.pop("lastPublishedBy", UNSET))

        def _parse_last_triggered_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("lastTriggeredAt", UNSET))

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        workflow_list_response_dto = cls(
            name=name,
            updated_at=updated_at,
            created_at=created_at,
            field_id=field_id,
            workflow_id=workflow_id,
            slug=slug,
            status=status,
            origin=origin,
            step_type_overviews=step_type_overviews,
            steps=steps,
            tags=tags,
            updated_by=updated_by,
            last_published_at=last_published_at,
            last_published_by=last_published_by,
            last_triggered_at=last_triggered_at,
            is_translation_enabled=is_translation_enabled,
        )

        workflow_list_response_dto.additional_properties = d
        return workflow_list_response_dto

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
