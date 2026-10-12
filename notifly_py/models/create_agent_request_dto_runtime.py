from enum import Enum


class CreateAgentRequestDtoRuntime(str, Enum):
    MANAGED = "managed"
    SELF_HOSTED = "self-hosted"

    def __str__(self) -> str:
        return str(self.value)
