from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_validation_error_dto import PayloadValidationErrorDto
    from ..models.payload_validation_exception_dto_ctx import PayloadValidationExceptionDtoCtx
    from ..models.payload_validation_exception_dto_message_type_3_type_0 import (
        PayloadValidationExceptionDtoMessageType3Type0,
    )
    from ..models.payload_validation_exception_dto_message_type_4_item_type_3 import (
        PayloadValidationExceptionDtoMessageType4ItemType3,
    )
    from ..models.payload_validation_exception_dto_schema import PayloadValidationExceptionDtoSchema


T = TypeVar("T", bound="PayloadValidationExceptionDto")


@_attrs_define
class PayloadValidationExceptionDto:
    """
    Attributes:
        status_code (float): HTTP status code of the error response. Example: 404.
        timestamp (str): Timestamp of when the error occurred. Example: 2024-12-12T13:00:00Z.
        path (str): The path where the error occurred. Example: /api/v1/resource.
        type_ (str): Type identifier for payload validation errors Example: PAYLOAD_VALIDATION_ERROR.
        errors (list[PayloadValidationErrorDto]): Array of detailed validation errors Example: [{'field': 'user.name',
            'message': "must have required property 'name'", 'value': {'age': 25}, 'schemaPath': '#/required'}].
        message (bool | float | list[bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str] |
            None | PayloadValidationExceptionDtoMessageType3Type0 | str | Unset): Value that failed validation Example: xx
            xx xx .
        ctx (PayloadValidationExceptionDtoCtx | Unset): Optional context object for additional error details. Example:
            {'workflowId': 'some_wf_id', 'stepId': 'some_wf_id'}.
        error_id (str | Unset): Optional unique identifier for the error, useful for tracking using Sentry and
                  New Relic, only available for 500. Example: abc123.
        schema (PayloadValidationExceptionDtoSchema | Unset): The JSON schema that was used for validation Example:
            {'type': 'object', 'properties': {'name': {'type': 'string'}, 'age': {'type': 'number'}}, 'required': ['name']}.
    """

    status_code: float
    timestamp: str
    path: str
    type_: str
    errors: list[PayloadValidationErrorDto]
    message: (
        bool
        | float
        | list[bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str]
        | None
        | PayloadValidationExceptionDtoMessageType3Type0
        | str
        | Unset
    ) = UNSET
    ctx: PayloadValidationExceptionDtoCtx | Unset = UNSET
    error_id: str | Unset = UNSET
    schema: PayloadValidationExceptionDtoSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.payload_validation_exception_dto_message_type_3_type_0 import (
            PayloadValidationExceptionDtoMessageType3Type0,
        )
        from ..models.payload_validation_exception_dto_message_type_4_item_type_3 import (
            PayloadValidationExceptionDtoMessageType4ItemType3,
        )

        status_code = self.status_code

        timestamp = self.timestamp

        path = self.path

        type_ = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        message: bool | dict[str, Any] | float | list[bool | dict[str, Any] | float | None | str] | None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, PayloadValidationExceptionDtoMessageType3Type0):
            message = self.message.to_dict()
        elif isinstance(self.message, list):
            message = []
            for message_type_4_item_data in self.message:
                message_type_4_item: bool | dict[str, Any] | float | None | str
                if isinstance(message_type_4_item_data, PayloadValidationExceptionDtoMessageType4ItemType3):
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

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "timestamp": timestamp,
                "path": path,
                "type": type_,
                "errors": errors,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if ctx is not UNSET:
            field_dict["ctx"] = ctx
        if error_id is not UNSET:
            field_dict["errorId"] = error_id
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payload_validation_error_dto import PayloadValidationErrorDto
        from ..models.payload_validation_exception_dto_ctx import PayloadValidationExceptionDtoCtx
        from ..models.payload_validation_exception_dto_message_type_3_type_0 import (
            PayloadValidationExceptionDtoMessageType3Type0,
        )
        from ..models.payload_validation_exception_dto_message_type_4_item_type_3 import (
            PayloadValidationExceptionDtoMessageType4ItemType3,
        )
        from ..models.payload_validation_exception_dto_schema import PayloadValidationExceptionDtoSchema

        d = dict(src_dict)
        status_code = d.pop("statusCode")

        timestamp = d.pop("timestamp")

        path = d.pop("path")

        type_ = d.pop("type")

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = PayloadValidationErrorDto.from_dict(errors_item_data)

            errors.append(errors_item)

        def _parse_message(
            data: object,
        ) -> (
            bool
            | float
            | list[bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str]
            | None
            | PayloadValidationExceptionDtoMessageType3Type0
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
                message_type_3_type_0 = PayloadValidationExceptionDtoMessageType3Type0.from_dict(data)

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
                    ) -> bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            message_type_4_item_type_3 = PayloadValidationExceptionDtoMessageType4ItemType3.from_dict(
                                data
                            )

                            return message_type_4_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(
                            bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str, data
                        )

                    message_type_4_item = _parse_message_type_4_item(message_type_4_item_data)

                    message_type_4.append(message_type_4_item)

                return message_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                bool
                | float
                | list[bool | float | None | PayloadValidationExceptionDtoMessageType4ItemType3 | str]
                | None
                | PayloadValidationExceptionDtoMessageType3Type0
                | str
                | Unset,
                data,
            )

        message = _parse_message(d.pop("message", UNSET))

        _ctx = d.pop("ctx", UNSET)
        ctx: PayloadValidationExceptionDtoCtx | Unset
        if isinstance(_ctx, Unset):
            ctx = UNSET
        else:
            ctx = PayloadValidationExceptionDtoCtx.from_dict(_ctx)

        error_id = d.pop("errorId", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: PayloadValidationExceptionDtoSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = PayloadValidationExceptionDtoSchema.from_dict(_schema)

        payload_validation_exception_dto = cls(
            status_code=status_code,
            timestamp=timestamp,
            path=path,
            type_=type_,
            errors=errors,
            message=message,
            ctx=ctx,
            error_id=error_id,
            schema=schema,
        )

        payload_validation_exception_dto.additional_properties = d
        return payload_validation_exception_dto

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
