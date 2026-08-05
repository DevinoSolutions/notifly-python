from enum import Enum


class IntegrationResponseDtoKind(str, Enum):
    AGENT = "agent"
    DELIVERY = "delivery"

    def __str__(self) -> str:
        return str(self.value)
