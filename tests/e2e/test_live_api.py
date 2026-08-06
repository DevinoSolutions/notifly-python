"""Opt-in live smoke tests against a real Notifly environment.

Skipped unless ``NOTIFLY_SECRET_KEY`` is set. Point ``NOTIFLY_BASE_URL`` at a non-production
environment when possible; ``NOTIFLY_E2E_WORKFLOW`` selects the workflow to trigger.

    NOTIFLY_SECRET_KEY=... uv run pytest tests/e2e -m e2e

They exist to prove the one thing mocks cannot: that the real API still wraps single entities
in ``{"data": ...}`` and that the SDK therefore returns populated models.
"""

from __future__ import annotations

import os
import uuid

import pytest

from notifly_py import Notifly
from notifly_py.exceptions import NotFoundError, ValidationError

pytestmark = [
    pytest.mark.e2e,
    pytest.mark.skipif(not os.getenv("NOTIFLY_SECRET_KEY"), reason="NOTIFLY_SECRET_KEY is not set"),
]


@pytest.fixture(scope="module")
def notifly() -> Notifly:
    return Notifly(
        os.environ["NOTIFLY_SECRET_KEY"],
        base_url=os.getenv("NOTIFLY_BASE_URL", "https://api.notifly.io"),
    )


def test_listing_subscribers_returns_a_populated_page(notifly: Notifly) -> None:
    page = notifly.subscribers.list(limit=1)
    assert hasattr(page, "data")
    assert page.total_count is not None


def test_create_read_delete_round_trip_returns_populated_models(notifly: Notifly) -> None:
    subscriber_id = f"notifly-py-e2e-{uuid.uuid4().hex[:12]}"
    created = notifly.subscribers.create(subscriber_id=subscriber_id, first_name="SDK", last_name="Smoke")
    assert created.subscriber_id == subscriber_id, "envelope unwrapping failed against the live API"

    fetched = notifly.subscribers.get(subscriber_id)
    assert fetched.first_name == "SDK"

    notifly.subscribers.delete(subscriber_id)
    with pytest.raises(NotFoundError):
        notifly.subscribers.get(subscriber_id)


def test_triggering_an_unknown_workflow_raises_a_typed_validation_error(notifly: Notifly) -> None:
    """The live error body proves what mocks assumed: required spec fields are often absent.

    The real 422 here carries no ``errors`` key, and the real 400 on this route carries no
    ``type`` — both are popped unguarded by the generated DTOs, so this used to escape as
    ``KeyError`` instead of a typed error. Kept live because only the API can tell us its
    error bodies changed shape.
    """
    with pytest.raises(ValidationError) as excinfo:
        notifly.events.trigger(
            workflow=f"notifly-py-e2e-missing-{uuid.uuid4().hex[:12]}",
            to=f"notifly-py-e2e-{uuid.uuid4().hex[:12]}",
        )

    assert excinfo.value.status_code in (400, 422)
    assert excinfo.value.message


@pytest.mark.skipif(not os.getenv("NOTIFLY_E2E_WORKFLOW"), reason="NOTIFLY_E2E_WORKFLOW is not set")
def test_trigger_returns_a_populated_acknowledgement(notifly: Notifly) -> None:
    subscriber_id = f"notifly-py-e2e-{uuid.uuid4().hex[:12]}"
    notifly.subscribers.create(subscriber_id=subscriber_id)
    try:
        result = notifly.events.trigger(
            workflow=os.environ["NOTIFLY_E2E_WORKFLOW"],
            to=subscriber_id,
            payload={"source": "notifly-py e2e"},
        )
        assert result.acknowledged is True
        assert result.transaction_id
    finally:
        notifly.subscribers.delete(subscriber_id)
