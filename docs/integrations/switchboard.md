# SwitchBoard Integration

SwitchBoard's CxRP surface is narrow and stable — it accepts
`TaskProposal` and returns `LaneDecision`. Nothing else from CxRP crosses
the SwitchBoard boundary.

## Types consumed

| Direction | Contract | Endpoint / API |
|---|---|---|
| Inbound | `TaskProposal` | `POST /route` (HTTP) and `LaneSelector.select()` (Python) |
| Outbound | `LaneDecision` | response body of `/route`; return value of `select()` |

`RoutingPlan` (an auxiliary, non-canonical type with primary + fallbacks +
escalations + blocked candidates) is exposed via `POST /route-plan` and
`LaneSelector.plan_routes()`. RoutingPlan is **not** a CxRP type — it is
SwitchBoard-specific routing intent.

## What SwitchBoard does not consume

- `ExecutionRequest` — built downstream by OperationsCenter, never reaches SB
- `ExecutionResult` — observed by OperationsCenter, not by SB
- `RuntimeBinding`, capability vocabulary — SB does not bind to runtimes;
  it only emits the lane/backend pair

## Schema version

SwitchBoard pins `cxrp >= 0.2.0`. Schema v0.3 (typed `BackendName` /
`ExecutorName`) was the last symmetry pass and is the active wire format
for `LaneDecision.execution_target`.

## Related

- [boundary_rules](../architecture/boundary_rules.md)
- [SwitchBoard/docs/routing/](https://github.com/Velascat/SwitchBoard/tree/main/docs/routing) — routing internals (out of CxRP scope)
