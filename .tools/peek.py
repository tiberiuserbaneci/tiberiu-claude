#!/usr/bin/env python3
"""peek.py — read MANY regions across MANY files in ONE call.

Usage:
  python3 /work/.tools/peek.py <<'JSON'
  [{"file": "/work/a.ts", "start": 40, "end": 90},
   {"file": "/work/b.ts"},
   {"file": "/work/c.py", "grep": "def handle", "ctx": 12}]
  JSON

Per region: "start"/"end" are 1-based inclusive line numbers (omit both for the
whole file). "grep" instead returns every match with "ctx" lines around it
(default 8) — use it when you know WHAT you want but not WHERE. Output is
line-numbered and labelled per region, so several files come back readable in
one result. Missing files are reported, never fatal.
"""
import json, sys, re, pathlib

try:
    regions = json.load(sys.stdin)
except Exception as e:
    print(f"FATAL: stdin is not valid JSON ({e})"); sys.exit(2)
if isinstance(regions, dict):
    regions = [regions]

missing = 0
for r in regions:
    path = r.get("file") or r.get("path") or ""
    p = pathlib.Path(path)
    if not p.is_file():
        print(f"━━ {path} ━━\nMISSING (not a file)"); missing += 1; continue
    try:
        lines = p.read_text(errors="replace").splitlines()
    except Exception as e:
        print(f"━━ {path} ━━\nUNREADABLE ({e})"); missing += 1; continue

    pat = r.get("grep")
    if pat:
        ctx = int(r.get("ctx", 8))
        try:
            rx = re.compile(pat)
        except re.error as e:
            print(f"━━ {path} ━━\nBAD REGEX {pat!r} ({e})"); missing += 1; continue
        hits = [i for i, l in enumerate(lines) if rx.search(l)]
        if not hits:
            print(f"━━ {path} — /{pat}/ ━━\n(no match in {len(lines)} lines)"); continue
        # Merge overlapping context windows so a cluster of hits prints once.
        spans = []
        for i in hits:
            lo, hi = max(0, i - ctx), min(len(lines), i + ctx + 1)
            if spans and lo <= spans[-1][1]:
                spans[-1][1] = max(spans[-1][1], hi)
            else:
                spans.append([lo, hi])
        print(f"━━ {path} — /{pat}/ — {len(hits)} match(es) in {len(spans)} window(s), file is {len(lines)} lines ━━")
        for lo, hi in spans:
            for i in range(lo, hi):
                print(f"{i+1:6d}\t{lines[i]}")
            print("       ⋯")
        continue

    start = int(r.get("start", 1))
    end = int(r.get("end", len(lines)))
    start = max(1, start); end = min(len(lines), end)
    print(f"━━ {path} — lines {start}-{end} of {len(lines)} ━━")
    for i in range(start - 1, end):
        print(f"{i+1:6d}\t{lines[i]}")

print(f"peek: {len(regions)} region(s), {missing} unreadable")
sys.exit(1 if missing == len(regions) else 0)
