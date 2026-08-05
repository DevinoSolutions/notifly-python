from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_preference_dto_condition import SubscriptionPreferenceDtoCondition
    from ..models.workflow_dto import WorkflowDto


T = TypeVar("T", bound="SubscriptionPreferenceDto")


@_attrs_define
class SubscriptionPreferenceDto:
    """
    Attributes:
        subscription_id (str): The unique identifier of the subscription Example: 64f5e95d3d7946d80d0cb679.
        enabled (bool): Whether the preference is enabled Example: True.
        workflow (None | Unset | WorkflowDto): Workflow information if this is a template-level preference
        condition (SubscriptionPreferenceDtoCondition | Unset): Optional condition using JSON Logic rules Example:
            {'and': [{'===': [{'var': 'tier'}, 'premium']}]}.
    """

    subscription_id: str
    enabled: bool
    workflow: None | Unset | WorkflowDto = UNSET
    condition: SubscriptionPreferenceDtoCondition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_dto import WorkflowDto

        subscription_id = self.subscription_id

        enabled = self.enabled

        workflow: dict[str, Any] | None | Unset
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        elif isinstance(self.workflow, WorkflowDto):
            workflow = self.workflow.to_dict()
        else:
            workflow = self.workflow

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
                "enabled": enabled,
            }
        )
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_preference_dto_condition import SubscriptionPreferenceDtoCondition
        from ..models.workflow_dto import WorkflowDto

        d = dict(src_dict)
        subscription_id = d.pop("subscriptionId")

        enabled = d.pop("enabled")

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

        _condition = d.pop("condition", UNSET)
        condition: SubscriptionPreferenceDtoCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = SubscriptionPreferenceDtoCondition.from_dict(_condition)

        subscription_preference_dto = cls(
            subscription_id=subscription_id,
            enabled=enabled,
            workflow=workflow,
            condition=condition,
        )

        subscription_preference_dto.additional_properties = d
        return subscription_preference_dto

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
