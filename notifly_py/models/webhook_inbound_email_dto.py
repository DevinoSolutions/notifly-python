from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_inbound_email_domain_dto import WebhookInboundEmailDomainDto
    from ..models.webhook_inbound_email_mail_dto import WebhookInboundEmailMailDto
    from ..models.webhook_inbound_email_route_dto import WebhookInboundEmailRouteDto


T = TypeVar("T", bound="WebhookInboundEmailDto")


@_attrs_define
class WebhookInboundEmailDto:
    """
    Attributes:
        domain (WebhookInboundEmailDomainDto):
        mail (WebhookInboundEmailMailDto):
        route (WebhookInboundEmailRouteDto | Unset):
    """

    domain: WebhookInboundEmailDomainDto
    mail: WebhookInboundEmailMailDto
    route: WebhookInboundEmailRouteDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain.to_dict()

        mail = self.mail.to_dict()

        route: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "mail": mail,
            }
        )
        if route is not UNSET:
            field_dict["route"] = route

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_inbound_email_domain_dto import WebhookInboundEmailDomainDto
        from ..models.webhook_inbound_email_mail_dto import WebhookInboundEmailMailDto
        from ..models.webhook_inbound_email_route_dto import WebhookInboundEmailRouteDto

        d = dict(src_dict)
        domain = WebhookInboundEmailDomainDto.from_dict(d.pop("domain"))

        mail = WebhookInboundEmailMailDto.from_dict(d.pop("mail"))

        _route = d.pop("route", UNSET)
        route: WebhookInboundEmailRouteDto | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = WebhookInboundEmailRouteDto.from_dict(_route)

        webhook_inbound_email_dto = cls(
            domain=domain,
            mail=mail,
            route=route,
        )

        webhook_inbound_email_dto.additional_properties = d
        return webhook_inbound_email_dto

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
