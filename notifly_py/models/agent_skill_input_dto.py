from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_skill_input_dto_type import AgentSkillInputDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_skill_input_dto_version_type_0 import AgentSkillInputDtoVersionType0


T = TypeVar("T", bound="AgentSkillInputDto")


@_attrs_define
class AgentSkillInputDto:
    """
    Attributes:
        type_ (AgentSkillInputDtoType):
        skill_id (str): Skill identifier, e.g. "xlsx" or "skill_01XJ5..."
        version (AgentSkillInputDtoVersionType0 | None | Unset): Version to pin. Omit for latest.
    """

    type_: AgentSkillInputDtoType
    skill_id: str
    version: AgentSkillInputDtoVersionType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_skill_input_dto_version_type_0 import AgentSkillInputDtoVersionType0

        type_ = self.type_.value

        skill_id = self.skill_id

        version: dict[str, Any] | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        elif isinstance(self.version, AgentSkillInputDtoVersionType0):
            version = self.version.to_dict()
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "skillId": skill_id,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_skill_input_dto_version_type_0 import AgentSkillInputDtoVersionType0

        d = dict(src_dict)
        type_ = AgentSkillInputDtoType(d.pop("type"))

        skill_id = d.pop("skillId")

        def _parse_version(data: object) -> AgentSkillInputDtoVersionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                version_type_0 = AgentSkillInputDtoVersionType0.from_dict(data)

                return version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentSkillInputDtoVersionType0 | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        agent_skill_input_dto = cls(
            type_=type_,
            skill_id=skill_id,
            version=version,
        )

        agent_skill_input_dto.additional_properties = d
        return agent_skill_input_dto

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
