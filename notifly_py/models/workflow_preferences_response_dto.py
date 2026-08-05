from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_preferences_dto import WorkflowPreferencesDto


T = TypeVar("T", bound="WorkflowPreferencesResponseDto")


@_attrs_define
class WorkflowPreferencesResponseDto:
    """
    Attributes:
        default (WorkflowPreferencesDto):
        user (None | Unset | WorkflowPreferencesDto): User-specific workflow preferences
    """

    default: WorkflowPreferencesDto
    user: None | Unset | WorkflowPreferencesDto = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_preferences_dto import WorkflowPreferencesDto

        default = self.default.to_dict()

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, WorkflowPreferencesDto):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_preferences_dto import WorkflowPreferencesDto

        d = dict(src_dict)
        default = WorkflowPreferencesDto.from_dict(d.pop("default"))

        def _parse_user(data: object) -> None | Unset | WorkflowPreferencesDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = WorkflowPreferencesDto.from_dict(data)

                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowPreferencesDto, data)

        user = _parse_user(d.pop("user", UNSET))

        workflow_preferences_response_dto = cls(
            default=default,
            user=user,
        )

        workflow_preferences_response_dto.additional_properties = d
        return workflow_preferences_response_dto

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
