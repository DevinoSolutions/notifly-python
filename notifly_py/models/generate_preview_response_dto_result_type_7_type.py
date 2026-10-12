from enum import Enum


class GeneratePreviewResponseDtoResultType7Type(str, Enum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
