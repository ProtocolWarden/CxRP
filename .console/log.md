# Log

_Chronological continuity log. Decisions, stop points, what changed and why._
_Not a task tracker — that's backlog.md. Keep entries concise and dated._

## Stop Points

- integrations/ docs refreshed (2026-05-07, on `main`): The three thin (5-line) integration stubs were rewritten with concrete details: which contracts cross which boundary, how each consumer uses them, schema_version pinning, and links to relevant consumer-side docs. operations_center.md now describes the cxrp_mapper.py bridge between OC's internal Pydantic mirror and canonical CxRP types. switchboard.md clarifies that RoutingPlan is SB-specific (not a CxRP type). operator_console.md explains the read-only file-based indirection (no Python coupling).

- docs/README.md index added (2026-05-07, on `main`): Required by Custodian R6 (newly landed). Indexes spec/ (v0.1, v0.2, execution_target), architecture/ (boundary_rules, compatibility, lifecycle), and integrations/ (operations_center, operator_console, switchboard).

- pyproject description had wrong protocol expansion (2026-05-06, on `main`): pyproject.toml said "Contract × Request Protocol" but every other surface (README, GitHub description, internal docs) uses "Contract eXecution Routing Protocol". Fixed for consistency on PyPI metadata.

- Schema 0.3 — symmetry pass: typed backend/executor on the wire (2026-05-05, on `main`): Closed-system simplification — every CxRP consumer is ours, so the "open strings on the wire" flexibility wasn't paying for itself. New `cxrp/vocabulary/executor.py` ships `BackendName` + `ExecutorName` enums with values matching OC's same-named enums. `LaneDecision` and `ExecutionRequest` and `ExecutionTargetEnvelope` all use the typed enums for backend/executor. Schema bumped 0.2 → 0.3; v0.2 frozen on disk; new v0.3 schemas with explicit enum constraints in JSON. Examples migrated to v0.3 directory. The flipped test that previously asserted "open strings at envelope level" now asserts the typed-enum rejection. 51 → 59 tests still pass; backwards-compat is at the version boundary, not within 0.3.

- ExecutionTargetEnvelope landed (2026-05-05, on `main`): Names the wire-shape execution target as a first-class concept. Frozen dataclass with `lane: LaneType` (typed) + `backend/executor: str | None` (open) + `runtime_binding: RuntimeBinding | None` (validated). Additive on `LaneDecision` and `ExecutionRequest` — legacy scattered `executor`/`backend` fields remain valid; the envelope rides alongside. schema_version stays at 0.2 (additive); v0.3 enum bump explicitly abandoned in favor of preserving open-string flexibility on the wire. JSON schemas updated to allow the new optional `execution_target` block. 8 new tests; 51 → 59. The full asymmetry rationale lives at `docs/spec/execution_target.md`.

- Phase 0 of Backend Control Audit framework landed (2026-05-05, on `main`): All 8 sub-items of the contract foundation. **0.1** Contract evolution policy added to README (additive non-breaking; renames/removals require schema_version bump; capability removals require deprecation cycle; `evidence.extensions` is the sole sanctioned extension slot). **0.2 + 0.8** New `Evidence` dataclass at `cxrp/contracts/evidence.py` carrying `files_changed`, `commands_run`, `tests_run`, `artifacts_created`, `failure_reason`, `extensions` — wired into `ExecutionResult` as `evidence` field plus a `summary` field; JSON schema updated to enforce `additionalProperties: false` at the evidence level (extensions go under `extensions`, not at the top). **0.3** `cxrp/vocabulary/capability.py` with `CapabilitySet` enum (7 coarse capabilities: repo_read, repo_patch, test_run, shell_read, shell_write, network_access, human_review). **0.4** Naming guardrail tests reject digits, size words (small/medium/large), and degree words (safe/strict/loose/limited/max/min) in capability names; soft cap of 8 to discourage bloat. **0.5–0.7** `cxrp/vocabulary/runtime.py` (RuntimeKind, SelectionMode enums, validity table, optional-field allow-list) + `cxrp/contracts/runtime_binding.py` with `__post_init__` validation rejecting invalid kind×selection_mode pairs and forbidden optional-fields-per-kind (e.g. `human` with `model=opus` → ValueError). RuntimeBinding wired into ExecutionRequest as optional field; schema updated. Architect-via-Claude-CLI-Opus use case has a dedicated test confirming construction + serialization + schema validation. 16 → 51 tests pass.

## Recent Decisions

| Decision | Rationale | Date |
|----------|-----------|------|
| CxrpExecutionResult typed deserialization | parse_execution_result(payload) validates and returns typed object; summarize_execution_result() now takes typed object not raw dict; T2 exclusion removed since tests now have real assertions | 2026-05-02 |
| C16 encoding fix in json_schema.py | 2× schema_path.read_text() missing encoding= keyword; Custodian C16 finding resolved | 2026-05-02 |

## Stop Points

_(none)_

## Notes

_Free-form scratch. Clear periodically._
