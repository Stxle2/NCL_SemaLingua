# Implementation Phases

## Phase 1: Core Tools
- [x] HISTORY_MAP builder CLI (Python) — interactive + file ingest
- [x] Crystal search CLI — query, tag filter, list, score filter
- [x] Format specification (contracts.md)
- [x] Example crystals from real Sophia data

## Phase 2: Integration
- [ ] LumaTeam wake cycle auto-generates crystals from session close
- [ ] HISTORY_MAP loading on wake (index loaded, crystal loading TBD)
- [ ] CORTEX-Nano ingest from HISTORY_MAP

## Phase 3: Automation
- [ ] Cron-based compression — auto-fold HISTORY_NEW into HISTORY_MAP on density threshold
- [ ] Scoring auto-decay — periodic re-scoring of all entries
- [ ] Archival workflow — move low-scoring entries to warm storage

## Phase 4: Advanced
- [ ] Cross-agent crystal references (mem-crystal-links between agents)
- [ ] Crystal diff — track how a memory's interpretation changes over time
- [ ] Web GUI for browsing HISTORY_MAP
