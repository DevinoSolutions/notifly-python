from enum import Enum


class WebhookCreatedWorkflowDtoWebhookPayloadWrapperType(str, Enum):
    WORKFLOW_CREATED = "workflow.created"

    def __str__(self) -> str:
        return str(self.value)
