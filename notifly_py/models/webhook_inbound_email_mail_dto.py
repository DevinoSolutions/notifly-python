from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_inbound_email_address_dto import WebhookInboundEmailAddressDto


T = TypeVar("T", bound="WebhookInboundEmailMailDto")


@_attrs_define
class WebhookInboundEmailMailDto:
    """
    Attributes:
        from_ (WebhookInboundEmailAddressDto):
        to (list[WebhookInboundEmailAddressDto]): Recipient address info
        subject (str): Email subject
        message_id (str): Message ID header
        html (str | Unset): HTML body
        text (str | Unset): Plain text body
    """

    from_: WebhookInboundEmailAddressDto
    to: list[WebhookInboundEmailAddressDto]
    subject: str
    message_id: str
    html: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.to_dict()

        to = []
        for to_item_data in self.to:
            to_item = to_item_data.to_dict()
            to.append(to_item)

        subject = self.subject

        message_id = self.message_id

        html = self.html

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "subject": subject,
                "messageId": message_id,
            }
        )
        if html is not UNSET:
            field_dict["html"] = html
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_inbound_email_address_dto import WebhookInboundEmailAddressDto

        d = dict(src_dict)
        from_ = WebhookInboundEmailAddressDto.from_dict(d.pop("from"))

        to = []
        _to = d.pop("to")
        for to_item_data in _to:
            to_item = WebhookInboundEmailAddressDto.from_dict(to_item_data)

            to.append(to_item)

        subject = d.pop("subject")

        message_id = d.pop("messageId")

        html = d.pop("html", UNSET)

        text = d.pop("text", UNSET)

        webhook_inbound_email_mail_dto = cls(
            from_=from_,
            to=to,
            subject=subject,
            message_id=message_id,
            html=html,
            text=text,
        )

        webhook_inbound_email_mail_dto.additional_properties = d
        return webhook_inbound_email_mail_dto

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
