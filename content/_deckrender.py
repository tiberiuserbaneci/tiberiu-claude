#!/usr/bin/env python3
"""Render a deck's nine slides in both native variants, and check what came out.

The two variants are not the same picture at two sizes, they carry different chrome, so the
failure this guards against is a variant quietly rendering the OTHER one's furniture: a mast
inside a reel he is going to cut over his own footage, or a Claude mark centred in the middle
of a carousel. That is invisible in a thumbnail and obvious in the feed.

  reel      1080x1920   no mast, no footer, no swipe chip. Claude mark on slide 1 only.
  reelx     1080x1920   the same chrome rules, carrying pictograms instead of dense copy.
  carousel  1080x1350   mast and footer on every slide, swipe chip on slide 1, no mark.

Also checked, per slide: nothing painted outside the safe box, and for `meter` the chart
actually fills its block, because a chart that does not is the airy block the operator rejects
on sight.

Usage:  python3 content/_deckrender.py deck-j-first10 deck-k-launchweek
"""
import importlib.util, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SIZE = {"reel": (1080, 1920), "reelx": (1080, 1920), "carousel": (1080, 1350)}


def _load(n):
    s = importlib.util.spec_from_file_location(n, REPO / "content" / f"{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


BR = _load("_browser")

# selector -> expected count per slide, by variant. None means "not checked".
CHROME = {
    "reel":     {".mast": 0, ".foot": 0, ".aichip": 0},
    "reelx":    {".mast": 0, ".foot": 0, ".aichip": 0},
    "carousel": {".mast": 1, ".foot": 1, ".markrow": 0},
}


def render(deck_id: str, variants=("reel", "carousel")) -> list[str]:
    bad = []
    with __import__("playwright.sync_api", fromlist=["sync_playwright"]).sync_playwright() as p:
        b = BR.launch(p)
        for variant in variants:
            w, h = SIZE[variant]
            src = REPO / f"content/build/{deck_id}-{variant}.html"
            outdir = REPO / f"content/decks/{deck_id}/{variant}-{w}x{h}"
            outdir.mkdir(parents=True, exist_ok=True)
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(f"file://{src}")
            pg.wait_for_timeout(1500)
            slides = pg.locator(".slide")
            n = slides.count()
            if n != 9:
                bad.append(f"{deck_id} {variant}: {n} slides, expected 9")
            for i in range(n):
                s = slides.nth(i)
                box = s.bounding_box()
                if round(box["width"]) != w or round(box["height"]) != h:
                    bad.append(f"{deck_id} {variant} {i+1:02d}: "
                               f"{round(box['width'])}x{round(box['height'])}, want {w}x{h}")
                for sel, want in CHROME[variant].items():
                    got = s.locator(sel).count()
                    if got != want:
                        bad.append(f"{deck_id} {variant} {i+1:02d}: {sel} x{got}, want {want}")
                # the mark belongs on slide 1 of a reel and nowhere else
                if variant.startswith("reel"):
                    want = 1 if i == 0 else 0
                    got = s.locator(".markrow").count()
                    if got != want:
                        bad.append(f"{deck_id} reel {i+1:02d}: .markrow x{got}, want {want}")
                if variant == "carousel" and i == 0 and s.locator(".aichip").count() != 1:
                    bad.append(f"{deck_id} carousel 01: missing the swipe chip")
                over = s.evaluate("""el => {
                  const safe = el.querySelector('.safe').getBoundingClientRect();
                  let worst = 0;
                  for (const n of el.querySelectorAll('.safe *')) {
                    const r = n.getBoundingClientRect();
                    if (!r.width || !r.height) continue;
                    worst = Math.max(worst, safe.top - r.top, r.bottom - safe.bottom,
                                            safe.left - r.left, r.right - safe.right);
                  }
                  return Math.round(worst);
                }""")
                if over > 2:
                    bad.append(f"{deck_id} {variant} {i+1:02d}: content spills the safe box "
                               f"by {over}px")
                # Fill is measured INSIDE the list, not on the panel. Measuring the panel's
                # own children always reports ~100 percent, because those children are flex
                # items that stretch by definition - which is how a receipt whose rows were
                # a quarter full passed this check. What matters is how much of each ROW its
                # own content occupies.
                fill = s.evaluate("""el => {
                  const list = el.querySelector('.rc-body, .mt-body, .lg, .tr, .sc, .cn-lines');
                  if (!list) return null;
                  // A row that paints its OWN surface is not measured. On the ledger and the
                  // grid the row is a glass card, so the card is the ink and the block is
                  // tiled by construction; on the receipt the row was bare text over the
                  // panel, so its ink really was just the glyphs. Judging both by glyph
                  // height flags a tiled block as airy, which is the guard crying wolf.
                  const painted = n => {
                    const cs = getComputedStyle(n);
                    return cs.boxShadow !== 'none' ||
                      !(cs.backgroundColor === 'transparent' ||
                        cs.backgroundColor === 'rgba(0, 0, 0, 0)');
                  };
                  let worst = 100;
                  for (const row of list.children) {
                    const rb = row.getBoundingClientRect();
                    if (rb.height < 8 || painted(row)) continue;
                    let top = Infinity, bot = -Infinity;
                    const walk = n => {
                      for (const c of n.children) {
                        const r = c.getBoundingClientRect();
                        if (r.height > 0 && r.width > 0) {
                          top = Math.min(top, r.top); bot = Math.max(bot, r.bottom);
                        }
                        walk(c);
                      }
                    };
                    walk(row);
                    if (!isFinite(top)) continue;
                    worst = Math.min(worst, Math.round(100 * (bot - top) / rb.height));
                  }
                  return worst;
                }""")
                # 28 percent, not 45. A row holding a single line of text can never fill
                # much more than 40 percent of the height a distributed list hands it, so a
                # high threshold cries wolf on correct work and gets ignored on the day it is
                # right. What this catches is the real regression: small type spread down a
                # tall block, which is what the receipt was at 24 percent before the rows
                # were given type worth their height.
                if fill is not None and fill < 28:
                    bad.append(f"{deck_id} {variant} {i+1:02d}: thinnest row only "
                               f"{fill}% full, the block reads airy")
                s.screenshot(path=str(outdir / f"{i+1:02d}.png"))
            pg.close()
        b.close()
    return bad


if __name__ == "__main__":
    ids = sys.argv[1:]
    if not ids:
        print(__doc__); sys.exit(2)
    allbad = []
    for d in ids:
        bad = render(d)
        allbad += bad
        print(f"{'FAIL' if bad else 'ok  '} {d}")
        for x in bad:
            print(f"       - {x}")
    print(f"\n{len(allbad)} problems" if allbad else "\nall clean")
    sys.exit(1 if allbad else 0)
