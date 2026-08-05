from enum import Enum


class WebhookInboundEmailDtoWebhookPayloadWrapperType(str, Enum):
    EMAIL_RECEIVED = "email.received"

    def __str__(self) -> str:
        return str(self.value)
