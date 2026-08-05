from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_control_dto_editor_type import EmailControlDtoEditorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_control_dto_skip import EmailControlDtoSkip


T = TypeVar("T", bound="EmailControlDto")


@_attrs_define
class EmailControlDto:
    """
    Attributes:
        subject (str): Subject of the email.
        body (str): Body content of the email, either a valid Maily JSON object, or html string. Default: ''.
        skip (EmailControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        editor_type (EmailControlDtoEditorType | Unset): Type of editor to use for the body. Default:
            EmailControlDtoEditorType.BLOCK.
        disable_output_sanitization (bool | Unset): Disable sanitization of the output. Default: False.
        layout_id (None | str | Unset): Layout ID to use for the email. Null means no layout, undefined means default
            layout.
    """

    subject: str
    body: str = ""
    skip: EmailControlDtoSkip | Unset = UNSET
    editor_type: EmailControlDtoEditorType | Unset = EmailControlDtoEditorType.BLOCK
    disable_output_sanitization: bool | Unset = False
    layout_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        body = self.body

        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        editor_type: str | Unset = UNSET
        if not isinstance(self.editor_type, Unset):
            editor_type = self.editor_type.value

        disable_output_sanitization = self.disable_output_sanitization

        layout_id: None | str | Unset
        if isinstance(self.layout_id, Unset):
            layout_id = UNSET
        else:
            layout_id = self.layout_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "body": body,
            }
        )
        if skip is not UNSET:
            field_dict["skip"] = skip
        if editor_type is not UNSET:
            field_dict["editorType"] = editor_type
        if disable_output_sanitization is not UNSET:
            field_dict["disableOutputSanitization"] = disable_output_sanitization
        if layout_id is not UNSET:
            field_dict["layoutId"] = layout_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_control_dto_skip import EmailControlDtoSkip

        d = dict(src_dict)
        subject = d.pop("subject")

        body = d.pop("body")

        _skip = d.pop("skip", UNSET)
        skip: EmailControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = EmailControlDtoSkip.from_dict(_skip)

        _editor_type = d.pop("editorType", UNSET)
        editor_type: EmailControlDtoEditorType | Unset
        if isinstance(_editor_type, Unset):
            editor_type = UNSET
        else:
            editor_type = EmailControlDtoEditorType(_editor_type)

        disable_output_sanitization = d.pop("disableOutputSanitization", UNSET)

        def _parse_layout_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layout_id = _parse_layout_id(d.pop("layoutId", UNSET))

        email_control_dto = cls(
            subject=subject,
            body=body,
            skip=skip,
            editor_type=editor_type,
            disable_output_sanitization=disable_output_sanitization,
            layout_id=layout_id,
        )

        email_control_dto.additional_properties = d
        return email_control_dto

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
