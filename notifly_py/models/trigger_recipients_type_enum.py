from enum import Enum


class TriggerRecipientsTypeEnum(str, Enum):
    SUBSCRIBER = "Subscriber"
    TOPIC = "Topic"

    def __str__(self) -> str:
        return str(self.value)
