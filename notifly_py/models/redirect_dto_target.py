from enum import Enum


class RedirectDtoTarget(str, Enum):
    VALUE_0 = "_self"
    VALUE_1 = "_blank"
    VALUE_2 = "_parent"
    VALUE_3 = "_top"
    VALUE_4 = "_unfencedTop"

    def __str__(self) -> str:
        return str(self.value)
