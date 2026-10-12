from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_agent_config_dto_providers_additional_property import (
        WorkflowAgentConfigDtoProvidersAdditionalProperty,
    )


T = TypeVar("T", bound="WorkflowAgentConfigDtoProviders")


@_attrs_define
class WorkflowAgentConfigDtoProviders:
    """Optional per-provider overrides keyed by providerId (e.g. novu-email-agent). Today only Novu Email replyTo is
    supported.

    """

    additional_properties: dict[str, WorkflowAgentConfigDtoProvidersAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_agent_config_dto_providers_additional_property import (
            WorkflowAgentConfigDtoProvidersAdditionalProperty,
        )

        d = dict(src_dict)
        workflow_agent_config_dto_providers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = WorkflowAgentConfigDtoProvidersAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        workflow_agent_config_dto_providers.additional_properties = additional_properties
        return workflow_agent_config_dto_providers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> WorkflowAgentConfigDtoProvidersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: WorkflowAgentConfigDtoProvidersAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
