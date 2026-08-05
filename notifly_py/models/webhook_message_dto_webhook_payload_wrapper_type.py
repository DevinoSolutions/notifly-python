from enum import Enum


class WebhookMessageDtoWebhookPayloadWrapperType(str, Enum):
    MESSAGE_SENT = "message.sent"

    def __str__(self) -> str:
        return str(self.value)
