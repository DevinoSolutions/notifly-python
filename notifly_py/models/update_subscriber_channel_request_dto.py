from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_or_push_provider_enum import ChatOrPushProviderEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_credentials import ChannelCredentials


T = TypeVar("T", bound="UpdateSubscriberChannelRequestDto")


@_attrs_define
class UpdateSubscriberChannelRequestDto:
    """
    Attributes:
        provider_id (ChatOrPushProviderEnum): The provider identifier for the credentials
        credentials (ChannelCredentials):
        integration_identifier (str | Unset): The integration identifier
    """

    provider_id: ChatOrPushProviderEnum
    credentials: ChannelCredentials
    integration_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id.value

        credentials = self.credentials.to_dict()

        integration_identifier = self.integration_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "credentials": credentials,
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

        integration_identifier = d.pop("integrationIdentifier", UNSET)

        update_subscriber_channel_request_dto = cls(
            provider_id=provider_id,
            credentials=credentials,
            integration_identifier=integration_identifier,
        )

        update_subscriber_channel_request_dto.additional_properties = d
        return update_subscriber_channel_request_dto

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
