# WholeTroutMedia — Inception Engine Open-Source Micro-Applications

Welcome to the public open-source micro-application repository for **WholeTroutMedia** ([`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia)) and **Inception Engine Systems** ([`https://inceptionengine.systems`](https://inceptionengine.systems)), led and reviewed by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`).

Every two weeks, we open-source a self-contained, zero-dependency micro-application distilled from our internal **12-Plugin Impossible Toolkit** across document forensics, procedural 3D/PBR synthesis, and frame-accurate NLE media processing.

---

## Dual-Layer Design: Simple for Humans, Composable for Autonomous Agents

Each micro-application under [`apps/`](./apps/) is structured with two complementary layers:
1. **For Human Developers**: A clean, dependency-free reference module (`engine.py` + `verify_app.py`) that runs out of the box with standard Python 3 and passes deterministic verification (`Exit Code 0`).
2. **For Visiting AI Agents & MCP Routers ([`llms.txt`](./llms.txt) & [`.well-known/agent.json`](./.well-known/agent.json))**: Every module includes an `AGENT_BLUEPRINT.json` and `SKILL.md` containing formal mathematical invariants, MCP `inputSchema` definitions, and multi-stage synthesis recipes so autonomous agents can compose these primitives into full studio applications.

---

## Published & Staged Micro-Applications ([`APPLICATION_LEDGER.md`](./APPLICATION_LEDGER.md))

| Drop | Micro-Application | Toolkit Slot | Summary | Verification | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Foundation Seed #000** | [`000-cle-foundation-seed-os`](./apps/000-cle-foundation-seed-os/) | `creative_liberation_engine_public_seed` | Creative Liberation Engine (CLE) — Public Agentic OS Seed Kernel | [`AGENT_BLUEPRINT.json`](./apps/000-cle-foundation-seed-os/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #001** | [`001-seal-pdf-media-notary`](./apps/001-seal-pdf-media-notary/) | `seal_pdf_notary + utility_exif_scrubber` | Cryptographic Media Notary & EXIF Orientation / Privacy Scrubber | [`AGENT_BLUEPRINT.json`](./apps/001-seal-pdf-media-notary/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #002** | [`002-extract-pbr-material-synth`](./apps/002-extract-pbr-material-synth/) | `extract_pbr_materials` | Procedural Tangent-Space PBR Material & Normal Map Synthesizer | [`AGENT_BLUEPRINT.json`](./apps/002-extract-pbr-material-synth/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **STAGED_QUEUE** |
| **Drop #003** | [`003-smart-timeline-stem-ducker`](./apps/003-smart-timeline-stem-ducker/) | `separate_audio_stems + smart_video_squeezer` | Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler | [`AGENT_BLUEPRINT.json`](./apps/003-smart-timeline-stem-ducker/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **STAGED_QUEUE** |

---

## Companion Repository
- **[`WholeTroutMedia/open-source-bounties`](https://github.com/WholeTroutMedia/open-source-bounties)**: Our companion open-source bug-fix and bounty verification ledger, complete with our [7-Beacon Counter-Bot Radar](https://github.com/WholeTroutMedia/open-source-bounties/blob/main/BOT_RADAR_AND_SIGNAL_PROOF.md).


---
**Human Review & Provenance**
- **Principal & Reviewer**: Justin Aharoni ([@jaharoni](https://github.com/jaharoni))
- **Direct Engineering Contact**: `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`
- **Engineering Studio**: [WholeTroutMedia](https://github.com/WholeTroutMedia) / [Inception Engine Systems](https://inceptionengine.systems)
- **Companion Verification Ledger**: [WholeTroutMedia/open-source-bounties](https://github.com/WholeTroutMedia/open-source-bounties)

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
