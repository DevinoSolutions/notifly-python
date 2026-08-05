from enum import Enum


class NotificationTriggerType(str, Enum):
    EVENT = "event"

    def __str__(self) -> str:
        return str(self.value)
