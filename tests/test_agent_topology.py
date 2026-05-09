# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2026 Velascat
"""AgentTopology tests + naming guardrails.

The guardrail tests reject topology names that smuggle quantifier or
degree semantics into the structural class. Topology is coarse;
policy carries the limits. See cxrp/vocabulary/agent_topology.py
and OperationsCenter ADR 0002.
"""
from __future__ import annotations

import re

import pytest

from cxrp.vocabulary.agent_topology import (
    _BANNED_DEGREE_TOKENS,
    _BANNED_SIZE_TOKENS,
    AgentTopology,
)


def test_agent_topology_members():
    assert AgentTopology.SINGLE_AGENT.value           == "single_agent"
    assert AgentTopology.SEQUENTIAL_MULTI_AGENT.value == "sequential_multi_agent"
    assert AgentTopology.DAG_WORKFLOW.value            == "dag_workflow"
    assert AgentTopology.SWARM_PARALLEL.value          == "swarm_parallel"


def test_member_count_at_most_four():
    """ADR 0002 G1 — four values maximum at launch."""
    assert len(list(AgentTopology)) <= 4


def test_values_are_lowercase_snake_case():
    for member in AgentTopology:
        assert re.fullmatch(r"[a-z][a-z_]*[a-z]", member.value), member.value


def test_values_have_no_numeric_suffix():
    for member in AgentTopology:
        assert not re.search(r"\d", member.value), (
            f"{member.value!r} contains a digit — quantifiers belong in policy"
        )


def test_values_have_no_size_words():
    for member in AgentTopology:
        tokens = set(member.value.split("_"))
        leaked = tokens & _BANNED_SIZE_TOKENS
        assert not leaked, (
            f"{member.value!r} contains size tokens {leaked}"
        )


def test_values_have_no_degree_words():
    for member in AgentTopology:
        tokens = set(member.value.split("_"))
        leaked = tokens & _BANNED_DEGREE_TOKENS
        assert not leaked, (
            f"{member.value!r} contains degree tokens {leaked}"
        )


def test_round_trip_from_string():
    for member in AgentTopology:
        assert AgentTopology(member.value) is member


def test_is_str_subclass():
    for member in AgentTopology:
        assert isinstance(member, str)


def test_invalid_value_raises():
    with pytest.raises(ValueError):
        AgentTopology("invalid_topology")
