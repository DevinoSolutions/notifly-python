from enum import Enum


class DeleteMessageResponseDtoStatus(str, Enum):
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
