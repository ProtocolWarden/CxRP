## Summary

<!-- One or two sentences describing what this PR does and why. -->

## Changes

<!-- Bullet list of what changed. -->

-

## Contract Impact

<!-- Check all that apply. -->

- [ ] No contract change (refactor, docs, tests, tooling only)
- [ ] Additive within current schema version (new optional field or enum value)
- [ ] Breaking change — introduces new `schemas/vX.Y/` revision
- [ ] Vocabulary change (`status`, `lane`, or `artifact` enums)
- [ ] Validation helper change

If this is a contract change, list the affected contracts:

- [ ] `TaskProposal`
- [ ] `LaneDecision`
- [ ] `ExecutionRequest`
- [ ] `ExecutionResult`

## Downstream Consumers

<!-- Note any expected impact on OperatorConsole, SwitchBoard, or OperationsCenter. -->

## Testing

- [ ] Tests pass: `PYTHONPATH=. .venv/bin/python -m pytest tests/ -v`
- [ ] Schemas updated under `schemas/vX.Y/` (if contract changed)
- [ ] Examples updated under `examples/vX.Y/` (if contract changed)
- [ ] Spec updated in `docs/spec/` (if normative behavior changed)

## Related Issues

<!-- Closes #N or References #N -->

## Notes for Reviewer

<!-- Anything non-obvious: migration considerations, deferred follow-ups, design trade-offs. -->
