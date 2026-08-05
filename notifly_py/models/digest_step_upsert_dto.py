from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_type_enum import StepTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.digest_control_dto import DigestControlDto
    from ..models.digest_step_upsert_dto_control_values_type_1 import DigestStepUpsertDtoControlValuesType1


T = TypeVar("T", bound="DigestStepUpsertDto")


@_attrs_define
class DigestStepUpsertDto:
    """
    Attributes:
        name (str): Name of the step
        type_ (StepTypeEnum): Type of the step
        field_id (str | Unset): Database identifier of the step. Used for updating the step.
        step_id (str | Unset): Unique identifier for the step
        control_values (DigestControlDto | DigestStepUpsertDtoControlValuesType1 | Unset): Control values for the Digest
            step.
    """

    name: str
    type_: StepTypeEnum
    field_id: str | Unset = UNSET
    step_id: str | Unset = UNSET
    control_values: DigestControlDto | DigestStepUpsertDtoControlValuesType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.digest_control_dto import DigestControlDto

        name = self.name

        type_ = self.type_.value

        field_id = self.field_id

        step_id = self.step_id

        control_values: dict[str, Any] | Unset
        if isinstance(self.control_values, Unset):
            control_values = UNSET
        elif isinstance(self.control_values, DigestControlDto):
            control_values = self.control_values.to_dict()
        else:
            control_values = self.control_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if step_id is not UNSET:
            field_dict["stepId"] = step_id
        if control_values is not UNSET:
            field_dict["controlValues"] = control_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.digest_control_dto import DigestControlDto
        from ..models.digest_step_upsert_dto_control_values_type_1 import DigestStepUpsertDtoControlValuesType1

        d = dict(src_dict)
        name = d.pop("name")

        type_ = StepTypeEnum(d.pop("type"))

        field_id = d.pop("_id", UNSET)

        step_id = d.pop("stepId", UNSET)

        def _parse_control_values(data: object) -> DigestControlDto | DigestStepUpsertDtoControlValuesType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                control_values_type_0 = DigestControlDto.from_dict(data)

                return control_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            control_values_type_1 = DigestStepUpsertDtoControlValuesType1.from_dict(data)

            return control_values_type_1

        control_values = _parse_control_values(d.pop("controlValues", UNSET))

        digest_step_upsert_dto = cls(
            name=name,
            type_=type_,
            field_id=field_id,
            step_id=step_id,
            control_values=control_values,
        )

        digest_step_upsert_dto.additional_properties = d
        return digest_step_upsert_dto

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
