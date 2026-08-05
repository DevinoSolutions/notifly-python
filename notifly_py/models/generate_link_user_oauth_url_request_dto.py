from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_link_user_oauth_url_request_dto_context import GenerateLinkUserOauthUrlRequestDtoContext


T = TypeVar("T", bound="GenerateLinkUserOauthUrlRequestDto")


@_attrs_define
class GenerateLinkUserOauthUrlRequestDto:
    """
    Attributes:
        subscriber_id (str): The subscriber ID to link to their chat identity. Required — this operation always binds a
            specific subscriber to a user identity in the chat provider. Example: subscriber-123.
        integration_identifier (str): Integration identifier
        connection_identifier (str | Unset): Identifier of the existing channel connection to associate this user
            endpoint with. Generated automatically if not provided. Example: slack-connection-abc123.
        context (GenerateLinkUserOauthUrlRequestDtoContext | Unset):
        user_scope (list[str] | Unset): **Slack only**: User-level OAuth scopes for "Sign in with Slack". Defaults to:
            identity.basic. **MS Teams**: ignored — uses delegated OpenID scopes (openid, profile, User.Read). Example:
            ['identity.basic'].
    """

    subscriber_id: str
    integration_identifier: str
    connection_identifier: str | Unset = UNSET
    context: GenerateLinkUserOauthUrlRequestDtoContext | Unset = UNSET
    user_scope: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriber_id = self.subscriber_id

        integration_identifier = self.integration_identifier

        connection_identifier = self.connection_identifier

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        user_scope: list[str] | Unset = UNSET
        if not isinstance(self.user_scope, Unset):
            user_scope = self.user_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriberId": subscriber_id,
                "integrationIdentifier": integration_identifier,
            }
        )
        if connection_identifier is not UNSET:
            field_dict["connectionIdentifier"] = connection_identifier
        if context is not UNSET:
            field_dict["context"] = context
        if user_scope is not UNSET:
            field_dict["userScope"] = user_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_link_user_oauth_url_request_dto_context import GenerateLinkUserOauthUrlRequestDtoContext

        d = dict(src_dict)
        subscriber_id = d.pop("subscriberId")

        integration_identifier = d.pop("integrationIdentifier")

        connection_identifier = d.pop("connectionIdentifier", UNSET)

        _context = d.pop("context", UNSET)
        context: GenerateLinkUserOauthUrlRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = GenerateLinkUserOauthUrlRequestDtoContext.from_dict(_context)

        user_scope = cast(list[str], d.pop("userScope", UNSET))

        generate_link_user_oauth_url_request_dto = cls(
            subscriber_id=subscriber_id,
            integration_identifier=integration_identifier,
            connection_identifier=connection_identifier,
            context=context,
            user_scope=user_scope,
        )

        generate_link_user_oauth_url_request_dto.additional_properties = d
        return generate_link_user_oauth_url_request_dto

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
