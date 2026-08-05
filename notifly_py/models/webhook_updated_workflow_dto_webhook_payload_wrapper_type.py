from enum import Enum


class WebhookUpdatedWorkflowDtoWebhookPayloadWrapperType(str, Enum):
    WORKFLOW_UPDATED = "workflow.updated"

    def __str__(self) -> str:
        return str(self.value)
