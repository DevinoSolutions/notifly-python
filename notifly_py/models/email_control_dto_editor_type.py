from enum import Enum


class EmailControlDtoEditorType(str, Enum):
    BLOCK = "block"
    HTML = "html"

    def __str__(self) -> str:
        return str(self.value)
