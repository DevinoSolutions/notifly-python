"""notifly-py — the official Python SDK for the Notifly API.

HAND-WRITTEN — this file replaces the generated ``__init__.py``. See ``scripts/regenerate.sh``.

Quickstart::

    from notifly_py import Notifly

    notifly = Notifly("<secret key>")
    notifly.events.trigger(workflow="welcome", to="subscriber_123", payload={"name": "Ada"})

The generated call style remains fully supported::

    from notifly_py import NotiflyClient
    from notifly_py.api.events import events_controller_trigger

    events_controller_trigger.sync(client=NotiflyClient(token="<secret key>"), body=...)
"""

from ._transport import RetryConfig
from ._version import __version__, user_agent
from .client import AuthenticatedClient, Client
from .exceptions import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
    NotiflyAPIError,
    NotiflyError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from .facade import AsyncNotifly, Notifly
from .notifly_client import DEFAULT_BASE_URL, NotiflyClient, from_bearer_token, from_secret_key

__all__ = (
    "DEFAULT_BASE_URL",
    "AsyncNotifly",
    "AuthenticatedClient",
    "AuthenticationError",
    "Client",
    "ConflictError",
    "NotFoundError",
    "Notifly",
    "NotiflyAPIError",
    "NotiflyClient",
    "NotiflyError",
    "RateLimitError",
    "RetryConfig",
    "ServerError",
    "ValidationError",
    "__version__",
    "from_bearer_token",
    "from_secret_key",
    "user_agent",
)
