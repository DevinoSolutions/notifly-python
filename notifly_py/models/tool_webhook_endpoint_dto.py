from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_webhook_endpoint_dto_method import ToolWebhookEndpointDtoMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_webhook_endpoint_dto_headers import ToolWebhookEndpointDtoHeaders


T = TypeVar("T", bound="ToolWebhookEndpointDto")


@_attrs_define
class ToolWebhookEndpointDto:
    """
    Attributes:
        url (str): Destination webhook URL (often a per-subscriber capability URL). Encrypted at rest on the channel
            endpoint (`endpoint` field). Example: https://example.com/tools/incoming.
        headers (ToolWebhookEndpointDtoHeaders | Unset): Optional headers (e.g. auth tokens) sent with every request to
            this webhook. Header values are encrypted at rest on the channel endpoint (`endpoint` field). Example:
            {'Authorization': 'Bearer <token>'}.
        method (ToolWebhookEndpointDtoMethod | Unset): Optional HTTP method override for this webhook. Defaults to the
            integration-level method. Example: POST.
    """

    url: str
    headers: ToolWebhookEndpointDtoHeaders | Unset = UNSET
    method: ToolWebhookEndpointDtoMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_webhook_endpoint_dto_headers import ToolWebhookEndpointDtoHeaders

        d = dict(src_dict)
        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: ToolWebhookEndpointDtoHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ToolWebhookEndpointDtoHeaders.from_dict(_headers)

        _method = d.pop("method", UNSET)
        method: ToolWebhookEndpointDtoMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ToolWebhookEndpointDtoMethod(_method)

        tool_webhook_endpoint_dto = cls(
            url=url,
            headers=headers,
            method=method,
        )

        tool_webhook_endpoint_dto.additional_properties = d
        return tool_webhook_endpoint_dto

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
