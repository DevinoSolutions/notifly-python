from enum import Enum


class AgentBehaviorDtoSubscriberAccess(str, Enum):
    OPEN = "open"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
