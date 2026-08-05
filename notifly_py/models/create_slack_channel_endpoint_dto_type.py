from enum import Enum


class CreateSlackChannelEndpointDtoType(str, Enum):
    SLACK_CHANNEL = "slack_channel"

    def __str__(self) -> str:
        return str(self.value)
