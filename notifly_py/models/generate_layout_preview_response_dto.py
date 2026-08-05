from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_layout_preview_response_dto_result_type_0 import GenerateLayoutPreviewResponseDtoResultType0
    from ..models.generate_layout_preview_response_dto_schema_type_0 import GenerateLayoutPreviewResponseDtoSchemaType0
    from ..models.layout_preview_payload_dto import LayoutPreviewPayloadDto


T = TypeVar("T", bound="GenerateLayoutPreviewResponseDto")


@_attrs_define
class GenerateLayoutPreviewResponseDto:
    """
    Attributes:
        preview_payload_example (LayoutPreviewPayloadDto):
        result (GenerateLayoutPreviewResponseDtoResultType0): Preview result
        schema (GenerateLayoutPreviewResponseDtoSchemaType0 | None | Unset): The payload schema that was used to
            generate the preview payload example
    """

    preview_payload_example: LayoutPreviewPayloadDto
    result: GenerateLayoutPreviewResponseDtoResultType0
    schema: GenerateLayoutPreviewResponseDtoSchemaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_layout_preview_response_dto_result_type_0 import (
            GenerateLayoutPreviewResponseDtoResultType0,
        )
        from ..models.generate_layout_preview_response_dto_schema_type_0 import (
            GenerateLayoutPreviewResponseDtoSchemaType0,
        )

        preview_payload_example = self.preview_payload_example.to_dict()

        result: dict[str, Any]
        if isinstance(self.result, GenerateLayoutPreviewResponseDtoResultType0):
            result = self.result.to_dict()

        schema: dict[str, Any] | None | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, GenerateLayoutPreviewResponseDtoSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "previewPayloadExample": preview_payload_example,
                "result": result,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_layout_preview_response_dto_result_type_0 import (
            GenerateLayoutPreviewResponseDtoResultType0,
        )
        from ..models.generate_layout_preview_response_dto_schema_type_0 import (
            GenerateLayoutPreviewResponseDtoSchemaType0,
        )
        from ..models.layout_preview_payload_dto import LayoutPreviewPayloadDto

        d = dict(src_dict)
        preview_payload_example = LayoutPreviewPayloadDto.from_dict(d.pop("previewPayloadExample"))

        def _parse_result(data: object) -> GenerateLayoutPreviewResponseDtoResultType0:
            if not isinstance(data, dict):
                raise TypeError()
            result_type_0 = GenerateLayoutPreviewResponseDtoResultType0.from_dict(data)

            return result_type_0

        result = _parse_result(d.pop("result"))

        def _parse_schema(data: object) -> GenerateLayoutPreviewResponseDtoSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = GenerateLayoutPreviewResponseDtoSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerateLayoutPreviewResponseDtoSchemaType0 | None | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        generate_layout_preview_response_dto = cls(
            preview_payload_example=preview_payload_example,
            result=result,
            schema=schema,
        )

        generate_layout_preview_response_dto.additional_properties = d
        return generate_layout_preview_response_dto

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
