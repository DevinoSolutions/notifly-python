from enum import Enum


class AgentReplyPayloadDtoTypingType0(str, Enum):
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
