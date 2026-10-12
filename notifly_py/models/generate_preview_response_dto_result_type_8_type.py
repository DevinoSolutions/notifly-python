from enum import Enum


class GeneratePreviewResponseDtoResultType8Type(str, Enum):
    DIGEST = "digest"

    def __str__(self) -> str:
        return str(self.value)
