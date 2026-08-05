from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelCredentials")


@_attrs_define
class ChannelCredentials:
    """
    Attributes:
        webhook_url (str | Unset): Webhook URL used by chat app integrations. The webhook should be obtained from the
            chat app provider. Example: https://example.com/webhook.
        channel (str | Unset): Channel specification for Mattermost chat notifications. Example: general.
        device_tokens (list[str] | Unset): Contains an array of the subscriber device tokens for a given provider. Used
            on Push integrations. Example: ['token1', 'token2', 'token3'].
        alert_uid (str | Unset): Alert UID for Grafana on-call webhook payload. Example: 12345-abcde.
        title (str | Unset): Title to be used with Grafana on-call webhook. Example: Critical Alert.
        image_url (str | Unset): Image URL property for Grafana on-call webhook. Example: https://example.com/image.png.
        state (str | Unset): State property for Grafana on-call webhook. Example: resolved.
        external_url (str | Unset): Link to upstream details property for Grafana on-call webhook. Example:
            https://example.com/details.
    """

    webhook_url: str | Unset = UNSET
    channel: str | Unset = UNSET
    device_tokens: list[str] | Unset = UNSET
    alert_uid: str | Unset = UNSET
    title: str | Unset = UNSET
    image_url: str | Unset = UNSET
    state: str | Unset = UNSET
    external_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        channel = self.channel

        device_tokens: list[str] | Unset = UNSET
        if not isinstance(self.device_tokens, Unset):
            device_tokens = self.device_tokens

        alert_uid = self.alert_uid

        title = self.title

        image_url = self.image_url

        state = self.state

        external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if channel is not UNSET:
            field_dict["channel"] = channel
        if device_tokens is not UNSET:
            field_dict["deviceTokens"] = device_tokens
        if alert_uid is not UNSET:
            field_dict["alertUid"] = alert_uid
        if title is not UNSET:
            field_dict["title"] = title
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if state is not UNSET:
            field_dict["state"] = state
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl", UNSET)

        channel = d.pop("channel", UNSET)

        device_tokens = cast(list[str], d.pop("deviceTokens", UNSET))

        alert_uid = d.pop("alertUid", UNSET)

        title = d.pop("title", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        state = d.pop("state", UNSET)

        external_url = d.pop("externalUrl", UNSET)

        channel_credentials = cls(
            webhook_url=webhook_url,
            channel=channel,
            device_tokens=device_tokens,
            alert_uid=alert_uid,
            title=title,
            image_url=image_url,
            state=state,
            external_url=external_url,
        )

        channel_credentials.additional_properties = d
        return channel_credentials

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
