from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_dto import ActionDto
    from ..models.in_app_control_dto_data import InAppControlDtoData
    from ..models.in_app_control_dto_skip import InAppControlDtoSkip
    from ..models.redirect_dto import RedirectDto


T = TypeVar("T", bound="InAppControlDto")


@_attrs_define
class InAppControlDto:
    """
    Attributes:
        skip (InAppControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        body (str | Unset): Content/body of the in-app message. Required if subject is empty.
        subject (str | Unset): Subject/title of the in-app message. Required if body is empty.
        avatar (str | Unset): URL for an avatar image. Must be a valid URL or start with / or {{ variable }}.
        primary_action (ActionDto | Unset):
        secondary_action (ActionDto | Unset):
        redirect (RedirectDto | Unset):
        disable_output_sanitization (bool | Unset): Disable sanitization of the output. Default: False.
        data (InAppControlDtoData | Unset): Additional data payload for the step.
    """

    skip: InAppControlDtoSkip | Unset = UNSET
    body: str | Unset = UNSET
    subject: str | Unset = UNSET
    avatar: str | Unset = UNSET
    primary_action: ActionDto | Unset = UNSET
    secondary_action: ActionDto | Unset = UNSET
    redirect: RedirectDto | Unset = UNSET
    disable_output_sanitization: bool | Unset = False
    data: InAppControlDtoData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        body = self.body

        subject = self.subject

        avatar = self.avatar

        primary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_action, Unset):
            primary_action = self.primary_action.to_dict()

        secondary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secondary_action, Unset):
            secondary_action = self.secondary_action.to_dict()

        redirect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        disable_output_sanitization = self.disable_output_sanitization

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip is not UNSET:
            field_dict["skip"] = skip
        if body is not UNSET:
            field_dict["body"] = body
        if subject is not UNSET:
            field_dict["subject"] = subject
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if primary_action is not UNSET:
            field_dict["primaryAction"] = primary_action
        if secondary_action is not UNSET:
            field_dict["secondaryAction"] = secondary_action
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if disable_output_sanitization is not UNSET:
            field_dict["disableOutputSanitization"] = disable_output_sanitization
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dto import ActionDto
        from ..models.in_app_control_dto_data import InAppControlDtoData
        from ..models.in_app_control_dto_skip import InAppControlDtoSkip
        from ..models.redirect_dto import RedirectDto

        d = dict(src_dict)
        _skip = d.pop("skip", UNSET)
        skip: InAppControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = InAppControlDtoSkip.from_dict(_skip)

        body = d.pop("body", UNSET)

        subject = d.pop("subject", UNSET)

        avatar = d.pop("avatar", UNSET)

        _primary_action = d.pop("primaryAction", UNSET)
        primary_action: ActionDto | Unset
        if isinstance(_primary_action, Unset):
            primary_action = UNSET
        else:
            primary_action = ActionDto.from_dict(_primary_action)

        _secondary_action = d.pop("secondaryAction", UNSET)
        secondary_action: ActionDto | Unset
        if isinstance(_secondary_action, Unset):
            secondary_action = UNSET
        else:
            secondary_action = ActionDto.from_dict(_secondary_action)

        _redirect = d.pop("redirect", UNSET)
        redirect: RedirectDto | Unset
        if isinstance(_redirect, Unset):
            redirect = UNSET
        else:
            redirect = RedirectDto.from_dict(_redirect)

        disable_output_sanitization = d.pop("disableOutputSanitization", UNSET)

        _data = d.pop("data", UNSET)
        data: InAppControlDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InAppControlDtoData.from_dict(_data)

        in_app_control_dto = cls(
            skip=skip,
            body=body,
            subject=subject,
            avatar=avatar,
            primary_action=primary_action,
            secondary_action=secondary_action,
            redirect=redirect,
            disable_output_sanitization=disable_output_sanitization,
            data=data,
        )

        in_app_control_dto.additional_properties = d
        return in_app_control_dto

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
