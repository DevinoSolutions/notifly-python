from enum import Enum


class CreateToolWebhookEndpointDtoType(str, Enum):
    TOOL_WEBHOOK = "tool_webhook"

    def __str__(self) -> str:
        return str(self.value)
