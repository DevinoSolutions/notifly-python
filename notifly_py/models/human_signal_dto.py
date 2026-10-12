from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.human_signal_dto_kind import HumanSignalDtoKind
from ..models.human_signal_dto_type import HumanSignalDtoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HumanSignalDto")


@_attrs_define
class HumanSignalDto:
    """
    Attributes:
        type_ (HumanSignalDtoType):
        kind (HumanSignalDtoKind): Interaction verb queued by `ctx.ask` / `ctx.approve` / `ctx.choose` / `ctx.tell`.
            Example: approve.
        prompt (str): Question, action description, or one-way message shown to the human. Example: Deploy v2.4.1 to
            production?.
        request_id (str): Client-minted id returned by the framework helper; echoed on `ctx.humanResponse.requestId`.
            Example: hr_7c2e1a3b-4d5f-6789-abcd-ef0123456789.
        options (list[str] | Unset): Choice labels — required for `choose`, ignored otherwise. Example: ['us-east', 'eu-
            west'].
        from_ (str | Unset): Attribution label rendered in the card. Example: deploy-bot.
        ttl_seconds (float | Unset): Seconds until the interaction expires. Default 86400 (24h), max 259200. Example:
            3600.
        to (list[str] | str | Unset): Novu subscriberId(s) allowed to settle this interaction (max 50). First valid
            answer wins. When omitted, the conversation subscriber is used. Subscriber ids only — not workflow topic
            recipients.
    """

    type_: HumanSignalDtoType
    kind: HumanSignalDtoKind
    prompt: str
    request_id: str
    options: list[str] | Unset = UNSET
    from_: str | Unset = UNSET
    ttl_seconds: float | Unset = UNSET
    to: list[str] | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        kind = self.kind.value

        prompt = self.prompt

        request_id = self.request_id

        options: list[str] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options

        from_ = self.from_

        ttl_seconds = self.ttl_seconds

        to: list[str] | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, list):
            to = self.to

        else:
            to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "kind": kind,
                "prompt": prompt,
                "requestId": request_id,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options
        if from_ is not UNSET:
            field_dict["from"] = from_
        if ttl_seconds is not UNSET:
            field_dict["ttlSeconds"] = ttl_seconds
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = HumanSignalDtoType(d.pop("type"))

        kind = HumanSignalDtoKind(d.pop("kind"))

        prompt = d.pop("prompt")

        request_id = d.pop("requestId")

        options = cast(list[str], d.pop("options", UNSET))

        from_ = d.pop("from", UNSET)

        ttl_seconds = d.pop("ttlSeconds", UNSET)

        def _parse_to(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_type_1 = cast(list[str], data)

                return to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        human_signal_dto = cls(
            type_=type_,
            kind=kind,
            prompt=prompt,
            request_id=request_id,
            options=options,
            from_=from_,
            ttl_seconds=ttl_seconds,
            to=to,
        )

        human_signal_dto.additional_properties = d
        return human_signal_dto

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
