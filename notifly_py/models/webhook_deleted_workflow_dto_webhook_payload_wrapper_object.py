from enum import Enum


class WebhookDeletedWorkflowDtoWebhookPayloadWrapperObject(str, Enum):
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
