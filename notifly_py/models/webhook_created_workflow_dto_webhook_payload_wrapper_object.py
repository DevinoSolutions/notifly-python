from enum import Enum


class WebhookCreatedWorkflowDtoWebhookPayloadWrapperObject(str, Enum):
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
