# `002-extract-pbr-material-synth` — Procedural Tangent-Space PBR Material & Normal Map Synthesizer

- **Release Drop**: `Drop #002` (Cycle 02 (Staged Bi-Weekly Queue))
- **Domain**: 3D, Shaders & Spatial Computing (`extract_pbr_materials`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`

## Overview
Pure-Python Sobel-Scharr tangent-space normal, roughness, and height map synthesizer from heightfield grids.

## Quick Start
```bash
python3 apps/002-extract-pbr-material-synth/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: 0125029d67a651de...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.


---
**Human Review & Provenance**
- **Principal & Reviewer**: Justin Aharoni ([@jaharoni](https://github.com/jaharoni))
- **Direct Engineering Contact**: `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`
- **Engineering Studio**: [WholeTroutMedia](https://github.com/WholeTroutMedia) / [Inception Engine Systems](https://inceptionengine.systems)
- **Companion Verification Ledger**: [WholeTroutMedia/open-source-bounties](https://github.com/WholeTroutMedia/open-source-bounties)

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
