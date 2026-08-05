from enum import Enum


class ActorTypeEnum(str, Enum):
    NONE = "none"
    SYSTEM_CUSTOM = "system_custom"
    SYSTEM_ICON = "system_icon"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
