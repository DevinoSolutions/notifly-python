from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_preference_channels_dto import PatchPreferenceChannelsDto


T = TypeVar("T", bound="BulkUpdateSubscriberPreferenceItemDto")


@_attrs_define
class BulkUpdateSubscriberPreferenceItemDto:
    """
    Attributes:
        channels (PatchPreferenceChannelsDto):
        workflow_id (str): Workflow internal _id, identifier or slug
    """

    channels: PatchPreferenceChannelsDto
    workflow_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = self.channels.to_dict()

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channels": channels,
                "workflowId": workflow_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_preference_channels_dto import PatchPreferenceChannelsDto

        d = dict(src_dict)
        channels = PatchPreferenceChannelsDto.from_dict(d.pop("channels"))

        workflow_id = d.pop("workflowId")

        bulk_update_subscriber_preference_item_dto = cls(
            channels=channels,
            workflow_id=workflow_id,
        )

        bulk_update_subscriber_preference_item_dto.additional_properties = d
        return bulk_update_subscriber_preference_item_dto

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
