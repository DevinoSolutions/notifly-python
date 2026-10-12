from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthDto")


@_attrs_define
class AuthDto:
    """
    Attributes:
        access_token (str):  Example: Workspace access token.
        refresh_token (str | Unset):  Example: Workspace refresh token.
        expires_at (str | Unset):  Example: 2026-06-15T12:00:00.000Z.
        refresh_token_expires_at (str | Unset):  Example: 2026-09-15T12:00:00.000Z.
    """

    access_token: str
    refresh_token: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    refresh_token_expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        expires_at = self.expires_at

        refresh_token_expires_at = self.refresh_token_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessToken": access_token,
            }
        )
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if refresh_token_expires_at is not UNSET:
            field_dict["refreshTokenExpiresAt"] = refresh_token_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("accessToken")

        refresh_token = d.pop("refreshToken", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        refresh_token_expires_at = d.pop("refreshTokenExpiresAt", UNSET)

        auth_dto = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at,
            refresh_token_expires_at=refresh_token_expires_at,
        )

        auth_dto.additional_properties = d
        return auth_dto

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
