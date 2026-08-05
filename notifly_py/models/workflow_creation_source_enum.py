from enum import Enum


class WorkflowCreationSourceEnum(str, Enum):
    AI = "ai"
    BRIDGE = "bridge"
    DASHBOARD = "dashboard"
    DROPDOWN = "dropdown"
    EDITOR = "editor"
    EMPTY_STATE = "empty_state"
    NOTIFICATION_DIRECTORY = "notification_directory"
    ONBOARDING_DIGEST_DEMO = "onboarding_digest_demo"
    ONBOARDING_GET_STARTED = "onboarding_get_started"
    ONBOARDING_IN_APP = "onboarding_in_app"
    TEMPLATE_STORE = "template_store"

    def __str__(self) -> str:
        return str(self.value)
