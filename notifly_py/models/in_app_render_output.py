from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_dto import ActionDto
    from ..models.in_app_render_output_data import InAppRenderOutputData
    from ..models.redirect_dto import RedirectDto


T = TypeVar("T", bound="InAppRenderOutput")


@_attrs_define
class InAppRenderOutput:
    """
    Attributes:
        body (str): Body of the in-app notification
        subject (str | Unset): Subject of the in-app notification
        avatar (str | Unset): Avatar for the in-app notification
        primary_action (ActionDto | Unset):
        secondary_action (ActionDto | Unset):
        data (InAppRenderOutputData | Unset): Additional data
        redirect (RedirectDto | Unset):
    """

    body: str
    subject: str | Unset = UNSET
    avatar: str | Unset = UNSET
    primary_action: ActionDto | Unset = UNSET
    secondary_action: ActionDto | Unset = UNSET
    data: InAppRenderOutputData | Unset = UNSET
    redirect: RedirectDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        subject = self.subject

        avatar = self.avatar

        primary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_action, Unset):
            primary_action = self.primary_action.to_dict()

        secondary_action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secondary_action, Unset):
            secondary_action = self.secondary_action.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        redirect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if primary_action is not UNSET:
            field_dict["primaryAction"] = primary_action
        if secondary_action is not UNSET:
            field_dict["secondaryAction"] = secondary_action
        if data is not UNSET:
            field_dict["data"] = data
        if redirect is not UNSET:
            field_dict["redirect"] = redirect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_dto import ActionDto
        from ..models.in_app_render_output_data import InAppRenderOutputData
        from ..models.redirect_dto import RedirectDto

        d = dict(src_dict)
        body = d.pop("body")

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

        _data = d.pop("data", UNSET)
        data: InAppRenderOutputData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InAppRenderOutputData.from_dict(_data)

        _redirect = d.pop("redirect", UNSET)
        redirect: RedirectDto | Unset
        if isinstance(_redirect, Unset):
            redirect = UNSET
        else:
            redirect = RedirectDto.from_dict(_redirect)

        in_app_render_output = cls(
            body=body,
            subject=subject,
            avatar=avatar,
            primary_action=primary_action,
            secondary_action=secondary_action,
            data=data,
            redirect=redirect,
        )

        in_app_render_output.additional_properties = d
        return in_app_render_output

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
