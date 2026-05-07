# OperatorConsole Integration

OperatorConsole's CxRP surface is read-only and indirect — it sees CxRP
types only as serialized payloads in run artifacts and as parameters to the
OperationsCenter subprocess CLI. OperatorConsole does not import runtime
behaviour from CxRP; it uses contract definitions only.

## Types observed

| Direction | Contract | Where |
|---|---|---|
| Outbound (constructed) | `TaskProposal`-shaped payload | `console run --goal …` writes to `~/.console/queue/<uuid>.json`; OC's intake watcher reads it |
| Inbound (read-only) | `ExecutionResult`-shaped payload | `console last`, `console runs`, `console runs --json` read from `~/.console/operations_center/runs/<run_id>/result.json` |

## How payloads cross the boundary

OperatorConsole does not call `cxrp.contracts` directly. Instead:

- **Submit:** `console run` writes a JSON payload to the queue directory.
  OC's intake worker consumes it, validates, and constructs the canonical
  `TaskProposal` server-side.
- **Inspect:** `console last` / `console runs` read run artifacts as opaque
  JSON and render selected fields. Schema fidelity is enforced by OC.

This indirection means OperatorConsole stays a thin operator UX layer with
no Python coupling to the contracts.

## Schema version

OperatorConsole has no `cxrp` dependency in its environment. CxRP version
compatibility is OC's concern at the read/write boundary.

## Related

- [boundary_rules](../architecture/boundary_rules.md)
- [OperatorConsole/docs/pipeline.md](https://github.com/Velascat/OperatorConsole/blob/main/docs/pipeline.md) — execution pipeline commands (run / last / runs)
