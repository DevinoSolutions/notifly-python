from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delay_step_response_dto_provider_overrides_type_0_additional_property import (
        DelayStepResponseDtoProviderOverridesType0AdditionalProperty,
    )


T = TypeVar("T", bound="DelayStepResponseDtoProviderOverridesType0")


@_attrs_define
class DelayStepResponseDtoProviderOverridesType0:
    """Per-provider content overrides keyed by providerId. Stored separately from controlValues and merged over the default
    body at send time. Keys are ChatProviderIdEnum / ToolProviderIdEnum values (e.g. `slack`, `whatsapp-business`,
    `pagerduty`).

        Example:
            {'slack': {'text': '{{payload.title}}', 'blocks': [{'type': 'divider'}]}, 'whatsapp-business': {'type': 'text',
                'text': {'body': '{{payload.title}}'}}, 'pagerduty': {'severity': 'warning', 'source': 'novu', 'summary':
                '{{payload.title}}'}}

    """

    additional_properties: dict[str, DelayStepResponseDtoProviderOverridesType0AdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delay_step_response_dto_provider_overrides_type_0_additional_property import (
            DelayStepResponseDtoProviderOverridesType0AdditionalProperty,
        )

        d = dict(src_dict)
        delay_step_response_dto_provider_overrides_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DelayStepResponseDtoProviderOverridesType0AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        delay_step_response_dto_provider_overrides_type_0.additional_properties = additional_properties
        return delay_step_response_dto_provider_overrides_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DelayStepResponseDtoProviderOverridesType0AdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DelayStepResponseDtoProviderOverridesType0AdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
