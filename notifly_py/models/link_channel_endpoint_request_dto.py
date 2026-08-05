from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LinkChannelEndpointRequestDto")


@_attrs_define
class LinkChannelEndpointRequestDto:
    """
    Attributes:
        integration_identifier (str): Integration identifier for the chat provider integration Example: telegram-bot.
        subscriber_id (str): External subscriber identifier to link to their chat identity Example: subscriber-123.
    """

    integration_identifier: str
    subscriber_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_identifier = self.integration_identifier

        subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrationIdentifier": integration_identifier,
                "subscriberId": subscriber_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier")

        subscriber_id = d.pop("subscriberId")

        link_channel_endpoint_request_dto = cls(
            integration_identifier=integration_identifier,
            subscriber_id=subscriber_id,
        )

        link_channel_endpoint_request_dto.additional_properties = d
        return link_channel_endpoint_request_dto

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
