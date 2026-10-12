from enum import Enum


class ToolWebhookEndpointDtoMethod(str, Enum):
    PATCH = "PATCH"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
