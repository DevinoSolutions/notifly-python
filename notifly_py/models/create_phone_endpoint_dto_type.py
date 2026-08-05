from enum import Enum


class CreatePhoneEndpointDtoType(str, Enum):
    PHONE = "phone"

    def __str__(self) -> str:
        return str(self.value)
