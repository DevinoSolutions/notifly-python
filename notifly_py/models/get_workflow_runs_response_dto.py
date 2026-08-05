from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_workflow_runs_dto import GetWorkflowRunsDto
    from ..models.get_workflow_runs_response_dto_next_type_0 import GetWorkflowRunsResponseDtoNextType0
    from ..models.get_workflow_runs_response_dto_previous_type_0 import GetWorkflowRunsResponseDtoPreviousType0


T = TypeVar("T", bound="GetWorkflowRunsResponseDto")


@_attrs_define
class GetWorkflowRunsResponseDto:
    """
    Attributes:
        data (list[GetWorkflowRunsDto]): Workflow runs data
        next_ (GetWorkflowRunsResponseDtoNextType0 | None | Unset): Next cursor for pagination
        previous (GetWorkflowRunsResponseDtoPreviousType0 | None | Unset): Previous cursor for pagination
    """

    data: list[GetWorkflowRunsDto]
    next_: GetWorkflowRunsResponseDtoNextType0 | None | Unset = UNSET
    previous: GetWorkflowRunsResponseDtoPreviousType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_workflow_runs_response_dto_next_type_0 import GetWorkflowRunsResponseDtoNextType0
        from ..models.get_workflow_runs_response_dto_previous_type_0 import GetWorkflowRunsResponseDtoPreviousType0

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_: dict[str, Any] | None | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        elif isinstance(self.next_, GetWorkflowRunsResponseDtoNextType0):
            next_ = self.next_.to_dict()
        else:
            next_ = self.next_

        previous: dict[str, Any] | None | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        elif isinstance(self.previous, GetWorkflowRunsResponseDtoPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_workflow_runs_dto import GetWorkflowRunsDto
        from ..models.get_workflow_runs_response_dto_next_type_0 import GetWorkflowRunsResponseDtoNextType0
        from ..models.get_workflow_runs_response_dto_previous_type_0 import GetWorkflowRunsResponseDtoPreviousType0

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetWorkflowRunsDto.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_(data: object) -> GetWorkflowRunsResponseDtoNextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_type_0 = GetWorkflowRunsResponseDtoNextType0.from_dict(data)

                return next_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkflowRunsResponseDtoNextType0 | None | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> GetWorkflowRunsResponseDtoPreviousType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = GetWorkflowRunsResponseDtoPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetWorkflowRunsResponseDtoPreviousType0 | None | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        get_workflow_runs_response_dto = cls(
            data=data,
            next_=next_,
            previous=previous,
        )

        get_workflow_runs_response_dto.additional_properties = d
        return get_workflow_runs_response_dto

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
