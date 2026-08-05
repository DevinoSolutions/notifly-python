from enum import Enum


class WorkflowRunStepsDetailsDtoStatus(str, Enum):
    CANCELED = "canceled"
    COMPLETED = "completed"
    DELAYED = "delayed"
    FAILED = "failed"
    MERGED = "merged"
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
