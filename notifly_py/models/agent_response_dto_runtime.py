from enum import Enum


class AgentResponseDtoRuntime(str, Enum):
    MANAGED = "managed"
    SELF_HOSTED = "self-hosted"

    def __str__(self) -> str:
        return str(self.value)
