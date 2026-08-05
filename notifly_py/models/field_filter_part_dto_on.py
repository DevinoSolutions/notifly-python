from enum import Enum


class FieldFilterPartDtoOn(str, Enum):
    PAYLOAD = "payload"
    SUBSCRIBER = "subscriber"

    def __str__(self) -> str:
        return str(self.value)
