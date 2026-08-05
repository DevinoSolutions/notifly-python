from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.publish_summary_dto import PublishSummaryDto
    from ..models.sync_result_dto import SyncResultDto


T = TypeVar("T", bound="PublishEnvironmentResponseDto")


@_attrs_define
class PublishEnvironmentResponseDto:
    """
    Attributes:
        results (list[SyncResultDto]): Sync results by resource type
        summary (PublishSummaryDto):
    """

    results: list[SyncResultDto]
    summary: PublishSummaryDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_summary_dto import PublishSummaryDto
        from ..models.sync_result_dto import SyncResultDto

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SyncResultDto.from_dict(results_item_data)

            results.append(results_item)

        summary = PublishSummaryDto.from_dict(d.pop("summary"))

        publish_environment_response_dto = cls(
            results=results,
            summary=summary,
        )

        publish_environment_response_dto.additional_properties = d
        return publish_environment_response_dto

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
