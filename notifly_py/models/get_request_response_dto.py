from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.request_log_response_dto import RequestLogResponseDto
    from ..models.trace_response_dto import TraceResponseDto


T = TypeVar("T", bound="GetRequestResponseDto")


@_attrs_define
class GetRequestResponseDto:
    """
    Attributes:
        request (RequestLogResponseDto):
        traces (list[TraceResponseDto]): Associated traces
    """

    request: RequestLogResponseDto
    traces: list[TraceResponseDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request = self.request.to_dict()

        traces = []
        for traces_item_data in self.traces:
            traces_item = traces_item_data.to_dict()
            traces.append(traces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "traces": traces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_log_response_dto import RequestLogResponseDto
        from ..models.trace_response_dto import TraceResponseDto

        d = dict(src_dict)
        request = RequestLogResponseDto.from_dict(d.pop("request"))

        traces = []
        _traces = d.pop("traces")
        for traces_item_data in _traces:
            traces_item = TraceResponseDto.from_dict(traces_item_data)

            traces.append(traces_item)

        get_request_response_dto = cls(
            request=request,
            traces=traces,
        )

        get_request_response_dto.additional_properties = d
        return get_request_response_dto

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
