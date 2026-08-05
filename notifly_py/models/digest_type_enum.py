from enum import Enum


class DigestTypeEnum(str, Enum):
    BACKOFF = "backoff"
    REGULAR = "regular"
    TIMED = "timed"

    def __str__(self) -> str:
        return str(self.value)
