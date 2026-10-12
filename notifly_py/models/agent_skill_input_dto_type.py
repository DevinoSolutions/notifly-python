from enum import Enum


class AgentSkillInputDtoType(str, Enum):
    ANTHROPIC = "anthropic"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
