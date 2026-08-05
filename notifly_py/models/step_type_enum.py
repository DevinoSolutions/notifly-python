from enum import Enum


class StepTypeEnum(str, Enum):
    CHAT = "chat"
    CUSTOM = "custom"
    DELAY = "delay"
    DIGEST = "digest"
    EMAIL = "email"
    HTTP_REQUEST = "http_request"
    IN_APP = "in_app"
    PUSH = "push"
    SMS = "sms"
    THROTTLE = "throttle"
    TRIGGER = "trigger"

    def __str__(self) -> str:
        return str(self.value)
