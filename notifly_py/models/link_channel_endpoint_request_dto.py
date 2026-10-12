from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_channel_endpoint_request_dto_context import LinkChannelEndpointRequestDtoContext


T = TypeVar("T", bound="LinkChannelEndpointRequestDto")


@_attrs_define
class LinkChannelEndpointRequestDto:
    """
    Attributes:
        integration_identifier (str): Integration identifier for the chat provider integration Example: telegram-bot.
        subscriber_id (str): External subscriber identifier to link to their chat identity Example: subscriber-123.
        context (LinkChannelEndpointRequestDtoContext | Unset):
        context_hash (str | Unset): HMAC-SHA256 of the canonicalized `context`, signed with the tenant environment
            secret key (the same "Inbox with context" signing scheme). Required when the integration has HMAC validation
            enabled. Example: a1b2c3d4e5f6....
    """

    integration_identifier: str
    subscriber_id: str
    context: LinkChannelEndpointRequestDtoContext | Unset = UNSET
    context_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_identifier = self.integration_identifier

        subscriber_id = self.subscriber_id

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        context_hash = self.context_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrationIdentifier": integration_identifier,
                "subscriberId": subscriber_id,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if context_hash is not UNSET:
            field_dict["contextHash"] = context_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_channel_endpoint_request_dto_context import LinkChannelEndpointRequestDtoContext

        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier")

        subscriber_id = d.pop("subscriberId")

        _context = d.pop("context", UNSET)
        context: LinkChannelEndpointRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = LinkChannelEndpointRequestDtoContext.from_dict(_context)

        context_hash = d.pop("contextHash", UNSET)

        link_channel_endpoint_request_dto = cls(
            integration_identifier=integration_identifier,
            subscriber_id=subscriber_id,
            context=context,
            context_hash=context_hash,
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
