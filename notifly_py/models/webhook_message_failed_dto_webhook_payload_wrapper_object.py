from enum import Enum


class WebhookMessageFailedDtoWebhookPayloadWrapperObject(str, Enum):
    MESSAGE = "message"

    def __str__(self) -> str:
        return str(self.value)
