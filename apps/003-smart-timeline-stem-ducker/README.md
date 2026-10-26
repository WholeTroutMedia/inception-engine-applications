# `003-smart-timeline-stem-ducker` — Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler

- **Release Drop**: `Drop #003` (Cycle 03 (Staged Bi-Weekly Queue))
- **Domain**: Cinema, Audio Stems & NLE Post-Production (`separate_audio_stems + smart_video_squeezer`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`

## Overview
Compiles declarative JSON edit decision lists and speech intervals into frame-accurate FCPXML 1.10 timelines with -18dB music ducking.

## Quick Start
```bash
python3 apps/003-smart-timeline-stem-ducker/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: ca687984b6343fca...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.


---
**Human Review & Provenance**
- **Principal & Reviewer**: Justin Aharoni ([@jaharoni](https://github.com/jaharoni))
- **Direct Engineering Contact**: `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`
- **Engineering Studio**: [WholeTroutMedia](https://github.com/WholeTroutMedia) / [Inception Engine Systems](https://inceptionengine.systems)
- **Companion Verification Ledger**: [WholeTroutMedia/open-source-bounties](https://github.com/WholeTroutMedia/open-source-bounties)

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
