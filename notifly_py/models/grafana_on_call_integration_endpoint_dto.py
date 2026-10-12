from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrafanaOnCallIntegrationEndpointDto")


@_attrs_define
class GrafanaOnCallIntegrationEndpointDto:
    """
    Attributes:
        url (str): Grafana IRM/OnCall incoming-webhook (Formatted Webhook) integration URL. The routing secret is
            embedded in the URL path. Encrypted at rest on the channel endpoint (`endpoint` field). Example:
            https://acme.grafana.net/integrations/v1/formatted_webhook/m12xmIjOcgwH74UF8CN4dk0Dh/.
        auth_token (str | Unset): Optional Grafana service account bearer token, required when the integration enforces
            authenticated ingestion. Encrypted at rest on the channel endpoint (`endpoint` field). Example: glsa_abc123....
    """

    url: str
    auth_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        auth_token = self.auth_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        auth_token = d.pop("authToken", UNSET)

        grafana_on_call_integration_endpoint_dto = cls(
            url=url,
            auth_token=auth_token,
        )

        grafana_on_call_integration_endpoint_dto.additional_properties = d
        return grafana_on_call_integration_endpoint_dto

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
