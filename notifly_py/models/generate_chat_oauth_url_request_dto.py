from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_chat_oauth_url_request_dto_connection_mode import GenerateChatOauthUrlRequestDtoConnectionMode
from ..models.generate_chat_oauth_url_request_dto_mode import GenerateChatOauthUrlRequestDtoMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_chat_oauth_url_request_dto_context import GenerateChatOauthUrlRequestDtoContext


T = TypeVar("T", bound="GenerateChatOauthUrlRequestDto")


@_attrs_define
class GenerateChatOauthUrlRequestDto:
    """
    Attributes:
        integration_identifier (str): Integration identifier
        subscriber_id (str | Unset): The subscriber ID to link the channel connection to. For Slack: Required for
            incoming webhook endpoints, optional for workspace connections. For MS Teams: Optional. Admin consent is tenant-
            wide and can be associated with a subscriber for organizational purposes. Example: subscriber-123.
        connection_identifier (str | Unset): Identifier of the channel connection that will be created. It is generated
            automatically if not provided. Example: slack-connection-abc123.
        context (GenerateChatOauthUrlRequestDtoContext | Unset):
        scope (list[str] | Unset): **Slack only**: OAuth scopes to request during authorization. These define the
            permissions your Slack integration will have. If not specified, default scopes will be used: chat:write,
            chat:write.public, channels:read, groups:read, users:read, users:read.email. **MS Teams**: This parameter is
            ignored. MS Teams uses admin consent with pre-configured permissions in Azure AD. Note: The generated OAuth URL
            expires after 5 minutes. Example: ['chat:write', 'chat:write.public', 'channels:read', 'groups:read',
            'users:read', 'users:read.email', 'incoming-webhook'].
        user_scope (list[str] | Unset): **Slack only, link_user mode**: User-level OAuth scopes to request during
            authorization. Used when mode is "link_user" to identify the Slack user via "Sign in with Slack". If not
            specified, defaults to: identity.basic. Example: ['identity.basic'].
        mode (GenerateChatOauthUrlRequestDtoMode | Unset): OAuth flow mode. Use "connect" (default) to create a
            workspace channel connection, or "link_user" to identify the subscriber's Slack user ID without creating a
            connection. Example: link_user.
        connection_mode (GenerateChatOauthUrlRequestDtoConnectionMode | Unset): Connection mode that determines how the
            channel connection is scoped. Use "subscriber" (default) to associate the connection with a specific subscriber.
            Use "shared" to associate the connection with a context instead of a subscriber — subscriberId will not be
            stored on the connection. Example: shared.
        auto_link_user (bool | Unset): When true, after the workspace/tenant connection is created the OAuth flow also
            links the subscriber who clicked "Connect" as a personal endpoint. For Slack, this uses the authed_user.id
            already returned by oauth.v2.access — no extra redirect. For MS Teams, this triggers a second OAuth redirect for
            delegated user-identity consent. Defaults to false when omitted; the SlackConnectButton and MsTeamsConnectButton
            SDK components default this to true. Example: True.
    """

    integration_identifier: str
    subscriber_id: str | Unset = UNSET
    connection_identifier: str | Unset = UNSET
    context: GenerateChatOauthUrlRequestDtoContext | Unset = UNSET
    scope: list[str] | Unset = UNSET
    user_scope: list[str] | Unset = UNSET
    mode: GenerateChatOauthUrlRequestDtoMode | Unset = UNSET
    connection_mode: GenerateChatOauthUrlRequestDtoConnectionMode | Unset = UNSET
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

        user_scope: list[str] | Unset = UNSET
        if not isinstance(self.user_scope, Unset):
            user_scope = self.user_scope

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

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
        if user_scope is not UNSET:
            field_dict["userScope"] = user_scope
        if mode is not UNSET:
            field_dict["mode"] = mode
        if connection_mode is not UNSET:
            field_dict["connectionMode"] = connection_mode
        if auto_link_user is not UNSET:
            field_dict["autoLinkUser"] = auto_link_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_chat_oauth_url_request_dto_context import GenerateChatOauthUrlRequestDtoContext

        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier")

        subscriber_id = d.pop("subscriberId", UNSET)

        connection_identifier = d.pop("connectionIdentifier", UNSET)

        _context = d.pop("context", UNSET)
        context: GenerateChatOauthUrlRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = GenerateChatOauthUrlRequestDtoContext.from_dict(_context)

        scope = cast(list[str], d.pop("scope", UNSET))

        user_scope = cast(list[str], d.pop("userScope", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: GenerateChatOauthUrlRequestDtoMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GenerateChatOauthUrlRequestDtoMode(_mode)

        _connection_mode = d.pop("connectionMode", UNSET)
        connection_mode: GenerateChatOauthUrlRequestDtoConnectionMode | Unset
        if isinstance(_connection_mode, Unset):
            connection_mode = UNSET
        else:
            connection_mode = GenerateChatOauthUrlRequestDtoConnectionMode(_connection_mode)

        auto_link_user = d.pop("autoLinkUser", UNSET)

        generate_chat_oauth_url_request_dto = cls(
            integration_identifier=integration_identifier,
            subscriber_id=subscriber_id,
            connection_identifier=connection_identifier,
            context=context,
            scope=scope,
            user_scope=user_scope,
            mode=mode,
            connection_mode=connection_mode,
            auto_link_user=auto_link_user,
        )

        generate_chat_oauth_url_request_dto.additional_properties = d
        return generate_chat_oauth_url_request_dto

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
