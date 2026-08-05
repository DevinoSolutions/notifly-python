from enum import Enum


class DelayControlDtoUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    MONTHS = "months"
    SECONDS = "seconds"
    WEEKS = "weeks"

    def __str__(self) -> str:
        return str(self.value)
