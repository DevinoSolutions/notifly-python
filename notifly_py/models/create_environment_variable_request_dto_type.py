from enum import Enum


class CreateEnvironmentVariableRequestDtoType(str, Enum):
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
