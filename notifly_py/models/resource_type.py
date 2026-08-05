from enum import Enum


class ResourceType(str, Enum):
    LAYOUT = "layout"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
