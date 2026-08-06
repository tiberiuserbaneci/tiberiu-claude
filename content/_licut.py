#!/usr/bin/env python3
"""Recut a 9:16 film to LinkedIn's 4:5 feed format, and prove nothing was clipped.

The 9:16 master reserves 300px at the top and 330px at the bottom for TikTok and Instagram
overlays (CLAUDE.md 9). LinkedIn paints nothing there, so on LinkedIn that 632px is reserve
protecting nothing while the feed scales the whole frame to the column width - the content
renders about 1.4x smaller than it needs to. 9:16 is a legal LinkedIn aspect (its range is
1:2.4 to 2.4:1), so this is a framing decision, not a compatibility one.

The crop window is placed from the MEASURED content band rather than the nominal safe box,
because the kinetic captions roam and a film whose words drift wider than the safe band would
lose them silently. The same measurement runs again on the output: if content touches an edge
after cropping, the cut is rejected instead of shipped.

Video is copied through a crop filter only - never re-laid-out - so the type stays exactly as
it was rendered, and audio is stream-copied.

Usage:
  python3 content/_licut.py content/ig/film-08-sender/reel.mp4 content/li/film-08-sender/
  python3 content/_licut.py <reel.mp4> <outdir> --thumb 27      # thumbnail at t=27s
"""
import argparse, functools, pathlib, shutil, subprocess, sys, tempfile

import numpy as np
from PIL import Image

print = functools.partial(print, flush=True)  # noqa: A001

OUT_W, OUT_H = 1080, 1350          # LinkedIn feed portrait
SRC_W, SRC_H = 1080, 1920
EDGE = 18                          # per-row edge energy that counts as content


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def content_band(mp4, height, fps=3):
    """First and last row carrying content, in the file's own pixel space."""
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", str(mp4),
                        "-vf", f"fps={fps},scale=270:{round(270 * height / OUT_W)}",
                        f"{td}/f%05d.png"], check=True)
        frames = sorted(pathlib.Path(td).glob("*.png"))
        if not frames:
            sys.exit(f"no frames decoded from {mp4}")
        h = np.asarray(Image.open(frames[0])).shape[0]
        rows = np.zeros(h, bool)
        for p in frames:
            a = np.asarray(Image.open(p).convert("L"), float)
            rows |= np.abs(np.diff(a, axis=1)).max(axis=1) > EDGE
    ys = np.where(rows)[0]
    if not len(ys):
        sys.exit(f"{mp4} measured as empty - check the EDGE threshold")
    return ys.min() / h * height, (ys.max() + 1) / h * height


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("reel")
    ap.add_argument("outdir")
    ap.add_argument("--thumb", type=float, default=None,
                    help="seconds; cut a 1080x1350 thumbnail from the recut film")
    a = ap.parse_args()

    reel = pathlib.Path(a.reel)
    out = pathlib.Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "linkedin-1080x1350.mp4"

    top, bot = content_band(reel, SRC_H)
    span = bot - top
    print(f"  source content  y {top:.0f} .. {bot:.0f}   span {span:.0f} of {SRC_H}")
    if span > OUT_H:
        sys.exit(f"content spans {span:.0f}px, taller than the {OUT_H}px window - "
                 f"this film cannot be cropped to 4:5 without losing {span - OUT_H:.0f}px")

    y = round(min(max((top + bot) / 2 - OUT_H / 2, 0), SRC_H - OUT_H))
    print(f"  crop            {OUT_W}x{OUT_H} at y={y}   margins "
          f"{top - y:.0f} top / {y + OUT_H - bot:.0f} bottom")

    subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", str(reel),
                    "-vf", f"crop={OUT_W}:{OUT_H}:0:{y}",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "copy",
                    "-movflags", "+faststart", str(dest), "-y"], check=True)

    ntop, nbot = content_band(dest, OUT_H)
    if ntop < 4 or nbot > OUT_H - 4:
        dest.unlink()
        sys.exit(f"CLIPPED: content reaches y {ntop:.0f}..{nbot:.0f} of {OUT_H} - cut rejected")
    print(f"  verified        y {ntop:.0f} .. {nbot:.0f}, nothing touches an edge")
    print(f"  {dest}  {dest.stat().st_size / 1e6:.1f} MB")

    if a.thumb is not None:
        png = out / "thumb-1080x1350.png"
        subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-ss", str(a.thumb),
                        "-i", str(dest), "-frames:v", "1", str(png), "-y"], check=True)
        scrub = pathlib.Path(__file__).with_name("_scrub.py")
        subprocess.run([sys.executable, str(scrub), str(png)], check=True)
        print(f"  thumbnail       {png} at t={a.thumb}s")


if __name__ == "__main__":
    main()
