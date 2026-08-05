from enum import Enum


class GenerateChatOauthUrlRequestDtoConnectionMode(str, Enum):
    SHARED = "shared"
    SUBSCRIBER = "subscriber"

    def __str__(self) -> str:
        return str(self.value)
