from enum import Enum


class ButtonTypeEnum(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
