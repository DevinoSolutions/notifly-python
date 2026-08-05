"""Package version and the SDK ``User-Agent``.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.
"""

from __future__ import annotations

import platform
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _package_version

PACKAGE_NAME = "notifly-py"

try:
    __version__ = _package_version(PACKAGE_NAME)
except PackageNotFoundError:  # running from a source checkout that was never installed
    __version__ = "0.0.0+unknown"


def user_agent() -> str:
    """Return the default ``User-Agent`` sent with every request.

    Format: ``notifly-py/<version> python/<x.y.z> httpx/<x.y.z>`` — stable enough for
    server-side attribution and version-adoption dashboards.
    """
    import httpx  # imported lazily so importing the version never pulls in httpx

    return f"{PACKAGE_NAME}/{__version__} python/{platform.python_version()} httpx/{httpx.__version__}"


__all__ = ["PACKAGE_NAME", "__version__", "user_agent"]
