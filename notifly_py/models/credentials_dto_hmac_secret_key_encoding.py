from enum import Enum


class CredentialsDtoHmacSecretKeyEncoding(str, Enum):
    BASE64 = "base64"
    HEX = "hex"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
