from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.phone_endpoint_dto import PhoneEndpointDto
    from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
    from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
    from ..models.webhook_endpoint_dto import WebhookEndpointDto


T = TypeVar("T", bound="UpdateChannelEndpointRequestDto")


@_attrs_define
class UpdateChannelEndpointRequestDto:
    """
    Attributes:
        endpoint (PhoneEndpointDto | SlackChannelEndpointDto | SlackUserEndpointDto | WebhookEndpointDto): Updated
            endpoint data. The structure must match the existing channel endpoint type.
    """

    endpoint: PhoneEndpointDto | SlackChannelEndpointDto | SlackUserEndpointDto | WebhookEndpointDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
        from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
        from ..models.webhook_endpoint_dto import WebhookEndpointDto

        endpoint: dict[str, Any]
        if isinstance(self.endpoint, SlackChannelEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, SlackUserEndpointDto):
            endpoint = self.endpoint.to_dict()
        elif isinstance(self.endpoint, WebhookEndpointDto):
            endpoint = self.endpoint.to_dict()
        else:
            endpoint = self.endpoint.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_endpoint_dto import PhoneEndpointDto
        from ..models.slack_channel_endpoint_dto import SlackChannelEndpointDto
        from ..models.slack_user_endpoint_dto import SlackUserEndpointDto
        from ..models.webhook_endpoint_dto import WebhookEndpointDto

        d = dict(src_dict)

        def _parse_endpoint(
            data: object,
        ) -> PhoneEndpointDto | SlackChannelEndpointDto | SlackUserEndpointDto | WebhookEndpointDto:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_0 = SlackChannelEndpointDto.from_dict(data)

                return endpoint_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_1 = SlackUserEndpointDto.from_dict(data)

                return endpoint_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_type_2 = WebhookEndpointDto.from_dict(data)

                return endpoint_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            endpoint_type_3 = PhoneEndpointDto.from_dict(data)

            return endpoint_type_3

        endpoint = _parse_endpoint(d.pop("endpoint"))

        update_channel_endpoint_request_dto = cls(
            endpoint=endpoint,
        )

        update_channel_endpoint_request_dto.additional_properties = d
        return update_channel_endpoint_request_dto

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
