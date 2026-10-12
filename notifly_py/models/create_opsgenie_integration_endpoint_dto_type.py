from enum import Enum


class CreateOpsgenieIntegrationEndpointDtoType(str, Enum):
    OPSGENIE_INTEGRATION = "opsgenie_integration"

    def __str__(self) -> str:
        return str(self.value)
