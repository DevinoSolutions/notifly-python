from enum import Enum


class GeneratePreviewResponseDtoResultType4Type(str, Enum):
    SMS = "sms"

    def __str__(self) -> str:
        return str(self.value)
