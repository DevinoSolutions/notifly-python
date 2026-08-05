from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generate_preview_response_dto_result_type_7_type import GeneratePreviewResponseDtoResultType7Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_regular_output import DigestRegularOutput


T = TypeVar("T", bound="GeneratePreviewResponseDtoResultType7")


@_attrs_define
class GeneratePreviewResponseDtoResultType7:
    """
    Attributes:
        type_ (GeneratePreviewResponseDtoResultType7Type | Unset):
        preview (DigestRegularOutput | Unset):
    """

    type_: GeneratePreviewResponseDtoResultType7Type | Unset = UNSET
    preview: DigestRegularOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_regular_output import DigestRegularOutput

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GeneratePreviewResponseDtoResultType7Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GeneratePreviewResponseDtoResultType7Type(_type_)

        _preview = d.pop("preview", UNSET)
        preview: DigestRegularOutput | Unset
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = DigestRegularOutput.from_dict(_preview)

        generate_preview_response_dto_result_type_7 = cls(
            type_=type_,
            preview=preview,
        )

        generate_preview_response_dto_result_type_7.additional_properties = d
        return generate_preview_response_dto_result_type_7

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
