from enum import Enum


class CreateMsTeamsUserEndpointDtoType(str, Enum):
    MS_TEAMS_USER = "ms_teams_user"

    def __str__(self) -> str:
        return str(self.value)
