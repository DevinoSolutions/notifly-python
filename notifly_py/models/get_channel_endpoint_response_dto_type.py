from enum import Enum


class GetChannelEndpointResponseDtoType(str, Enum):
    GRAFANA_ONCALL_INTEGRATION = "grafana_oncall_integration"
    LINE_USER = "line_user"
    MS_TEAMS_CHANNEL = "ms_teams_channel"
    MS_TEAMS_USER = "ms_teams_user"
    OPSGENIE_INTEGRATION = "opsgenie_integration"
    PAGERDUTY_SERVICE = "pagerduty_service"
    PHONE = "phone"
    SLACK_CHANNEL = "slack_channel"
    SLACK_USER = "slack_user"
    TELEGRAM_CHAT = "telegram_chat"
    TOOL_WEBHOOK = "tool_webhook"
    WEBEX_PERSON = "webex_person"
    WEBEX_ROOM = "webex_room"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
