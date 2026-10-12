from enum import Enum


class ChatControlDtoEditorType(str, Enum):
    BLOCK = "block"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
