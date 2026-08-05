from enum import Enum


class BuilderFieldTypeEnum(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    GROUP = "GROUP"
    LIST = "LIST"
    MULTI_LIST = "MULTI_LIST"
    NUMBER = "NUMBER"
    STATEMENT = "STATEMENT"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
