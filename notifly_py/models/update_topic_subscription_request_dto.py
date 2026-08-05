from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
    from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto


T = TypeVar("T", bound="UpdateTopicSubscriptionRequestDto")


@_attrs_define
class UpdateTopicSubscriptionRequestDto:
    """
    Attributes:
        name (str | Unset): The name of the subscription Example: My Subscription.
        preferences (list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset): The preferences of
            the topic. Can be a simple workflow ID string, workflow preference object, or group filter object Example:
            [{'workflowId': 'workflow-123', 'condition': {'===': [{'var': 'tier'}, 'premium']}}].
    """

    name: str | Unset = UNSET
    preferences: list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
        from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto

        name = self.name

        preferences: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = []
            for preferences_item_data in self.preferences:
                preferences_item: dict[str, Any] | str
                if isinstance(preferences_item_data, WorkflowPreferenceRequestDto):
                    preferences_item = preferences_item_data.to_dict()
                elif isinstance(preferences_item_data, GroupPreferenceFilterDto):
                    preferences_item = preferences_item_data.to_dict()
                else:
                    preferences_item = preferences_item_data
                preferences.append(preferences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_preference_filter_dto import GroupPreferenceFilterDto
        from ..models.workflow_preference_request_dto import WorkflowPreferenceRequestDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _preferences = d.pop("preferences", UNSET)
        preferences: list[GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto] | Unset = UNSET
        if _preferences is not UNSET:
            preferences = []
            for preferences_item_data in _preferences:

                def _parse_preferences_item(
                    data: object,
                ) -> GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        preferences_item_type_1 = WorkflowPreferenceRequestDto.from_dict(data)

                        return preferences_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        preferences_item_type_2 = GroupPreferenceFilterDto.from_dict(data)

                        return preferences_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(GroupPreferenceFilterDto | str | WorkflowPreferenceRequestDto, data)

                preferences_item = _parse_preferences_item(preferences_item_data)

                preferences.append(preferences_item)

        update_topic_subscription_request_dto = cls(
            name=name,
            preferences=preferences,
        )

        update_topic_subscription_request_dto.additional_properties = d
        return update_topic_subscription_request_dto

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
