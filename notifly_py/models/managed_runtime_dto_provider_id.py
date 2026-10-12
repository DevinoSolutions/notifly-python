from enum import Enum


class ManagedRuntimeDtoProviderId(str, Enum):
    ANTHROPIC = "anthropic"
    ANTHROPIC_AWS = "anthropic-aws"
    NOVU_ANTHROPIC = "novu-anthropic"

    def __str__(self) -> str:
        return str(self.value)
