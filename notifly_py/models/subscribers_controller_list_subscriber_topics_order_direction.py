from enum import Enum


class SubscribersControllerListSubscriberTopicsOrderDirection(str, Enum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
