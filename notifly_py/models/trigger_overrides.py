from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_level_enum import SeverityLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_overrides import ChannelOverrides
    from ..models.trigger_overrides_chat import TriggerOverridesChat
    from ..models.trigger_overrides_email import TriggerOverridesEmail
    from ..models.trigger_overrides_providers import TriggerOverridesProviders
    from ..models.trigger_overrides_push import TriggerOverridesPush
    from ..models.trigger_overrides_sms import TriggerOverridesSms
    from ..models.trigger_overrides_steps import TriggerOverridesSteps


T = TypeVar("T", bound="TriggerOverrides")


@_attrs_define
class TriggerOverrides:
    """
    Attributes:
        steps (TriggerOverridesSteps | Unset): This could be used to override provider specific configurations or layout
            at the step level Example: {'email-step': {'providers': {'sendgrid': {'templateId': '1234567890'}}, 'layoutId':
            'step-specific-layout'}}.
        channels (ChannelOverrides | Unset):
        providers (TriggerOverridesProviders | Unset): Overrides the provider configuration for the entire workflow and
            all steps Example: {'sendgrid': {'templateId': '1234567890'}}.
        email (TriggerOverridesEmail | Unset): Override the email provider specific configurations for the entire
            workflow
        push (TriggerOverridesPush | Unset): Override the push provider specific configurations for the entire workflow
        sms (TriggerOverridesSms | Unset): Override the sms provider specific configurations for the entire workflow
        chat (TriggerOverridesChat | Unset): Override the chat provider specific configurations for the entire workflow
        layout_identifier (str | Unset): Override the layout identifier for the entire workflow
        severity (SeverityLevelEnum | Unset): Severity of the workflow
    """

    steps: TriggerOverridesSteps | Unset = UNSET
    channels: ChannelOverrides | Unset = UNSET
    providers: TriggerOverridesProviders | Unset = UNSET
    email: TriggerOverridesEmail | Unset = UNSET
    push: TriggerOverridesPush | Unset = UNSET
    sms: TriggerOverridesSms | Unset = UNSET
    chat: TriggerOverridesChat | Unset = UNSET
    layout_identifier: str | Unset = UNSET
    severity: SeverityLevelEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps.to_dict()

        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        push: dict[str, Any] | Unset = UNSET
        if not isinstance(self.push, Unset):
            push = self.push.to_dict()

        sms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sms, Unset):
            sms = self.sms.to_dict()

        chat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chat, Unset):
            chat = self.chat.to_dict()

        layout_identifier = self.layout_identifier

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if steps is not UNSET:
            field_dict["steps"] = steps
        if channels is not UNSET:
            field_dict["channels"] = channels
        if providers is not UNSET:
            field_dict["providers"] = providers
        if email is not UNSET:
            field_dict["email"] = email
        if push is not UNSET:
            field_dict["push"] = push
        if sms is not UNSET:
            field_dict["sms"] = sms
        if chat is not UNSET:
            field_dict["chat"] = chat
        if layout_identifier is not UNSET:
            field_dict["layoutIdentifier"] = layout_identifier
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_overrides import ChannelOverrides
        from ..models.trigger_overrides_chat import TriggerOverridesChat
        from ..models.trigger_overrides_email import TriggerOverridesEmail
        from ..models.trigger_overrides_providers import TriggerOverridesProviders
        from ..models.trigger_overrides_push import TriggerOverridesPush
        from ..models.trigger_overrides_sms import TriggerOverridesSms
        from ..models.trigger_overrides_steps import TriggerOverridesSteps

        d = dict(src_dict)
        _steps = d.pop("steps", UNSET)
        steps: TriggerOverridesSteps | Unset
        if isinstance(_steps, Unset):
            steps = UNSET
        else:
            steps = TriggerOverridesSteps.from_dict(_steps)

        _channels = d.pop("channels", UNSET)
        channels: ChannelOverrides | Unset
        if isinstance(_channels, Unset):
            channels = UNSET
        else:
            channels = ChannelOverrides.from_dict(_channels)

        _providers = d.pop("providers", UNSET)
        providers: TriggerOverridesProviders | Unset
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = TriggerOverridesProviders.from_dict(_providers)

        _email = d.pop("email", UNSET)
        email: TriggerOverridesEmail | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = TriggerOverridesEmail.from_dict(_email)

        _push = d.pop("push", UNSET)
        push: TriggerOverridesPush | Unset
        if isinstance(_push, Unset):
            push = UNSET
        else:
            push = TriggerOverridesPush.from_dict(_push)

        _sms = d.pop("sms", UNSET)
        sms: TriggerOverridesSms | Unset
        if isinstance(_sms, Unset):
            sms = UNSET
        else:
            sms = TriggerOverridesSms.from_dict(_sms)

        _chat = d.pop("chat", UNSET)
        chat: TriggerOverridesChat | Unset
        if isinstance(_chat, Unset):
            chat = UNSET
        else:
            chat = TriggerOverridesChat.from_dict(_chat)

        layout_identifier = d.pop("layoutIdentifier", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: SeverityLevelEnum | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityLevelEnum(_severity)

        trigger_overrides = cls(
            steps=steps,
            channels=channels,
            providers=providers,
            email=email,
            push=push,
            sms=sms,
            chat=chat,
            layout_identifier=layout_identifier,
            severity=severity,
        )

        trigger_overrides.additional_properties = d
        return trigger_overrides

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
