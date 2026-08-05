from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_telegram_chat_endpoint_dto_type import CreateTelegramChatEndpointDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_telegram_chat_endpoint_dto_context import CreateTelegramChatEndpointDtoContext
    from ..models.telegram_chat_endpoint_dto import TelegramChatEndpointDto


T = TypeVar("T", bound="CreateTelegramChatEndpointDto")


@_attrs_define
class CreateTelegramChatEndpointDto:
    """
    Attributes:
        subscriber_id (str): The subscriber ID to which the channel endpoint is linked Example: subscriber-123.
        integration_identifier (str): The identifier of the integration to use for this channel endpoint. Example:
            slack-prod.
        type_ (CreateTelegramChatEndpointDtoType): Type of channel endpoint Example: telegram_chat.
        endpoint (TelegramChatEndpointDto):
        identifier (str | Unset): The unique identifier for the channel endpoint. If not provided, one will be generated
            automatically. Example: slack-channel-user123-abc4.
        context (CreateTelegramChatEndpointDtoContext | Unset):
        connection_identifier (str | Unset): The identifier of the channel connection to use for this channel endpoint.
            Example: slack-connection-abc123.
    """

    subscriber_id: str
    integration_identifier: str
    type_: CreateTelegramChatEndpointDtoType
    endpoint: TelegramChatEndpointDto
    identifier: str | Unset = UNSET
    context: CreateTelegramChatEndpointDtoContext | Unset = UNSET
    connection_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriber_id = self.subscriber_id

        integration_identifier = self.integration_identifier

        type_ = self.type_.value

        endpoint = self.endpoint.to_dict()

        identifier = self.identifier

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        connection_identifier = self.connection_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriberId": subscriber_id,
                "integrationIdentifier": integration_identifier,
                "type": type_,
                "endpoint": endpoint,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if context is not UNSET:
            field_dict["context"] = context
        if connection_identifier is not UNSET:
            field_dict["connectionIdentifier"] = connection_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_telegram_chat_endpoint_dto_context import CreateTelegramChatEndpointDtoContext
        from ..models.telegram_chat_endpoint_dto import TelegramChatEndpointDto

        d = dict(src_dict)
        subscriber_id = d.pop("subscriberId")

        integration_identifier = d.pop("integrationIdentifier")

        type_ = CreateTelegramChatEndpointDtoType(d.pop("type"))

        endpoint = TelegramChatEndpointDto.from_dict(d.pop("endpoint"))

        identifier = d.pop("identifier", UNSET)

        _context = d.pop("context", UNSET)
        context: CreateTelegramChatEndpointDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = CreateTelegramChatEndpointDtoContext.from_dict(_context)

        connection_identifier = d.pop("connectionIdentifier", UNSET)

        create_telegram_chat_endpoint_dto = cls(
            subscriber_id=subscriber_id,
            integration_identifier=integration_identifier,
            type_=type_,
            endpoint=endpoint,
            identifier=identifier,
            context=context,
            connection_identifier=connection_identifier,
        )

        create_telegram_chat_endpoint_dto.additional_properties = d
        return create_telegram_chat_endpoint_dto

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
