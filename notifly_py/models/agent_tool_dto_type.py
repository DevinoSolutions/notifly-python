from enum import Enum


class AgentToolDtoType(str, Enum):
    BUILTIN = "builtin"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
