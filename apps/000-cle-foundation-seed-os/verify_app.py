#!/usr/bin/env python3
"""Verification Suite for Creative Liberation Engine (000-cle-foundation-seed-os)."""

from engine import curate_active_palette, shape_creative_flow, verify_finished_work


def main() -> int:
    s1 = shape_creative_flow(0.25, parallel_streams=1, dedicated_studio_pass=False)
    s2 = shape_creative_flow(0.85, parallel_streams=4, dedicated_studio_pass=False)
    s3 = shape_creative_flow(0.50, parallel_streams=1, dedicated_studio_pass=True)
    assert s1["stage"] == 1 and s1["active_streams"] == 1
    assert s2["stage"] == 2 and s2["active_streams"] == 3
    assert s3["stage"] == 3 and s3["mode"] == "DEEP_STUDIO_CRAFT"

    sample_palette = [
        {"name": f"craft-{i:02d}", "description": "Open creative capability " * 4, "priority": i}
        for i in range(25)
    ]
    curated = curate_active_palette(sample_palette, canvas_capacity=1800)
    assert curated["used_capacity"] <= 1800
    assert curated["palette"][0]["name"] == "craft-24"

    clean_work = verify_finished_work("def create(x):\n    return x * 2\n", verification_exit_code=0)
    assert clean_work["complete"] is True and clean_work["status"] == "READY"

    incomplete_work = verify_finished_work("def create(x):\n    raise NotImplementedError\n", verification_exit_code=0)
    assert incomplete_work["complete"] is False and incomplete_work["status"] == "NEEDS_REFINEMENT"

    print("[PASS] 000-cle-foundation-seed-os (Creative Liberation Engine) verified (exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
