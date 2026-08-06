#!/usr/bin/env python3
"""apply_hunks.py — apply many hunks across many files in ONE call.

Usage:
  python3 /work/.tools/apply_hunks.py [--dry-run] <<'JSON'
  [{"file": "/work/a.ts", "old": "exact unique text", "new": "replacement"},
   {"file": "/work/b.ts", "old": "…", "new": "…"}]
  JSON

Rules: "old" must occur EXACTLY once in its file (include surrounding lines to
disambiguate). Prints counts and verdicts only, never file bodies. Idempotent:
a hunk whose "new" is already present is reported ALREADY, not failed.
Exit 0 only if every hunk applied or was already applied.
"""
import json, sys, collections

dry = "--dry-run" in sys.argv
try:
    hunks = json.load(sys.stdin)
except Exception as e:
    print(f"FATAL: stdin is not valid JSON ({e})"); sys.exit(2)
if isinstance(hunks, dict):
    hunks = [hunks]

by_file = collections.OrderedDict()
for h in hunks:
    by_file.setdefault(h["file"], []).append(h)

applied = already = failed = 0
for path, hs in by_file.items():
    try:
        src = original = open(path).read()
    except Exception as e:
        print(f"FAIL {path}: cannot read ({e})"); failed += len(hs); continue
    for h in hs:
        old, new = h["old"], h["new"]
        n = src.count(old)
        if n == 1:
            src = src.replace(old, new, 1); applied += 1
        elif n == 0 and new and new in src:
            already += 1
        else:
            failed += 1
            why = "not found" if n == 0 else f"{n} matches, need exactly 1"
            print(f"FAIL {path}: {why}: {old[:70]!r}")
    if src != original and not dry:
        open(path, "w").write(src)

verb = "would apply" if dry else "applied"
print(f"{verb} {applied}, already-present {already}, failed {failed}, across {len(by_file)} file(s)")
sys.exit(1 if failed else 0)
