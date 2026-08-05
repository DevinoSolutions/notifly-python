from enum import Enum


class LayoutResponseDtoSortField(str, Enum):
    CREATEDAT = "createdAt"
    NAME = "name"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
