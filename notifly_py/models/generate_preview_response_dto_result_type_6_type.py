from enum import Enum


class GeneratePreviewResponseDtoResultType6Type(str, Enum):
    CHAT = "chat"

    def __str__(self) -> str:
        return str(self.value)
