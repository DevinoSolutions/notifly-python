from enum import Enum


class ActivityControllerGetLogsSource(str, Enum):
    HTTP = "http"
    INBOUND_EMAIL = "inbound_email"

    def __str__(self) -> str:
        return str(self.value)
