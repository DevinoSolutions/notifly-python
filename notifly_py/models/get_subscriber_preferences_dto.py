from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscriber_global_preference_dto import SubscriberGlobalPreferenceDto
    from ..models.subscriber_workflow_preference_dto import SubscriberWorkflowPreferenceDto


T = TypeVar("T", bound="GetSubscriberPreferencesDto")


@_attrs_define
class GetSubscriberPreferencesDto:
    """
    Attributes:
        global_ (SubscriberGlobalPreferenceDto):
        workflows (list[SubscriberWorkflowPreferenceDto]): Workflow-specific preference settings
    """

    global_: SubscriberGlobalPreferenceDto
    workflows: list[SubscriberWorkflowPreferenceDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_ = self.global_.to_dict()

        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()
            workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "global": global_,
                "workflows": workflows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_global_preference_dto import SubscriberGlobalPreferenceDto
        from ..models.subscriber_workflow_preference_dto import SubscriberWorkflowPreferenceDto

        d = dict(src_dict)
        global_ = SubscriberGlobalPreferenceDto.from_dict(d.pop("global"))

        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in _workflows:
            workflows_item = SubscriberWorkflowPreferenceDto.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        get_subscriber_preferences_dto = cls(
            global_=global_,
            workflows=workflows,
        )

        get_subscriber_preferences_dto.additional_properties = d
        return get_subscriber_preferences_dto

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
