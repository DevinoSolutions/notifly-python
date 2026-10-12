from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_agent_request_dto_runtime import CreateAgentRequestDtoRuntime
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_runtime_dto import ManagedRuntimeDto


T = TypeVar("T", bound="CreateAgentRequestDto")


@_attrs_define
class CreateAgentRequestDto:
    """
    Attributes:
        name (str): Required when not adopting an existing managed agent (i.e. when managedRuntime.externalAgentId is
            absent). Optional in adopt mode where the name is resolved from the provider.
        identifier (str): Required when not adopting an existing managed agent. Auto-generated from the provider agent
            name when omitted in adopt mode.
        description (str | Unset):
        active (bool | Unset):  Default: True.
        runtime (CreateAgentRequestDtoRuntime | Unset):
        managed_runtime (ManagedRuntimeDto | Unset):
    """

    name: str
    identifier: str
    description: str | Unset = UNSET
    active: bool | Unset = True
    runtime: CreateAgentRequestDtoRuntime | Unset = UNSET
    managed_runtime: ManagedRuntimeDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        description = self.description

        active = self.active

        runtime: str | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.value

        managed_runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.managed_runtime, Unset):
            managed_runtime = self.managed_runtime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identifier": identifier,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if managed_runtime is not UNSET:
            field_dict["managedRuntime"] = managed_runtime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.managed_runtime_dto import ManagedRuntimeDto

        d = dict(src_dict)
        name = d.pop("name")

        identifier = d.pop("identifier")

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        _runtime = d.pop("runtime", UNSET)
        runtime: CreateAgentRequestDtoRuntime | Unset
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = CreateAgentRequestDtoRuntime(_runtime)

        _managed_runtime = d.pop("managedRuntime", UNSET)
        managed_runtime: ManagedRuntimeDto | Unset
        if isinstance(_managed_runtime, Unset):
            managed_runtime = UNSET
        else:
            managed_runtime = ManagedRuntimeDto.from_dict(_managed_runtime)

        create_agent_request_dto = cls(
            name=name,
            identifier=identifier,
            description=description,
            active=active,
            runtime=runtime,
            managed_runtime=managed_runtime,
        )

        create_agent_request_dto.additional_properties = d
        return create_agent_request_dto

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
