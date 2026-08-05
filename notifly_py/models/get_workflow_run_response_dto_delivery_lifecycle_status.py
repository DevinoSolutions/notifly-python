from enum import Enum


class GetWorkflowRunResponseDtoDeliveryLifecycleStatus(str, Enum):
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
