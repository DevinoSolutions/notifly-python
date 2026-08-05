from enum import Enum


class GetWorkflowRunsDtoDeliveryLifecycleStatus(str, Enum):
    CANCELED = "canceled"
    DELIVERED = "delivered"
    ERRORED = "errored"
    INTERACTED = "interacted"
    MERGED = "merged"
    PENDING = "pending"
    SENT = "sent"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
