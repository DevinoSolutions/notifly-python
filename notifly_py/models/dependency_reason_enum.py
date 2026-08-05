from enum import Enum


class DependencyReasonEnum(str, Enum):
    LAYOUT_EXISTS_IN_TARGET = "LAYOUT_EXISTS_IN_TARGET"
    LAYOUT_REQUIRED_FOR_WORKFLOW = "LAYOUT_REQUIRED_FOR_WORKFLOW"

    def __str__(self) -> str:
        return str(self.value)
