from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_notification_step_response_dto_control_variables import (
        ActivityNotificationStepResponseDtoControlVariables,
    )
    from ..models.activity_notification_step_response_dto_issues import ActivityNotificationStepResponseDtoIssues
    from ..models.activity_notification_step_response_dto_metadata import ActivityNotificationStepResponseDtoMetadata
    from ..models.activity_notification_step_response_dto_reply_callback import (
        ActivityNotificationStepResponseDtoReplyCallback,
    )
    from ..models.message_template_dto import MessageTemplateDto
    from ..models.step_filter_dto import StepFilterDto


T = TypeVar("T", bound="ActivityNotificationStepResponseDto")


@_attrs_define
class ActivityNotificationStepResponseDto:
    """
    Attributes:
        field_id (str): Unique identifier of the step
        active (bool): Whether the step is active or not
        filters (list[StepFilterDto]): Filter criteria for the step
        field_template_id (str): The identifier for the template associated with this step
        reply_callback (ActivityNotificationStepResponseDtoReplyCallback | Unset): Reply callback settings
        control_variables (ActivityNotificationStepResponseDtoControlVariables | Unset): Control variables
        metadata (ActivityNotificationStepResponseDtoMetadata | Unset): Metadata for the workflow step
        issues (ActivityNotificationStepResponseDtoIssues | Unset): Step issues
        template (MessageTemplateDto | Unset):
        variants (list[ActivityNotificationStepResponseDto] | Unset): Variants of the step
        name (str | Unset): The name of the step
        field_parent_id (None | str | Unset): The unique identifier for the parent step
    """

    field_id: str
    active: bool
    filters: list[StepFilterDto]
    field_template_id: str
    reply_callback: ActivityNotificationStepResponseDtoReplyCallback | Unset = UNSET
    control_variables: ActivityNotificationStepResponseDtoControlVariables | Unset = UNSET
    metadata: ActivityNotificationStepResponseDtoMetadata | Unset = UNSET
    issues: ActivityNotificationStepResponseDtoIssues | Unset = UNSET
    template: MessageTemplateDto | Unset = UNSET
    variants: list[ActivityNotificationStepResponseDto] | Unset = UNSET
    name: str | Unset = UNSET
    field_parent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        active = self.active

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        field_template_id = self.field_template_id

        reply_callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_callback, Unset):
            reply_callback = self.reply_callback.to_dict()

        control_variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_variables, Unset):
            control_variables = self.control_variables.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        name = self.name

        field_parent_id: None | str | Unset
        if isinstance(self.field_parent_id, Unset):
            field_parent_id = UNSET
        else:
            field_parent_id = self.field_parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "active": active,
                "filters": filters,
                "_templateId": field_template_id,
            }
        )
        if reply_callback is not UNSET:
            field_dict["replyCallback"] = reply_callback
        if control_variables is not UNSET:
            field_dict["controlVariables"] = control_variables
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if issues is not UNSET:
            field_dict["issues"] = issues
        if template is not UNSET:
            field_dict["template"] = template
        if variants is not UNSET:
            field_dict["variants"] = variants
        if name is not UNSET:
            field_dict["name"] = name
        if field_parent_id is not UNSET:
            field_dict["_parentId"] = field_parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_notification_step_response_dto_control_variables import (
            ActivityNotificationStepResponseDtoControlVariables,
        )
        from ..models.activity_notification_step_response_dto_issues import ActivityNotificationStepResponseDtoIssues
        from ..models.activity_notification_step_response_dto_metadata import (
            ActivityNotificationStepResponseDtoMetadata,
        )
        from ..models.activity_notification_step_response_dto_reply_callback import (
            ActivityNotificationStepResponseDtoReplyCallback,
        )
        from ..models.message_template_dto import MessageTemplateDto
        from ..models.step_filter_dto import StepFilterDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        active = d.pop("active")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = StepFilterDto.from_dict(filters_item_data)

            filters.append(filters_item)

        field_template_id = d.pop("_templateId")

        _reply_callback = d.pop("replyCallback", UNSET)
        reply_callback: ActivityNotificationStepResponseDtoReplyCallback | Unset
        if isinstance(_reply_callback, Unset):
            reply_callback = UNSET
        else:
            reply_callback = ActivityNotificationStepResponseDtoReplyCallback.from_dict(_reply_callback)

        _control_variables = d.pop("controlVariables", UNSET)
        control_variables: ActivityNotificationStepResponseDtoControlVariables | Unset
        if isinstance(_control_variables, Unset):
            control_variables = UNSET
        else:
            control_variables = ActivityNotificationStepResponseDtoControlVariables.from_dict(_control_variables)

        _metadata = d.pop("metadata", UNSET)
        metadata: ActivityNotificationStepResponseDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ActivityNotificationStepResponseDtoMetadata.from_dict(_metadata)

        _issues = d.pop("issues", UNSET)
        issues: ActivityNotificationStepResponseDtoIssues | Unset
        if isinstance(_issues, Unset):
            issues = UNSET
        else:
            issues = ActivityNotificationStepResponseDtoIssues.from_dict(_issues)

        _template = d.pop("template", UNSET)
        template: MessageTemplateDto | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = MessageTemplateDto.from_dict(_template)

        _variants = d.pop("variants", UNSET)
        variants: list[ActivityNotificationStepResponseDto] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = ActivityNotificationStepResponseDto.from_dict(variants_item_data)

                variants.append(variants_item)

        name = d.pop("name", UNSET)

        def _parse_field_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_parent_id = _parse_field_parent_id(d.pop("_parentId", UNSET))

        activity_notification_step_response_dto = cls(
            field_id=field_id,
            active=active,
            filters=filters,
            field_template_id=field_template_id,
            reply_callback=reply_callback,
            control_variables=control_variables,
            metadata=metadata,
            issues=issues,
            template=template,
            variants=variants,
            name=name,
            field_parent_id=field_parent_id,
        )

        activity_notification_step_response_dto.additional_properties = d
        return activity_notification_step_response_dto

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
