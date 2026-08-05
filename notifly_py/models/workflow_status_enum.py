from enum import Enum


class WorkflowStatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
