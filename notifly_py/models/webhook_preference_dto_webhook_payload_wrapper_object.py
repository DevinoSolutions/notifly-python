from enum import Enum


class WebhookPreferenceDtoWebhookPayloadWrapperObject(str, Enum):
    PREFERENCE = "preference"

    def __str__(self) -> str:
        return str(self.value)
