from enum import Enum


class CreateSlackUserEndpointDtoType(str, Enum):
    SLACK_USER = "slack_user"

    def __str__(self) -> str:
        return str(self.value)
