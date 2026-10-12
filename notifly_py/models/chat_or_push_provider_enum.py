from enum import Enum


class ChatOrPushProviderEnum(str, Enum):
    APNS = "apns"
    APPIO = "appio"
    CHAT_WEBHOOK = "chat-webhook"
    DISCORD = "discord"
    EXPO = "expo"
    FCM = "fcm"
    GETSTREAM = "getstream"
    GRAFANA_ON_CALL = "grafana-on-call"
    LINE = "line"
    MATTERMOST = "mattermost"
    MSTEAMS = "msteams"
    NOVU_SLACK = "novu-slack"
    NOVU_WEB_CHAT = "novu-web-chat"
    ONE_SIGNAL = "one-signal"
    PUSHER_BEAMS = "pusher-beams"
    PUSHPAD = "pushpad"
    PUSH_WEBHOOK = "push-webhook"
    ROCKET_CHAT = "rocket-chat"
    RYVER = "ryver"
    SENDBLUE = "sendblue"
    SLACK = "slack"
    TELEGRAM = "telegram"
    WEBEX_MESSAGING = "webex-messaging"
    WEB_PUSH = "web-push"
    WHATSAPP_BUSINESS = "whatsapp-business"
    ZULIP = "zulip"

    def __str__(self) -> str:
        return str(self.value)
