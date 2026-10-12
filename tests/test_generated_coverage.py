"""Nothing in ``openapi.json`` may be silently dropped by the generator.

openapi-python-client reports a schema or operation it cannot handle as a *warning* and still exits 0:
the model disappears, and so does every endpoint that touches it (``AgentBehaviorDto`` once took
``PATCH /v1/agents/{identifier}`` with it). These tests fail the build instead.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = REPO_ROOT / "notifly_py"
HTTP_METHODS = ("get", "post", "put", "patch", "delete")


@pytest.fixture(scope="module")
def spec() -> dict[str, Any]:
    return json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))


def _snake(name: str) -> str:
    """openapi-python-client's file naming: ``MessageCTA`` -> ``message_cta``, ``OAuthUrl`` -> ``o_auth_url``."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name.replace("__", "_")).lower()


def test_every_spec_operation_has_a_generated_module(spec: dict[str, Any]) -> None:
    generated = {
        module.stem for module in PACKAGE_ROOT.glob("api/*/*.py") if module.name != "__init__.py"
    }
    operation_ids = [
        operation["operationId"]
        for path_item in spec["paths"].values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS
    ]

    missing = sorted(op for op in operation_ids if _snake(op) not in generated)

    assert not missing, f"operations the generator dropped: {missing}"
    assert len(generated) == len(operation_ids)


def test_every_spec_schema_has_a_generated_model(spec: dict[str, Any]) -> None:
    generated = {module.stem for module in (PACKAGE_ROOT / "models").glob("*.py")}

    missing = sorted(name for name in spec["components"]["schemas"] if _snake(name) not in generated)

    assert not missing, f"schemas the generator dropped: {missing}"
