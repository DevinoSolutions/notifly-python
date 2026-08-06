"""The client the SDK actually recommends: :class:`NotiflyClient`.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

It is a drop-in subclass of the generated :class:`notifly_py.client.AuthenticatedClient` that
fixes three things the generator cannot know about:

1. **``ApiKey`` is the default auth prefix.** Notifly wants ``Authorization: ApiKey <key>``;
   the generated default is ``Bearer``, which silently 401s with a secret key.
2. **The ``{"data": ...}`` response envelope is unwrapped** (see :mod:`notifly_py._envelope`).
3. **Requests are retried** with ``Retry-After`` support and carry a real ``User-Agent``.

Every generated operation module accepts this class wherever it accepts
``AuthenticatedClient``, so the raw call style keeps working::

    from notifly_py import NotiflyClient
    from notifly_py.api.events import events_controller_trigger

    client = NotiflyClient(token="<secret key>")
    events_controller_trigger.sync(client=client, body=...)
"""

from __future__ import annotations

from typing import Any

import httpx
from attrs import define, field

from ._transport import RetryConfig, build_async_transport, build_sync_transport
from ._version import user_agent as default_user_agent
from .client import AuthenticatedClient

DEFAULT_BASE_URL = "https://api.notifly.io"
API_KEY_PREFIX = "ApiKey"
BEARER_PREFIX = "Bearer"


@define
class NotiflyClient(AuthenticatedClient):
    """An :class:`AuthenticatedClient` wired for the real Notifly API.

    Args:
        token: The Notifly secret key (or a dashboard JWT if ``prefix="Bearer"``).
        base_url: API root. Defaults to ``https://api.notifly.io``.
        prefix: Authorization scheme. Defaults to ``ApiKey``.
        retry_config: Retry policy; pass ``RetryConfig(max_retries=0)`` to disable retries.
        unwrap_data_envelope: Set to ``False`` only if the API ever stops wrapping single
            entities in ``{"data": ...}`` — see :mod:`notifly_py._envelope`.
        user_agent: Overrides the default ``notifly-sdk/<version> ...`` User-Agent.
    """

    retry_config: RetryConfig = field(factory=RetryConfig, kw_only=True)
    unwrap_data_envelope: bool = field(default=True, kw_only=True)
    user_agent: str | None = field(default=None, kw_only=True)
    # Re-declared to change the inherited defaults. attrs moves re-declared attributes to the
    # end of the field order, so construct NotiflyClient with keyword arguments.
    _base_url: str = field(default=DEFAULT_BASE_URL, alias="base_url")
    prefix: str = API_KEY_PREFIX

    def _client_headers(self) -> dict[str, str]:
        headers: dict[str, str] = {"User-Agent": self.user_agent or default_user_agent()}
        headers.update(self._headers)
        headers[self.auth_header_name] = f"{self.prefix} {self.token}" if self.prefix else self.token
        self._headers.update(headers)
        return headers

    def _httpx_kwargs(self) -> dict[str, Any]:
        kwargs = dict(self._httpx_args)
        kwargs.pop("transport", None)
        return kwargs

    def get_httpx_client(self) -> httpx.Client:
        """Return the underlying ``httpx.Client``, building one with the SDK transport stack."""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._client_headers(),
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=build_sync_transport(
                    inner=self._httpx_args.get("transport"),
                    unwrap_data_envelope=self.unwrap_data_envelope,
                    retry_config=self.retry_config,
                ),
                **self._httpx_kwargs(),
            )
        return self._client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        """Return the underlying ``httpx.AsyncClient``, building one with the SDK transport stack."""
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(
                base_url=self._base_url,
                cookies=self._cookies,
                headers=self._client_headers(),
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=self._follow_redirects,
                transport=build_async_transport(
                    inner=self._httpx_args.get("transport"),
                    unwrap_data_envelope=self.unwrap_data_envelope,
                    retry_config=self.retry_config,
                ),
                **self._httpx_kwargs(),
            )
        return self._async_client


def from_secret_key(
    secret_key: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    max_retries: int | None = None,
    **kwargs: Any,
) -> NotiflyClient:
    """Build a :class:`NotiflyClient` from a Notifly secret key.

    ``max_retries`` is a shortcut for ``retry_config=RetryConfig(max_retries=...)``.
    """
    if max_retries is not None:
        kwargs.setdefault("retry_config", RetryConfig(max_retries=max_retries))
    return NotiflyClient(base_url=base_url, token=secret_key, **kwargs)


def from_bearer_token(
    token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    **kwargs: Any,
) -> NotiflyClient:
    """Build a :class:`NotiflyClient` for a dashboard JWT (``Authorization: Bearer <jwt>``).

    Only needed for the internal, session-authenticated operations listed in
    :mod:`notifly_py.internal_ops`.
    """
    kwargs.setdefault("prefix", BEARER_PREFIX)
    return NotiflyClient(base_url=base_url, token=token, **kwargs)


__all__ = [
    "API_KEY_PREFIX",
    "BEARER_PREFIX",
    "DEFAULT_BASE_URL",
    "NotiflyClient",
    "from_bearer_token",
    "from_secret_key",
]
