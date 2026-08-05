from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_connect_oauth_url_request_dto_connection_mode import (
    GenerateConnectOauthUrlRequestDtoConnectionMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_connect_oauth_url_request_dto_context import GenerateConnectOauthUrlRequestDtoContext


T = TypeVar("T", bound="GenerateConnectOauthUrlRequestDto")


@_attrs_define
class GenerateConnectOauthUrlRequestDto:
    """
    Attributes:
        integration_identifier (str): Integration identifier
        subscriber_id (str | Unset): The subscriber ID to associate with the channel connection. For Slack: optional for
            workspace connections (required only for incoming-webhook scope). For MS Teams: optional. Admin consent is
            tenant-wide. Example: subscriber-123.
        connection_identifier (str | Unset): Identifier of the channel connection that will be created. Generated
            automatically if not provided. Example: slack-connection-abc123.
        context (GenerateConnectOauthUrlRequestDtoContext | Unset):
        scope (list[str] | Unset): **Slack only**: OAuth scopes to request during authorization. If not specified,
            default scopes will be used: chat:write, chat:write.public, channels:read, groups:read, users:read,
            users:read.email. **MS Teams**: ignored — uses admin consent with pre-configured Azure AD permissions. Example:
            ['chat:write', 'chat:write.public', 'channels:read'].
        connection_mode (GenerateConnectOauthUrlRequestDtoConnectionMode | Unset): Connection mode that determines how
            the channel connection is scoped. "subscriber" (default) associates the connection with a specific subscriber.
            "shared" associates the connection with a context instead of a subscriber. Example: shared.
        auto_link_user (bool | Unset): When true (default when connectionMode is "subscriber"), after the
            workspace/tenant connection is created the OAuth flow also links the subscriber who clicked "Connect" as a
            personal endpoint. For Slack, uses the authed_user.id returned by oauth.v2.access — no extra redirect. For MS
            Teams, triggers a second OAuth redirect for delegated user-identity consent. Set to false to only create the
            workspace connection without linking the individual user. Example: True.
    """

    integration_identifier: str
    subscriber_id: str | Unset = UNSET
    connection_identifier: str | Unset = UNSET
    context: GenerateConnectOauthUrlRequestDtoContext | Unset = UNSET
    scope: list[str] | Unset = UNSET
    connection_mode: GenerateConnectOauthUrlRequestDtoConnectionMode | Unset = UNSET
    auto_link_user: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_identifier = self.integration_identifier

        subscriber_id = self.subscriber_id

        connection_identifier = self.connection_identifier

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        scope: list[str] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        connection_mode: str | Unset = UNSET
        if not isinstance(self.connection_mode, Unset):
            connection_mode = self.connection_mode.value

        auto_link_user = self.auto_link_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrationIdentifier": integration_identifier,
            }
        )
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id
        if connection_identifier is not UNSET:
            field_dict["connectionIdentifier"] = connection_identifier
        if context is not UNSET:
            field_dict["context"] = context
        if scope is not UNSET:
            field_dict["scope"] = scope
        if connection_mode is not UNSET:
            field_dict["connectionMode"] = connection_mode
        if auto_link_user is not UNSET:
            field_dict["autoLinkUser"] = auto_link_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_connect_oauth_url_request_dto_context import GenerateConnectOauthUrlRequestDtoContext

        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier")

        subscriber_id = d.pop("subscriberId", UNSET)

        connection_identifier = d.pop("connectionIdentifier", UNSET)

        _context = d.pop("context", UNSET)
        context: GenerateConnectOauthUrlRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = GenerateConnectOauthUrlRequestDtoContext.from_dict(_context)

        scope = cast(list[str], d.pop("scope", UNSET))

        _connection_mode = d.pop("connectionMode", UNSET)
        connection_mode: GenerateConnectOauthUrlRequestDtoConnectionMode | Unset
        if isinstance(_connection_mode, Unset):
            connection_mode = UNSET
        else:
            connection_mode = GenerateConnectOauthUrlRequestDtoConnectionMode(_connection_mode)

        auto_link_user = d.pop("autoLinkUser", UNSET)

        generate_connect_oauth_url_request_dto = cls(
            integration_identifier=integration_identifier,
            subscriber_id=subscriber_id,
            connection_identifier=connection_identifier,
            context=context,
            scope=scope,
            connection_mode=connection_mode,
            auto_link_user=auto_link_user,
        )

        generate_connect_oauth_url_request_dto.additional_properties = d
        return generate_connect_oauth_url_request_dto

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
