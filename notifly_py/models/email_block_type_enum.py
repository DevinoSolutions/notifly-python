from enum import Enum


class EmailBlockTypeEnum(str, Enum):
    BUTTON = "button"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
