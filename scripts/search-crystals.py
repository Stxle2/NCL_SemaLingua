#!/usr/bin/env python3
"""
Search memory crystals by query string or tags.

Usage:
  python3 scripts/search-crystals.py --query "genesis"
  python3 scripts/search-crystals.py --tag genesis
  python3 scripts/search-crystals.py --list
"""

import argparse
import json
import os
import sys


def load(path):
    if not os.path.exists(path):
        print(f"Error: {path} not found")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def search(entries, query=None, tag=None, min_score=None):
    results = []
    ql = query.lower() if query else None
    for e in entries:
        score = 0
        if ql:
            combined = " ".join([
                e.get("summary", ""),
                e.get("memory_id", ""),
                " ".join(e.get("tags", []))
            ]).lower()
            if ql in combined:
                score += 5
        if tag and tag in e.get("tags", []):
            score += 3
        if min_score is not None and e.get("retention_score", 0) < min_score:
            continue
        if query or tag:
            if score > 0:
                results.append((score, e))
        else:
            results.append((0, e))
    results.sort(key=lambda x: -x[0])
    return [r[1] for r in results]


def display(e, show_path=False):
    print(f"\n{'─'*60}")
    print(f"  {e.get('memory_id', '?')}")
    print(f"  Sig: {e.get('significance', '?'):>6}  "
          f"Retention: {e.get('retention_score', 0):.1f}  "
          f"Decay: {e.get('decay_factor', 0):.1f}")
    print(f"  Tags: {', '.join(e.get('tags', []))}")
    print(f"  Summary: {e.get('summary', '?')[:120]}")
    if show_path:
        print(f"  Path: {e.get('artifact_path', '?')}")


def main():
    ap = argparse.ArgumentParser(description="Search memory crystals")
    ap.add_argument("--query", "-q", help="Search query")
    ap.add_argument("--tag", "-t", help="Filter by tag")
    ap.add_argument("--history-map", default="./memories/HISTORY_MAP.json")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--min-score", type=float)
    ap.add_argument("--paths", action="store_true")
    ap.add_argument("--limit", type=int, default=20)
    args = ap.parse_args()

    hm = load(args.history_map)
    entries = hm.get("entries", [])

    if args.list:
        for e in entries[:args.limit]:
            display(e, args.paths)
        print(f"\n  {len(entries)} total (showing {min(args.limit, len(entries))})")
    elif args.query or args.tag:
        results = search(entries, args.query, args.tag, args.min_score)
        for e in results[:args.limit]:
            display(e, args.paths)
        print(f"\n  {len(results)} matches")
    else:
        print(f"HISTORY_MAP: {len(entries)} entries. Use --list or --query.")


if __name__ == "__main__":
    main()
