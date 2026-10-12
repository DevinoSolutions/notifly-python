from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_ref_dto import FileRefDto
    from ..models.tool_approval_card_reply_content_dto_tool_approval_card import (
        ToolApprovalCardReplyContentDtoToolApprovalCard,
    )


T = TypeVar("T", bound="ToolApprovalCardReplyContentDto")


@_attrs_define
class ToolApprovalCardReplyContentDto:
    """
    Attributes:
        tool_approval_card (ToolApprovalCardReplyContentDtoToolApprovalCard): Novu tool-approval card descriptor (`type:
            "tool-approval-card"`). Used with `toolApprovalRequest` to render Approve/Deny UI. Example: {'type': 'tool-
            approval-card', 'title': 'Approve refund?', 'subtitle': 'issue_refund · ORD-42 · $25.00', 'approveLabel':
            'Approve', 'denyLabel': 'Deny'}.
        files (list[FileRefDto] | Unset):
    """

    tool_approval_card: ToolApprovalCardReplyContentDtoToolApprovalCard
    files: list[FileRefDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_approval_card = self.tool_approval_card.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toolApprovalCard": tool_approval_card,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_ref_dto import FileRefDto
        from ..models.tool_approval_card_reply_content_dto_tool_approval_card import (
            ToolApprovalCardReplyContentDtoToolApprovalCard,
        )

        d = dict(src_dict)
        tool_approval_card = ToolApprovalCardReplyContentDtoToolApprovalCard.from_dict(d.pop("toolApprovalCard"))

        _files = d.pop("files", UNSET)
        files: list[FileRefDto] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileRefDto.from_dict(files_item_data)

                files.append(files_item)

        tool_approval_card_reply_content_dto = cls(
            tool_approval_card=tool_approval_card,
            files=files,
        )

        tool_approval_card_reply_content_dto.additional_properties = d
        return tool_approval_card_reply_content_dto

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
