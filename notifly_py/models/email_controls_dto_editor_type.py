from enum import Enum


class EmailControlsDtoEditorType(str, Enum):
    BLOCK = "block"
    HTML = "html"

    def __str__(self) -> str:
        return str(self.value)
