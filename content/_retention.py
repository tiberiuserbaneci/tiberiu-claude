#!/usr/bin/env python3
"""Measure the first seconds of a film the way the feed does: frame by frame.

Episode 01 held better than half its traffic through second three and fell to 10-12% from
second four, at an 80%+ skip rate. That is not a taste problem, it is a measurable one, and
guessing at which of "the graphic was weak" or "the sentence was wrong" caused it wastes a
render each time. So this reads the actual frames and reports two numbers per sample:

  ink     what fraction of the frame carries content at all (edge energy). A frame that has
          lost its hook and not yet built its scene reads near zero here while still looking
          "fine" in a still, because the eye forgives an empty frame it is only passing
          through and a scrolling thumb does not.

  motion  how much changed since the last sample, measured as the busiest TILE rather than
          the mean of the frame. A question mark popping in is 0.05% of the pixels and
          averages away to nothing, but the eye goes straight to it. Scoring the frame
          globally called all three films dead in a window where two of them were fine, so
          the metric is local: split the frame into tiles, report the busiest one. A held
          frame still scores zero, and vertical video has no scrubber, so a viewer's only
          evidence that the clip is going somewhere is that the picture keeps moving.

The output is a trough report: the weakest window in the opening, which is the frame the
audience actually left on. Run it before shipping any film.

Usage:
  python3 content/_retention.py content/cortex-film-01.html
  python3 content/_retention.py content/*-film-*.html --to 8 --step 0.1
"""
import argparse, importlib.util, json, pathlib, sys

import numpy as np

print = __import__("functools").partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Floors, set from what the three built films actually measure rather than from taste.
# A film may sit under them for a beat; it may not sit under them across the opening, which
# is the only stretch where the audience is still deciding.
INK_FLOOR = 0.012      # fraction of pixels carrying an edge
MOTION_FLOOR = 0.010   # busiest-tile change between samples, see tile_motion
INK_CLIFF = 0.45       # a scene may not drop below this share of the hook's peak coverage
OPENING = 8.0          # seconds that decide retention


def _film():
    spec = importlib.util.spec_from_file_location("_film", ROOT / "content" / "_film.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def edges(gray: np.ndarray) -> float:
    """Fraction of the frame carrying an edge.

    Gradient magnitude rather than brightness: these films run cream type on cream and ivory
    on graphite, so any absolute threshold measures the background colour and calls a blank
    canvas full. An edge is content by definition, whatever the palette.
    """
    gy = np.abs(np.diff(gray, axis=0))[:, :-1]
    gx = np.abs(np.diff(gray, axis=1))[:-1, :]
    return float(((gx + gy) > 14).mean())


def tile_motion(a: np.ndarray, b: np.ndarray, grid=(10, 6)) -> float:
    """Change in the busiest tile, not across the whole frame.

    The mean over 1080x1920 is dominated by however much of the frame is holding still, so a
    small element arriving reads as no motion at all. Splitting into tiles and taking the
    maximum matches what the eye does, which is to track the one thing that moved.
    """
    h, w = a.shape
    th, tw = h // grid[0], w // grid[1]
    d = np.abs(a - b) / 255.0
    best = 0.0
    for i in range(grid[0]):
        for j in range(grid[1]):
            best = max(best, float(d[i * th:(i + 1) * th, j * tw:(j + 1) * tw].mean()))
    return best


def sample(pg, loc, t: float, size=(216, 384)) -> np.ndarray:
    pg.evaluate("ms=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=ms})", t * 1000)
    from io import BytesIO
    from PIL import Image
    raw = loc.screenshot(type="jpeg", quality=70)
    im = Image.open(BytesIO(raw)).convert("L").resize(size, Image.BILINEAR)
    return np.asarray(im, dtype=np.float32)


def measure(html: pathlib.Path, to: float, step: float) -> dict:
    m = _film()
    from playwright.sync_api import sync_playwright

    meta = m.read_meta(html)
    built = m.build_vo(meta, html.with_name(html.stem + "-vo.mp3"))
    marks = built[1] if built else [b["t"] for b in meta["beats"]]
    caps = None
    if built and meta.get("hook"):
        cache = html.with_name(html.stem + "-vo.align.json")
        if cache.exists():
            words = m.words_from(json.loads(cache.read_text())["alignment"])
            hook_end = next((w[2] for w in words if w[0].endswith(".")), 2.5) + 0.05
            caps = m.build_captions(meta, words, hook_end,
                                    cta_at=marks[5] if len(marks) > 5 else None, marks=marks)

    rows, prev = [], None
    with sync_playwright() as pw:
        b, pg, loc = m._open_stage(pw, html, meta, marks, caps)
        t = 0.0
        while t <= to + 1e-9:
            g = sample(pg, loc, t)
            ink = edges(g)
            mot = 0.0 if prev is None else tile_motion(g, prev)
            rows.append({"t": round(t, 2), "ink": ink, "motion": mot})
            prev, t = g, t + step
        b.close()
    return {"film": html.name, "rows": rows}


def report(res: dict) -> bool:
    rows = res["rows"]
    print(f"\n=== {res['film']} ===")
    print(f"{'t':>6} {'ink':>7} {'motion':>8}  {'':20}")
    worst_ink = min(rows[1:], key=lambda r: r["ink"])
    # a still stretch matters more than a single still frame, so score a 0.5s window
    win = max(1, int(round(0.5 / (rows[1]['t'] - rows[0]['t']))))
    runs = [(sum(r["motion"] for r in rows[i:i + win]) / win, rows[i]["t"])
            for i in range(1, len(rows) - win + 1)]
    worst_mot = min(runs) if runs else (0, 0)

    peak = max(r["ink"] for r in rows)
    peak_t = next(r["t"] for r in rows if r["ink"] == peak)

    for r in rows:
        flag = ""
        if r["t"] > 0 and r["ink"] < INK_FLOOR:
            flag += " EMPTY"
        if r["t"] > 0 and r["motion"] < MOTION_FLOOR:
            flag += " STILL"
        if r["t"] > peak_t and r["ink"] < peak * INK_CLIFF:
            flag += " CLIFF"
        bar = "#" * int(r["ink"] * 400)
        print(f"{r['t']:6.2f} {r['ink']:7.4f} {r['motion']:8.5f}  {bar[:24]:24}{flag}")

    print(f"  peak ink      {peak:.4f} at t={peak_t:.2f}s (the hook)")
    print(f"  trough ink    {worst_ink['ink']:.4f} at t={worst_ink['t']:.2f}s "
          f"({worst_ink['ink'] / peak:.0%} of peak, floor {INK_FLOOR})")
    print(f"  stillest 0.5s {worst_mot[0]:.5f} from t={worst_mot[1]:.2f}s "
          f"(floor {MOTION_FLOOR})")
    bad = [r for r in rows if r["t"] > 0 and (r["ink"] < INK_FLOOR or r["motion"] < MOTION_FLOOR
                                              or (r["t"] > peak_t and r["ink"] < peak * INK_CLIFF))]
    if bad:
        print(f"  FAIL {len(bad)} of {len(rows) - 1} samples in the opening are empty, still, "
              f"or below {INK_CLIFF:.0%} of the hook's coverage")
        print("       " + ", ".join(f"{r['t']:.2f}s" for r in bad[:14]))
        return False
    print("  PASS opening stays full, keeps moving, and never falls off the hook's cliff")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("films", nargs="+")
    ap.add_argument("--to", type=float, default=OPENING)
    ap.add_argument("--step", type=float, default=0.1)
    a = ap.parse_args()
    ok = True
    for f in a.films:
        ok &= report(measure(pathlib.Path(f), a.to, a.step))
    print("\nRETENTION: " + ("ALL PASS" if ok else "FAIL - fix before shipping"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
