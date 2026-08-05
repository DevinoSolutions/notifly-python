from enum import Enum


class TriggerEventResponseDtoStatus(str, Enum):
    ERROR = "error"
    INVALID_RECIPIENTS = "invalid_recipients"
    NO_TENANT_FOUND = "no_tenant_found"
    NO_WORKFLOW_ACTIVE_STEPS_DEFINED = "no_workflow_active_steps_defined"
    NO_WORKFLOW_STEPS_DEFINED = "no_workflow_steps_defined"
    PROCESSED = "processed"
    TRIGGER_NOT_ACTIVE = "trigger_not_active"

    def __str__(self) -> str:
        return str(self.value)
