from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.card_reply_content_dto import CardReplyContentDto
    from ..models.markdown_reply_content_dto import MarkdownReplyContentDto
    from ..models.tool_approval_card_reply_content_dto import ToolApprovalCardReplyContentDto


T = TypeVar("T", bound="EditPayloadDto")


@_attrs_define
class EditPayloadDto:
    """
    Attributes:
        message_id (str): Platform message id of the message to edit. Example: 1712345678.123456.
        content (CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto): Replacement content.
            Exactly one of markdown, card, or toolApprovalCard.
    """

    message_id: str
    content: CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.card_reply_content_dto import CardReplyContentDto
        from ..models.markdown_reply_content_dto import MarkdownReplyContentDto

        message_id = self.message_id

        content: dict[str, Any]
        if isinstance(self.content, MarkdownReplyContentDto):
            content = self.content.to_dict()
        elif isinstance(self.content, CardReplyContentDto):
            content = self.content.to_dict()
        else:
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_reply_content_dto import CardReplyContentDto
        from ..models.markdown_reply_content_dto import MarkdownReplyContentDto
        from ..models.tool_approval_card_reply_content_dto import ToolApprovalCardReplyContentDto

        d = dict(src_dict)
        message_id = d.pop("messageId")

        def _parse_content(
            data: object,
        ) -> CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = MarkdownReplyContentDto.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = CardReplyContentDto.from_dict(data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            content_type_2 = ToolApprovalCardReplyContentDto.from_dict(data)

            return content_type_2

        content = _parse_content(d.pop("content"))

        edit_payload_dto = cls(
            message_id=message_id,
            content=content,
        )

        edit_payload_dto.additional_properties = d
        return edit_payload_dto

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
