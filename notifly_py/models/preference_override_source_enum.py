from enum import Enum


class PreferenceOverrideSourceEnum(str, Enum):
    SUBSCRIBER = "subscriber"
    TEMPLATE = "template"
    WORKFLOWOVERRIDE = "workflowOverride"

    def __str__(self) -> str:
        return str(self.value)
