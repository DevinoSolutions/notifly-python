from enum import Enum


class DiffActionEnum(str, Enum):
    ADDED = "added"
    DELETED = "deleted"
    MODIFIED = "modified"
    MOVED = "moved"
    UNCHANGED = "unchanged"

    def __str__(self) -> str:
        return str(self.value)
