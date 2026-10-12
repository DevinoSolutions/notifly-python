from enum import Enum


class CreateWebexRoomEndpointDtoType(str, Enum):
    WEBEX_ROOM = "webex_room"

    def __str__(self) -> str:
        return str(self.value)
