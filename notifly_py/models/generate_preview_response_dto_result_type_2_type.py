from enum import Enum


class GeneratePreviewResponseDtoResultType2Type(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
