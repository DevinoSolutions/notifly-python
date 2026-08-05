from enum import Enum


class AuditLogControllerExportFormat(str, Enum):
    CSV = "csv"
    NDJSON = "ndjson"

    def __str__(self) -> str:
        return str(self.value)
