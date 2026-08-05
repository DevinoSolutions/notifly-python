from enum import Enum


class PreferenceLevelEnum(str, Enum):
    GLOBAL = "global"
    TEMPLATE = "template"

    def __str__(self) -> str:
        return str(self.value)
