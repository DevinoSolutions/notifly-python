from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_preview_payload_dto import LayoutPreviewPayloadDto
    from ..models.layout_preview_request_dto_control_values import LayoutPreviewRequestDtoControlValues


T = TypeVar("T", bound="LayoutPreviewRequestDto")


@_attrs_define
class LayoutPreviewRequestDto:
    """
    Attributes:
        control_values (LayoutPreviewRequestDtoControlValues | Unset): Optional control values for layout preview
        preview_payload (LayoutPreviewPayloadDto | Unset):
    """

    control_values: LayoutPreviewRequestDtoControlValues | Unset = UNSET
    preview_payload: LayoutPreviewPayloadDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_values, Unset):
            control_values = self.control_values.to_dict()

        preview_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview_payload, Unset):
            preview_payload = self.preview_payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_values is not UNSET:
            field_dict["controlValues"] = control_values
        if preview_payload is not UNSET:
            field_dict["previewPayload"] = preview_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_preview_payload_dto import LayoutPreviewPayloadDto
        from ..models.layout_preview_request_dto_control_values import LayoutPreviewRequestDtoControlValues

        d = dict(src_dict)
        _control_values = d.pop("controlValues", UNSET)
        control_values: LayoutPreviewRequestDtoControlValues | Unset
        if isinstance(_control_values, Unset):
            control_values = UNSET
        else:
            control_values = LayoutPreviewRequestDtoControlValues.from_dict(_control_values)

        _preview_payload = d.pop("previewPayload", UNSET)
        preview_payload: LayoutPreviewPayloadDto | Unset
        if isinstance(_preview_payload, Unset):
            preview_payload = UNSET
        else:
            preview_payload = LayoutPreviewPayloadDto.from_dict(_preview_payload)

        layout_preview_request_dto = cls(
            control_values=control_values,
            preview_payload=preview_payload,
        )

        layout_preview_request_dto.additional_properties = d
        return layout_preview_request_dto

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
