---
name: 000-cle-foundation-seed-os
description: >-
  Lightweight, zero-dependency 3-Gear task router, context budget packer, and pre-execution invariant gate.
---

# Agent Synthesis Skill: `000-cle-foundation-seed-os` (Creative Liberation Engine (CLE) — Public Agentic OS Seed Kernel)

- **Toolkit Slot**: `creative_liberation_engine_public_seed`
- **Engine SHA-256**: `9613aea9af2344bb2d7be0c91122b600e47ae85a9f94259e9c1b861eb2daa90e`
- **Verification**: `[PASS] 000-cle-foundation-seed-os verified (3-Gear Router + Context Budgeter + Referee Gate, exit code 0).`

## Constitutional Invariants for Autonomous Agents
- Default to Gear 1 Solo Fast-Path for single-file and low-latency tasks to preserve 100% of the prompt prefix cache.
- Cap Gear 2 parallel micro-pods at 3 concurrent workers (Scout + Specialist + Referee) with zero nested subagent cascades.
- Maintain strict progressive context budgets so system instructions and skill frontmatter never cross model truncation cliffs.
- Enforce a fail-closed Deterministic Referee Gate (Exit Code 0 + zero placeholder stubs) before emitting any artifact.

## Multi-Stage Synthesis Recipe
1. Stage 1 (Gear Triage): Evaluate task complexity and parallelism via route_execution_gear() before spawning any subagents.
1. Stage 2 (Progressive Context Packing): Mount only high-priority skill descriptors within max_char_budget via pack_progressive_context().
1. Stage 3 (Referee Certification): Run referee_audit_artifact() and standalone verification scripts (exit code 0) before completing the turn.

## MCP Tool Registration Schema
See [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) for the ready-to-mount `inputSchema`.
