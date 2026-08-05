from enum import Enum


class ActivityControllerGetChartsStatusesItem(str, Enum):
    COMPLETED = "completed"
    ERROR = "error"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
