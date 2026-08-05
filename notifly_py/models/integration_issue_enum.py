from enum import Enum


class IntegrationIssueEnum(str, Enum):
    INBOX_NOT_CONNECTED = "INBOX_NOT_CONNECTED"
    MISSING_INTEGRATION = "MISSING_INTEGRATION"

    def __str__(self) -> str:
        return str(self.value)
