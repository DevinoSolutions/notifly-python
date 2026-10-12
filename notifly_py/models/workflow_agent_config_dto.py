from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_agent_config_dto_providers import WorkflowAgentConfigDtoProviders


T = TypeVar("T", bound="WorkflowAgentConfigDto")


@_attrs_define
class WorkflowAgentConfigDto:
    """
    Attributes:
        identifier (str): Public agent identifier used to route this workflow through an agent's connected channels.
        providers (WorkflowAgentConfigDtoProviders | Unset): Optional per-provider overrides keyed by providerId (e.g.
            novu-email-agent). Today only Novu Email replyTo is supported.
    """

    identifier: str
    providers: WorkflowAgentConfigDtoProviders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
            }
        )
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_agent_config_dto_providers import WorkflowAgentConfigDtoProviders

        d = dict(src_dict)
        identifier = d.pop("identifier")

        _providers = d.pop("providers", UNSET)
        providers: WorkflowAgentConfigDtoProviders | Unset
        if isinstance(_providers, Unset):
            providers = UNSET
        else:
            providers = WorkflowAgentConfigDtoProviders.from_dict(_providers)

        workflow_agent_config_dto = cls(
            identifier=identifier,
            providers=providers,
        )

        workflow_agent_config_dto.additional_properties = d
        return workflow_agent_config_dto

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
