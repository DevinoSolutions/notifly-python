from enum import Enum


class AgentPlanUsageDtoLimitSource(str, Enum):
    PLAN = "plan"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
