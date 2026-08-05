from enum import Enum


class DigestTimedMetadataType(str, Enum):
    TIMED = "timed"

    def __str__(self) -> str:
        return str(self.value)
