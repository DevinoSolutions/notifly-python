from enum import Enum


class MarkMessageActionAsSeenDtoStatus(str, Enum):
    DONE = "done"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
