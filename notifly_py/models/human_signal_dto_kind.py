from enum import Enum


class HumanSignalDtoKind(str, Enum):
    APPROVE = "approve"
    ASK = "ask"
    CHOOSE = "choose"
    TELL = "tell"

    def __str__(self) -> str:
        return str(self.value)
