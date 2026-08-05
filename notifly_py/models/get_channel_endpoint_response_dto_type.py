from enum import Enum


class GetChannelEndpointResponseDtoType(str, Enum):
    MS_TEAMS_CHANNEL = "ms_teams_channel"
    MS_TEAMS_USER = "ms_teams_user"
    PHONE = "phone"
    SLACK_CHANNEL = "slack_channel"
    SLACK_USER = "slack_user"
    TELEGRAM_CHAT = "telegram_chat"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
