from enum import Enum


class CreateTelegramChatEndpointDtoType(str, Enum):
    TELEGRAM_CHAT = "telegram_chat"

    def __str__(self) -> str:
        return str(self.value)
