from enum import Enum


class WebhookUpdatedWorkflowDtoWebhookPayloadWrapperObject(str, Enum):
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
