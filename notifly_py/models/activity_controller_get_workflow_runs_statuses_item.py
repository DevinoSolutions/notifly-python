from enum import Enum


class ActivityControllerGetWorkflowRunsStatusesItem(str, Enum):
    COMPLETED = "completed"
    ERROR = "error"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
