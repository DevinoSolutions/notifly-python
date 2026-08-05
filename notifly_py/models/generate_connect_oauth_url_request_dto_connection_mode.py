from enum import Enum


class GenerateConnectOauthUrlRequestDtoConnectionMode(str, Enum):
    SHARED = "shared"
    SUBSCRIBER = "subscriber"

    def __str__(self) -> str:
        return str(self.value)
