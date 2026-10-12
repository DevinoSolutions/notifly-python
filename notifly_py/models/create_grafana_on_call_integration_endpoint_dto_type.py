from enum import Enum


class CreateGrafanaOnCallIntegrationEndpointDtoType(str, Enum):
    GRAFANA_ONCALL_INTEGRATION = "grafana_oncall_integration"

    def __str__(self) -> str:
        return str(self.value)
