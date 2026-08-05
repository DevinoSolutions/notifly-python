from enum import Enum


class EnvironmentVariableResponseDtoType(str, Enum):
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
