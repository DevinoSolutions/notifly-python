from enum import Enum


class CreateMsTeamsChannelEndpointDtoType(str, Enum):
    MS_TEAMS_CHANNEL = "ms_teams_channel"

    def __str__(self) -> str:
        return str(self.value)
