# Notifly Python SDK (`notifly-py`)

Official Python SDK for the [Notifly](https://notifly.io) API — open-source, self-hostable notification infrastructure (in-app inbox, push, email, SMS, chat).

Covers the full Notifly REST surface (131 operations): events/triggers, subscribers, topics, workflows, messages, notifications, integrations, layouts, environments, audit logs, and more. Fully typed (`py.typed`), sync **and** async on `httpx`.

## Install

```bash
pip install notifly-py
```

Requires Python 3.11+.

## Authentication

Notifly authenticates with your environment's secret key via the `Authorization: ApiKey <secret_key>` header:

```python
from notifly_py import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.notifly.io",  # or your self-hosted API URL
    token="<NOTIFLY_SECRET_KEY>",
    prefix="ApiKey",
)
```

> **Note:** `prefix="ApiKey"` is required — the default `Bearer` prefix is for JWT sessions, not API keys.

## Trigger a workflow

```python
from notifly_py.api.events import events_controller_trigger
from notifly_py.models import TriggerEventRequestDto, TriggerEventRequestDtoPayload

payload = TriggerEventRequestDtoPayload()
payload.additional_properties = {"body": "Hello from Python!"}

with client as client:
    result = events_controller_trigger.sync(
        client=client,
        body=TriggerEventRequestDto(
            name="my-workflow",          # workflow identifier
            to="subscriber-id",          # or SubscriberPayloadDto / TopicPayloadDto / list of them
            payload=payload,
        ),
    )
```

Or async:

```python
async with client as client:
    result = await events_controller_trigger.asyncio(client=client, body=...)
```

## API structure

Endpoints live under `notifly_py.api.<tag>`, one module per operation. Each module exposes four call styles:

| Function | Behavior |
| --- | --- |
| `sync` | blocking, returns the parsed body (or `None`) |
| `sync_detailed` | blocking, returns `Response` (status code, headers, parsed body) |
| `asyncio` | async, returns the parsed body |
| `asyncio_detailed` | async, returns `Response` |

Available tags: `audit_logs`, `channel_connections`, `channel_endpoints`, `contexts`, `environment_variables`, `environments`, `events`, `integrations`, `layouts`, `messages`, `notifications`, `subscribers`, `topics`, `workflows`.

All request/response models are in `notifly_py.models`.

## Client options

Both `Client` and `AuthenticatedClient` accept:

- `timeout` — an `httpx.Timeout`
- `verify_ssl` — path to a CA bundle, or `False` (not recommended)
- `headers` / `cookies` — extra values sent with every request
- `raise_on_unexpected_status` — raise `errors.UnexpectedStatus` on undocumented status codes (recommended: `True`)

Advanced `httpx` customization:

```python
import httpx

client = AuthenticatedClient(base_url="https://api.notifly.io", token=key, prefix="ApiKey")
client.set_httpx_client(httpx.Client(base_url="https://api.notifly.io", proxy="http://localhost:8030"))
```

Clients support context managers (recommended) or manual use; the underlying `httpx` client keeps connections open until closed.

## Development

This SDK is **generated** from the Notifly OpenAPI spec — do not hand-edit files under `notifly_py/` (except to regenerate).

- Spec snapshot: `openapi.yaml` (produced by the [DevinoSolutions/notifly](https://github.com/DevinoSolutions/notifly) monorepo build: `apps/api/dist/swagger-spec.json` + Speakeasy overlay).
- Generator: [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), pinned in `scripts/regenerate.sh`.
- To regenerate after a spec update: replace `openapi.yaml`, run `scripts/regenerate.sh`, review the diff, bump `version` in `pyproject.toml`.

Releases publish to PyPI via GitHub Actions [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (`.github/workflows/publish.yml`) — no tokens.

## License

MIT — see [LICENSE](LICENSE).
