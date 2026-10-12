from enum import Enum


class MetadataClearSignalDtoType(str, Enum):
    METADATA = "metadata"

    def __str__(self) -> str:
        return str(self.value)
