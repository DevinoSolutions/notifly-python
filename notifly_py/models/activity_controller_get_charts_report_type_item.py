from enum import Enum


class ActivityControllerGetChartsReportTypeItem(str, Enum):
    ACTIVE_SUBSCRIBERS = "active-subscribers"
    ACTIVE_SUBSCRIBERS_TREND = "active-subscribers-trend"
    AVG_MESSAGES_PER_SUBSCRIBER = "avg-messages-per-subscriber"
    DELIVERY_TREND = "delivery-trend"
    INTERACTION_TREND = "interaction-trend"
    MESSAGES_DELIVERED = "messages-delivered"
    PROVIDER_BY_VOLUME = "provider-by-volume"
    TOTAL_INTERACTIONS = "total-interactions"
    WORKFLOW_BY_VOLUME = "workflow-by-volume"
    WORKFLOW_RUNS_COUNT = "workflow-runs-count"
    WORKFLOW_RUNS_METRIC = "workflow-runs-metric"
    WORKFLOW_RUNS_TREND = "workflow-runs-trend"

    def __str__(self) -> str:
        return str(self.value)
