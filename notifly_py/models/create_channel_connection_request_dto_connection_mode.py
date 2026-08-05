from enum import Enum


class CreateChannelConnectionRequestDtoConnectionMode(str, Enum):
    SHARED = "shared"
    SUBSCRIBER = "subscriber"

    def __str__(self) -> str:
        return str(self.value)
