from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IssueTelegramMobileLinkResponseDto")


@_attrs_define
class IssueTelegramMobileLinkResponseDto:
    """
    Attributes:
        token (str): Opaque, single-use token identifying this Telegram mobile-setup session
        url (str): Absolute URL the user can open on a mobile device to complete Telegram setup
        expires_at (str): ISO-8601 timestamp at which the token expires
    """

    token: str
    url: str
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        url = self.url

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "url": url,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        url = d.pop("url")

        expires_at = d.pop("expiresAt")

        issue_telegram_mobile_link_response_dto = cls(
            token=token,
            url=url,
            expires_at=expires_at,
        )

        issue_telegram_mobile_link_response_dto.additional_properties = d
        return issue_telegram_mobile_link_response_dto

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
