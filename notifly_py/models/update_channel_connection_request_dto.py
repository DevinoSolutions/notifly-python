from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auth_dto import AuthDto
    from ..models.workspace_dto import WorkspaceDto


T = TypeVar("T", bound="UpdateChannelConnectionRequestDto")


@_attrs_define
class UpdateChannelConnectionRequestDto:
    """
    Attributes:
        workspace (WorkspaceDto):
        auth (AuthDto):
    """

    workspace: WorkspaceDto
    auth: AuthDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace = self.workspace.to_dict()

        auth = self.auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace": workspace,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_dto import AuthDto
        from ..models.workspace_dto import WorkspaceDto

        d = dict(src_dict)
        workspace = WorkspaceDto.from_dict(d.pop("workspace"))

        auth = AuthDto.from_dict(d.pop("auth"))

        update_channel_connection_request_dto = cls(
            workspace=workspace,
            auth=auth,
        )

        update_channel_connection_request_dto.additional_properties = d
        return update_channel_connection_request_dto

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
