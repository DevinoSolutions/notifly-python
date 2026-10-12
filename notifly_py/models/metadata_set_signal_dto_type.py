from enum import Enum


class MetadataSetSignalDtoType(str, Enum):
    METADATA = "metadata"

    def __str__(self) -> str:
        return str(self.value)
