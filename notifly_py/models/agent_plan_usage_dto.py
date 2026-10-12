from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_plan_usage_dto_limit_source import AgentPlanUsageDtoLimitSource

T = TypeVar("T", bound="AgentPlanUsageDto")


@_attrs_define
class AgentPlanUsageDto:
    """
    Attributes:
        used (float): Current usage count for the resource in this environment.
        limit (float): Amount included in the organization plan.
        total_created (float): Total agents in this environment, including inactive ones.
        creation_limit (float): Hard cap on total agents the organization can create per environment. For plan-limited
            tiers this is the plan limit plus a small grace buffer; for unlimited tiers it is the platform system limit.
        limit_source (AgentPlanUsageDtoLimitSource): Which constraint produced the limits. `plan` limits are lifted by
            upgrading; `system` limits (platform cap or per-organization override) require contacting the Novu team.
    """

    used: float
    limit: float
    total_created: float
    creation_limit: float
    limit_source: AgentPlanUsageDtoLimitSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        limit = self.limit

        total_created = self.total_created

        creation_limit = self.creation_limit

        limit_source = self.limit_source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "limit": limit,
                "totalCreated": total_created,
                "creationLimit": creation_limit,
                "limitSource": limit_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used")

        limit = d.pop("limit")

        total_created = d.pop("totalCreated")

        creation_limit = d.pop("creationLimit")

        limit_source = AgentPlanUsageDtoLimitSource(d.pop("limitSource"))

        agent_plan_usage_dto = cls(
            used=used,
            limit=limit,
            total_created=total_created,
            creation_limit=creation_limit,
            limit_source=limit_source,
        )

        agent_plan_usage_dto.additional_properties = d
        return agent_plan_usage_dto

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
