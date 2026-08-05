from enum import Enum


class CreateWebhookEndpointDtoType(str, Enum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
