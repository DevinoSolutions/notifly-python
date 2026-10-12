# Changelog

All notable changes to `notifly-sdk` are documented here. This project follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] — 2026-10-12

Regenerated from the Notifly OpenAPI document v3.19.1 (142 operations, 11 new) with
`openapi-python-client` 0.29.0.

### Added

- The Agents API, available as `notifly_py.api.agents` (generated modules, `sync` / `sync_detailed` /
  `asyncio` / `asyncio_detailed` each): `AgentsController_createAgent`, `_listAgents`, `_getAgent`,
  `_updateAgent`, `_deleteAgent`, `_updateAgentBridge`, `AgentIntegrationsController_addAgentIntegration`,
  `_listAgentIntegrations`, `_updateAgentIntegration`, `_removeAgentIntegration` and
  `AgentReplyController_handleAgentReplyHandler`. These are not on the `Notifly` facade yet.
- New models for agents, reply payloads and signals, the Grafana OnCall / Line / Opsgenie / PagerDuty /
  tool-webhook / Webex endpoint types, and tool workflow steps.
- `connection_mode` filter on `ChannelConnectionsController_listChannelConnections`; `tool` channel
  and step type; `rules` on integrations; `data` on topics; `bridge_url` on contexts; `agent_id`
  and `bridge_url` on event triggers; `provider_overrides` on every workflow step response;
  `create_subscriber_if_missing` on the channel endpoint create DTOs; new provider ids
  (`sendly`, `anypost`, `ruach-sms`, `webex-messaging`, `line`, `sendblue`, `novu-web-chat`,
  `pagerduty`, `opsgenie`, `grafana`, `tool-webhook`).
- `scripts/prepare_spec.py`: named fixes and union order pinning (`scripts/union_order.json`) applied
  to a copy of `openapi.json` before generation. The first fix types
  `AgentBehaviorDto.reactionOnResolved` as a nullable string; the API declares it `type: object` with
  the default `"check"`, and the generator answers that by silently dropping `AgentBehaviorDto`,
  `AgentResponseDto`, `ListAgentsResponseDto`, `UpdateAgentRequestDto` and
  `PATCH /v1/agents/{identifier}`. The second drops the server-side behavior defaults (see Changed).
- Tests for all eleven Agents operations (request shape, parsing through the `data` envelope, model
  round trips), for the spec fixes, and a generated-coverage gate that fails when the generator
  drops any operation or schema.

### Changed

- `LayoutsController_list` and `WorkflowController_searchWorkflows` now document bounds on their
  paging parameters: `limit` 1-100, `offset` 0 or more.
- Fields that became optional (typed `... | Unset`, default `UNSET`; code that read them as always
  present now has to handle `Unset`): `ChatRenderOutput.body`, `UpdateTopicRequestDto.name`,
  `UpdateWorkflowDto.origin`.
- Unions that gained a variant (`ToolStepUpsertDto` / `ToolStepResponseDto` / the `tool` preview /
  the new endpoint types), so an `isinstance` ladder over them needs a new branch:
  `CreateWorkflowDto.steps`, `UpdateWorkflowDto.steps`, `WorkflowResponseDto.steps`,
  `GeneratePreviewResponseDto.result`, `GetChannelEndpointResponseDto.endpoint`,
  `UpdateChannelEndpointRequestDto.endpoint` and the body of `ChannelEndpointsController_createChannelEndpoint`.
- Model fields were added before existing ones on 29 models (for example `provider_overrides` on every
  step response DTO, `rules` on the integration request DTOs, `agent` on `CreateWorkflowDto` and
  `WorkflowResponseDto`, `bridge_url` / `agent_id` on `TriggerEventRequestDto`,
  `create_subscriber_if_missing` on the seven `Create*EndpointDto`, `data` on `TopicResponseDto`,
  `bcc` on `WebhookInboundEmailMailDto`) and `UpdateWorkflowDto` moved `origin` after its required
  fields. Every field is keyword-friendly and nothing was removed or renamed, but code that built these
  models with positional arguments must switch to keyword arguments.
- Inline union variants keep their numbers. The generator names `GeneratePreviewResponseDto.result`
  variants by position and the API inserted the new `tool` preview before `delay` and `digest`, which
  would have turned `...ResultType7` from the delay preview into the tool preview and dropped
  `ResultType7Type.DELAY` / `ResultType8Type.DIGEST`. `scripts/union_order.json` now pins the variant
  order of every union and new variants go last, so `...ResultType7` stays delay, `...ResultType8` stays
  digest and the tool preview is `...ResultType9`. No class or enum member of 0.1.1 was removed or
  renamed.
- A partial `PATCH /v1/agents/{identifier}` no longer overwrites stored values with defaults.
  `AgentBehaviorDto.acknowledgeOnReceived` and `.reactionOnResolved` carried the documented defaults
  (`true`, `"check"`), so `UpdateAgentRequestDto(behavior=AgentBehaviorDto(subscriber_access=...))`
  also sent both and reset them. The API applies those defaults itself on read and `$set`s only the
  behavior fields present in the body, so the generator now sees them without a default: an unset
  field is omitted and `reaction_on_resolved=None` still sends `null` to turn the reaction off.

### Notes

- `AgentsController_createAgent` takes a required `novu_analytics_source` header argument and
  `AgentsController_deleteAgent` a required `delete_from_provider` query argument, because the API
  declares them required.


## [0.1.1] — 2026-09-23

### Changed

- Package metadata and documentation only, no behaviour changes: the PyPI summary and README now
  describe this as the client SDK for the Notifly API. The earlier wording described the Notifly
  platform as open-source and self-hostable, which it is not — only this client SDK is open
  source (MIT). Also dropped the `novu` keyword and internal platform source paths from the
  `notifly_py._envelope` docstring.

## [0.1.0] — 2026-08-06 (first PyPI publish)

First release. Generated from the Notifly OpenAPI document (v3.17.1, 131 operations) with
`openapi-python-client` 0.29.0, plus a hand-written layer on top.

### Added

- Full sync + async coverage of the Notifly REST API — 131 operations, 715 models, `py.typed`.
- `Notifly` / `AsyncNotifly` facade with grouped resources (`events`, `subscribers`, `topics`,
  `workflows`, `messages`, `notifications`, `integrations`) instead of 131 flat modules.
- `NotiflyClient`, defaulting to the `ApiKey` authorization prefix Notifly actually expects,
  plus `from_secret_key()` / `from_bearer_token()` constructors.
- Runtime unwrapping of the API's single-entity `{"data": ...}` response envelope, installed as
  an httpx transport so it applies to every operation and survives regeneration. Without it the
  generated models parse the envelope instead of the payload.
- Typed exception hierarchy over `ErrorDto`: `AuthenticationError`, `NotFoundError`,
  `ValidationError`, `ConflictError`, `RateLimitError` (with `retry_after`), `ServerError`.
- Automatic retries with exponential backoff, jitter and `Retry-After` support; non-idempotent
  methods are retried only when an `idempotency-key` is supplied.
- Auto-pagination helpers for the cursor, offset and page-number styles (`iter_all()`, `iter_*`).
- `__version__` and an identifying `User-Agent`.
- Test suite (167 tests) covering the envelope contract, auth headers, errors, retries,
  pagination, the facade, the spec contract and the drift gate; opt-in live E2E tests.
- Scheduled spec-drift workflow that re-checks the envelope contract, route coverage and the
  bearer-only operation registry against the live public OpenAPI document.

### Fixed

- Error responses whose body omits a field the OpenAPI document marks required no longer escape
  as `KeyError`. The generated error DTOs pop their required keys unguarded (`ErrorDto` pops
  `statusCode`/`timestamp`/`path`, `ValidationErrorDto` also pops `errors`,
  `PayloadValidationExceptionDto` also pops `type`), and production omits some of them — a live
  400 from `POST /v1/events/trigger` carries no `type`, and the everyday "unknown workflow" 422
  carries no `errors`. The facade now drops an unparsable error model and rebuilds the typed
  exception from the raw body, so those surface as `ValidationError` as documented. Success
  bodies are unaffected and still raise when unparsable.

### Notes

- Sixteen shipped operations require a dashboard JWT rather than a secret key. They are recorded
  in `notifly_py.internal_ops` and excluded from the `Notifly` facade.
- The Notifly API does not emit RFC 9457 `application/problem+json`; the exception hierarchy maps
  its `ErrorDto` shape instead.

[unreleased]: https://github.com/DevinoSolutions/notifly-python/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/DevinoSolutions/notifly-python/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/DevinoSolutions/notifly-python/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/DevinoSolutions/notifly-python/releases/tag/v0.1.0
