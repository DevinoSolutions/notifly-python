from enum import Enum


class WebhookPreferenceDtoWebhookPayloadWrapperType(str, Enum):
    PREFERENCE_UPDATED = "preference.updated"

    def __str__(self) -> str:
        return str(self.value)
