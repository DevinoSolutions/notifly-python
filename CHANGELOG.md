# Changelog

All notable changes to `notifly-sdk` are documented here. This project follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[unreleased]: https://github.com/DevinoSolutions/notifly-python/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/DevinoSolutions/notifly-python/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/DevinoSolutions/notifly-python/releases/tag/v0.1.0
