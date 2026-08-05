from enum import Enum


class MarkAllMessageAsRequestDtoMarkAs(str, Enum):
    READ = "read"
    SEEN = "seen"
    UNREAD = "unread"
    UNSEEN = "unseen"

    def __str__(self) -> str:
        return str(self.value)
