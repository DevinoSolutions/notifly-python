from enum import Enum


class StepIssueSeverityEnum(str, Enum):
    ERROR = "error"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
