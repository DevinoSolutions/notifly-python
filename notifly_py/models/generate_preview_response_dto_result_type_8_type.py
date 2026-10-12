from enum import Enum


class GeneratePreviewResponseDtoResultType8Type(str, Enum):
    DELAY = "delay"

    def __str__(self) -> str:
        return str(self.value)
