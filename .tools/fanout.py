#!/usr/bin/env python3
# fanout.py — N independent judgments in ONE round, in parallel.
# Fill ITEMS + build_prompt(). Each item is judged by its own model call; the
# item's text NEVER enters the agent's context — only the summary printed here.
# KIND: "classify" (short verdict, cheap) | "extract" (structured fields, cheap)
#       | "generate" (content that ships — runs on this session's own model)
import json, subprocess, concurrent.futures, pathlib

KIND = "classify"
OUT_DIR = pathlib.Path("/work/.tools/fanout-out")
ITEMS = [
    # "path/or/value", ...   (one entry per independent judgment)
]

def build_prompt(item: str) -> str:
    # Include the instruction AND the item's content. For a file:
    #   body = pathlib.Path(item).read_text()[:12000]
    #   return f"Does this file use the deprecated prop? Answer YES or NO plus the line.\n\n{body}"
    return f"INSTRUCTION HERE\n\n{item}"

def one(item: str):
    try:
        p = subprocess.run(
            ["ultron", "ai", "run", "--kind", KIND, "--prompt", build_prompt(item)],
            capture_output=True, text=True, timeout=120)
        if p.returncode != 0:
            return item, None, (p.stderr or p.stdout or "failed").strip()[:120]
        return item, p.stdout.strip(), None
    except Exception as e:
        return item, None, str(e)[:120]

OUT_DIR.mkdir(parents=True, exist_ok=True)
results, failures = {}, {}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for item, text, err in ex.map(one, ITEMS):
        (failures if err else results)[item] = err or text
# One retry, failures only.
if failures:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for item, text, err in ex.map(one, list(failures)):
            if not err:
                results[item] = text
                failures.pop(item, None)

for item, text in results.items():
    (OUT_DIR / (item.strip("/").replace("/", "_")[:80] + ".txt")).write_text(str(text))
(OUT_DIR / "summary.json").write_text(json.dumps({"ok": list(results), "failed": failures}, indent=1))

# CONTEXT DISCIPLINE: print a TABLE, never the bodies. Full text is on disk.
print(f"fanout: {len(results)} ok, {len(failures)} failed → {OUT_DIR}")
for item, text in list(results.items())[:40]:
    print(f"  {item[:52]:54s} {str(text).splitlines()[0][:70] if text else ''}")
for item, err in failures.items():
    print(f"  FAILED {item[:52]:47s} {err}")
