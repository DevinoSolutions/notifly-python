from enum import Enum


class SubscribersControllerGetSubscriberPreferencesCriticality(str, Enum):
    ALL = "all"
    CRITICAL = "critical"
    NONCRITICAL = "nonCritical"

    def __str__(self) -> str:
        return str(self.value)
