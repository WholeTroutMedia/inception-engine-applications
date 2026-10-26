#!/usr/bin/env python3
"""000-cle-foundation-seed-os: Creative Liberation Engine (CLE) Public Agentic OS Seed Kernel.

A clean, zero-dependency foundational seed of the Creative Liberation Engine:
  1. 3-Gear Execution Router (Gear 1 Solo Fast-Path, Gear 2 Parallel Micro-Pod, Gear 3 Local Compute)
  2. Progressive Disclosure Context Budgeter (Prevents context-window truncation cliffs)
  3. Deterministic Pre-Flight Referee Gate (Blocks placeholder stubs and unverified outputs)
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


def route_execution_gear(
    task_complexity: float,
    parallel_branches: int = 1,
    requires_heavy_media_compute: bool = False,
) -> dict[str, Any]:
    """Deterministic 3-Gear Execution Router for autonomous agentic harnesses."""
    if requires_heavy_media_compute:
        return {
            "gear": 3,
            "mode": "GEAR_3_SOVEREIGN_COMPUTE",
            "max_concurrent_workers": 1,
            "max_step_budget": 50,
            "description": "Route heavy media, 3D manifold, or neural synthesis workloads to dedicated compute.",
        }
    if parallel_branches >= 2 or task_complexity >= 0.7:
        return {
            "gear": 2,
            "mode": "GEAR_2_PARALLEL_MICRO_POD",
            "max_concurrent_workers": min(3, max(2, parallel_branches)),
            "max_step_budget": 35,
            "description": "Spawn a bounded 2-3 agent micro-pod (Scout + Builder + Referee) with zero nested cascades.",
        }
    return {
        "gear": 1,
        "mode": "GEAR_1_SOLO_FAST_PATH",
        "max_concurrent_workers": 1,
        "max_step_budget": 25,
        "description": "Execute directly in-process with zero handoff latency and 100% prompt-cache preservation.",
    }


def pack_progressive_context(
    skills: list[dict[str, Any]],
    max_char_budget: int = 15000,
) -> dict[str, Any]:
    """Pack skill descriptors by priority without crossing the context truncation cliff."""
    ordered = sorted(skills, key=lambda s: (-int(s.get("priority", 0)), str(s.get("name", ""))))
    mounted: list[dict[str, str]] = []
    used_chars = 0
    for skill in ordered:
        entry = {"name": str(skill["name"]), "description": str(skill["description"]).strip()}
        serialized_len = len(json.dumps(entry))
        if used_chars + serialized_len <= max_char_budget:
            mounted.append(entry)
            used_chars += serialized_len
    return {
        "mounted_count": len(mounted),
        "total_candidates": len(skills),
        "used_chars": used_chars,
        "max_char_budget": max_char_budget,
        "headroom_chars": max_char_budget - used_chars,
        "mounted_skills": mounted,
    }


def referee_audit_artifact(code_text: str, verification_exit_code: int) -> dict[str, Any]:
    """Deterministic Referee Gate: reject placeholder stubs and require exit code 0."""
    banned_markers = ["// TODO", "# TODO", "NotImplementedError", "PLACEHOLDER_STUB"]
    violations = [m for m in banned_markers if m in code_text]
    if verification_exit_code != 0:
        violations.append(f"Non-zero verification exit code: {verification_exit_code}")
    passed = len(violations) == 0
    return {
        "passed": passed,
        "status": "CERTIFIED_EXIT_0" if passed else "CIRCUIT_BREAKER_HALT",
        "violations": violations,
        "artifact_sha256": hashlib.sha256(code_text.encode("utf-8")).hexdigest(),
    }
