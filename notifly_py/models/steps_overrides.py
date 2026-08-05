from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.steps_overrides_providers import StepsOverridesProviders


T = TypeVar("T", bound="StepsOverrides")


@_attrs_define
class StepsOverrides:
    """
    Attributes:
        providers (StepsOverridesProviders | Unset): Passing the provider id and the provider specific configurations
            Example: {'sendgrid': {'templateId': '1234567890'}}.
        layout_id (None | str | Unset): Override the or remove the layout for this specific step Example: welcome-email-
            layout.
    """

    providers: StepsOverridesProviders | Unset = UNSET
    layout_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        layout_id: None | str | Unset
        if isinstance(self.layout_id, Unset):
            layout_id = UNSET
        else:
            layout_id = self.layout_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers
        if layout_id is not UNSET:
            field_dict["layoutId"] = layout_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.steps_overrides_providers import StepsOverridesProviders

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: StepsOverridesProviders | Unset
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = StepsOverridesProviders.from_dict(_providers)

        def _parse_layout_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layout_id = _parse_layout_id(d.pop("layoutId", UNSET))

        steps_overrides = cls(
            providers=providers,
            layout_id=layout_id,
        )

        steps_overrides.additional_properties = d
        return steps_overrides

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
