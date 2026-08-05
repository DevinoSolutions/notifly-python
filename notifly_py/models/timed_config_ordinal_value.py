from enum import Enum


class TimedConfigOrdinalValue(str, Enum):
    DAY = "day"
    FRIDAY = "friday"
    MONDAY = "monday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    THURSDAY = "thursday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    WEEKDAY = "weekday"
    WEEKEND = "weekend"

    def __str__(self) -> str:
        return str(self.value)
