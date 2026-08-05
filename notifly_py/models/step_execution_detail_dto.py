from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_details_status_enum import ExecutionDetailsStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_execution_detail_dto_raw_type_0 import StepExecutionDetailDtoRawType0


T = TypeVar("T", bound="StepExecutionDetailDto")


@_attrs_define
class StepExecutionDetailDto:
    """
    Attributes:
        field_id (str): Unique identifier of the execution detail
        status (ExecutionDetailsStatusEnum): Status of the execution detail
        detail (str): Detailed information about the execution
        created_at (str | Unset): Creation time of the execution detail
        provider_id (str | Unset): Provider identifier
        raw (None | StepExecutionDetailDtoRawType0 | Unset): Raw data of the execution
    """

    field_id: str
    status: ExecutionDetailsStatusEnum
    detail: str
    created_at: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    raw: None | StepExecutionDetailDtoRawType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_execution_detail_dto_raw_type_0 import StepExecutionDetailDtoRawType0

        field_id = self.field_id

        status = self.status.value

        detail = self.detail

        created_at = self.created_at

        provider_id = self.provider_id

        raw: dict[str, Any] | None | Unset
        if isinstance(self.raw, Unset):
            raw = UNSET
        elif isinstance(self.raw, StepExecutionDetailDtoRawType0):
            raw = self.raw.to_dict()
        else:
            raw = self.raw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "status": status,
                "detail": detail,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_execution_detail_dto_raw_type_0 import StepExecutionDetailDtoRawType0

        d = dict(src_dict)
        field_id = d.pop("_id")

        status = ExecutionDetailsStatusEnum(d.pop("status"))

        detail = d.pop("detail")

        created_at = d.pop("createdAt", UNSET)

        provider_id = d.pop("providerId", UNSET)

        def _parse_raw(data: object) -> None | StepExecutionDetailDtoRawType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_type_0 = StepExecutionDetailDtoRawType0.from_dict(data)

                return raw_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepExecutionDetailDtoRawType0 | Unset, data)

        raw = _parse_raw(d.pop("raw", UNSET))

        step_execution_detail_dto = cls(
            field_id=field_id,
            status=status,
            detail=detail,
            created_at=created_at,
            provider_id=provider_id,
            raw=raw,
        )

        step_execution_detail_dto.additional_properties = d
        return step_execution_detail_dto

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
