from enum import Enum


class ExecutionDetailsStatusEnum(str, Enum):
    FAILED = "Failed"
    PENDING = "Pending"
    QUEUED = "Queued"
    READCONFIRMATION = "ReadConfirmation"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
