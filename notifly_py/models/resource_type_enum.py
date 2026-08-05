from enum import Enum


class ResourceTypeEnum(str, Enum):
    BRIDGE = "BRIDGE"
    ECHO = "ECHO"
    REGULAR = "REGULAR"

    def __str__(self) -> str:
        return str(self.value)
