from enum import Enum


class TextAlignEnum(str, Enum):
    CENTER = "center"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
