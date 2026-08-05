from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_channel_connection_response_dto_channel import GetChannelConnectionResponseDtoChannel
from ..models.get_channel_connection_response_dto_provider_id import GetChannelConnectionResponseDtoProviderId

if TYPE_CHECKING:
    from ..models.auth_dto import AuthDto
    from ..models.workspace_dto import WorkspaceDto


T = TypeVar("T", bound="GetChannelConnectionResponseDto")


@_attrs_define
class GetChannelConnectionResponseDto:
    """
    Attributes:
        identifier (str): The unique identifier of the channel endpoint.
        channel (GetChannelConnectionResponseDtoChannel): The channel type (email, sms, push, chat, etc.).
        provider_id (GetChannelConnectionResponseDtoProviderId): The provider identifier (e.g., sendgrid, twilio, slack,
            etc.). Example: slack.
        integration_identifier (None | str): The identifier of the integration to use for this channel endpoint.
            Example: slack-prod.
        subscriber_id (None | str): The subscriber ID to which the channel connection is linked Example: subscriber-123.
        context_keys (list[str]): The context of the channel connection Example: ['tenant:org-123', 'region:us-east-1'].
        workspace (WorkspaceDto):
        auth (AuthDto):
        created_at (str): The timestamp indicating when the channel endpoint was created, in ISO 8601 format.
        updated_at (str): The timestamp indicating when the channel endpoint was last updated, in ISO 8601 format.
    """

    identifier: str
    channel: GetChannelConnectionResponseDtoChannel
    provider_id: GetChannelConnectionResponseDtoProviderId
    integration_identifier: None | str
    subscriber_id: None | str
    context_keys: list[str]
    workspace: WorkspaceDto
    auth: AuthDto
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        channel = self.channel.value

        provider_id = self.provider_id.value

        integration_identifier: None | str
        integration_identifier = self.integration_identifier

        subscriber_id: None | str
        subscriber_id = self.subscriber_id

        context_keys = self.context_keys

        workspace = self.workspace.to_dict()

        auth = self.auth.to_dict()

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
                "subscriberId": subscriber_id,
                "contextKeys": context_keys,
                "workspace": workspace,
                "auth": auth,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_dto import AuthDto
        from ..models.workspace_dto import WorkspaceDto

        d = dict(src_dict)
        identifier = d.pop("identifier")

        channel = GetChannelConnectionResponseDtoChannel(d.pop("channel"))

        provider_id = GetChannelConnectionResponseDtoProviderId(d.pop("providerId"))

        def _parse_integration_identifier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        integration_identifier = _parse_integration_identifier(d.pop("integrationIdentifier"))

        def _parse_subscriber_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subscriber_id = _parse_subscriber_id(d.pop("subscriberId"))

        context_keys = cast(list[str], d.pop("contextKeys"))

        workspace = WorkspaceDto.from_dict(d.pop("workspace"))

        auth = AuthDto.from_dict(d.pop("auth"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_channel_connection_response_dto = cls(
            identifier=identifier,
            channel=channel,
            provider_id=provider_id,
            integration_identifier=integration_identifier,
            subscriber_id=subscriber_id,
            context_keys=context_keys,
            workspace=workspace,
            auth=auth,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_channel_connection_response_dto.additional_properties = d
        return get_channel_connection_response_dto

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
