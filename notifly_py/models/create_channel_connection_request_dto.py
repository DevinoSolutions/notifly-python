from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_channel_connection_request_dto_connection_mode import (
    CreateChannelConnectionRequestDtoConnectionMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_dto import AuthDto
    from ..models.create_channel_connection_request_dto_context import CreateChannelConnectionRequestDtoContext
    from ..models.workspace_dto import WorkspaceDto


T = TypeVar("T", bound="CreateChannelConnectionRequestDto")


@_attrs_define
class CreateChannelConnectionRequestDto:
    """
    Attributes:
        integration_identifier (str): The identifier of the integration to use for this channel connection. Example:
            slack-prod.
        workspace (WorkspaceDto):
        auth (AuthDto):
        identifier (str | Unset): The unique identifier for the channel connection. If not provided, one will be
            generated automatically. Example: slack-prod-user123-abc4.
        subscriber_id (str | Unset): The subscriber ID to link the channel connection to Example: subscriber-123.
        context (CreateChannelConnectionRequestDtoContext | Unset):
        connection_mode (CreateChannelConnectionRequestDtoConnectionMode | Unset): Connection mode that determines how
            the channel connection is scoped. Use "subscriber" (default) to associate the connection with a specific
            subscriber. Use "shared" to associate the connection with a context instead of a subscriber — subscriberId will
            not be stored on the connection. Example: shared.
    """

    integration_identifier: str
    workspace: WorkspaceDto
    auth: AuthDto
    identifier: str | Unset = UNSET
    subscriber_id: str | Unset = UNSET
    context: CreateChannelConnectionRequestDtoContext | Unset = UNSET
    connection_mode: CreateChannelConnectionRequestDtoConnectionMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_identifier = self.integration_identifier

        workspace = self.workspace.to_dict()

        auth = self.auth.to_dict()

        identifier = self.identifier

        subscriber_id = self.subscriber_id

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        connection_mode: str | Unset = UNSET
        if not isinstance(self.connection_mode, Unset):
            connection_mode = self.connection_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrationIdentifier": integration_identifier,
                "workspace": workspace,
                "auth": auth,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id
        if context is not UNSET:
            field_dict["context"] = context
        if connection_mode is not UNSET:
            field_dict["connectionMode"] = connection_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_dto import AuthDto
        from ..models.create_channel_connection_request_dto_context import CreateChannelConnectionRequestDtoContext
        from ..models.workspace_dto import WorkspaceDto

        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier")

        workspace = WorkspaceDto.from_dict(d.pop("workspace"))

        auth = AuthDto.from_dict(d.pop("auth"))

        identifier = d.pop("identifier", UNSET)

        subscriber_id = d.pop("subscriberId", UNSET)

        _context = d.pop("context", UNSET)
        context: CreateChannelConnectionRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = CreateChannelConnectionRequestDtoContext.from_dict(_context)

        _connection_mode = d.pop("connectionMode", UNSET)
        connection_mode: CreateChannelConnectionRequestDtoConnectionMode | Unset
        if isinstance(_connection_mode, Unset):
            connection_mode = UNSET
        else:
            connection_mode = CreateChannelConnectionRequestDtoConnectionMode(_connection_mode)

        create_channel_connection_request_dto = cls(
            integration_identifier=integration_identifier,
            workspace=workspace,
            auth=auth,
            identifier=identifier,
            subscriber_id=subscriber_id,
            context=context,
            connection_mode=connection_mode,
        )

        create_channel_connection_request_dto.additional_properties = d
        return create_channel_connection_request_dto

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
