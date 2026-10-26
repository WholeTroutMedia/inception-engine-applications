#!/usr/bin/env python3
"""Deterministic Verification Suite for 000-cle-foundation-seed-os."""

from engine import pack_progressive_context, referee_audit_artifact, route_execution_gear


def main() -> int:
    g1 = route_execution_gear(0.25, parallel_branches=1, requires_heavy_media_compute=False)
    g2 = route_execution_gear(0.85, parallel_branches=4, requires_heavy_media_compute=False)
    g3 = route_execution_gear(0.50, parallel_branches=1, requires_heavy_media_compute=True)
    assert g1["gear"] == 1 and g1["max_concurrent_workers"] == 1
    assert g2["gear"] == 2 and g2["max_concurrent_workers"] == 3
    assert g3["gear"] == 3 and g3["mode"] == "GEAR_3_SOVEREIGN_COMPUTE"

    sample_skills = [
        {"name": f"skill-{i:02d}", "description": "Deterministic capability descriptor " * 4, "priority": i}
        for i in range(40)
    ]
    packed = pack_progressive_context(sample_skills, max_char_budget=1800)
    assert packed["used_chars"] <= 1800
    assert packed["mounted_skills"][0]["name"] == "skill-39"

    clean_audit = referee_audit_artifact("def solve(x):\n    return x * 2\n", verification_exit_code=0)
    assert clean_audit["passed"] is True and clean_audit["status"] == "CERTIFIED_EXIT_0"

    stub_audit = referee_audit_artifact("def solve(x):\n    raise NotImplementedError\n", verification_exit_code=0)
    assert stub_audit["passed"] is False and stub_audit["status"] == "CIRCUIT_BREAKER_HALT"

    print("[PASS] 000-cle-foundation-seed-os verified (3-Gear Router + Context Budgeter + Referee Gate, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
