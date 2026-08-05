from enum import Enum


class SyncActionEnum(str, Enum):
    CREATED = "created"
    DELETED = "deleted"
    SKIPPED = "skipped"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
