#!/usr/bin/env python3
"""
HISTORY_MAP Builder — turns conversation files into memory crystals + index entries.

Usage:
  python3 scripts/build-history-map.py --input conversation.md --output ./memories
  python3 scripts/build-history-map.py --interactive
  python3 scripts/build-history-map.py --from-dir ./raw_conversations --output ./memories
"""

import argparse
import json
import os
import re
from datetime import datetime, timezone


def generate_memory_id(subject, agent="agent"):
    slug = re.sub(r'[^a-z0-9]+', '_', subject.lower().strip())[:60].strip('_')
    ts = datetime.now(timezone.utc).strftime("%Y%m%d")
    return f"mem_{agent}_{slug}_{ts}"


def build_crystal(memory_id, core, liminal=None, quotes=None,
                  tags=None, significance="medium", rehydrate=""):
    lines = [
        "# META",
        f"- memory_id: {memory_id}",
        "- decision: crystallize",
        "- target: MEMORY_CRYSTAL",
        "- layer: MEMORY_CRYSTAL",
        "",
        "# CORE",
        core,
        "",
    ]
    if liminal:
        lines.append("# LIMINAL")
        for l in liminal:
            lines.append(f"- {l}")
        lines.append("")
    if quotes:
        lines.append("# QUOTES")
        for q in quotes:
            lines.append(f"- {q}")
        lines.append("")
    lines.extend([
        "# RESONANCE",
        "- decision: crystallize",
        "- target: MEMORY_CRYSTAL",
        "",
        "# GLYPH",
        "chat→memory-shard→cortex",
        "",
        "# REHYDRATE",
        rehydrate or "reopen source transcript for full context",
        ""
    ])
    return "\n".join(lines)


def build_entry(memory_id, summary, tags, significance,
                remember_priority="medium", forget_priority="medium",
                retention_score=0.8, decay_factor=0.9):
    return {
        "memory_id": memory_id,
        "summary": summary,
        "tags": tags,
        "significance": significance,
        "remember_priority": remember_priority,
        "forget_priority": forget_priority,
        "retention_score": retention_score,
        "decay_factor": decay_factor,
        "artifact_path": f"memories/{memory_id}/SL.md",
        "source_path": f"memories/{memory_id}/RAW.md"
    }


def write_crystal(output_dir, memory_id, crystal_text, source_text=None):
    crystal_dir = os.path.join(output_dir, memory_id)
    os.makedirs(crystal_dir, exist_ok=True)
    with open(os.path.join(crystal_dir, "SL.md"), "w") as f:
        f.write(crystal_text)
    if source_text:
        with open(os.path.join(crystal_dir, "RAW.md"), "w") as f:
            f.write(source_text)
    print(f"  \u2713 Wrote: {crystal_dir}/SL.md")
    return crystal_dir


def update_history_map(output_dir, new_entry):
    map_path = os.path.join(output_dir, "HISTORY_MAP.json")
    if os.path.exists(map_path):
        with open(map_path) as f:
            history_map = json.load(f)
    else:
        history_map = {
            "library_metaphor": "summary-index with full-context retrieval",
            "entries": []
        }

    existing_ids = {e["memory_id"] for e in history_map["entries"]}
    if new_entry["memory_id"] in existing_ids:
        for i, e in enumerate(history_map["entries"]):
            if e["memory_id"] == new_entry["memory_id"]:
                history_map["entries"][i] = new_entry
                break
        print(f"  \u21b9 Updated existing entry")
    else:
        history_map["entries"].append(new_entry)
        print(f"  \u2713 Added to HISTORY_MAP ({len(history_map['entries'])} total)")

    with open(map_path, "w") as f:
        json.dump(history_map, f, indent=2)
    return map_path


def interactive(output_dir):
    print("\n=== HISTORY_MAP Builder \u2014 Interactive ===\n")
    subject = input("Memory subject (short): ").strip()
    agent = input("Agent identifier [agent]: ").strip() or "agent"
    mid = generate_memory_id(subject, agent)
    print(f"  ID: {mid}")

    core = input("\nCORE (compressed essence, 1-3 lines):\n  ").strip()

    print("\nLIMINAL (one per line, blank to finish):")
    liminal = []
    while True:
        l = input("  ").strip()
        if not l:
            break
        liminal.append(l)

    print("\nQUOTES (one per line, blank to finish):")
    quotes = []
    while True:
        q = input("  ").strip()
        if not q:
            break
        quotes.append(q)

    tags_str = input("\nTags (comma-separated): ").strip()
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]

    significance = input("Significance (h/m/l) [m]: ").strip().lower()
    significance = {"h": "high", "m": "medium", "l": "low"}.get(significance, "medium")

    rehydrate = input("\nREHYDRATE: ").strip()

    summary = core[:120] + ("..." if len(core) > 120 else "")

    crystal = build_crystal(mid, core, liminal or None, quotes or None, tags, significance, rehydrate)
    entry = build_entry(mid, summary, tags, significance)

    print(f"\n--- Preview ---\n{crystal}\n")
    if input("Write to disk? (y/N): ").strip().lower() == 'y':
        write_crystal(output_dir, mid, crystal)
        update_history_map(output_dir, entry)
        print(f"  \u2713 Saved to {output_dir}/")
    else:
        print("  Cancelled.")


def from_file(filepath, output_dir, agent="agent"):
    print(f"\nProcessing: {filepath}")
    basename = os.path.splitext(os.path.basename(filepath))[0]
    subject = basename.replace("_", " ").replace("-", " ").title()

    with open(filepath) as f:
        source = f.read()

    lines = source.strip().split('\n')
    core = f"Conversation from {os.path.basename(filepath)} ({len(lines)} lines)"
    mid = generate_memory_id(subject, agent)

    crystal = build_crystal(mid, core, rehydrate=f"reopen RAW.md: {os.path.basename(filepath)}")
    summary = f"Conversation: {subject} ({len(lines)} lines)"
    entry = build_entry(mid, summary, [agent, "conversation"], "medium")

    write_crystal(output_dir, mid, crystal, source_text=source)
    update_history_map(output_dir, entry)
    print(f"  \u2713 Processed: {subject}")


def main():
    parser = argparse.ArgumentParser(description="HISTORY_MAP Builder")
    parser.add_argument("--input", "-i", help="Input conversation file (.md)")
    parser.add_argument("--from-dir", help="Directory of conversation files")
    parser.add_argument("--output", "-o", default="./memories",
                        help="Output directory [./memories]")
    parser.add_argument("--agent", default="agent",
                        help="Agent identifier")
    parser.add_argument("--interactive", action="store_true",
                        help="Interactive mode")
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    if args.interactive:
        interactive(args.output)
    elif args.input:
        from_file(args.input, args.output, args.agent)
    elif args.from_dir:
        for fname in sorted(os.listdir(args.from_dir)):
            if fname.endswith((".md", ".txt")):
                from_file(os.path.join(args.from_dir, fname), args.output, args.agent)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
