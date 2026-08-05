from enum import Enum


class EnvironmentResponseDtoType(str, Enum):
    DEV = "dev"
    PROD = "prod"

    def __str__(self) -> str:
        return str(self.value)
