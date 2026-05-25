# NCL_SemaLingua

**Memory crystal format, HISTORY_MAP builder, and agent continuity toolkit.**

SemaLingua began as a compression system for session tokens. This repo productizes it into a complete **memory substrate for agent identity** — turning raw conversation into durable, scored, retrievable memory crystals indexed in a HISTORY_MAP.

## What This Repo Provides

- **Memory Crystal Format** — the SL.md section structure (META → CORE → LIMINAL → QUOTES → RESONANCE → GLYPH → REHYDRATE)
- **HISTORY_MAP Builder** — CLI tool that ingests conversation files and outputs structured memory crystals + index entries
- **Continuity Integration** — how SemaLingua fits into the 7-layer agent stack
- **Scoring & Decay Model** — retention scoring for automatic archival decisions

## Repo Boundary

This repo owns:
- Memory crystal format specification and tooling
- HISTORY_MAP index generation and management
- CLI tools for crystal creation, search, and maintenance
- Documentation and examples

This repo does not own:
- Session compaction (see [Stxle2/SemaLingua](https://github.com/Stxle2/SemaLingua))
- Agent identity layers (SOUL, PRINCIPLES, CORE)
- Cross-agent memory federation (NCL_CortexNet, future)

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
