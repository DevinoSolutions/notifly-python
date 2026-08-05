from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_channel_endpoint_response_dto_channel import GetChannelEndpointResponseDtoChannel
from ..models.get_channel_endpoint_response_dto_provider_id import GetChannelEndpointResponseDtoProviderId
from ..models.get_channel_endpoint_response_dto_type import GetChannelEndpointResponseDtoType

if TYPE_CHECKING:
    from ..models.ms_teams_channel_endpoint_dto import MsTeamsChannelEndpointDto
    from ..models.ms_teams_user_endpoint_dto import MsTeamsUserEndpointDto
    from ..models.phone_endpoint_dto import PhoneEndpointDto
    from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
    from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
    from ..models.telegram_chat_endpoint_dto import TelegramChatEndpointDto
    from ..models.webhook_endpoint_dto import WebhookEndpointDto


T = TypeVar("T", bound="GetChannelEndpointResponseDto")


@_attrs_define
class GetChannelEndpointResponseDto:
    """
    Attributes:
        identifier (str): The unique identifier of the channel endpoint.
        channel (GetChannelEndpointResponseDtoChannel): The channel type (email, sms, push, chat, etc.).
        provider_id (GetChannelEndpointResponseDtoProviderId): The provider identifier (e.g., sendgrid, twilio, slack,
            etc.). Example: slack.
        integration_identifier (None | str): The identifier of the integration to use for this channel endpoint.
            Example: slack-prod.
        connection_identifier (None | str): The identifier of the channel connection used for this endpoint. Example:
            slack-connection-abc123.
        subscriber_id (None | str): The subscriber ID to which the channel endpoint is linked Example: subscriber-123.
        context_keys (list[str]): The context of the channel connection Example: ['tenant:org-123', 'region:us-east-1'].
        type_ (GetChannelEndpointResponseDtoType): Type of channel endpoint Example: slack_channel.
        endpoint (MsTeamsChannelEndpointDto | MsTeamsUserEndpointDto | PhoneEndpointDto | SlackChannelEndpointDto |
            SlackUserEndpointDto | TelegramChatEndpointDto | WebhookEndpointDto): Endpoint data specific to the channel type
        created_at (str): The timestamp indicating when the channel endpoint was created, in ISO 8601 format.
        updated_at (str): The timestamp indicating when the channel endpoint was last updated, in ISO 8601 format.
    """

    identifier: str
    channel: GetChannelEndpointResponseDtoChannel
    provider_id: GetChannelEndpointResponseDtoProviderId
    integration_identifier: None | str
    connection_identifier: None | str
    subscriber_id: None | str
    context_keys: list[str]
    type_: GetChannelEndpointResponseDtoType
    endpoint: (
        MsTeamsChannelEndpointDto
        | MsTeamsUserEndpointDto
        | PhoneEndpointDto
        | SlackChannelEndpointDto
        | SlackUserEndpointDto
        | TelegramChatEndpointDto
        | WebhookEndpointDto
    )
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ms_teams_channel_endpoint_dto import MsTeamsChannelEndpointDto
        from ..models.ms_teams_user_endpoint_dto import MsTeamsUserEndpointDto
        from ..models.phone_endpoint_dto import PhoneEndpointDto
        from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
        from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
        from ..models.webhook_endpoint_dto import WebhookEndpointDto

        identifier = self.identifier

        channel = self.channel.value

        provider_id = self.provider_id.value

        integration_identifier: None | str
        integration_identifier = self.integration_identifier

        connection_identifier: None | str
        connection_identifier = self.connection_identifier

        subscriber_id: None | str
        subscriber_id = self.subscriber_id

        context_keys = self.context_keys

        type_ = self.type_.value

        endpoint: dict[str, Any]
        if isinstance(self.endpoint, SlackChannelEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, SlackUserEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, WebhookEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, PhoneEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, MsTeamsChannelEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, MsTeamsUserEndpointDto):
            endpoint = self.endpoint.to_dict()
        else:
            endpoint = self.endpoint.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "channel": channel,
                "providerId": provider_id,
                "integrationIdentifier": integration_identifier,
                "connectionIdentifier": connection_identifier,
                "subscriberId": subscriber_id,
                "contextKeys": context_keys,
                "type": type_,
                "endpoint": endpoint,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ms_teams_channel_endpoint_dto import MsTeamsChannelEndpointDto
        from ..models.ms_teams_user_endpoint_dto import MsTeamsUserEndpointDto
        from ..models.phone_endpoint_dto import PhoneEndpointDto
        from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
        from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
        from ..models.telegram_chat_endpoint_dto import TelegramChatEndpointDto
        from ..models.webhook_endpoint_dto import WebhookEndpointDto

        d = dict(src_dict)
        identifier = d.pop("identifier")

        channel = GetChannelEndpointResponseDtoChannel(d.pop("channel"))

        provider_id = GetChannelEndpointResponseDtoProviderId(d.pop("providerId"))

        def _parse_integration_identifier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        integration_identifier = _parse_integration_identifier(d.pop("integrationIdentifier"))

        def _parse_connection_identifier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connection_identifier = _parse_connection_identifier(d.pop("connectionIdentifier"))

        def _parse_subscriber_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subscriber_id = _parse_subscriber_id(d.pop("subscriberId"))

        context_keys = cast(list[str], d.pop("contextKeys"))

        type_ = GetChannelEndpointResponseDtoType(d.pop("type"))

        def _parse_endpoint(
            data: object,
        ) -> (
            MsTeamsChannelEndpointDto
            | MsTeamsUserEndpointDto
            | PhoneEndpointDto
            | SlackChannelEndpointDto
            | SlackUserEndpointDto
            | TelegramChatEndpointDto
            | WebhookEndpointDto
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_0 = SlackChannelEndpointDto.from_dict(data)

                return endpoint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_1 = SlackUserEndpointDto.from_dict(data)

                return endpoint_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_2 = WebhookEndpointDto.from_dict(data)

                return endpoint_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_3 = PhoneEndpointDto.from_dict(data)

                return endpoint_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_4 = MsTeamsChannelEndpointDto.from_dict(data)

                return endpoint_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_5 = MsTeamsUserEndpointDto.from_dict(data)

                return endpoint_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            endpoint_type_6 = TelegramChatEndpointDto.from_dict(data)

            return endpoint_type_6

        endpoint = _parse_endpoint(d.pop("endpoint"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_channel_endpoint_response_dto = cls(
            identifier=identifier,
            channel=channel,
            provider_id=provider_id,
            integration_identifier=integration_identifier,
            connection_identifier=connection_identifier,
            subscriber_id=subscriber_id,
            context_keys=context_keys,
            type_=type_,
            endpoint=endpoint,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_channel_endpoint_response_dto.additional_properties = d
        return get_channel_endpoint_response_dto

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
