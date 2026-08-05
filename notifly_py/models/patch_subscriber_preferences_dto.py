from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_preference_channels_dto import PatchPreferenceChannelsDto
    from ..models.patch_subscriber_preferences_dto_context import PatchSubscriberPreferencesDtoContext
    from ..models.schedule_dto import ScheduleDto


T = TypeVar("T", bound="PatchSubscriberPreferencesDto")


@_attrs_define
class PatchSubscriberPreferencesDto:
    """
    Attributes:
        channels (PatchPreferenceChannelsDto | Unset):
        workflow_id (str | Unset): Workflow internal _id, identifier or slug. If provided, update workflow specific
            preferences, otherwise update global preferences
        schedule (ScheduleDto | Unset):
        context (PatchSubscriberPreferencesDtoContext | Unset):
    """

    channels: PatchPreferenceChannelsDto | Unset = UNSET
    workflow_id: str | Unset = UNSET
    schedule: ScheduleDto | Unset = UNSET
    context: PatchSubscriberPreferencesDtoContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        workflow_id = self.workflow_id

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_preference_channels_dto import PatchPreferenceChannelsDto
        from ..models.patch_subscriber_preferences_dto_context import PatchSubscriberPreferencesDtoContext
        from ..models.schedule_dto import ScheduleDto

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: PatchPreferenceChannelsDto | Unset
        if isinstance(_channels, Unset):
            channels = UNSET
        else:
            channels = PatchPreferenceChannelsDto.from_dict(_channels)

        workflow_id = d.pop("workflowId", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: ScheduleDto | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ScheduleDto.from_dict(_schedule)

        _context = d.pop("context", UNSET)
        context: PatchSubscriberPreferencesDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = PatchSubscriberPreferencesDtoContext.from_dict(_context)

        patch_subscriber_preferences_dto = cls(
            channels=channels,
            workflow_id=workflow_id,
            schedule=schedule,
            context=context,
        )

        patch_subscriber_preferences_dto.additional_properties = d
        return patch_subscriber_preferences_dto

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
