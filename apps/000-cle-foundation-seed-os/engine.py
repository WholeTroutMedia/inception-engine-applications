#!/usr/bin/env python3
"""000-cle-foundation-seed-os: Creative Liberation Engine.

An open creative foundation shaped by the imagination of the person using it.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


def shape_creative_flow(
    intent_depth: float,
    parallel_streams: int = 1,
    dedicated_studio_pass: bool = False,
) -> dict[str, Any]:
    """Adapt the creative flow naturally to the scope of the creator's intent."""
    if dedicated_studio_pass:
        return {
            "stage": 3,
            "mode": "DEEP_STUDIO_CRAFT",
            "active_streams": 1,
            "horizon": 50,
            "description": "Focus full creative depth on high-resolution synthesis and craft.",
        }
    if parallel_streams >= 2 or intent_depth >= 0.7:
        return {
            "stage": 2,
            "mode": "HARMONIZED_ENSEMBLE",
            "active_streams": min(3, max(2, parallel_streams)),
            "horizon": 35,
            "description": "Coordinate parallel creative perspectives in harmony.",
        }
    return {
        "stage": 1,
        "mode": "DIRECT_EXPRESSION",
        "active_streams": 1,
        "horizon": 25,
        "description": "Move directly from thought to expression with zero friction.",
    }


def curate_active_palette(
    capabilities: list[dict[str, Any]],
    canvas_capacity: int = 15000,
) -> dict[str, Any]:
    """Select the clearest tools for the current creative moment while keeping the canvas uncluttered."""
    ordered = sorted(capabilities, key=lambda s: (-int(s.get("priority", 0)), str(s.get("name", ""))))
    selected: list[dict[str, str]] = []
    used = 0
    for item in ordered:
        entry = {"name": str(item["name"]), "description": str(item["description"]).strip()}
        size = len(json.dumps(entry))
        if used + size <= canvas_capacity:
            selected.append(entry)
            used += size
    return {
        "selected_count": len(selected),
        "total_available": len(capabilities),
        "used_capacity": used,
        "canvas_capacity": canvas_capacity,
        "open_space": canvas_capacity - used,
        "palette": selected,
    }


def verify_finished_work(work_text: str, verification_exit_code: int) -> dict[str, Any]:
    """Ensure every piece of work is complete and ready before presentation."""
    unfinished_markers = ["// TODO", "# TODO", "NotImplementedError", "PLACEHOLDER_STUB"]
    gaps = [m for m in unfinished_markers if m in work_text]
    if verification_exit_code != 0:
        gaps.append(f"Non-zero verification exit code: {verification_exit_code}")
    complete = len(gaps) == 0
    return {
        "complete": complete,
        "status": "READY" if complete else "NEEDS_REFINEMENT",
        "gaps": gaps,
        "work_sha256": hashlib.sha256(work_text.encode("utf-8")).hexdigest(),
    }
