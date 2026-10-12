from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type_enum import ChannelTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentIntegrationResponseIntegrationDto")


@_attrs_define
class AgentIntegrationResponseIntegrationDto:
    """
    Attributes:
        field_id (str): Integration document _id.
        identifier (str): The integration identifier (matches the integration store), not the internal MongoDB _id.
        name (str):
        provider_id (str):
        active (bool):
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
        shared_inbound_address (str | Unset): The Novu shared inbox address for this agent. Set whenever the cloud
            shared-inbox feature is enabled. The dashboard uses this as the headline inbound address and to render the
            shared inbox row in the inbox list.
        default_sender_name (str | Unset): Default email From display name for this agent (NovuAgent integrations only).
            Falls back to the agent name when not explicitly stored on the integration credentials.
        shared_inbox_disabled (bool | Unset): When true, the worker drops inbound mail addressed to this agent on the
            shared `agentconnect.sh` domain. Custom-domain routes still deliver. Meaningful on cloud-enabled NovuAgent
            integrations; on self-hosted it is set defensively at provisioning time and is effectively redundant.
    """

    field_id: str
    identifier: str
    name: str
    provider_id: str
    active: bool
    channel: ChannelTypeEnum | Unset = UNSET
    shared_inbound_address: str | Unset = UNSET
    default_sender_name: str | Unset = UNSET
    shared_inbox_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        identifier = self.identifier

        name = self.name

        provider_id = self.provider_id

        active = self.active

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        shared_inbound_address = self.shared_inbound_address

        default_sender_name = self.default_sender_name

        shared_inbox_disabled = self.shared_inbox_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "identifier": identifier,
                "name": name,
                "providerId": provider_id,
                "active": active,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel
        if shared_inbound_address is not UNSET:
            field_dict["sharedInboundAddress"] = shared_inbound_address
        if default_sender_name is not UNSET:
            field_dict["defaultSenderName"] = default_sender_name
        if shared_inbox_disabled is not UNSET:
            field_dict["sharedInboxDisabled"] = shared_inbox_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("_id")

        identifier = d.pop("identifier")

        name = d.pop("name")

        provider_id = d.pop("providerId")

        active = d.pop("active")

        _channel = d.pop("channel", UNSET)
        channel: ChannelTypeEnum | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = ChannelTypeEnum(_channel)

        shared_inbound_address = d.pop("sharedInboundAddress", UNSET)

        default_sender_name = d.pop("defaultSenderName", UNSET)

        shared_inbox_disabled = d.pop("sharedInboxDisabled", UNSET)

        agent_integration_response_integration_dto = cls(
            field_id=field_id,
            identifier=identifier,
            name=name,
            provider_id=provider_id,
            active=active,
            channel=channel,
            shared_inbound_address=shared_inbound_address,
            default_sender_name=default_sender_name,
            shared_inbox_disabled=shared_inbox_disabled,
        )

        agent_integration_response_integration_dto.additional_properties = d
        return agent_integration_response_integration_dto

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
