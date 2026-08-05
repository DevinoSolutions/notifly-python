from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_preference_dto import WorkflowPreferenceDto
    from ..models.workflow_preferences_dto_channels import WorkflowPreferencesDtoChannels


T = TypeVar("T", bound="WorkflowPreferencesDto")


@_attrs_define
class WorkflowPreferencesDto:
    """
    Attributes:
        all_ (WorkflowPreferenceDto): A preference for the workflow. The values specified here will be used if no
            preference is specified for a channel.
        channels (WorkflowPreferencesDtoChannels): Preferences for different communication channels Example: {'email':
            {'enabled': True}, 'sms': {'enabled': False}}.
    """

    all_: WorkflowPreferenceDto
    channels: WorkflowPreferencesDtoChannels
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_preference_dto import WorkflowPreferenceDto

        all_: dict[str, Any]
        if isinstance(self.all_, WorkflowPreferenceDto):
            all_ = self.all_.to_dict()

        channels = self.channels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all": all_,
                "channels": channels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_preference_dto import WorkflowPreferenceDto
        from ..models.workflow_preferences_dto_channels import WorkflowPreferencesDtoChannels

        d = dict(src_dict)

        def _parse_all_(data: object) -> WorkflowPreferenceDto:
            if not isinstance(data, dict):
                raise TypeError()
            all_type_0 = WorkflowPreferenceDto.from_dict(data)

            return all_type_0

        all_ = _parse_all_(d.pop("all"))

        channels = WorkflowPreferencesDtoChannels.from_dict(d.pop("channels"))

        workflow_preferences_dto = cls(
            all_=all_,
            channels=channels,
        )

        workflow_preferences_dto.additional_properties = d
        return workflow_preferences_dto

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
