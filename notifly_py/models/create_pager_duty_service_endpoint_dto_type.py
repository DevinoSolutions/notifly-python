from enum import Enum


class CreatePagerDutyServiceEndpointDtoType(str, Enum):
    PAGERDUTY_SERVICE = "pagerduty_service"

    def __str__(self) -> str:
        return str(self.value)
