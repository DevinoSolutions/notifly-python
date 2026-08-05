from enum import Enum


class ResourceOriginEnum(str, Enum):
    EXTERNAL = "external"
    NOVU_CLOUD = "novu-cloud"
    NOVU_CLOUD_V1 = "novu-cloud-v1"

    def __str__(self) -> str:
        return str(self.value)
