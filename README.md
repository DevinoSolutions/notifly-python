# Notifly Python SDK (`notifly-py`)

Official Python SDK for the [Notifly](https://notifly.io) API — open-source, self-hostable notification infrastructure (in-app inbox, push, email, SMS, chat).

Covers the Notifly REST surface (131 operations): events/triggers, subscribers, topics, workflows, messages, notifications, integrations, layouts, environments, and more. Fully typed (`py.typed`), sync **and** async on `httpx`, with a hand-written ergonomic layer on top of a generated core.

## Install

```bash
pip install notifly-py
```

Requires Python 3.11+.

## Quickstart

```python
from notifly_py import Notifly

notifly = Notifly("<NOTIFLY_SECRET_KEY>")

result = notifly.events.trigger(
    workflow="welcome",                 # workflow trigger identifier
    to="subscriber_123",                # subscriber id, payload object, or a list of them
    payload={"name": "Ada"},
)
print(result.transaction_id)
```

Async is the same surface, awaited:

```python
from notifly_py import AsyncNotifly

async with AsyncNotifly("<NOTIFLY_SECRET_KEY>") as notifly:
    result = await notifly.events.trigger(workflow="welcome", to="subscriber_123")
```

The client is configured for the hosted API by default. For a self-hosted deployment pass `base_url="https://notifly.internal"`.

## What the client does for you

| Behaviour | Detail |
| --- | --- |
| **Response envelope** | The API wraps single entities as `{"data": {...}}`. The SDK unwraps that at the transport layer, so you always get a populated model. Paginated bodies (`data` + `totalCount` + cursors) are left alone. |
| **Auth prefix** | `Authorization: ApiKey <secret key>` by default. The raw generated `AuthenticatedClient` defaults to `Bearer`, which silently 401s with a secret key. |
| **Retries** | `429`, `408`, `502`, `503`, `504` and connection errors are retried with exponential backoff + jitter, honouring `Retry-After`. `GET`/`PUT`/`DELETE` always; `POST`/`PATCH` only when you pass an `idempotency_key`. |
| **Typed errors** | The facade raises `NotFoundError`, `ValidationError`, `RateLimitError`, … instead of returning a fourteen-member union. |
| **Pagination** | `iter_all()` / `iter_*()` walk every page — cursor, offset and page-number styles all handled. |
| **User-Agent** | `notifly-py/<version> python/<x.y.z> httpx/<x.y.z>`. |

## Resources

```python
notifly.events.trigger(workflow=..., to=..., payload=...)
notifly.events.trigger_bulk([...])
notifly.events.broadcast(body=...)
notifly.events.cancel(transaction_id)

notifly.subscribers.create(subscriber_id="u_1", email="ada@example.com")
notifly.subscribers.get("u_1")
notifly.subscribers.update("u_1", last_name="Lovelace")
notifly.subscribers.delete("u_1")
notifly.subscribers.list(limit=50, email="ada@example.com")
notifly.subscribers.iter_all()                       # every page, flattened
notifly.subscribers.get_preferences("u_1")
notifly.subscribers.list_notifications("u_1")
notifly.subscribers.register_device_token("u_1", "fcm", body=...)

notifly.topics.upsert(key="product-updates", name="Product updates")
notifly.topics.subscribe("product-updates", ["u_1", "u_2"])
notifly.topics.unsubscribe("product-updates", ["u_1"])
notifly.topics.iter_subscriptions("product-updates")

notifly.workflows.list() / .get(id) / .create(body) / .patch(id, body) / .delete(id) / .iter_all()
notifly.messages.list() / .iter_all() / .delete(id)
notifly.notifications.list() / .iter_all() / .get(id)
notifly.integrations.list() / .list_active() / .create(body) / .update(id, body) / .delete(id)
```

Any parameter documented for an operation can be passed through as a keyword argument — for example `notifly.subscribers.list(limit=100, order_direction="DESC")`. Every method also accepts `idempotency_key=...`.

## Errors

```python
from notifly_py import NotFoundError, RateLimitError, ValidationError

try:
    notifly.subscribers.get("missing")
except NotFoundError as error:
    print(error.status_code, error.message, error.error_id)
except ValidationError as error:
    print(error.errors, error.ctx)
except RateLimitError as error:
    print(error.retry_after, error.rate_limit)
```

Hierarchy: `NotiflyError` → `NotiflyAPIError` → `AuthenticationError` (401/403), `NotFoundError` (404), `ValidationError` (400/422), `ConflictError` (409), `RateLimitError` (429), `ServerError` (5xx). Notifly does not emit RFC 9457 `problem+json`; these map its `ErrorDto` shape.

## Configuration

```python
from notifly_py import Notifly, RetryConfig

notifly = Notifly(
    "<NOTIFLY_SECRET_KEY>",
    base_url="https://api.notifly.io",
    retry_config=RetryConfig(max_retries=4, backoff_factor=0.5, max_retry_after=30.0),
    timeout=httpx.Timeout(30.0),
    headers={"x-tenant": "acme"},
)
```

`Notifly(..., max_retries=0)` disables retries. `unwrap_data_envelope=False` disables envelope unwrapping (only needed if the API ever stops wrapping — the scheduled spec-drift job watches for exactly that).

## Advanced: the generated client

The ergonomic layer is additive. The generated modules remain the escape hatch for the operations the facade does not name, and they accept the same client:

```python
from notifly_py import NotiflyClient
from notifly_py.api.layouts import layouts_controller_list

client = NotiflyClient(token="<NOTIFLY_SECRET_KEY>")
page = layouts_controller_list.sync(client=client, limit=10)
```

Endpoints live under `notifly_py.api.<tag>`, one module per operation, each exposing four call styles:

| Function | Behavior |
| --- | --- |
| `sync` | blocking, returns the parsed body (or `None`) |
| `sync_detailed` | blocking, returns `Response` (status code, headers, parsed body) |
| `asyncio` | async, returns the parsed body |
| `asyncio_detailed` | async, returns `Response` |

Tags: `audit_logs`, `channel_connections`, `channel_endpoints`, `contexts`, `default`, `environment_variables`, `environments`, `events`, `integrations`, `layouts`, `messages`, `notifications`, `subscribers`, `topics`, `workflows`. All models live in `notifly_py.models`.

These functions return unions and never raise on HTTP errors — that is by design; only the facade raises.

### Dashboard-only operations

Sixteen shipped operations authenticate with a dashboard JWT rather than a secret key (activity/charts, audit logs, translations, workflow duplication). They are listed in `notifly_py.internal_ops.INTERNAL_ONLY_OPERATIONS`, excluded from the `Notifly` facade, and reachable only with `notifly_py.from_bearer_token(...)`.

## Testing against the SDK

`respx` mocks below the SDK's transports, so all of its behaviour (including unwrapping and retries) stays active:

```python
import httpx, respx
from notifly_py import Notifly

@respx.mock
def test_welcome_email():
    respx.post("https://api.notifly.io/v1/events/trigger").mock(
        return_value=httpx.Response(201, json={"data": {"acknowledged": True, "status": "processed"}})
    )
    assert Notifly("sk_test").events.trigger(workflow="welcome", to="u_1").acknowledged
```

## Development

The core of this SDK is **generated** from the Notifly OpenAPI document. Never hand-edit `notifly_py/api/**` or `notifly_py/models/**`.

- Spec snapshot: `openapi.json` — the internal-SDK flavor produced by the [DevinoSolutions/notifly](https://github.com/DevinoSolutions/notifly) monorepo (`apps/api/exportOpenAPIJSON.ts`).
- Generator: [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), pinned in `scripts/regenerate.sh`.
- Hand-written modules layered on top (preserved across regeneration): `__init__.py`, `_envelope.py`, `_transport.py`, `_version.py`, `exceptions.py`, `facade.py`, `internal_ops.py`, `notifly_client.py`, `pagination.py`.

```bash
uv sync --group dev
uv run pytest            # unit suite, no network
uv run ruff check .
uv run mypy              # strict, hand-written layer only
uv run python scripts/check_drift.py        # committed spec vs the live public document
NOTIFLY_SECRET_KEY=... uv run pytest tests/e2e   # opt-in live smoke
```

To regenerate after a spec update: replace `openapi.json`, run `scripts/regenerate.sh`, run the test suite (the envelope regression tests are the gate), review the diff, bump `version` in `pyproject.toml`.

Releases publish to PyPI via GitHub Actions [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (`.github/workflows/publish.yml`) — no tokens.

## License

MIT — see [LICENSE](LICENSE).
