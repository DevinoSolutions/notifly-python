from enum import Enum


class TimedConfigMonthlyType(str, Enum):
    EACH = "each"
    ON = "on"

    def __str__(self) -> str:
        return str(self.value)
