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
OPENING = 0.0          # 0 means the whole film: an empty frame at the turn costs as much
                       # as one at second three, and measuring only the opening missed a two
                       # second void in episode 04's fifth beat that the operator caught by
                       # eye. Retention is decided in the opening; the film is watched all
                       # the way down.


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

    seam = None
    if built and meta.get("hook"):
        cache = html.with_name(html.stem + "-vo.align.json")
        if cache.exists():
            w2 = m.words_from(json.loads(cache.read_text())["alignment"])
            hk = [x for x in w2 if x[1] < hook_end]
            if hk:
                seam = hk[-1][2] + float(meta.get("hook_hold", .15))

    if to <= 0:
        # A NARRATED film is as long as its take plus a 0.7s tail, so sampling 0.4s past the
        # last spoken word still lands inside the render and is worth checking - that tail is
        # where a payoff flashes and vanishes. A SILENT film declares its own duration and the
        # renderer emits exactly that many frames, so the same 0.4s reaches past the end of
        # the mp4 and measures a page nobody will ever see. It reported a dead half second
        # "from t=6.00" on a 6.00s film, which is a guard failing work for frames that do not
        # exist, and that is how a guard gets ignored on the day it is right.
        to = built[2] + .4 if built else meta.get("duration", 30)

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
    return {"film": html.name, "rows": rows, "seam": seam}


def report(res: dict) -> bool:
    rows = res["rows"]
    print(f"\n=== {res['film']} ===")
    print(f"{'t':>6} {'ink':>7} {'motion':>8}  {'':20}")
    # Every film opens from an empty frame and the first hook word takes about 0.7s to
    # resolve out of its blur. Scoring that as a trough measures the entrance, not a defect,
    # and because the score is trough/peak it punishes a film for having a DENSER peak: the
    # same opening frame reads as 12% of a thin hook and 0.9% of a strong one. Judge from the
    # moment the first word has landed.
    ENTRANCE = 0.8
    worst_ink = min([r for r in rows if r["t"] >= ENTRANCE] or rows[1:],
                    key=lambda r: r["ink"])
    # a still stretch matters more than a single still frame, so score a 0.5s window
    win = max(1, int(round(0.5 / (rows[1]['t'] - rows[0]['t']))))
    runs = [(sum(r["motion"] for r in rows[i:i + win]) / win, rows[i]["t"])
            for i in range(1, len(rows) - win + 1)]
    worst_mot = min(runs) if runs else (0, 0)

    # the hook's own coverage, measured before the incoming sheet can add to it
    seam = res.get("seam")
    hookrows = [r for r in rows if seam is None or r["t"] <= seam - 0.5] or rows
    peak = max(r["ink"] for r in hookrows)
    peak_t = next(r["t"] for r in hookrows if r["ink"] == peak)
    end = rows[-1]["t"] - 1.5                     # the closing hold is not a swipe risk
    roll, rollink = {}, {}
    for i in range(len(rows)):
        seg = rows[i:i + win]
        roll[rows[i]["t"]] = sum(r["motion"] for r in seg) / len(seg)
        rollink[rows[i]["t"]] = sum(r["ink"] for r in seg) / len(seg)

    for r in rows:
        flag = ""
        if r["t"] >= peak_t and r["ink"] < INK_FLOOR:
            flag += " EMPTY"
        if peak_t <= r["t"] <= end and roll[r["t"]] < MOTION_FLOOR:
            flag += " STILL"
        if r["t"] > peak_t and rollink[r["t"]] < peak * INK_CLIFF:
            flag += " CLIFF"
        bar = "#" * int(r["ink"] * 400)
        print(f"{r['t']:6.2f} {r['ink']:7.4f} {r['motion']:8.5f}  {bar[:24]:24}{flag}")

    print(f"  peak ink      {peak:.4f} at t={peak_t:.2f}s (the hook)")
    print(f"  trough ink    {worst_ink['ink']:.4f} at t={worst_ink['t']:.2f}s "
          f"({worst_ink['ink'] / peak:.0%} of peak, floor {INK_FLOOR})")
    print(f"  stillest 0.5s {worst_mot[0]:.5f} from t={worst_mot[1]:.2f}s "
          f"(floor {MOTION_FLOOR})")
    bad = [r for r in rows if r["t"] >= peak_t and (r["ink"] < INK_FLOOR
                                              or (peak_t <= r["t"] <= end and roll[r["t"]] < MOTION_FLOOR)
                                              or (r["t"] > peak_t and rollink[r["t"]] < peak * INK_CLIFF))]
    share = len(bad) / max(1, len(rows) - 1)
    print(f"  flagged       {len(bad)} of {len(rows) - 1} samples ({share:.1%})")
    if bad:
        print("       " + ", ".join(f"{r['t']:.2f}s" for r in bad[:14]))

    # The verdict is RELATIVE, because the absolute thresholds above were invented and the
    # film the operator declared the standard does not meet them: episode 04 flags 7.7% of
    # its own samples. A guard that fails the reference is measuring the wrong thing, and one
    # that fails everything gets ignored. So the reference IS the bar: a film ships if it is
    # no worse than the approved episode on flagged share, trough and stillness.
    base = baseline()
    if not base:
        print("  NOTE  no baseline recorded; run --baseline <approved film> to set the bar")
        return True
    slack = 1.30                      # 30% worse than the reference is still a pass
    checks = [("flagged share", share, base["share"] * slack + 0.02, False),
              ("trough vs peak", worst_ink["ink"] / peak, base["trough"] / slack, True),
              ("stillest 0.5s", worst_mot[0], base["still"] / slack, True)]
    ok = True
    for name, got, bar, higher_better in checks:
        good = got >= bar if higher_better else got <= bar
        ok &= good
        print(f"  {'ok ' if good else 'BAD'} {name:16} {got:.5f} vs {base['name']} bar {bar:.5f}")
    print("  " + ("PASS at or above the approved episode" if ok
                  else "FAIL below the approved episode - fix before shipping"))
    return ok


BASELINE = pathlib.Path(__file__).resolve().parent / "_retention-baseline.json"


def baseline():
    return json.loads(BASELINE.read_text()) if BASELINE.exists() else None


def record_baseline(html: pathlib.Path, res: dict) -> None:
    """Freeze an approved film's numbers as the bar every later film is judged against."""
    rows = res["rows"]
    win = max(1, int(round(0.5 / (rows[1]["t"] - rows[0]["t"]))))
    seam = res.get("seam")
    hookrows = [r for r in rows if seam is None or r["t"] <= seam - 0.5] or rows
    peak = max(r["ink"] for r in hookrows)
    peak_t = next(r["t"] for r in hookrows if r["ink"] == peak)
    end = rows[-1]["t"] - 1.5
    roll = {r["t"]: sum(x["motion"] for x in rows[i:i + win]) / len(rows[i:i + win])
            for i, r in enumerate(rows)}
    rollink = {r["t"]: sum(x["ink"] for x in rows[i:i + win]) / len(rows[i:i + win])
               for i, r in enumerate(rows)}
    bad = [r for r in rows if r["t"] >= peak_t and (r["ink"] < INK_FLOOR
           or (peak_t <= r["t"] <= end and roll[r["t"]] < MOTION_FLOOR)
           or (r["t"] > peak_t and rollink[r["t"]] < peak * INK_CLIFF))]
    runs = [sum(r["motion"] for r in rows[i:i + win]) / win
            for i in range(1, len(rows) - win + 1)]
    BASELINE.write_text(json.dumps({
        "name": html.stem,
        "share": len(bad) / max(1, len(rows) - 1),
        "trough": min(r["ink"] for r in rows if r["t"] >= 0.8) / peak,
        "still": min(runs) if runs else 0.0,
    }, indent=2))
    print(f"  baseline written from {html.stem}: {BASELINE.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("films", nargs="+")
    ap.add_argument("--to", type=float, default=OPENING)  # 0 -> measured take length
    ap.add_argument("--step", type=float, default=0.1)
    ap.add_argument("--baseline", action="store_true",
                    help="record this film as the bar every later film is judged against")
    a = ap.parse_args()
    ok = True
    for f in a.films:
        html = pathlib.Path(f)
        res = measure(html, a.to, a.step)
        if a.baseline:
            record_baseline(html, res)
            continue
        ok &= report(res)
    print("\nRETENTION: " + ("ALL PASS" if ok else "FAIL - fix before shipping"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
