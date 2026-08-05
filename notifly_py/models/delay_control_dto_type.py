from enum import Enum


class DelayControlDtoType(str, Enum):
    REGULAR = "regular"
    TIMED = "timed"

    def __str__(self) -> str:
        return str(self.value)
