from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_preview_response_dto_result_type_0 import GeneratePreviewResponseDtoResultType0
    from ..models.generate_preview_response_dto_result_type_1 import GeneratePreviewResponseDtoResultType1
    from ..models.generate_preview_response_dto_result_type_2 import GeneratePreviewResponseDtoResultType2
    from ..models.generate_preview_response_dto_result_type_3 import GeneratePreviewResponseDtoResultType3
    from ..models.generate_preview_response_dto_result_type_4 import GeneratePreviewResponseDtoResultType4
    from ..models.generate_preview_response_dto_result_type_5 import GeneratePreviewResponseDtoResultType5
    from ..models.generate_preview_response_dto_result_type_6 import GeneratePreviewResponseDtoResultType6
    from ..models.generate_preview_response_dto_result_type_7 import GeneratePreviewResponseDtoResultType7
    from ..models.generate_preview_response_dto_result_type_8 import GeneratePreviewResponseDtoResultType8
    from ..models.generate_preview_response_dto_schema_type_0 import GeneratePreviewResponseDtoSchemaType0
    from ..models.preview_payload_dto import PreviewPayloadDto


T = TypeVar("T", bound="GeneratePreviewResponseDto")


@_attrs_define
class GeneratePreviewResponseDto:
    """
    Attributes:
        preview_payload_example (PreviewPayloadDto):
        result (GeneratePreviewResponseDtoResultType0 | GeneratePreviewResponseDtoResultType1 |
            GeneratePreviewResponseDtoResultType2 | GeneratePreviewResponseDtoResultType3 |
            GeneratePreviewResponseDtoResultType4 | GeneratePreviewResponseDtoResultType5 |
            GeneratePreviewResponseDtoResultType6 | GeneratePreviewResponseDtoResultType7 |
            GeneratePreviewResponseDtoResultType8): Preview result
        schema (GeneratePreviewResponseDtoSchemaType0 | None | Unset): The payload schema that was used to generate the
            preview payload example
        novu_signature (str | Unset): Sample novu-signature header value for HTTP request steps
    """

    preview_payload_example: PreviewPayloadDto
    result: (
        GeneratePreviewResponseDtoResultType0
        | GeneratePreviewResponseDtoResultType1
        | GeneratePreviewResponseDtoResultType2
        | GeneratePreviewResponseDtoResultType3
        | GeneratePreviewResponseDtoResultType4
        | GeneratePreviewResponseDtoResultType5
        | GeneratePreviewResponseDtoResultType6
        | GeneratePreviewResponseDtoResultType7
        | GeneratePreviewResponseDtoResultType8
    )
    schema: GeneratePreviewResponseDtoSchemaType0 | None | Unset = UNSET
    novu_signature: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_preview_response_dto_result_type_0 import GeneratePreviewResponseDtoResultType0
        from ..models.generate_preview_response_dto_result_type_1 import GeneratePreviewResponseDtoResultType1
        from ..models.generate_preview_response_dto_result_type_2 import GeneratePreviewResponseDtoResultType2
        from ..models.generate_preview_response_dto_result_type_3 import GeneratePreviewResponseDtoResultType3
        from ..models.generate_preview_response_dto_result_type_4 import GeneratePreviewResponseDtoResultType4
        from ..models.generate_preview_response_dto_result_type_5 import GeneratePreviewResponseDtoResultType5
        from ..models.generate_preview_response_dto_result_type_6 import GeneratePreviewResponseDtoResultType6
        from ..models.generate_preview_response_dto_result_type_7 import GeneratePreviewResponseDtoResultType7
        from ..models.generate_preview_response_dto_schema_type_0 import GeneratePreviewResponseDtoSchemaType0

        preview_payload_example = self.preview_payload_example.to_dict()

        result: dict[str, Any]
        if isinstance(self.result, GeneratePreviewResponseDtoResultType0):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType1):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType2):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType3):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType4):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType5):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType6):
            result = self.result.to_dict()
        elif isinstance(self.result, GeneratePreviewResponseDtoResultType7):
            result = self.result.to_dict()
        else:
            result = self.result.to_dict()

        schema: dict[str, Any] | None | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, GeneratePreviewResponseDtoSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        novu_signature = self.novu_signature

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
        if novu_signature is not UNSET:
            field_dict["novuSignature"] = novu_signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_preview_response_dto_result_type_0 import GeneratePreviewResponseDtoResultType0
        from ..models.generate_preview_response_dto_result_type_1 import GeneratePreviewResponseDtoResultType1
        from ..models.generate_preview_response_dto_result_type_2 import GeneratePreviewResponseDtoResultType2
        from ..models.generate_preview_response_dto_result_type_3 import GeneratePreviewResponseDtoResultType3
        from ..models.generate_preview_response_dto_result_type_4 import GeneratePreviewResponseDtoResultType4
        from ..models.generate_preview_response_dto_result_type_5 import GeneratePreviewResponseDtoResultType5
        from ..models.generate_preview_response_dto_result_type_6 import GeneratePreviewResponseDtoResultType6
        from ..models.generate_preview_response_dto_result_type_7 import GeneratePreviewResponseDtoResultType7
        from ..models.generate_preview_response_dto_result_type_8 import GeneratePreviewResponseDtoResultType8
        from ..models.generate_preview_response_dto_schema_type_0 import GeneratePreviewResponseDtoSchemaType0
        from ..models.preview_payload_dto import PreviewPayloadDto

        d = dict(src_dict)
        preview_payload_example = PreviewPayloadDto.from_dict(d.pop("previewPayloadExample"))

        def _parse_result(
            data: object,
        ) -> (
            GeneratePreviewResponseDtoResultType0
            | GeneratePreviewResponseDtoResultType1
            | GeneratePreviewResponseDtoResultType2
            | GeneratePreviewResponseDtoResultType3
            | GeneratePreviewResponseDtoResultType4
            | GeneratePreviewResponseDtoResultType5
            | GeneratePreviewResponseDtoResultType6
            | GeneratePreviewResponseDtoResultType7
            | GeneratePreviewResponseDtoResultType8
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = GeneratePreviewResponseDtoResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_1 = GeneratePreviewResponseDtoResultType1.from_dict(data)

                return result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_2 = GeneratePreviewResponseDtoResultType2.from_dict(data)

                return result_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_3 = GeneratePreviewResponseDtoResultType3.from_dict(data)

                return result_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_4 = GeneratePreviewResponseDtoResultType4.from_dict(data)

                return result_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_5 = GeneratePreviewResponseDtoResultType5.from_dict(data)

                return result_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_6 = GeneratePreviewResponseDtoResultType6.from_dict(data)

                return result_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_7 = GeneratePreviewResponseDtoResultType7.from_dict(data)

                return result_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            result_type_8 = GeneratePreviewResponseDtoResultType8.from_dict(data)

            return result_type_8

        result = _parse_result(d.pop("result"))

        def _parse_schema(data: object) -> GeneratePreviewResponseDtoSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = GeneratePreviewResponseDtoSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GeneratePreviewResponseDtoSchemaType0 | None | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        novu_signature = d.pop("novuSignature", UNSET)

        generate_preview_response_dto = cls(
            preview_payload_example=preview_payload_example,
            result=result,
            schema=schema,
            novu_signature=novu_signature,
        )

        generate_preview_response_dto.additional_properties = d
        return generate_preview_response_dto

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
