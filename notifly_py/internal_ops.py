"""Registry of the bearer-only (dashboard-session) operations shipped in this SDK.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

``openapi.json`` is the *internal SDK* flavor of the Notifly OpenAPI document. It keeps
operations that the public document drops, because
``open.api.manipulation.component.ts::filterBearerOnlyIfExternal()`` removes every endpoint
whose ``security`` has no API-key scheme when generating the public flavor.

Sixteen operations in this package are therefore **JWT/dashboard-session only**: a Notifly
secret key gets a 401 on all of them. They are excluded from the :class:`notifly_py.Notifly`
facade — the supported public surface — but the generated modules are still shipped so a
first-party caller holding a dashboard token can reach them via
:func:`notifly_py.from_bearer_token`.

``ActivityController_getCharts`` carries a second caveat: it is the **only** operation in the
whole document whose success schema's sole property is ``data``, which makes its body
indistinguishable from the ``{"data": ...}`` envelope (see :mod:`notifly_py._envelope`).
That ambiguity is confined to this internal operation; no public operation is affected.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType

INTERNAL_ONLY_OPERATIONS: Mapping[str, str] = MappingProxyType(
    {
        # operationId -> generated module path
        "ActivityController_getCharts": "notifly_py.api.default.activity_controller_get_charts",
        "ActivityController_getLogs": "notifly_py.api.default.activity_controller_get_logs",
        "ActivityController_getRequestTraces": "notifly_py.api.default.activity_controller_get_request_traces",
        "ActivityController_getWorkflowRun": "notifly_py.api.default.activity_controller_get_workflow_run",
        "ActivityController_getWorkflowRuns": "notifly_py.api.default.activity_controller_get_workflow_runs",
        "AuditLogController_export": "notifly_py.api.audit_logs.audit_log_controller_export",
        "AuditLogController_list": "notifly_py.api.audit_logs.audit_log_controller_list",
        "TranslationController_deleteGroup": "notifly_py.api.default.translation_controller_delete_group",
        "TranslationController_getGroup": "notifly_py.api.default.translation_controller_get_group",
        "TranslationController_getMasterJson": "notifly_py.api.default.translation_controller_get_master_json",
        "TranslationController_getTranslation": "notifly_py.api.default.translation_controller_get_translation",
        "TranslationController_list": "notifly_py.api.default.translation_controller_list",
        "TranslationController_save": "notifly_py.api.default.translation_controller_save",
        "TranslationController_upload": "notifly_py.api.default.translation_controller_upload",
        "TranslationController_uploadMasterJson": "notifly_py.api.default.translation_controller_upload_master_json",
        "WorkflowController_duplicateWorkflow": "notifly_py.api.workflows.workflow_controller_duplicate_workflow",
    }
)
"""Operations that require a dashboard JWT. Secret keys are rejected with 401."""

INTERNAL_ONLY_MODULES: frozenset[str] = frozenset(INTERNAL_ONLY_OPERATIONS.values())


def is_internal_operation(operation_id: str) -> bool:
    """Return ``True`` when ``operation_id`` needs a dashboard JWT rather than a secret key."""
    return operation_id in INTERNAL_ONLY_OPERATIONS


def is_internal_module(module_path: str) -> bool:
    """Return ``True`` when a generated module implements a bearer-only operation."""
    return module_path in INTERNAL_ONLY_MODULES


__all__ = [
    "INTERNAL_ONLY_MODULES",
    "INTERNAL_ONLY_OPERATIONS",
    "is_internal_module",
    "is_internal_operation",
]
