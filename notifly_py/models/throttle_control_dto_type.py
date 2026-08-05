from enum import Enum


class ThrottleControlDtoType(str, Enum):
    DYNAMIC = "dynamic"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
