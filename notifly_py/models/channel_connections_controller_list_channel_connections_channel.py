from enum import Enum


class ChannelConnectionsControllerListChannelConnectionsChannel(str, Enum):
    CHAT = "chat"
    EMAIL = "email"
    IN_APP = "in_app"
    PUSH = "push"
    SMS = "sms"
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
