from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_result_dto_output import ToolResultDtoOutput


T = TypeVar("T", bound="ToolResultDto")


@_attrs_define
class ToolResultDto:
    """
    Attributes:
        tool_call_id (str): Id of the tool call this result resolves. Example: call_abc123.
        tool_name (str | Unset): Name of the tool that produced this result. Example: lookup_order.
        output (ToolResultDtoOutput | Unset): JSON-serializable tool output (or the execution-denied marker).
        preview (str | Unset): Human-readable preview for the display timeline. Example: Order ORD-42 is shipped.
    """

    tool_call_id: str
    tool_name: str | Unset = UNSET
    output: ToolResultDtoOutput | Unset = UNSET
    preview: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_call_id = self.tool_call_id

        tool_name = self.tool_name

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        preview = self.preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toolCallId": tool_call_id,
            }
        )
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name
        if output is not UNSET:
            field_dict["output"] = output
        if preview is not UNSET:
            field_dict["preview"] = preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_result_dto_output import ToolResultDtoOutput

        d = dict(src_dict)
        tool_call_id = d.pop("toolCallId")

        tool_name = d.pop("toolName", UNSET)

        _output = d.pop("output", UNSET)
        output: ToolResultDtoOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = ToolResultDtoOutput.from_dict(_output)

        preview = d.pop("preview", UNSET)

        tool_result_dto = cls(
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            output=output,
            preview=preview,
        )

        tool_result_dto.additional_properties = d
        return tool_result_dto

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
