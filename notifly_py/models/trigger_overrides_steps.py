from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.steps_overrides import StepsOverrides


T = TypeVar("T", bound="TriggerOverridesSteps")


@_attrs_define
class TriggerOverridesSteps:
    """This could be used to override provider specific configurations or layout at the step level

    Example:
        {'email-step': {'providers': {'sendgrid': {'templateId': '1234567890'}}, 'layoutId': 'step-specific-layout'}}

    """

    additional_properties: dict[str, StepsOverrides] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.steps_overrides import StepsOverrides

        d = dict(src_dict)
        trigger_overrides_steps = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StepsOverrides.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        trigger_overrides_steps.additional_properties = additional_properties
        return trigger_overrides_steps

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StepsOverrides:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StepsOverrides) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
