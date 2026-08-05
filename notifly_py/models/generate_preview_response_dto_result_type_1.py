from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_preview_response_dto_result_type_1_type import GeneratePreviewResponseDtoResultType1Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_render_output import EmailRenderOutput
    from ..models.preview_error_dto import PreviewErrorDto


T = TypeVar("T", bound="GeneratePreviewResponseDtoResultType1")


@_attrs_define
class GeneratePreviewResponseDtoResultType1:
    """
    Attributes:
        type_ (GeneratePreviewResponseDtoResultType1Type | Unset):
        preview (EmailRenderOutput | Unset):
        error (PreviewErrorDto | Unset):
    """

    type_: GeneratePreviewResponseDtoResultType1Type | Unset = UNSET
    preview: EmailRenderOutput | Unset = UNSET
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
        from ..models.email_render_output import EmailRenderOutput
        from ..models.preview_error_dto import PreviewErrorDto

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GeneratePreviewResponseDtoResultType1Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GeneratePreviewResponseDtoResultType1Type(_type_)

        _preview = d.pop("preview", UNSET)
        preview: EmailRenderOutput | Unset
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = EmailRenderOutput.from_dict(_preview)

        _error = d.pop("error", UNSET)
        error: PreviewErrorDto | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PreviewErrorDto.from_dict(_error)

        generate_preview_response_dto_result_type_1 = cls(
            type_=type_,
            preview=preview,
            error=error,
        )

        generate_preview_response_dto_result_type_1.additional_properties = d
        return generate_preview_response_dto_result_type_1

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
