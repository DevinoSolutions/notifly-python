from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
    from ..models.subscriber_preference_override_dto import SubscriberPreferenceOverrideDto
    from ..models.subscriber_preferences_workflow_info_dto import SubscriberPreferencesWorkflowInfoDto


T = TypeVar("T", bound="SubscriberWorkflowPreferenceDto")


@_attrs_define
class SubscriberWorkflowPreferenceDto:
    """
    Attributes:
        enabled (bool): Whether notifications are enabled for this workflow
        channels (SubscriberPreferenceChannels):
        overrides (list[SubscriberPreferenceOverrideDto]): List of preference overrides
        workflow (SubscriberPreferencesWorkflowInfoDto):
        updated_at (str | Unset): Timestamp when the subscriber last updated their preference. Only present if
            subscriber explicitly set preferences.
    """

    enabled: bool
    channels: SubscriberPreferenceChannels
    overrides: list[SubscriberPreferenceOverrideDto]
    workflow: SubscriberPreferencesWorkflowInfoDto
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        channels = self.channels.to_dict()

        overrides = []
        for overrides_item_data in self.overrides:
            overrides_item = overrides_item_data.to_dict()
            overrides.append(overrides_item)

        workflow = self.workflow.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "channels": channels,
                "overrides": overrides,
                "workflow": workflow,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
        from ..models.subscriber_preference_override_dto import SubscriberPreferenceOverrideDto
        from ..models.subscriber_preferences_workflow_info_dto import SubscriberPreferencesWorkflowInfoDto

        d = dict(src_dict)
        enabled = d.pop("enabled")

        channels = SubscriberPreferenceChannels.from_dict(d.pop("channels"))

        overrides = []
        _overrides = d.pop("overrides")
        for overrides_item_data in _overrides:
            overrides_item = SubscriberPreferenceOverrideDto.from_dict(overrides_item_data)

            overrides.append(overrides_item)

        workflow = SubscriberPreferencesWorkflowInfoDto.from_dict(d.pop("workflow"))

        updated_at = d.pop("updatedAt", UNSET)

        subscriber_workflow_preference_dto = cls(
            enabled=enabled,
            channels=channels,
            overrides=overrides,
            workflow=workflow,
            updated_at=updated_at,
        )

        subscriber_workflow_preference_dto.additional_properties = d
        return subscriber_workflow_preference_dto

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
