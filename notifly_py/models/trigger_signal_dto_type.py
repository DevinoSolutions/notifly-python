from enum import Enum


class TriggerSignalDtoType(str, Enum):
    TRIGGER = "trigger"

    def __str__(self) -> str:
        return str(self.value)
