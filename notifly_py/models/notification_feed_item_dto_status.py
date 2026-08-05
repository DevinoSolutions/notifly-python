from enum import Enum


class NotificationFeedItemDtoStatus(str, Enum):
    ERROR = "error"
    SENT = "sent"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
