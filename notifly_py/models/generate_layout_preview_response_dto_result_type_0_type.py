from enum import Enum


class GenerateLayoutPreviewResponseDtoResultType0Type(str, Enum):
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
