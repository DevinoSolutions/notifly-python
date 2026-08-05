from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_validation_value_type_3 import ConstraintValidationValueType3
    from ..models.constraint_validation_value_type_4_item_type_3 import ConstraintValidationValueType4ItemType3


T = TypeVar("T", bound="ConstraintValidation")


@_attrs_define
class ConstraintValidation:
    """
    Attributes:
        messages (list[str]): List of validation error messages Example: ['Field is required', 'Invalid format'].
        value (bool | ConstraintValidationValueType3 | float | list[bool | ConstraintValidationValueType4ItemType3 |
            float | None | str] | None | str | Unset): Value that failed validation Example: xx xx xx .
    """

    messages: list[str]
    value: (
        bool
        | ConstraintValidationValueType3
        | float
        | list[bool | ConstraintValidationValueType4ItemType3 | float | None | str]
        | None
        | str
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.constraint_validation_value_type_3 import ConstraintValidationValueType3
        from ..models.constraint_validation_value_type_4_item_type_3 import ConstraintValidationValueType4ItemType3

        messages = self.messages

        value: bool | dict[str, Any] | float | list[bool | dict[str, Any] | float | None | str] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ConstraintValidationValueType3):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_4_item_data in self.value:
                value_type_4_item: bool | dict[str, Any] | float | None | str
                if isinstance(value_type_4_item_data, ConstraintValidationValueType4ItemType3):
                    value_type_4_item = value_type_4_item_data.to_dict()
                else:
                    value_type_4_item = value_type_4_item_data
                value.append(value_type_4_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_validation_value_type_3 import ConstraintValidationValueType3
        from ..models.constraint_validation_value_type_4_item_type_3 import ConstraintValidationValueType4ItemType3

        d = dict(src_dict)
        messages = cast(list[str], d.pop("messages"))

        def _parse_value(
            data: object,
        ) -> (
            bool
            | ConstraintValidationValueType3
            | float
            | list[bool | ConstraintValidationValueType4ItemType3 | float | None | str]
            | None
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
                value_type_3 = ConstraintValidationValueType3.from_dict(data)

                return value_type_3
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
                    ) -> bool | ConstraintValidationValueType4ItemType3 | float | None | str:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_4_item_type_3 = ConstraintValidationValueType4ItemType3.from_dict(data)

                            return value_type_4_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(bool | ConstraintValidationValueType4ItemType3 | float | None | str, data)

                    value_type_4_item = _parse_value_type_4_item(value_type_4_item_data)

                    value_type_4.append(value_type_4_item)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | ConstraintValidationValueType3
                | float
                | list[bool | ConstraintValidationValueType4ItemType3 | float | None | str]
                | None
                | str
                | Unset,
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        constraint_validation = cls(
            messages=messages,
            value=value,
        )

        constraint_validation.additional_properties = d
        return constraint_validation

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
