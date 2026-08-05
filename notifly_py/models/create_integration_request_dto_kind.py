from enum import Enum


class CreateIntegrationRequestDtoKind(str, Enum):
    AGENT = "agent"
    DELIVERY = "delivery"

    def __str__(self) -> str:
        return str(self.value)
