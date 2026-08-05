from enum import Enum


class IntegrationResponseDtoChannel(str, Enum):
    CHAT = "chat"
    EMAIL = "email"
    IN_APP = "in_app"
    PUSH = "push"
    SMS = "sms"

    def __str__(self) -> str:
        return str(self.value)
