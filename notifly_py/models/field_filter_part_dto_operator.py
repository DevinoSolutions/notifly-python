from enum import Enum


class FieldFilterPartDtoOperator(str, Enum):
    ALL_IN = "ALL_IN"
    ANY_IN = "ANY_IN"
    BETWEEN = "BETWEEN"
    EQUAL = "EQUAL"
    IN = "IN"
    LARGER = "LARGER"
    LARGER_EQUAL = "LARGER_EQUAL"
    LIKE = "LIKE"
    NOT_BETWEEN = "NOT_BETWEEN"
    NOT_EQUAL = "NOT_EQUAL"
    NOT_IN = "NOT_IN"
    NOT_LIKE = "NOT_LIKE"
    SMALLER = "SMALLER"
    SMALLER_EQUAL = "SMALLER_EQUAL"

    def __str__(self) -> str:
        return str(self.value)
