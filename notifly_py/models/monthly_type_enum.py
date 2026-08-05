from enum import Enum


class MonthlyTypeEnum(str, Enum):
    EACH = "each"
    ON = "on"

    def __str__(self) -> str:
        return str(self.value)
