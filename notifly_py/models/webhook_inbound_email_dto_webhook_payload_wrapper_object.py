from enum import Enum


class WebhookInboundEmailDtoWebhookPayloadWrapperObject(str, Enum):
    EMAIL_INBOUND = "email_inbound"

    def __str__(self) -> str:
        return str(self.value)
