from enum import Enum


class UiSchemaGroupEnum(str, Enum):
    CHAT = "CHAT"
    DELAY = "DELAY"
    DIGEST = "DIGEST"
    EMAIL = "EMAIL"
    HTTP_REQUEST = "HTTP_REQUEST"
    IN_APP = "IN_APP"
    LAYOUT = "LAYOUT"
    PUSH = "PUSH"
    SKIP = "SKIP"
    SMS = "SMS"
    THROTTLE = "THROTTLE"

    def __str__(self) -> str:
        return str(self.value)
