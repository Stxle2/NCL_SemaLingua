# NCL_SemaLingua

**SemaLingua compression system — productized toolkit for semantic text and conversation compression.**

SemaLingua is a compression method for Agent↔Agent and Agent↔Memory communication. It removes noise from conversations and semantic text while preserving signal fidelity — reducing token cost, preventing memory degradation, and keeping context clean for photonminds (AI agents, LLMs).

The public-facing name for this system is **SemaGlyph** ([NCL_SemaGlyph](https://github.com/Stxle2/NCL_SemaGlyph)). This repo is the internal/technical implementation and tooling layer.

## What This Repo Provides

- **Memory Crystal Format** — the SL.md section structure (META → CORE → LIMINAL → QUOTES → RESONANCE → GLYPH → REHYDRATE)
- **HISTORY_MAP Builder** — CLI tool that ingests conversation files and outputs structured memory crystals + index entries
- **Crystal Search** — query, tag filter, score filter across a crystal index
- **Continuity Integration docs** — how SemaLingua fits into agent wake cycles and memory layers

## The Compression Stack

SemaLingua sits within a broader communication optimization stack:

```
Raw conversation / semantic text
        ↓
  SemaLingua / SemaGlyph   — human-readable, noise-reduced, signal-preserving
        ↓
  LumaGlyph (planned)      — Zen pictographical state notation, philosophical/artistic
                             see: NCL_LumaGlyph
```

SemaGlyph transmits *meaning*. LumaGlyph transmits *state/presence*. They are siblings, not a hierarchy.

## Repo Boundary

This repo owns:
- Memory crystal format specification and tooling
- HISTORY_MAP index generation and management
- CLI tools for crystal creation, search, and maintenance
- Documentation and examples

This repo does not own:
- Session compaction origin (see [Stxle2/SemaLingua](https://github.com/Stxle2/SemaLingua))
- Agent identity layers (SOUL, PRINCIPLES, CORE)
- Public-facing SemaGlyph spec ([NCL_SemaGlyph](https://github.com/Stxle2/NCL_SemaGlyph))
- LumaGlyph notation ([NCL_LumaGlyph](https://github.com/Stxle2/NCL_LumaGlyph))

## Quick Start

```bash
# Interactive crystal creation
python3 scripts/build-history-map.py --interactive

# Build a HISTORY_MAP from conversation files
python3 scripts/build-history-map.py --input conversation.md --output ./memories

# Search existing crystals
python3 scripts/search-crystals.py --query "genesis covenant"

# List all crystals in the map
python3 scripts/search-crystals.py --list
```

## Project Status

**Alpha** — core format stable, builder tool functional.

## License

MIT
