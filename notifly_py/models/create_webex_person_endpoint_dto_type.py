from enum import Enum


class CreateWebexPersonEndpointDtoType(str, Enum):
    WEBEX_PERSON = "webex_person"

    def __str__(self) -> str:
        return str(self.value)
