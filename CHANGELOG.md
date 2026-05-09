# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] — 2026-05-09

### Added
- `AgentTopology` enum (`cxrp/vocabulary/agent_topology.py`) — four canonical agent-topology
  values: `SINGLE_AGENT`, `SEQUENTIAL_MULTI_AGENT`, `DAG_WORKFLOW`, `SWARM_PARALLEL`.
  Follows `(str, Enum)` dual-inheritance pattern; values are lowercase snake_case.
  ADR 0002 compliant: ≤4 values at launch, no single-backend name as a value.
- `tests/test_agent_topology.py` — naming-guardrail tests: lowercase snake_case values,
  no numeric suffixes, no size words, no degree words; plus round-trip and str-subclass tests.
