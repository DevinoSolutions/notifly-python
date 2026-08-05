from enum import Enum


class GeneratePreviewResponseDtoResultType5Type(str, Enum):
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
