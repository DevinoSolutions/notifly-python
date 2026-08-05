from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.http_method_enum import HttpMethodEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_request_control_dto_response_body_schema import HttpRequestControlDtoResponseBodySchema
    from ..models.http_request_key_value_pair_dto import HttpRequestKeyValuePairDto


T = TypeVar("T", bound="HttpRequestControlDto")


@_attrs_define
class HttpRequestControlDto:
    """
    Attributes:
        method (HttpMethodEnum): HTTP method
        url (str): Target URL for the HTTP request
        headers (list[HttpRequestKeyValuePairDto] | Unset): Request headers as key-value pairs
        body (list[HttpRequestKeyValuePairDto] | str | Unset): Request body as a raw JSON string. Key-value arrays are
            supported for legacy workflows.
        response_body_schema (HttpRequestControlDtoResponseBodySchema | Unset): JSON schema to validate response body
            against
        enforce_schema_validation (bool | Unset): Whether to enforce response body schema validation
        continue_on_failure (bool | Unset): Whether to continue workflow execution on failure
    """

    method: HttpMethodEnum
    url: str
    headers: list[HttpRequestKeyValuePairDto] | Unset = UNSET
    body: list[HttpRequestKeyValuePairDto] | str | Unset = UNSET
    response_body_schema: HttpRequestControlDtoResponseBodySchema | Unset = UNSET
    enforce_schema_validation: bool | Unset = UNSET
    continue_on_failure: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        url = self.url

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        body: list[dict[str, Any]] | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        elif isinstance(self.body, list):
            body = []
            for body_type_1_item_data in self.body:
                body_type_1_item = body_type_1_item_data.to_dict()
                body.append(body_type_1_item)

        else:
            body = self.body

        response_body_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_body_schema, Unset):
            response_body_schema = self.response_body_schema.to_dict()

        enforce_schema_validation = self.enforce_schema_validation

        continue_on_failure = self.continue_on_failure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body
        if response_body_schema is not UNSET:
            field_dict["responseBodySchema"] = response_body_schema
        if enforce_schema_validation is not UNSET:
            field_dict["enforceSchemaValidation"] = enforce_schema_validation
        if continue_on_failure is not UNSET:
            field_dict["continueOnFailure"] = continue_on_failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_request_control_dto_response_body_schema import HttpRequestControlDtoResponseBodySchema
        from ..models.http_request_key_value_pair_dto import HttpRequestKeyValuePairDto

        d = dict(src_dict)
        method = HttpMethodEnum(d.pop("method"))

        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: list[HttpRequestKeyValuePairDto] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = HttpRequestKeyValuePairDto.from_dict(headers_item_data)

                headers.append(headers_item)

        def _parse_body(data: object) -> list[HttpRequestKeyValuePairDto] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                body_type_1 = []
                _body_type_1 = data
                for body_type_1_item_data in _body_type_1:
                    body_type_1_item = HttpRequestKeyValuePairDto.from_dict(body_type_1_item_data)

                    body_type_1.append(body_type_1_item)

                return body_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HttpRequestKeyValuePairDto] | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        _response_body_schema = d.pop("responseBodySchema", UNSET)
        response_body_schema: HttpRequestControlDtoResponseBodySchema | Unset
        if isinstance(_response_body_schema, Unset):
            response_body_schema = UNSET
        else:
            response_body_schema = HttpRequestControlDtoResponseBodySchema.from_dict(_response_body_schema)

        enforce_schema_validation = d.pop("enforceSchemaValidation", UNSET)

        continue_on_failure = d.pop("continueOnFailure", UNSET)

        http_request_control_dto = cls(
            method=method,
            url=url,
            headers=headers,
            body=body,
            response_body_schema=response_body_schema,
            enforce_schema_validation=enforce_schema_validation,
            continue_on_failure=continue_on_failure,
        )

        http_request_control_dto.additional_properties = d
        return http_request_control_dto

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
