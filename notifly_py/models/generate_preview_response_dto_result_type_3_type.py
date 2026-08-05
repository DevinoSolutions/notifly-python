from enum import Enum


class GeneratePreviewResponseDtoResultType3Type(str, Enum):
    IN_APP = "in_app"

    def __str__(self) -> str:
        return str(self.value)
