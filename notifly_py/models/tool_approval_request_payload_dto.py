from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_approval_request_payload_dto_input import ToolApprovalRequestPayloadDtoInput


T = TypeVar("T", bound="ToolApprovalRequestPayloadDto")


@_attrs_define
class ToolApprovalRequestPayloadDto:
    """
    Attributes:
        approval_id (str): Unique id for this approval request (matches the AI SDK approvalId). Example: apr_01HZX.
        tool_call_id (str): Id of the tool call awaiting approval. Example: call_refund_1.
        name (str): Name of the gated tool. Example: issue_refund.
        input_ (ToolApprovalRequestPayloadDtoInput | Unset): Tool input the model proposed. Example: {'orderId':
            'ORD-42', 'amountCents': 2500}.
        approve_action_id (str | Unset): Server-minted approve action id. When omitted, self-hosted tool-approval:* is
            minted at persist. Example: tool-approval:approve:apr_01HZX.
        deny_action_id (str | Unset): Server-minted deny action id. When omitted, self-hosted tool-approval:* is minted
            at persist. Example: tool-approval:deny:apr_01HZX.
        mcp_server_name (str | Unset): MCP server name when the gated tool is from an MCP server (for UI labels).
            Example: GitHub.
    """

    approval_id: str
    tool_call_id: str
    name: str
    input_: ToolApprovalRequestPayloadDtoInput | Unset = UNSET
    approve_action_id: str | Unset = UNSET
    deny_action_id: str | Unset = UNSET
    mcp_server_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_id = self.approval_id

        tool_call_id = self.tool_call_id

        name = self.name

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        approve_action_id = self.approve_action_id

        deny_action_id = self.deny_action_id

        mcp_server_name = self.mcp_server_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approvalId": approval_id,
                "toolCallId": tool_call_id,
                "name": name,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if approve_action_id is not UNSET:
            field_dict["approveActionId"] = approve_action_id
        if deny_action_id is not UNSET:
            field_dict["denyActionId"] = deny_action_id
        if mcp_server_name is not UNSET:
            field_dict["mcpServerName"] = mcp_server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_approval_request_payload_dto_input import ToolApprovalRequestPayloadDtoInput

        d = dict(src_dict)
        approval_id = d.pop("approvalId")

        tool_call_id = d.pop("toolCallId")

        name = d.pop("name")

        _input_ = d.pop("input", UNSET)
        input_: ToolApprovalRequestPayloadDtoInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = ToolApprovalRequestPayloadDtoInput.from_dict(_input_)

        approve_action_id = d.pop("approveActionId", UNSET)

        deny_action_id = d.pop("denyActionId", UNSET)

        mcp_server_name = d.pop("mcpServerName", UNSET)

        tool_approval_request_payload_dto = cls(
            approval_id=approval_id,
            tool_call_id=tool_call_id,
            name=name,
            input_=input_,
            approve_action_id=approve_action_id,
            deny_action_id=deny_action_id,
            mcp_server_name=mcp_server_name,
        )

        tool_approval_request_payload_dto.additional_properties = d
        return tool_approval_request_payload_dto

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
