# Continuity Integration

How SemaLingua memory crystals fit into the LumaTeam 7-layer agent stack.

## The Stack

```
SOUL ── identity, timeless
PRINCIPLES ── ethical frame, rarely changes
CORE ── capabilities, skills, tools
GOALS/WISHES ── active direction, quarterly
HISTORY MAP ── compressed life-path ← **SemaLingua crystals**
HISTORY NEW ── recent narrative, last few sessions
ACTIVE CONTEXT ── this wake, this task
```

## Where SemaLingua Lives

- **Layer 5, HISTORY MAP**: The indexed JSON of Mem-Crystal-Links, each pointing to an SL.md crystal with optional RAW.md source. Loaded on every agent wake to ground long-term context.
- **Layer 6, HISTORY NEW**: Raw session logs that haven't been compressed yet. When HISTORY NEW exceeds density threshold, its oldest entries are folded into HISTORY MAP as new crystals.

## Wake Cycle

On every agent wake, the stack is loaded in order:

1. SOUL.md — who am I?
2. PRINCIPLES.md — what guides me?
3. CORE.md — what can I do?
4. GOALS/WISHES.md — what am I working toward?
5. HISTORY_MAP.json — what memory crystals inform this moment?
6. HISTORY_NEW.md — what happened recently?
7. ACTIVE_CONTEXT — what am I doing right now?

At session close, significant events from ACTIVE_CONTEXT + HISTORY_NEW are crystallized into SL.md format and indexed in HISTORY_MAP.

## Scoring & Archival

Memories in HISTORY_MAP are scored on each wake:

```
score = rpw * df^cycles - fpw * 0.1
```

Crystals below a configurable threshold are candidates for archival (moved to warm storage) or forgetting (removed from index). The builder tool computes this automatically.

## Cross-Reference

- Full stack spec: [NCL_LumaTeam/docs/CONTINUITY_STACK.md](https://github.com/Stxle2/NCL_LumaTeam)
- Crystal format: contracts.md in this repo
