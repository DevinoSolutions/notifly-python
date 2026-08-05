from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_log_response_dto_source import RequestLogResponseDtoSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_log_response_dto_transaction_id_type_0 import RequestLogResponseDtoTransactionIdType0


T = TypeVar("T", bound="RequestLogResponseDto")


@_attrs_define
class RequestLogResponseDto:
    """
    Attributes:
        id (str): Request log identifier
        created_at (str): Creation timestamp
        url (str): Request URL
        url_pattern (str): URL pattern
        method (str): HTTP method
        status_code (float): HTTP status code
        path (str): Request path
        hostname (str): Request hostname
        ip (str): Client IP address
        user_agent (str): User agent string
        request_body (str): Request body
        response_body (str): Response body
        user_id (str): User identifier
        organization_id (str): Organization identifier
        environment_id (str): Environment identifier
        auth_type (str): Authentication type
        duration_ms (float): Request duration in milliseconds
        source (RequestLogResponseDtoSource): Origin of the request: 'http' for API triggers or 'inbound_email' for
            inbound mail
        transaction_id (None | RequestLogResponseDtoTransactionIdType0 | Unset): Transaction identifier
    """

    id: str
    created_at: str
    url: str
    url_pattern: str
    method: str
    status_code: float
    path: str
    hostname: str
    ip: str
    user_agent: str
    request_body: str
    response_body: str
    user_id: str
    organization_id: str
    environment_id: str
    auth_type: str
    duration_ms: float
    source: RequestLogResponseDtoSource
    transaction_id: None | RequestLogResponseDtoTransactionIdType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.request_log_response_dto_transaction_id_type_0 import RequestLogResponseDtoTransactionIdType0

        id = self.id

        created_at = self.created_at

        url = self.url

        url_pattern = self.url_pattern

        method = self.method

        status_code = self.status_code

        path = self.path

        hostname = self.hostname

        ip = self.ip

        user_agent = self.user_agent

        request_body = self.request_body

        response_body = self.response_body

        user_id = self.user_id

        organization_id = self.organization_id

        environment_id = self.environment_id

        auth_type = self.auth_type

        duration_ms = self.duration_ms

        source = self.source.value

        transaction_id: dict[str, Any] | None | Unset
        if isinstance(self.transaction_id, Unset):
            transaction_id = UNSET
        elif isinstance(self.transaction_id, RequestLogResponseDtoTransactionIdType0):
            transaction_id = self.transaction_id.to_dict()
        else:
            transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "url": url,
                "urlPattern": url_pattern,
                "method": method,
                "statusCode": status_code,
                "path": path,
                "hostname": hostname,
                "ip": ip,
                "userAgent": user_agent,
                "requestBody": request_body,
                "responseBody": response_body,
                "userId": user_id,
                "organizationId": organization_id,
                "environmentId": environment_id,
                "authType": auth_type,
                "durationMs": duration_ms,
                "source": source,
            }
        )
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_log_response_dto_transaction_id_type_0 import RequestLogResponseDtoTransactionIdType0

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("createdAt")

        url = d.pop("url")

        url_pattern = d.pop("urlPattern")

        method = d.pop("method")

        status_code = d.pop("statusCode")

        path = d.pop("path")

        hostname = d.pop("hostname")

        ip = d.pop("ip")

        user_agent = d.pop("userAgent")

        request_body = d.pop("requestBody")

        response_body = d.pop("responseBody")

        user_id = d.pop("userId")

        organization_id = d.pop("organizationId")

        environment_id = d.pop("environmentId")

        auth_type = d.pop("authType")

        duration_ms = d.pop("durationMs")

        source = RequestLogResponseDtoSource(d.pop("source"))

        def _parse_transaction_id(data: object) -> None | RequestLogResponseDtoTransactionIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transaction_id_type_0 = RequestLogResponseDtoTransactionIdType0.from_dict(data)

                return transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequestLogResponseDtoTransactionIdType0 | Unset, data)

        transaction_id = _parse_transaction_id(d.pop("transactionId", UNSET))

        request_log_response_dto = cls(
            id=id,
            created_at=created_at,
            url=url,
            url_pattern=url_pattern,
            method=method,
            status_code=status_code,
            path=path,
            hostname=hostname,
            ip=ip,
            user_agent=user_agent,
            request_body=request_body,
            response_body=response_body,
            user_id=user_id,
            organization_id=organization_id,
            environment_id=environment_id,
            auth_type=auth_type,
            duration_ms=duration_ms,
            source=source,
            transaction_id=transaction_id,
        )

        request_log_response_dto.additional_properties = d
        return request_log_response_dto

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
