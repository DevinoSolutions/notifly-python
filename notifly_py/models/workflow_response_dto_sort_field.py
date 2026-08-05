from enum import Enum


class WorkflowResponseDtoSortField(str, Enum):
    CREATEDAT = "createdAt"
    LASTTRIGGEREDAT = "lastTriggeredAt"
    NAME = "name"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
