from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_validation_error_dto_value_type_3_type_0 import PayloadValidationErrorDtoValueType3Type0
    from ..models.payload_validation_error_dto_value_type_4_item_type_3 import (
        PayloadValidationErrorDtoValueType4ItemType3,
    )


T = TypeVar("T", bound="PayloadValidationErrorDto")


@_attrs_define
class PayloadValidationErrorDto:
    """
    Attributes:
        field (str): Field path that failed validation Example: user.name.
        message (str): Validation error message Example: must have required property 'name'.
        value (bool | float | list[bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str] | None |
            PayloadValidationErrorDtoValueType3Type0 | str | Unset): The actual value that failed validation Example:
            {'age': 25}.
        schema_path (str | Unset): JSON Schema path where the validation failed Example: #/required.
    """

    field: str
    message: str
    value: (
        bool
        | float
        | list[bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str]
        | None
        | PayloadValidationErrorDtoValueType3Type0
        | str
        | Unset
    ) = UNSET
    schema_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payload_validation_error_dto_value_type_3_type_0 import PayloadValidationErrorDtoValueType3Type0
        from ..models.payload_validation_error_dto_value_type_4_item_type_3 import (
            PayloadValidationErrorDtoValueType4ItemType3,
        )

        field = self.field

        message = self.message

        value: bool | dict[str, Any] | float | list[bool | dict[str, Any] | float | None | str] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PayloadValidationErrorDtoValueType3Type0):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_4_item_data in self.value:
                value_type_4_item: bool | dict[str, Any] | float | None | str
                if isinstance(value_type_4_item_data, PayloadValidationErrorDtoValueType4ItemType3):
                    value_type_4_item = value_type_4_item_data.to_dict()
                else:
                    value_type_4_item = value_type_4_item_data
                value.append(value_type_4_item)

        else:
            value = self.value

        schema_path = self.schema_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "message": message,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if schema_path is not UNSET:
            field_dict["schemaPath"] = schema_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payload_validation_error_dto_value_type_3_type_0 import PayloadValidationErrorDtoValueType3Type0
        from ..models.payload_validation_error_dto_value_type_4_item_type_3 import (
            PayloadValidationErrorDtoValueType4ItemType3,
        )

        d = dict(src_dict)
        field = d.pop("field")

        message = d.pop("message")

        def _parse_value(
            data: object,
        ) -> (
            bool
            | float
            | list[bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str]
            | None
            | PayloadValidationErrorDtoValueType3Type0
            | str
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_3_type_0 = PayloadValidationErrorDtoValueType3Type0.from_dict(data)

                return value_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_4 = []
                _value_type_4 = data
                for value_type_4_item_data in _value_type_4:

                    def _parse_value_type_4_item(
                        data: object,
                    ) -> bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_4_item_type_3 = PayloadValidationErrorDtoValueType4ItemType3.from_dict(data)

                            return value_type_4_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str, data)

                    value_type_4_item = _parse_value_type_4_item(value_type_4_item_data)

                    value_type_4.append(value_type_4_item)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | list[bool | float | None | PayloadValidationErrorDtoValueType4ItemType3 | str]
                | None
                | PayloadValidationErrorDtoValueType3Type0
                | str
                | Unset,
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        schema_path = d.pop("schemaPath", UNSET)

        payload_validation_error_dto = cls(
            field=field,
            message=message,
            value=value,
            schema_path=schema_path,
        )

        payload_validation_error_dto.additional_properties = d
        return payload_validation_error_dto

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
