from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_payload_dto_context import PreviewPayloadDtoContext
    from ..models.preview_payload_dto_env import PreviewPayloadDtoEnv
    from ..models.preview_payload_dto_payload import PreviewPayloadDtoPayload
    from ..models.preview_payload_dto_steps import PreviewPayloadDtoSteps
    from ..models.subscriber_response_dto_optional import SubscriberResponseDtoOptional


T = TypeVar("T", bound="PreviewPayloadDto")


@_attrs_define
class PreviewPayloadDto:
    """
    Attributes:
        subscriber (SubscriberResponseDtoOptional | Unset):
        actor (SubscriberResponseDtoOptional | Unset):
        payload (PreviewPayloadDtoPayload | Unset): Payload data
        steps (PreviewPayloadDtoSteps | Unset): Steps data
        context (PreviewPayloadDtoContext | Unset):
        env (PreviewPayloadDtoEnv | Unset): Environment variables data
    """

    subscriber: SubscriberResponseDtoOptional | Unset = UNSET
    actor: SubscriberResponseDtoOptional | Unset = UNSET
    payload: PreviewPayloadDtoPayload | Unset = UNSET
    steps: PreviewPayloadDtoSteps | Unset = UNSET
    context: PreviewPayloadDtoContext | Unset = UNSET
    env: PreviewPayloadDtoEnv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriber: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps.to_dict()

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber
        if actor is not UNSET:
            field_dict["actor"] = actor
        if payload is not UNSET:
            field_dict["payload"] = payload
        if steps is not UNSET:
            field_dict["steps"] = steps
        if context is not UNSET:
            field_dict["context"] = context
        if env is not UNSET:
            field_dict["env"] = env

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_payload_dto_context import PreviewPayloadDtoContext
        from ..models.preview_payload_dto_env import PreviewPayloadDtoEnv
        from ..models.preview_payload_dto_payload import PreviewPayloadDtoPayload
        from ..models.preview_payload_dto_steps import PreviewPayloadDtoSteps
        from ..models.subscriber_response_dto_optional import SubscriberResponseDtoOptional

        d = dict(src_dict)
        _subscriber = d.pop("subscriber", UNSET)
        subscriber: SubscriberResponseDtoOptional | Unset
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = SubscriberResponseDtoOptional.from_dict(_subscriber)

        _actor = d.pop("actor", UNSET)
        actor: SubscriberResponseDtoOptional | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = SubscriberResponseDtoOptional.from_dict(_actor)

        _payload = d.pop("payload", UNSET)
        payload: PreviewPayloadDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = PreviewPayloadDtoPayload.from_dict(_payload)

        _steps = d.pop("steps", UNSET)
        steps: PreviewPayloadDtoSteps | Unset
        if isinstance(_steps, Unset):
            steps = UNSET
        else:
            steps = PreviewPayloadDtoSteps.from_dict(_steps)

        _context = d.pop("context", UNSET)
        context: PreviewPayloadDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = PreviewPayloadDtoContext.from_dict(_context)

        _env = d.pop("env", UNSET)
        env: PreviewPayloadDtoEnv | Unset
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = PreviewPayloadDtoEnv.from_dict(_env)

        preview_payload_dto = cls(
            subscriber=subscriber,
            actor=actor,
            payload=payload,
            steps=steps,
            context=context,
            env=env,
        )

        preview_payload_dto.additional_properties = d
        return preview_payload_dto

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
