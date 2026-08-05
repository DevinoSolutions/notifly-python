from enum import Enum


class DigestRegularMetadataType(str, Enum):
    BACKOFF = "backoff"
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
