from enum import Enum


class LayoutCreationSourceEnum(str, Enum):
    DASHBOARD = "dashboard"

    def __str__(self) -> str:
        return str(self.value)
