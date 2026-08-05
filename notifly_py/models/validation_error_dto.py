from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error_dto_ctx import ValidationErrorDtoCtx
    from ..models.validation_error_dto_errors import ValidationErrorDtoErrors
    from ..models.validation_error_dto_message_type_3_type_0 import ValidationErrorDtoMessageType3Type0
    from ..models.validation_error_dto_message_type_4_item_type_3 import ValidationErrorDtoMessageType4ItemType3


T = TypeVar("T", bound="ValidationErrorDto")


@_attrs_define
class ValidationErrorDto:
    """
    Attributes:
        status_code (float): HTTP status code of the error response. Example: 404.
        timestamp (str): Timestamp of when the error occurred. Example: 2024-12-12T13:00:00Z.
        path (str): The path where the error occurred. Example: /api/v1/resource.
        errors (ValidationErrorDtoErrors): A record of validation errors keyed by field name Example: {'fieldName1':
            {'messages': ['Field is required', 'Must be a valid email address'], 'value': 'invalidEmail'}, 'fieldName2':
            {'messages': ['Must be at least 18 years old'], 'value': 17}, 'fieldName3': {'messages': ['Must be a boolean
            value'], 'value': True}, 'fieldName4': {'messages': ['Must be a valid object'], 'value': {'key': 'value'}},
            'fieldName5': {'messages': ['Field is missing'], 'value': None}, 'fieldName6': {'messages': ['Undefined
            value']}}.
        message (bool | float | list[bool | float | None | str | ValidationErrorDtoMessageType4ItemType3] | None | str |
            Unset | ValidationErrorDtoMessageType3Type0): Value that failed validation Example: xx xx xx .
        ctx (ValidationErrorDtoCtx | Unset): Optional context object for additional error details. Example:
            {'workflowId': 'some_wf_id', 'stepId': 'some_wf_id'}.
        error_id (str | Unset): Optional unique identifier for the error, useful for tracking using Sentry and
                  New Relic, only available for 500. Example: abc123.
    """

    status_code: float
    timestamp: str
    path: str
    errors: ValidationErrorDtoErrors
    message: (
        bool
        | float
        | list[bool | float | None | str | ValidationErrorDtoMessageType4ItemType3]
        | None
        | str
        | Unset
        | ValidationErrorDtoMessageType3Type0
    ) = UNSET
    ctx: ValidationErrorDtoCtx | Unset = UNSET
    error_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_error_dto_message_type_3_type_0 import ValidationErrorDtoMessageType3Type0
        from ..models.validation_error_dto_message_type_4_item_type_3 import ValidationErrorDtoMessageType4ItemType3

        status_code = self.status_code

        timestamp = self.timestamp

        path = self.path

        errors = self.errors.to_dict()

        message: bool | dict[str, Any] | float | list[bool | dict[str, Any] | float | None | str] | None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, ValidationErrorDtoMessageType3Type0):
            message = self.message.to_dict()
        elif isinstance(self.message, list):
            message = []
            for message_type_4_item_data in self.message:
                message_type_4_item: bool | dict[str, Any] | float | None | str
                if isinstance(message_type_4_item_data, ValidationErrorDtoMessageType4ItemType3):
                    message_type_4_item = message_type_4_item_data.to_dict()
                else:
                    message_type_4_item = message_type_4_item_data
                message.append(message_type_4_item)

        else:
            message = self.message

        ctx: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ctx, Unset):
            ctx = self.ctx.to_dict()

        error_id = self.error_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "timestamp": timestamp,
                "path": path,
                "errors": errors,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if ctx is not UNSET:
            field_dict["ctx"] = ctx
        if error_id is not UNSET:
            field_dict["errorId"] = error_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error_dto_ctx import ValidationErrorDtoCtx
        from ..models.validation_error_dto_errors import ValidationErrorDtoErrors
        from ..models.validation_error_dto_message_type_3_type_0 import ValidationErrorDtoMessageType3Type0
        from ..models.validation_error_dto_message_type_4_item_type_3 import ValidationErrorDtoMessageType4ItemType3

        d = dict(src_dict)
        status_code = d.pop("statusCode")

        timestamp = d.pop("timestamp")

        path = d.pop("path")

        errors = ValidationErrorDtoErrors.from_dict(d.pop("errors"))

        def _parse_message(
            data: object,
        ) -> (
            bool
            | float
            | list[bool | float | None | str | ValidationErrorDtoMessageType4ItemType3]
            | None
            | str
            | Unset
            | ValidationErrorDtoMessageType3Type0
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_3_type_0 = ValidationErrorDtoMessageType3Type0.from_dict(data)

                return message_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                message_type_4 = []
                _message_type_4 = data
                for message_type_4_item_data in _message_type_4:

                    def _parse_message_type_4_item(
                        data: object,
                    ) -> bool | float | None | str | ValidationErrorDtoMessageType4ItemType3:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            message_type_4_item_type_3 = ValidationErrorDtoMessageType4ItemType3.from_dict(data)

                            return message_type_4_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(bool | float | None | str | ValidationErrorDtoMessageType4ItemType3, data)

                    message_type_4_item = _parse_message_type_4_item(message_type_4_item_data)

                    message_type_4.append(message_type_4_item)

                return message_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | list[bool | float | None | str | ValidationErrorDtoMessageType4ItemType3]
                | None
                | str
                | Unset
                | ValidationErrorDtoMessageType3Type0,
                data,
            )

        message = _parse_message(d.pop("message", UNSET))

        _ctx = d.pop("ctx", UNSET)
        ctx: ValidationErrorDtoCtx | Unset
        if isinstance(_ctx, Unset):
            ctx = UNSET
        else:
            ctx = ValidationErrorDtoCtx.from_dict(_ctx)

        error_id = d.pop("errorId", UNSET)

        validation_error_dto = cls(
            status_code=status_code,
            timestamp=timestamp,
            path=path,
            errors=errors,
            message=message,
            ctx=ctx,
            error_id=error_id,
        )

        validation_error_dto.additional_properties = d
        return validation_error_dto

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
