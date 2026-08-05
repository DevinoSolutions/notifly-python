from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_preview_response_dto_result_type_3_type import GeneratePreviewResponseDtoResultType3Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_app_render_output import InAppRenderOutput
    from ..models.preview_error_dto import PreviewErrorDto


T = TypeVar("T", bound="GeneratePreviewResponseDtoResultType3")


@_attrs_define
class GeneratePreviewResponseDtoResultType3:
    """
    Attributes:
        type_ (GeneratePreviewResponseDtoResultType3Type | Unset):
        preview (InAppRenderOutput | Unset):
        error (PreviewErrorDto | Unset):
    """

    type_: GeneratePreviewResponseDtoResultType3Type | Unset = UNSET
    preview: InAppRenderOutput | Unset = UNSET
    error: PreviewErrorDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if preview is not UNSET:
            field_dict["preview"] = preview
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_app_render_output import InAppRenderOutput
        from ..models.preview_error_dto import PreviewErrorDto

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GeneratePreviewResponseDtoResultType3Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GeneratePreviewResponseDtoResultType3Type(_type_)

        _preview = d.pop("preview", UNSET)
        preview: InAppRenderOutput | Unset
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = InAppRenderOutput.from_dict(_preview)

        _error = d.pop("error", UNSET)
        error: PreviewErrorDto | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PreviewErrorDto.from_dict(_error)

        generate_preview_response_dto_result_type_3 = cls(
            type_=type_,
            preview=preview,
            error=error,
        )

        generate_preview_response_dto_result_type_3.additional_properties = d
        return generate_preview_response_dto_result_type_3

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
