from enum import Enum


class DelayRegularMetadataType(str, Enum):
    REGULAR = "regular"

    def __str__(self) -> str:
        return str(self.value)
