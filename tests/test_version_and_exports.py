"""Package metadata, public exports and the User-Agent (PRD G9)."""

from __future__ import annotations

import re

import pytest

import notifly_py
from notifly_py import __version__, user_agent


def test_version_is_exported_and_looks_like_a_version() -> None:
    assert isinstance(__version__, str)
    assert re.match(r"^\d+\.\d+\.\d+", __version__) or __version__.startswith("0.0.0+"), __version__


def test_user_agent_identifies_the_sdk_python_and_httpx() -> None:
    agent = user_agent()
    assert agent.startswith(f"notifly-sdk/{__version__} ")
    assert " python/" in agent
    assert " httpx/" in agent


@pytest.mark.parametrize(
    "name",
    [
        "Notifly",
        "AsyncNotifly",
        "NotiflyClient",
        "Client",
        "AuthenticatedClient",
        "from_secret_key",
        "from_bearer_token",
        "RetryConfig",
        "NotiflyError",
        "NotiflyAPIError",
        "AuthenticationError",
        "NotFoundError",
        "ValidationError",
        "ConflictError",
        "RateLimitError",
        "ServerError",
        "DEFAULT_BASE_URL",
        "__version__",
        "user_agent",
    ],
)
def test_public_names_are_importable_from_the_package_root(name: str) -> None:
    assert hasattr(notifly_py, name)
    assert name in notifly_py.__all__


def test_the_generated_escape_hatch_is_still_importable() -> None:
    from notifly_py.api.events import events_controller_trigger

    for call_style in ("sync", "sync_detailed", "asyncio", "asyncio_detailed"):
        assert hasattr(events_controller_trigger, call_style)
