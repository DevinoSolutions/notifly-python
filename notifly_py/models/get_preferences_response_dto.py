from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preference_level_enum import PreferenceLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_preferences_response_dto_condition_type_0 import GetPreferencesResponseDtoConditionType0
    from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
    from ..models.workflow_dto import WorkflowDto


T = TypeVar("T", bound="GetPreferencesResponseDto")


@_attrs_define
class GetPreferencesResponseDto:
    """
    Attributes:
        level (PreferenceLevelEnum): The level of the preference (global or template)
        enabled (bool): Whether the preference is enabled Example: True.
        channels (SubscriberPreferenceChannels):
        workflow (None | Unset | WorkflowDto): Workflow information if this is a template-level preference
        condition (GetPreferencesResponseDtoConditionType0 | None | Unset): Condition using JSON Logic rules
    """

    level: PreferenceLevelEnum
    enabled: bool
    channels: SubscriberPreferenceChannels
    workflow: None | Unset | WorkflowDto = UNSET
    condition: GetPreferencesResponseDtoConditionType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_preferences_response_dto_condition_type_0 import GetPreferencesResponseDtoConditionType0
        from ..models.workflow_dto import WorkflowDto

        level = self.level.value

        enabled = self.enabled

        channels = self.channels.to_dict()

        workflow: dict[str, Any] | None | Unset
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        elif isinstance(self.workflow, WorkflowDto):
            workflow = self.workflow.to_dict()
        else:
            workflow = self.workflow

        condition: dict[str, Any] | None | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        elif isinstance(self.condition, GetPreferencesResponseDtoConditionType0):
            condition = self.condition.to_dict()
        else:
            condition = self.condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "enabled": enabled,
                "channels": channels,
            }
        )
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_preferences_response_dto_condition_type_0 import GetPreferencesResponseDtoConditionType0
        from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
        from ..models.workflow_dto import WorkflowDto

        d = dict(src_dict)
        level = PreferenceLevelEnum(d.pop("level"))

        enabled = d.pop("enabled")

        channels = SubscriberPreferenceChannels.from_dict(d.pop("channels"))

        def _parse_workflow(data: object) -> None | Unset | WorkflowDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workflow_type_1 = WorkflowDto.from_dict(data)

                return workflow_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowDto, data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))

        def _parse_condition(data: object) -> GetPreferencesResponseDtoConditionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_0 = GetPreferencesResponseDtoConditionType0.from_dict(data)

                return condition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetPreferencesResponseDtoConditionType0 | None | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))

        get_preferences_response_dto = cls(
            level=level,
            enabled=enabled,
            channels=channels,
            workflow=workflow,
            condition=condition,
        )

        get_preferences_response_dto.additional_properties = d
        return get_preferences_response_dto

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
