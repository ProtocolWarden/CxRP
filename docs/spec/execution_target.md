# ExecutionTarget Model

> One concept, two layers, deliberate asymmetry.

`ExecutionTarget` is the **named first-class boundary object** that
groups every axis of "what to run, with what, powered by what, sourced
from where." It exists in two distinct shapes — one on the wire, one
in OperationsCenter — and the line between them is intentional.

## The four execution axes

```text
Lane             = what kind of work is this?
Backend/Executor = what performs it?
RuntimeBinding   = what powers it?
Provenance       = which fork/ref/patches supply the backend?
```

All four are first-class as concepts. They are *represented* differently
across the wire/runtime boundary on purpose.

## Asymmetry table

| Axis             | CxRP wire contract | OperationsCenter boundary           |
|------------------|--------------------|-------------------------------------|
| **Lane**         | typed enum (`LaneType`) | narrowed enum (`LaneName`)     |
| **RuntimeBinding** | validated dataclass (`RuntimeBinding`) | validated mirror (`RuntimeBindingSummary`) |
| **Backend**      | open string         | strict enum (`BackendName`)        |
| **Executor**     | open string         | strict enum or lane-role mapping   |
| **Provenance**   | not present         | `BackendProvenance` (registry-derived) |

## Why the asymmetry is deliberate

### CxRP stays flexible on backend/executor

CxRP is a portable protocol. New backends and executors arrive faster
than coordinated CxRP minor-version rollouts can absorb. Keeping
`backend: str` and `executor: str` open at the wire means:

- A new tool (`some_future_tool_we_dont_know_yet`) can flow through
  CxRP without a contract bump
- Consumer-side narrowing rejects unknowns at the boundary, where
  rejection is appropriate

### OperationsCenter stays strict at execution

OC dispatches actual subprocess work. Strict typing at the execution
boundary lets the binder, drift detector, and policy engine be
exhaustive instead of speculative. Unknown `backend` strings from CxRP
are rejected loudly at OC's binding step — they never reach the adapter.

### Provenance is OC-owned

Which fork commit + patches are running is **deployment-specific**, not
**protocol intent**. Two OC deployments routing to the same backend may
have different forks; that's a runtime fact OC owns via the upstream
registry, not something SwitchBoard or other CxRP producers should know.

## Two shapes

```text
CxRP envelope                              OperationsCenter binding
─────────────────────────                  ───────────────────────────
ExecutionTargetEnvelope                    BoundExecutionTarget
  lane: LaneType                             lane: LaneName
  backend: str | None             →          backend: BackendName
  executor: str | None            →          executor: ExecutorName
  runtime_binding: RuntimeBinding            runtime_binding: RuntimeBindingSummary
                                             provenance: BackendProvenance | None
                                                                    ↑ filled from
                                                                      OC upstream
                                                                      registry
```

The arrow is `bind_execution_target(envelope, catalog, policy)`.

## Lifecycle

```text
1. SwitchBoard selects lane + recommends backend/executor/runtime
2. SwitchBoard emits an ExecutionTargetEnvelope (CxRP wire shape)
3. OperationsCenter validates + narrows + resolves provenance
4. OperationsCenter produces a BoundExecutionTarget (strict)
5. Coordinator dispatches the BoundExecutionTarget to the adapter
6. ExecutionResult records the bound target for audit/replay
```

## What goes where (canonical phrasing)

Avoid ambiguous phrases like "lane/backend/runtime thingy" in shared
docs. Use these instead:

| Phrase | Meaning |
|---|---|
| `ExecutionTargetEnvelope` | The CxRP wire-level intent |
| `BoundExecutionTarget`    | The OC-validated executable target |
| `BackendProvenance`       | The OC-owned source-of-truth for what fork/ref runs |

## Non-goals

- ExecutionTarget does **not** make backend/executor enums global in
  CxRP. The asymmetry is the design.
- Provenance does **not** travel on the CxRP wire. It is OC-internal.
- Adopting `ExecutionTargetEnvelope` does **not** require a CxRP
  schema_version bump — it lands as an additive optional field.
