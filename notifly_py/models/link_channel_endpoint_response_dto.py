from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_channel_endpoint_response_dto_provider_metadata import (
        LinkChannelEndpointResponseDtoProviderMetadata,
    )


T = TypeVar("T", bound="LinkChannelEndpointResponseDto")


@_attrs_define
class LinkChannelEndpointResponseDto:
    """
    Attributes:
        url (str): URL the subscriber opens to link their chat identity (OAuth URL or deep link) Example:
            https://t.me/MyBot?start=AbCdEfGhIjKlMnOpQrStUvWxYz012345.
        provider_metadata (LinkChannelEndpointResponseDtoProviderMetadata | Unset): Provider-specific metadata returned
            alongside the link URL Example: {'botUsername': 'MyBot', 'expiresAt': '2026-06-23T12:00:00.000Z'}.
    """

    url: str
    provider_metadata: LinkChannelEndpointResponseDtoProviderMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        provider_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_metadata, Unset):
            provider_metadata = self.provider_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if provider_metadata is not UNSET:
            field_dict["providerMetadata"] = provider_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_channel_endpoint_response_dto_provider_metadata import (
            LinkChannelEndpointResponseDtoProviderMetadata,
        )

        d = dict(src_dict)
        url = d.pop("url")

        _provider_metadata = d.pop("providerMetadata", UNSET)
        provider_metadata: LinkChannelEndpointResponseDtoProviderMetadata | Unset
        if isinstance(_provider_metadata, Unset):
            provider_metadata = UNSET
        else:
            provider_metadata = LinkChannelEndpointResponseDtoProviderMetadata.from_dict(_provider_metadata)

        link_channel_endpoint_response_dto = cls(
            url=url,
            provider_metadata=provider_metadata,
        )

        link_channel_endpoint_response_dto.additional_properties = d
        return link_channel_endpoint_response_dto

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
