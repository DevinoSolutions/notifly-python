from enum import Enum


class GenerateChatOauthUrlRequestDtoMode(str, Enum):
    CONNECT = "connect"
    LINK_USER = "link_user"

    def __str__(self) -> str:
        return str(self.value)
