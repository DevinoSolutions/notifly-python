from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_reply_payload_dto_typing_type_0 import AgentReplyPayloadDtoTypingType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_reaction_payload_dto import AddReactionPayloadDto
    from ..models.card_reply_content_dto import CardReplyContentDto
    from ..models.delete_message_payload_dto import DeleteMessagePayloadDto
    from ..models.edit_payload_dto import EditPayloadDto
    from ..models.human_signal_dto import HumanSignalDto
    from ..models.markdown_reply_content_dto import MarkdownReplyContentDto
    from ..models.metadata_clear_signal_dto import MetadataClearSignalDto
    from ..models.metadata_delete_signal_dto import MetadataDeleteSignalDto
    from ..models.metadata_set_signal_dto import MetadataSetSignalDto
    from ..models.resolve_dto import ResolveDto
    from ..models.tool_approval_card_reply_content_dto import ToolApprovalCardReplyContentDto
    from ..models.tool_approval_request_payload_dto import ToolApprovalRequestPayloadDto
    from ..models.tool_result_dto import ToolResultDto
    from ..models.trigger_signal_dto import TriggerSignalDto
    from ..models.typing_status_dto import TypingStatusDto


T = TypeVar("T", bound="AgentReplyPayloadDto")


@_attrs_define
class AgentReplyPayloadDto:
    """
    Attributes:
        conversation_id (str): Conversation id to reply into. Obtained from the inbound agent event / bridge payload.
            Example: 64f5a1c2e8b7a3d9f0c1b2a3.
        integration_identifier (str): Channel integration identifier linked to the agent for this conversation (e.g.
            `slack-support`). Example: slack-support.
        reply (CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto | Unset): Outbound
            message content. Exactly one of `markdown`, `card`, or `toolApprovalCard`. Optional `files` attach to the
            message. Cannot be combined with `edit`.
        tool_approval_request (ToolApprovalRequestPayloadDto | Unset):
        edit (EditPayloadDto | Unset):
        resolve (ResolveDto | Unset):
        signals (list[HumanSignalDto | MetadataClearSignalDto | MetadataDeleteSignalDto | MetadataSetSignalDto |
            TriggerSignalDto] | Unset): Side-effect signals executed during this turn: conversation metadata mutations, Novu
            workflow triggers, or human-in-the-loop interactions.
        tool_results (list[ToolResultDto] | Unset): Tool-call outcomes to persist in conversation history (typically
            before the assistant reply).
        add_reactions (list[AddReactionPayloadDto] | Unset): Emoji reactions to add to existing platform messages.
        delete_messages (list[DeleteMessagePayloadDto] | Unset): Delete previously posted platform messages. Removes the
            rendered message only — history is preserved.
        typing (AgentReplyPayloadDtoTypingType0 | TypingStatusDto | Unset): Per-turn typing/status control. Pass `{
            status?: string }` to set/update the status (omit `status` for "Thinking…"), or `"stop"` to clear it. Best-
            effort per platform. Example: {'status': 'Looking up your order…'}.
        error (bool | Unset): Bridge reports that the customer runtime failed this turn. Cannot be combined with other
            actions. Novu delivers generic user-facing error copy. Example: True.
    """

    conversation_id: str
    integration_identifier: str
    reply: CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto | Unset = UNSET
    tool_approval_request: ToolApprovalRequestPayloadDto | Unset = UNSET
    edit: EditPayloadDto | Unset = UNSET
    resolve: ResolveDto | Unset = UNSET
    signals: (
        list[
            HumanSignalDto | MetadataClearSignalDto | MetadataDeleteSignalDto | MetadataSetSignalDto | TriggerSignalDto
        ]
        | Unset
    ) = UNSET
    tool_results: list[ToolResultDto] | Unset = UNSET
    add_reactions: list[AddReactionPayloadDto] | Unset = UNSET
    delete_messages: list[DeleteMessagePayloadDto] | Unset = UNSET
    typing: AgentReplyPayloadDtoTypingType0 | TypingStatusDto | Unset = UNSET
    error: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.card_reply_content_dto import CardReplyContentDto
        from ..models.markdown_reply_content_dto import MarkdownReplyContentDto
        from ..models.metadata_clear_signal_dto import MetadataClearSignalDto
        from ..models.metadata_delete_signal_dto import MetadataDeleteSignalDto
        from ..models.metadata_set_signal_dto import MetadataSetSignalDto
        from ..models.trigger_signal_dto import TriggerSignalDto

        conversation_id = self.conversation_id

        integration_identifier = self.integration_identifier

        reply: dict[str, Any] | Unset
        if isinstance(self.reply, Unset):
            reply = UNSET
        elif isinstance(self.reply, MarkdownReplyContentDto):
            reply = self.reply.to_dict()
        elif isinstance(self.reply, CardReplyContentDto):
            reply = self.reply.to_dict()
        else:
            reply = self.reply.to_dict()

        tool_approval_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_approval_request, Unset):
            tool_approval_request = self.tool_approval_request.to_dict()

        edit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.edit, Unset):
            edit = self.edit.to_dict()

        resolve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolve, Unset):
            resolve = self.resolve.to_dict()

        signals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.signals, Unset):
            signals = []
            for signals_item_data in self.signals:
                signals_item: dict[str, Any]
                if isinstance(signals_item_data, MetadataSetSignalDto):
                    signals_item = signals_item_data.to_dict()
                elif isinstance(signals_item_data, MetadataDeleteSignalDto):
                    signals_item = signals_item_data.to_dict()
                elif isinstance(signals_item_data, MetadataClearSignalDto):
                    signals_item = signals_item_data.to_dict()
                elif isinstance(signals_item_data, TriggerSignalDto):
                    signals_item = signals_item_data.to_dict()
                else:
                    signals_item = signals_item_data.to_dict()

                signals.append(signals_item)

        tool_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool_results, Unset):
            tool_results = []
            for tool_results_item_data in self.tool_results:
                tool_results_item = tool_results_item_data.to_dict()
                tool_results.append(tool_results_item)

        add_reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add_reactions, Unset):
            add_reactions = []
            for add_reactions_item_data in self.add_reactions:
                add_reactions_item = add_reactions_item_data.to_dict()
                add_reactions.append(add_reactions_item)

        delete_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delete_messages, Unset):
            delete_messages = []
            for delete_messages_item_data in self.delete_messages:
                delete_messages_item = delete_messages_item_data.to_dict()
                delete_messages.append(delete_messages_item)

        typing: dict[str, Any] | str | Unset
        if isinstance(self.typing, Unset):
            typing = UNSET
        elif isinstance(self.typing, AgentReplyPayloadDtoTypingType0):
            typing = self.typing.value
        else:
            typing = self.typing.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversationId": conversation_id,
                "integrationIdentifier": integration_identifier,
            }
        )
        if reply is not UNSET:
            field_dict["reply"] = reply
        if tool_approval_request is not UNSET:
            field_dict["toolApprovalRequest"] = tool_approval_request
        if edit is not UNSET:
            field_dict["edit"] = edit
        if resolve is not UNSET:
            field_dict["resolve"] = resolve
        if signals is not UNSET:
            field_dict["signals"] = signals
        if tool_results is not UNSET:
            field_dict["toolResults"] = tool_results
        if add_reactions is not UNSET:
            field_dict["addReactions"] = add_reactions
        if delete_messages is not UNSET:
            field_dict["deleteMessages"] = delete_messages
        if typing is not UNSET:
            field_dict["typing"] = typing
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_reaction_payload_dto import AddReactionPayloadDto
        from ..models.card_reply_content_dto import CardReplyContentDto
        from ..models.delete_message_payload_dto import DeleteMessagePayloadDto
        from ..models.edit_payload_dto import EditPayloadDto
        from ..models.human_signal_dto import HumanSignalDto
        from ..models.markdown_reply_content_dto import MarkdownReplyContentDto
        from ..models.metadata_clear_signal_dto import MetadataClearSignalDto
        from ..models.metadata_delete_signal_dto import MetadataDeleteSignalDto
        from ..models.metadata_set_signal_dto import MetadataSetSignalDto
        from ..models.resolve_dto import ResolveDto
        from ..models.tool_approval_card_reply_content_dto import ToolApprovalCardReplyContentDto
        from ..models.tool_approval_request_payload_dto import ToolApprovalRequestPayloadDto
        from ..models.tool_result_dto import ToolResultDto
        from ..models.trigger_signal_dto import TriggerSignalDto
        from ..models.typing_status_dto import TypingStatusDto

        d = dict(src_dict)
        conversation_id = d.pop("conversationId")

        integration_identifier = d.pop("integrationIdentifier")

        def _parse_reply(
            data: object,
        ) -> CardReplyContentDto | MarkdownReplyContentDto | ToolApprovalCardReplyContentDto | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_type_0 = MarkdownReplyContentDto.from_dict(data)

                return reply_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_type_1 = CardReplyContentDto.from_dict(data)

                return reply_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            reply_type_2 = ToolApprovalCardReplyContentDto.from_dict(data)

            return reply_type_2

        reply = _parse_reply(d.pop("reply", UNSET))

        _tool_approval_request = d.pop("toolApprovalRequest", UNSET)
        tool_approval_request: ToolApprovalRequestPayloadDto | Unset
        if isinstance(_tool_approval_request, Unset):
            tool_approval_request = UNSET
        else:
            tool_approval_request = ToolApprovalRequestPayloadDto.from_dict(_tool_approval_request)

        _edit = d.pop("edit", UNSET)
        edit: EditPayloadDto | Unset
        if isinstance(_edit, Unset):
            edit = UNSET
        else:
            edit = EditPayloadDto.from_dict(_edit)

        _resolve = d.pop("resolve", UNSET)
        resolve: ResolveDto | Unset
        if isinstance(_resolve, Unset):
            resolve = UNSET
        else:
            resolve = ResolveDto.from_dict(_resolve)

        _signals = d.pop("signals", UNSET)
        signals: (
            list[
                HumanSignalDto
                | MetadataClearSignalDto
                | MetadataDeleteSignalDto
                | MetadataSetSignalDto
                | TriggerSignalDto
            ]
            | Unset
        ) = UNSET
        if _signals is not UNSET:
            signals = []
            for signals_item_data in _signals:

                def _parse_signals_item(
                    data: object,
                ) -> (
                    HumanSignalDto
                    | MetadataClearSignalDto
                    | MetadataDeleteSignalDto
                    | MetadataSetSignalDto
                    | TriggerSignalDto
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        signals_item_type_0 = MetadataSetSignalDto.from_dict(data)

                        return signals_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        signals_item_type_1 = MetadataDeleteSignalDto.from_dict(data)

                        return signals_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        signals_item_type_2 = MetadataClearSignalDto.from_dict(data)

                        return signals_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        signals_item_type_3 = TriggerSignalDto.from_dict(data)

                        return signals_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    signals_item_type_4 = HumanSignalDto.from_dict(data)

                    return signals_item_type_4

                signals_item = _parse_signals_item(signals_item_data)

                signals.append(signals_item)

        _tool_results = d.pop("toolResults", UNSET)
        tool_results: list[ToolResultDto] | Unset = UNSET
        if _tool_results is not UNSET:
            tool_results = []
            for tool_results_item_data in _tool_results:
                tool_results_item = ToolResultDto.from_dict(tool_results_item_data)

                tool_results.append(tool_results_item)

        _add_reactions = d.pop("addReactions", UNSET)
        add_reactions: list[AddReactionPayloadDto] | Unset = UNSET
        if _add_reactions is not UNSET:
            add_reactions = []
            for add_reactions_item_data in _add_reactions:
                add_reactions_item = AddReactionPayloadDto.from_dict(add_reactions_item_data)

                add_reactions.append(add_reactions_item)

        _delete_messages = d.pop("deleteMessages", UNSET)
        delete_messages: list[DeleteMessagePayloadDto] | Unset = UNSET
        if _delete_messages is not UNSET:
            delete_messages = []
            for delete_messages_item_data in _delete_messages:
                delete_messages_item = DeleteMessagePayloadDto.from_dict(delete_messages_item_data)

                delete_messages.append(delete_messages_item)

        def _parse_typing(data: object) -> AgentReplyPayloadDtoTypingType0 | TypingStatusDto | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                typing_type_0 = AgentReplyPayloadDtoTypingType0(data)

                return typing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            typing_type_1 = TypingStatusDto.from_dict(data)

            return typing_type_1

        typing = _parse_typing(d.pop("typing", UNSET))

        error = d.pop("error", UNSET)

        agent_reply_payload_dto = cls(
            conversation_id=conversation_id,
            integration_identifier=integration_identifier,
            reply=reply,
            tool_approval_request=tool_approval_request,
            edit=edit,
            resolve=resolve,
            signals=signals,
            tool_results=tool_results,
            add_reactions=add_reactions,
            delete_messages=delete_messages,
            typing=typing,
            error=error,
        )

        agent_reply_payload_dto.additional_properties = d
        return agent_reply_payload_dto

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
