from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowPreferenceDto")


@_attrs_define
class WorkflowPreferenceDto:
    """
    Attributes:
        enabled (bool): A flag specifying if notification delivery is enabled for the workflow. If true, notification
            delivery is enabled by default for all channels. This setting can be overridden by the channel preferences.
            Default: True.
        read_only (bool): A flag specifying if the preference is read-only. If true, the preference cannot be changed by
            the Subscriber. Default: False.
    """

    enabled: bool = True
    read_only: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "readOnly": read_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        read_only = d.pop("readOnly")

        workflow_preference_dto = cls(
            enabled=enabled,
            read_only=read_only,
        )

        workflow_preference_dto.additional_properties = d
        return workflow_preference_dto

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
