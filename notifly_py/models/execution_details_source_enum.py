from enum import Enum


class ExecutionDetailsSourceEnum(str, Enum):
    CREDENTIALS = "Credentials"
    INTERNAL = "Internal"
    PAYLOAD = "Payload"
    WEBHOOK = "Webhook"

    def __str__(self) -> str:
        return str(self.value)
