from enum import Enum


class WebhookDeletedWorkflowDtoWebhookPayloadWrapperType(str, Enum):
    WORKFLOW_DELETED = "workflow.deleted"

    def __str__(self) -> str:
        return str(self.value)
