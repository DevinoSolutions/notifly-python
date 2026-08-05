from enum import Enum


class ActivityControllerGetWorkflowRunsSeverityItem(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
