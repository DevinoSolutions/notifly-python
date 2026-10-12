from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentIntegrationSummaryDto")


@_attrs_define
class AgentIntegrationSummaryDto:
    """
    Attributes:
        integration_id (str): Integration document id.
        provider_id (str):
        name (str):
        identifier (str):
        active (bool):
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
    """

    integration_id: str
    provider_id: str
    name: str
    identifier: str
    active: bool
    channel: ChannelTypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_id = self.integration_id

        provider_id = self.provider_id

        name = self.name

        identifier = self.identifier

        active = self.active

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrationId": integration_id,
                "providerId": provider_id,
                "name": name,
                "identifier": identifier,
                "active": active,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integration_id = d.pop("integrationId")

        provider_id = d.pop("providerId")

        name = d.pop("name")

        identifier = d.pop("identifier")

        active = d.pop("active")

        _channel = d.pop("channel", UNSET)
        channel: ChannelTypeEnum | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = ChannelTypeEnum(_channel)

        agent_integration_summary_dto = cls(
            integration_id=integration_id,
            provider_id=provider_id,
            name=name,
            identifier=identifier,
            active=active,
            channel=channel,
        )

        agent_integration_summary_dto.additional_properties = d
        return agent_integration_summary_dto

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
