from enum import Enum


class MetadataDeleteSignalDtoAction(str, Enum):
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)
