from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_or_push_provider_enum import ChatOrPushProviderEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_credentials import ChannelCredentials


T = TypeVar("T", bound="ChannelSettingsDto")


@_attrs_define
class ChannelSettingsDto:
    """
    Attributes:
        provider_id (ChatOrPushProviderEnum): The provider identifier for the credentials
        credentials (ChannelCredentials):
        field_integration_id (str): The unique identifier of the integration associated with this channel.
        integration_identifier (str | Unset): The integration identifier
    """

    provider_id: ChatOrPushProviderEnum
    credentials: ChannelCredentials
    field_integration_id: str
    integration_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id.value

        credentials = self.credentials.to_dict()

        field_integration_id = self.field_integration_id

        integration_identifier = self.integration_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "credentials": credentials,
                "_integrationId": field_integration_id,
            }
        )
        if integration_identifier is not UNSET:
            field_dict["integrationIdentifier"] = integration_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_credentials import ChannelCredentials

        d = dict(src_dict)
        provider_id = ChatOrPushProviderEnum(d.pop("providerId"))

        credentials = ChannelCredentials.from_dict(d.pop("credentials"))

        field_integration_id = d.pop("_integrationId")

        integration_identifier = d.pop("integrationIdentifier", UNSET)

        channel_settings_dto = cls(
            provider_id=provider_id,
            credentials=credentials,
            field_integration_id=field_integration_id,
            integration_identifier=integration_identifier,
        )

        channel_settings_dto.additional_properties = d
        return channel_settings_dto

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
