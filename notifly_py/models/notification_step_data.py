from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delay_regular_metadata import DelayRegularMetadata
    from ..models.delay_scheduled_metadata import DelayScheduledMetadata
    from ..models.digest_regular_metadata import DigestRegularMetadata
    from ..models.digest_timed_metadata import DigestTimedMetadata
    from ..models.message_template import MessageTemplate
    from ..models.reply_callback import ReplyCallback
    from ..models.step_filter_dto import StepFilterDto


T = TypeVar("T", bound="NotificationStepData")


@_attrs_define
class NotificationStepData:
    """
    Attributes:
        field_id (str | Unset): Unique identifier for the notification step.
        uuid (str | Unset): Universally unique identifier for the notification step.
        name (str | Unset): Name of the notification step.
        field_template_id (str | Unset): ID of the template associated with this notification step.
        active (bool | Unset): Indicates whether the notification step is active.
        should_stop_on_fail (bool | Unset): Determines if the process should stop on failure.
        template (MessageTemplate | Unset):
        filters (list[StepFilterDto] | Unset): Filters applied to this notification step.
        field_parent_id (str | Unset): ID of the parent notification step, if applicable.
        metadata (DelayRegularMetadata | DelayScheduledMetadata | DigestRegularMetadata | DigestTimedMetadata | Unset):
            Metadata associated with the workflow step. Can vary based on the type of step.
        reply_callback (ReplyCallback | Unset):
    """

    field_id: str | Unset = UNSET
    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    field_template_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    should_stop_on_fail: bool | Unset = UNSET
    template: MessageTemplate | Unset = UNSET
    filters: list[StepFilterDto] | Unset = UNSET
    field_parent_id: str | Unset = UNSET
    metadata: DelayRegularMetadata | DelayScheduledMetadata | DigestRegularMetadata | DigestTimedMetadata | Unset = (
        UNSET
    )
    reply_callback: ReplyCallback | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delay_regular_metadata import DelayRegularMetadata
        from ..models.digest_regular_metadata import DigestRegularMetadata
        from ..models.digest_timed_metadata import DigestTimedMetadata

        field_id = self.field_id

        uuid = self.uuid

        name = self.name

        field_template_id = self.field_template_id

        active = self.active

        should_stop_on_fail = self.should_stop_on_fail

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_parent_id = self.field_parent_id

        metadata: dict[str, Any] | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DigestRegularMetadata):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, DigestTimedMetadata):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, DelayRegularMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata.to_dict()

        reply_callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reply_callback, Unset):
            reply_callback = self.reply_callback.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if field_template_id is not UNSET:
            field_dict["_templateId"] = field_template_id
        if active is not UNSET:
            field_dict["active"] = active
        if should_stop_on_fail is not UNSET:
            field_dict["shouldStopOnFail"] = should_stop_on_fail
        if template is not UNSET:
            field_dict["template"] = template
        if filters is not UNSET:
            field_dict["filters"] = filters
        if field_parent_id is not UNSET:
            field_dict["_parentId"] = field_parent_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if reply_callback is not UNSET:
            field_dict["replyCallback"] = reply_callback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delay_regular_metadata import DelayRegularMetadata
        from ..models.delay_scheduled_metadata import DelayScheduledMetadata
        from ..models.digest_regular_metadata import DigestRegularMetadata
        from ..models.digest_timed_metadata import DigestTimedMetadata
        from ..models.message_template import MessageTemplate
        from ..models.reply_callback import ReplyCallback
        from ..models.step_filter_dto import StepFilterDto

        d = dict(src_dict)
        field_id = d.pop("_id", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        field_template_id = d.pop("_templateId", UNSET)

        active = d.pop("active", UNSET)

        should_stop_on_fail = d.pop("shouldStopOnFail", UNSET)

        _template = d.pop("template", UNSET)
        template: MessageTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = MessageTemplate.from_dict(_template)

        _filters = d.pop("filters", UNSET)
        filters: list[StepFilterDto] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = StepFilterDto.from_dict(filters_item_data)

                filters.append(filters_item)

        field_parent_id = d.pop("_parentId", UNSET)

        def _parse_metadata(
            data: object,
        ) -> DelayRegularMetadata | DelayScheduledMetadata | DigestRegularMetadata | DigestTimedMetadata | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DigestRegularMetadata.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = DigestTimedMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_2 = DelayRegularMetadata.from_dict(data)

                return metadata_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            metadata_type_3 = DelayScheduledMetadata.from_dict(data)

            return metadata_type_3

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        _reply_callback = d.pop("replyCallback", UNSET)
        reply_callback: ReplyCallback | Unset
        if isinstance(_reply_callback, Unset):
            reply_callback = UNSET
        else:
            reply_callback = ReplyCallback.from_dict(_reply_callback)

        notification_step_data = cls(
            field_id=field_id,
            uuid=uuid,
            name=name,
            field_template_id=field_template_id,
            active=active,
            should_stop_on_fail=should_stop_on_fail,
            template=template,
            filters=filters,
            field_parent_id=field_parent_id,
            metadata=metadata,
            reply_callback=reply_callback,
        )

        notification_step_data.additional_properties = d
        return notification_step_data

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
