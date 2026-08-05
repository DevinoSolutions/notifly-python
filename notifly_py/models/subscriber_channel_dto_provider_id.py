from enum import Enum


class SubscriberChannelDtoProviderId(str, Enum):
    APNS = "apns"
    APPIO = "appio"
    CHAT_WEBHOOK = "chat-webhook"
    DISCORD = "discord"
    EXPO = "expo"
    FCM = "fcm"
    GETSTREAM = "getstream"
    GRAFANA_ON_CALL = "grafana-on-call"
    MATTERMOST = "mattermost"
    MSTEAMS = "msteams"
    NOVU_SLACK = "novu-slack"
    ONE_SIGNAL = "one-signal"
    PUSHER_BEAMS = "pusher-beams"
    PUSHPAD = "pushpad"
    PUSH_WEBHOOK = "push-webhook"
    ROCKET_CHAT = "rocket-chat"
    RYVER = "ryver"
    SLACK = "slack"
    TELEGRAM = "telegram"
    WEB_PUSH = "web-push"
    WHATSAPP_BUSINESS = "whatsapp-business"
    ZULIP = "zulip"

    def __str__(self) -> str:
        return str(self.value)
