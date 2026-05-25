# NCL_SemaLingua — Contracts

## 1. Memory Crystal Contract

A memory crystal is a single SL.md file.

### Required Sections

```
# META
- memory_id: <unique_string>
- decision: crystallize
- target: MEMORY_CRYSTAL
- layer: MEMORY_CRYSTAL

# CORE
<SL-compressed essence — 1-3 lines>

# RESONANCE
- decision: crystallize
- target: MEMORY_CRYSTAL

# GLYPH
<glyph flow, e.g. "chat→memory-shard→cortex">

# REHYDRATE
<instructions for future recall>
```

### Optional Sections

```
# LIMINAL
<open questions, unresolved tensions>

# QUOTES
<key verbatim exchanges>
```

## 2. HISTORY_MAP Index Contract

```json
{
  "library_metaphor": "summary-index with full-context retrieval",
  "entries": [
    {
      "memory_id": "mem_unique_id",
      "summary": "SL-compressed essence — fast-scan content",
      "tags": ["tag1", "tag2"],
      "significance": "high|medium|low",
      "remember_priority": "high|medium|low",
      "forget_priority": "high|medium|low",
      "retention_score": 0.0,
      "decay_factor": 0.9,
      "artifact_path": "memories/<id>/SL.md",
      "source_path": "memories/<id>/RAW.md"
    }
  ]
}
```

### Scoring

```
score = rpw * df^cycles - fpw * 0.1
```

| Level | Remember Weight | Forget Weight |
|-------|----------------|---------------|
| high  | 1.0            | 0.1           |
| medium | 0.5           | 0.5           |
| low   | 0.1            | 0.9           |

| Decay | Rate | Use Case |
|-------|------|----------|
| 0.9   | Slow | Genesis events, major decisions |
| 0.5   | Medium | Project milestones |
| 0.1   | Fast | Ephemeral notes |

## 3. Integration Points

- **LumaTeam**: loads HISTORY_MAP as layer 5 of continuity stack (SOUL → PRINCIPLES → CORE → GOALS/WISHES → HISTORY MAP → HISTORY NEW → ACTIVE CONTEXT)
- **CORTEX-Nano**: reads crystals for local recall
- **NCL_SkaiNetLink**: transports crystals between agents
