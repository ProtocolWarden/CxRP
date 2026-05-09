# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
"""AgentTopology — canonical agent-topology vocabulary for CxRP contracts.

Topology answers "how many agents collaborate?" at the structural level.
Quantifiers (thread counts, concurrency limits) belong in policy, not
topology names. See ADR 0002 in OperationsCenter for naming guardrails.

Naming guardrails (enforced by ``test_agent_topology.py``):
  - values are lowercase_snake_case
  - no numeric suffixes      (single_agent_1 ❌)
  - no size words            (small / medium / large ❌)
  - no degree words          (safe / strict / loose / limited / max / min ❌)

ADR 0002 guardrails:
  G1 — four values maximum at launch; new values require two-backend proof.
  G2 — no value may equal a single backend's name.
"""
from __future__ import annotations

from enum import Enum


class AgentTopology(str, Enum):
    """Canonical agent topology vocabulary for CxRP contracts."""

    SINGLE_AGENT           = "single_agent"
    SEQUENTIAL_MULTI_AGENT = "sequential_multi_agent"
    DAG_WORKFLOW           = "dag_workflow"
    SWARM_PARALLEL         = "swarm_parallel"


_BANNED_DEGREE_TOKENS = frozenset({
    "safe", "strict", "loose", "limited", "max", "min",
})
_BANNED_SIZE_TOKENS = frozenset({
    "small", "medium", "large",
})
