from enum import Enum


class WebhookMessageFailedDtoWebhookPayloadWrapperType(str, Enum):
    MESSAGE_FAILED = "message.failed"

    def __str__(self) -> str:
        return str(self.value)
