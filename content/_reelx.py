#!/usr/bin/env python3
"""The reel cut of a deck: hook, pictogram, one line. Nothing else on the slide.

WHY A SEPARATE CUT AND NOT A SETTING. The carousel and the reel are not one material at two
sizes, they are two materials, because the reader sets the pace on one and the platform sets
it on the other. Measured on the shipped decks: a reel content slide carried a mean of 75
words, at one second per slide. A person takes in five to eight words in that second. The
density that earns a save on a carousel is what loses the viewer on a reel, so the carousel
keeps every word it has and the reel is rewritten to about twenty.

WHAT CARRIES THE MISSING FIFTY WORDS. The pictogram, and only if it is a thing rather than a
chart. `_picto` draws a calendar with nine of twelve months filled, a funnel whose last stage
is actually the narrow one, a page with one clause lit. The number is inside the drawing, so
the sentence does not have to spend itself saying it, and the slide survives being seen
rather than read.

The reel spec is a `reel` key on the deck's existing spec: seven rows, each a hook, a
pictogram and one line. Everything else - theme, keyword, cover, the ask - is the deck's own
and is not restated here, so the two cuts can never drift apart on the things that identify
them.

Usage:
  python3 content/_reelx.py deck-a-year          # build the page
  python3 content/_reelx.py deck-a-year --render # build, render nine PNGs, scrub them
"""
import importlib.util, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


# ------------------------------------------------------------------ deck A, the reel cut
#
# Seven mistakes, seven pictograms, no form twice. The carousel argues each one two ways,
# struck through against the fix; the reel only names the mistake, because the fix is what
# the ask is for and a reel that gives away its own payoff has nothing to comment for.
#
# Every number here is already in the deck's carousel copy. Nothing was invented to make a
# drawing work, which is the failure mode a pictogram set invites: the shape wants twelve
# cells, so you find yourself rounding nine months into a year.
DECK_A_REEL = [
    {"h": "Nine months<br>before one<br><em>sale</em>",
     "obj": {"form": "calendar", "cols": 4, "rows": 3, "lit": 9,
             "k": "months building", "v": "9"},
     "line": "Every feature felt like progress. None of it was <em>evidence</em>."},

    {"h": "Every job<br>came back<br>to <em>me</em>",
     "obj": {"form": "flow", "n": 5, "hub": True, "hub_n": "1",
             "k": "jobs, one person", "v": "5"},
     "line": "Research, outreach, invoices, the deck. All of it, <em>badly</em>."},

    {"h": "Four months<br>of <em>polish</em>",
     "obj": {"form": "files", "n": 5, "k": "months nobody noticed", "v": "4"},
     "line": "Ready is a feeling, and the feeling never <em>arrives</em>."},

    {"h": "Forty one deals.<br><em>Nine</em> were real.",
     "obj": {"form": "pipeline", "stages": ["41", "22", "14", "9"], "lit": 3,
             "k": "open, and real", "v": "41 / 9"},
     "line": "A reply felt like a deal. Thirty two of them were <em>not</em>."},

    {"h": "Ten minutes,<br><em>every</em> session",
     "obj": {"form": "clockface", "pct": 17, "k": "minutes, every time", "v": "10"},
     "line": "Re-explaining my own company. Every morning, from <em>zero</em>."},

    {"h": "Sixty hours.<br>One thing<br><em>scaled</em>.",
     "obj": {"form": "chart", "vals": [22, 30, 38, 47, 54, 60],
             "k": "hours a week", "v": "60"},
     "line": "The hours were the only thing that ever went <em>up</em>."},

    {"h": "One bad line,<br>a <em>hundred</em><br>times",
     "obj": {"form": "doc", "lit": 3, "k": "line, your name on it", "v": "1"},
     "line": "Volume is easy. Getting your name back is <em>not</em>."},
]

REELS = {"deck-a-year": DECK_A_REEL}


def spec_for(deck_id: str) -> dict:
    """The deck's own spec, plus its reel rows. Importing a batch file is safe: every batch
    guards its registration and rendering behind __main__, so nothing is written or logged."""
    for batch in sorted(REPO.glob("content/_decks_batch*.py")):
        mod = load(batch.stem)
        for name in dir(mod):
            v = getattr(mod, name)
            if isinstance(v, dict) and v.get("id") == deck_id:
                return dict(v, reel=REELS[deck_id])
    sys.exit(f"{deck_id}: no spec found in any content/_decks_batch*.py")


def build(deck_id: str) -> pathlib.Path:
    fonts = load("_fonts").embedded_css()
    css = load("_deck_css").CSS
    out = REPO / f"content/build/{deck_id}-reelx.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(load("_glassdeck").build(spec_for(deck_id), css, fonts, "reelx"))
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    for deck_id in args:
        page = build(deck_id)
        print(f"built  {page.relative_to(REPO)}")
        if "--render" in sys.argv:
            bad = load("_deckrender").render(deck_id, variants=("reelx",))
            for x in bad:
                print(f"  FAIL {x}")
            outdir = REPO / f"content/decks/{deck_id}/reelx-1080x1920"
            subprocess.run([sys.executable, str(REPO / "content/_scrub.py"),
                            *[str(p) for p in sorted(outdir.glob("*.png"))]], check=True)
            print(f"{'FAIL' if bad else 'ok   '}  {outdir.relative_to(REPO)}")
            if bad:
                sys.exit(1)
