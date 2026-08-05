from enum import Enum


class ChannelCTATypeEnum(str, Enum):
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)
