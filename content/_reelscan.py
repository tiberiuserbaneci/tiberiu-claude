#!/usr/bin/env python3
"""Measure a posted reel the way `_retention.py` measures our own films, but from the mp4.

`_retention.py` drives a page and seeks its animations; a reel that already exists as video
needs the same two numbers read straight off the frames, so a reference clip and one of our
renders can be compared on one axis:

  ink     fraction of pixels carrying an edge - how much is on screen at all
  motion  busiest TILE between consecutive samples, never the frame mean, because a small
          element entering is what the eye follows and a mean averages it away

Prints a per-sample curve plus the segment summary, so "the slideshow kills it" stops being a
description and becomes a place on the timeline.

Usage:
  python3 content/_reelscan.py <file.mp4> [--step 0.2] [--cut 3.6]
"""
import argparse, functools, pathlib, subprocess, sys, tempfile

import numpy as np
from PIL import Image

print = functools.partial(print, flush=True)  # noqa: A001

W, H = 216, 384          # sample size; tiles below divide it evenly
TX, TY = 6, 8            # tile grid for the motion metric
EDGE = 14                # gradient that counts as an edge, same as _retention


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def frames(mp4, step):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", str(mp4),
                        "-vf", f"fps={1/step},scale={W}:{H}", f"{td}/f%05d.png"], check=True)
        for p in sorted(pathlib.Path(td).glob("*.png")):
            yield np.asarray(Image.open(p).convert("L"), dtype=float)


def scan(mp4, step):
    out, prev = [], None
    for i, a in enumerate(frames(mp4, step)):
        gx = np.abs(np.diff(a, axis=1))[:, :W - 1]
        gy = np.abs(np.diff(a, axis=0))[:H - 1, :]
        ink = ((gx[:H - 1] > EDGE) | (gy[:, :W - 1] > EDGE)).mean()
        if prev is None:
            motion = 0.0
        else:
            d = np.abs(a - prev)
            th, tw = H // TY, W // TX
            motion = max(d[y*th:(y+1)*th, x*tw:(x+1)*tw].mean()
                         for y in range(TY) for x in range(TX)) / 255
        out.append((i * step, ink, motion))
        prev = a
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mp4")
    ap.add_argument("--step", type=float, default=0.2)
    ap.add_argument("--cut", type=float, default=None,
                    help="seconds where the live plate ends, to summarise each half")
    a = ap.parse_args()

    rows = scan(pathlib.Path(a.mp4), a.step)
    peak = max(r[1] for r in rows)
    print(f"  t      ink    motion   (ink bar, peak {peak:.4f})")
    for t, ink, mo in rows:
        bar = "#" * round(ink / peak * 26)
        mark = "  <- still" if mo < 0.004 else ""
        print(f"  {t:5.2f}  {ink:.4f}  {mo:.4f}  {bar:<26}{mark}")

    def seg(lo, hi, label):
        s = [r for r in rows if lo <= r[0] < hi]
        if not s:
            return
        stills = sum(1 for r in s if r[2] < 0.004)
        print(f"  {label:22} ink mean {np.mean([r[1] for r in s]):.4f}   "
              f"motion mean {np.mean([r[2] for r in s]):.4f}   "
              f"still samples {stills}/{len(s)} ({stills/len(s)*100:.0f}%)")

    print()
    if a.cut:
        seg(0, a.cut, "live plate")
        seg(a.cut, 1e9, "after the plate")
    seg(0, 1e9, "whole clip")


if __name__ == "__main__":
    main()
