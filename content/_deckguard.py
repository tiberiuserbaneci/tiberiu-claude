#!/usr/bin/env python3
"""Anti-anticipation guard. The audience must never be able to predict the next material.

Operator, 2026-08-08: "NU REPETI TEMELE LA INFINIT PENTRU CA OBOSESTI AUDIENTA - CHIAR DACA
DOUA SEAMANA TREBUIE SA EXISTE UN MIC TWIST ... AUDIENTA NU TREBUIE SA TI ANTICIPEZE
URMATORUL MATERIAL".

At a hundred reels this cannot live in anybody's head, and a rule that lives only in prose is
a rule that gets broken on the day it matters. So the run is recorded and checked. Every deck
registers into MANIFEST.json, and `check()` refuses one that would make the feed predictable:

  1  DESIGN may not repeat the previous deck's, and may not appear 3 times in the last 5.
  2  THEME alternates. Two blacks or two whites back to back is the fastest way to make a
     grid look like one long post.
  3  FAMILY - the subject family, not the title - may not appear in the last 4 decks. Two
     decks about money are two decks about money however differently they are worded.
  4  TWIST - when a family does come back, it must carry a declared twist naming what is
     different about it. "Same subject, new numbers" is not a twist.
  5  BREAK - at least one deck in every run of 4 must be marked `break=True`: a simple 2D
     glassmorphism graphic piece that interrupts the series. Four structured decks in a row
     is a pattern, and a pattern is something the audience can skip.

The point of 5 is worth being explicit about. Consistency is what makes a set recognisable
and it is also what makes it skippable. The break slot exists so the eye cannot settle.
"""
import json, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = REPO / "content" / "decks" / "MANIFEST.json"


def load() -> list:
    if not MANIFEST.exists():
        return []
    return json.loads(MANIFEST.read_text()).get("decks", [])


def save(decks: list) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps({"decks": decks}, indent=2) + "\n")


def check(spec: dict, run: list) -> list[str]:
    """Everything wrong with shipping `spec` next, given the decks already shipped."""
    bad = []
    prev = run[-1] if run else None
    last5 = run[-5:]
    last4 = run[-4:]

    if prev and spec["design"] == prev["design"]:
        bad.append(f"design '{spec['design']}' repeats the previous deck ({prev['id']})")
    if sum(1 for d in last5 if d["design"] == spec["design"]) >= 2:
        bad.append(f"design '{spec['design']}' would be the 3rd in the last 5")
    if prev and spec["theme"] == prev["theme"]:
        bad.append(f"theme '{spec['theme']}' repeats the previous deck ({prev['id']})")

    clash = [d for d in last4 if d.get("family") == spec.get("family")]
    if clash and not spec.get("twist"):
        bad.append(f"family '{spec.get('family')}' already ran in the last 4 "
                   f"({clash[-1]['id']}) and this deck declares no twist")

    # the break slot: at least one in every four
    window = last4 + [spec]
    if len(window) >= 4 and not any(d.get("break") for d in window[-4:]):
        bad.append("no break deck in the last 4 - the series has become predictable, "
                   "one of them must be a simple graphic piece")
    return bad


def register(spec: dict, run: list | None = None) -> list:
    """Check, then record. Raises rather than letting a predictable deck through."""
    run = load() if run is None else run
    bad = check(spec, run)
    if bad:
        raise ValueError(f"{spec['id']} would make the feed predictable:\n  - "
                         + "\n  - ".join(bad))
    run.append({"id": spec["id"], "design": spec["design"], "theme": spec["theme"],
                "family": spec.get("family", "unset"), "keyword": spec["keyword"],
                "break": bool(spec.get("break")), "twist": spec.get("twist", "")})
    save(run)
    return run


if __name__ == "__main__":
    run = load()
    print(f"{len(run)} decks on record")
    for d in run:
        mark = "  [BREAK]" if d["break"] else ""
        print(f"  {d['id']:18} {d['design']:8} {d['theme']:6} {d['family']:12} "
              f"{d['keyword']}{mark}")
