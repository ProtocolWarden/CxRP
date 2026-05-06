# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
"""ExecutionTargetEnvelope — the named CxRP wire-level execution target.

Groups the existing scattered fields (lane, backend, executor,
runtime_binding) under one explicit boundary object. CxRP keeps the
asymmetry by design:

  - lane            : typed enum
  - runtime_binding : validated dataclass
  - backend         : open string
  - executor        : open string

Unknown backend/executor strings are rejected by *consumers* (e.g. OC's
``bind_execution_target``), not by the wire schema itself.

Provenance does NOT belong here — it is deployment-specific and OC-owned.

See ``docs/spec/execution_target.md`` for the full asymmetry rationale.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from cxrp.contracts.runtime_binding import RuntimeBinding
from cxrp.vocabulary.lane import LaneType


@dataclass(frozen=True)
class ExecutionTargetEnvelope:
    """The portable, CxRP-shaped execution target.

    Designed to ride additively on existing contracts (LaneDecision,
    ExecutionRequest) so consumers can migrate at their own pace. The
    pre-existing scattered fields (``executor``, ``backend``, etc.)
    remain valid; this envelope is the new canonical representation.
    """

    lane: LaneType
    backend: Optional[str] = None
    executor: Optional[str] = None
    runtime_binding: Optional[RuntimeBinding] = None
