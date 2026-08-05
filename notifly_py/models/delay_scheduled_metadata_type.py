from enum import Enum


class DelayScheduledMetadataType(str, Enum):
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
