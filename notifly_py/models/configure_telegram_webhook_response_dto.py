from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigureTelegramWebhookResponseDto")


@_attrs_define
class ConfigureTelegramWebhookResponseDto:
    """
    Attributes:
        webhook_url (str): URL Notifly registered with Telegram for incoming updates
        configured_at (str): ISO-8601 timestamp the webhook was configured at
        bot_username (str): Resolved bot username from getMe
    """

    webhook_url: str
    configured_at: str
    bot_username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        configured_at = self.configured_at

        bot_username = self.bot_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhookUrl": webhook_url,
                "configuredAt": configured_at,
                "botUsername": bot_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl")

        configured_at = d.pop("configuredAt")

        bot_username = d.pop("botUsername")

        configure_telegram_webhook_response_dto = cls(
            webhook_url=webhook_url,
            configured_at=configured_at,
            bot_username=bot_username,
        )

        configure_telegram_webhook_response_dto.additional_properties = d
        return configure_telegram_webhook_response_dto

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
