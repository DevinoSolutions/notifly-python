from enum import Enum


class CreateLineUserEndpointDtoType(str, Enum):
    LINE_USER = "line_user"

    def __str__(self) -> str:
        return str(self.value)
