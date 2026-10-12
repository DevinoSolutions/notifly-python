from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_behavior_dto_subscriber_access import AgentBehaviorDtoSubscriberAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentBehaviorDto")


@_attrs_define
class AgentBehaviorDto:
    """
    Attributes:
        acknowledge_on_received (bool | Unset): Acknowledge incoming messages. On platforms that support a native typing
            indicator (e.g. Slack, WhatsApp, Microsoft Teams, Telegram), shows a "Typing…" indicator while the agent
            processes the message. On platforms that do not (e.g. Email), reacts with an "eyes" emoji to the first inbound
            message in a thread. Default: true Default: True.
        reaction_on_resolved (None | str | Unset): Cross-platform emoji name for resolved conversations (e.g. "check",
            "star"). Set to null to disable. Default: "check" Default: 'check'.
        subscriber_access (AgentBehaviorDtoSubscriberAccess | Unset): Controls whether the agent accepts inbound
            messages from senders not yet linked to a subscriber, across all channels. "open" on managed agents auto-creates
            a lightweight subscriber so the agent can reply; on custom-code / self-hosted agents, the turn is forwarded to
            the bridge with a null subscriber. "restricted" rejects unknown senders with a managed denial reply (any
            runtime). Optional on update (partial PATCH). Persisted agents always have a value — managed create defaults to
            "open"; self-hosted create defaults to "restricted".
    """

    acknowledge_on_received: bool | Unset = True
    reaction_on_resolved: None | str | Unset = "check"
    subscriber_access: AgentBehaviorDtoSubscriberAccess | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledge_on_received = self.acknowledge_on_received

        reaction_on_resolved: None | str | Unset
        if isinstance(self.reaction_on_resolved, Unset):
            reaction_on_resolved = UNSET
        else:
            reaction_on_resolved = self.reaction_on_resolved

        subscriber_access: str | Unset = UNSET
        if not isinstance(self.subscriber_access, Unset):
            subscriber_access = self.subscriber_access.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledge_on_received is not UNSET:
            field_dict["acknowledgeOnReceived"] = acknowledge_on_received
        if reaction_on_resolved is not UNSET:
            field_dict["reactionOnResolved"] = reaction_on_resolved
        if subscriber_access is not UNSET:
            field_dict["subscriberAccess"] = subscriber_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledge_on_received = d.pop("acknowledgeOnReceived", UNSET)

        def _parse_reaction_on_resolved(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reaction_on_resolved = _parse_reaction_on_resolved(d.pop("reactionOnResolved", UNSET))

        _subscriber_access = d.pop("subscriberAccess", UNSET)
        subscriber_access: AgentBehaviorDtoSubscriberAccess | Unset
        if isinstance(_subscriber_access, Unset):
            subscriber_access = UNSET
        else:
            subscriber_access = AgentBehaviorDtoSubscriberAccess(_subscriber_access)

        agent_behavior_dto = cls(
            acknowledge_on_received=acknowledge_on_received,
            reaction_on_resolved=reaction_on_resolved,
            subscriber_access=subscriber_access,
        )

        agent_behavior_dto.additional_properties = d
        return agent_behavior_dto

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
