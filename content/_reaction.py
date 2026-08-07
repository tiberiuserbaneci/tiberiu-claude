#!/usr/bin/env python3
"""Join an operator reaction plate to a generated segment, without the seam the reference bleeds.

Measured on the operator's viral (`content/_reelscan.py`, see analysis/reaction-format.md):
the slideshow after the plate is dead 57% of its samples, and three of its cuts pass through a
fully black frame. Two of those faults are the seam's, not the slides', so this owns the seam:

  - **The plate is trimmed to its live part.** The supplied plate is 2.87s but fades to black
    over its last 0.8s - ink measures exactly 0.0000 for three straight samples. Cutting on
    duration would carry that black into the middle of the piece, which is the single worst
    frame to put in a feed. `--trim` is measured by default, not guessed.
  - **The join is a crossfade, never a cut.** `xfade` holds both sides on screen through the
    transition, so ink never reaches zero and the eye is carried instead of interrupted.

Audio: the plate's own audio is kept over its own span and faded out across the join; the
segment is silent by design, so the result is a reel that opens on room tone and goes quiet,
rather than one that cuts from sound to nothing.

Usage:
  python3 content/_reaction.py <plate.mp4> <segment.mp4> <out.mp4> [--xf 0.4] [--trim auto]
"""
import argparse, functools, pathlib, subprocess, sys, tempfile

import numpy as np
from PIL import Image

print = functools.partial(print, flush=True)  # noqa: A001

W, H = 1080, 1920
EDGE = 14
DEAD = 0.008          # ink below this is a frame with essentially nothing on it


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def duration(p):
    out = subprocess.run([ffmpeg(), "-hide_banner", "-i", str(p)],
                         capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            hh, mm, ss = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(hh) * 3600 + int(mm) * 60 + float(ss)
    sys.exit(f"could not read duration of {p}")


def live_end(plate, step=0.1):
    """Last moment the plate still has a picture, so a baked-in fade never reaches the join."""
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", str(plate),
                        "-vf", f"fps={1/step},scale=216:384", f"{td}/f%05d.png"], check=True)
        inks = []
        for p in sorted(pathlib.Path(td).glob("*.png")):
            a = np.asarray(Image.open(p).convert("L"), dtype=float)
            gx = np.abs(np.diff(a, axis=1))[:383, :]
            gy = np.abs(np.diff(a, axis=0))[:, :215]
            inks.append(((gx > EDGE) | (gy > EDGE)).mean())
    last = 0
    for i, v in enumerate(inks):
        if v >= DEAD:
            last = i
    return (last + 1) * step, inks


HOOK_HTML = """<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent}
FONTS
.wrap{position:absolute;left:70px;right:70px;top:300px;display:flex;flex-direction:column;
  align-items:flex-start;gap:10px}
.l{display:inline-block;background:#0F0F0E;color:#FAFAF7;padding:12px 22px 15px;
  border-radius:10px;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;
  font-size:62px;line-height:1.06;letter-spacing:-1.5px;
  box-shadow:0 18px 44px rgba(0,0,0,.55)}
.l em{font-style:normal;color:#E9784E}
</style><div class="wrap">LINES</div>"""


def hook_png(text, out):
    """Render the hook card with our own type rather than an ffmpeg default face.

    The reference's card is the iOS caption box - system font, pure black, default radius. It
    is the one part of a viral that is not the operator's, and it costs nothing to own.
    """
    import importlib.util

    from playwright.sync_api import sync_playwright

    def load(name):
        spec = importlib.util.spec_from_file_location(name, pathlib.Path(__file__).with_name(f"{name}.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        return m

    # embedded_css() is the one that returns CSS; build() returns a Path, and picking it by
    # name order put a PosixPath into the stylesheet.
    css = load("_fonts").embedded_css()
    exe = load("_film").chromium_path()      # same resolved binary the films render with
    lines = "".join(f'<span class="l">{ln.strip()}</span>'
                    for ln in text.split("|") if ln.strip())
    html = HOOK_HTML.replace("FONTS", css).replace("LINES", lines)
    tmp = pathlib.Path(out).with_suffix(".html")
    tmp.write_text(html)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(f"file://{tmp.resolve()}")
        pg.wait_for_timeout(600)
        pg.screenshot(path=str(out), omit_background=True)
        b.close()
    tmp.unlink()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plate"); ap.add_argument("segment"); ap.add_argument("out")
    ap.add_argument("--xf", type=float, default=0.4, help="crossfade seconds")
    ap.add_argument("--trim", default="auto",
                    help="seconds of plate to keep, or 'auto' to measure where it goes dark")
    ap.add_argument("--hook", default=None,
                    help="hook line over the plate; use | for a line break")
    a = ap.parse_args()

    plate, seg, out = pathlib.Path(a.plate), pathlib.Path(a.segment), pathlib.Path(a.out)
    praw = duration(plate)

    if a.trim == "auto":
        keep, inks = live_end(plate)
        dead = sum(1 for v in inks if v < DEAD)
        print(f"  plate      {praw:.2f}s, live to {keep:.2f}s "
              f"({dead} dark sample(s) trimmed from the tail)")
    else:
        keep = float(a.trim)
        print(f"  plate      {praw:.2f}s, keeping {keep:.2f}s (given)")

    if keep < a.xf + 0.5:
        sys.exit(f"plate has only {keep:.2f}s of picture, too short for a {a.xf}s crossfade")

    sdur = duration(seg)
    offset = keep - a.xf
    total = offset + sdur
    print(f"  segment    {sdur:.2f}s")
    print(f"  crossfade  {a.xf:.2f}s starting at {offset:.2f}s -> {total:.2f}s total")

    # Both sides are normalised to the same size, rate and pixel format before xfade: the filter
    # requires it, and a plate shot at 1440x2560 will otherwise fail rather than scale.
    # Filter order matters: `format` must come AFTER `setsar`. The other way round makes
    # ffmpeg reinitialise the graph at the xfade and die with a bare "Error reinitializing
    # filters", which names nothing useful.
    norm = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H},fps=30,setsar=1,format=yuv420p")
    card = None
    if a.hook:
        card = out.with_name(out.stem + "-hook.png")
        hook_png(a.hook, card)
        print(f"  hook card  {card.name}")

    # The card rides the plate and fades out ACROSS the join rather than being cut with it, so
    # one element carries the eye over the seam instead of the frame being replaced wholesale.
    plate_v = (f"[0:v]trim=0:{keep},setpts=PTS-STARTPTS,{norm}"
               + (f"[pv];[2:v]format=rgba,"
                  f"fade=t=in:st=0.25:d=0.35:alpha=1,"
                  f"fade=t=out:st={max(offset - 0.15, 0.6)}:d=0.4:alpha=1[hc];"
                  f"[pv][hc]overlay=0:0" if card else ""))
    fc = (f"{plate_v}[a];"
          # No setpts on this side: the segment already starts at zero, and resetting its
          # timestamps AFTER the format conversion is what made xfade fail to align.
          f"[1:v]{norm}[b];"
          f"[a][b]xfade=transition=fade:duration={a.xf}:offset={offset}[v];"
          f"[0:a]atrim=0:{keep},asetpts=PTS-STARTPTS,"
          f"afade=t=out:st={max(offset - 0.1, 0)}:d={a.xf + 0.1},"
          f"apad=whole_dur={total}[aud]")
    cmd = [ffmpeg(), "-hide_banner", "-loglevel", "error",
           "-i", str(plate), "-i", str(seg)]
    if card:
        cmd += ["-loop", "1", "-t", str(keep), "-i", str(card)]
    subprocess.run(cmd + [
                    "-filter_complex", fc, "-map", "[v]", "-map", "[aud]",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "19",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    "-movflags", "+faststart", str(out), "-y"], check=True)
    print(f"  {out}  {out.stat().st_size / 1e6:.1f} MB")

    scrub = pathlib.Path(__file__).with_name("_scrub.py")
    if scrub.exists() and out.suffix == ".png":
        subprocess.run([sys.executable, str(scrub), str(out)], check=True)


if __name__ == "__main__":
    main()
