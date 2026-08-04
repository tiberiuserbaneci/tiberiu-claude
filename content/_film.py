#!/usr/bin/env python3
"""Ultron FILM renderer. Turns an animated HTML page into a narrated vertical MP4.

The whole trick is that we do NOT screen-record. Screen recording drops frames and
gives you a different result on every run. Instead we freeze the CSS clock and step
it by hand, one frame at a time:

    document.getAnimations().forEach(a => { a.pause(); a.currentTime = t_ms })

Every animation in the page runs on one master timeline (`animation: x <DUR>s linear
infinite`) with percentage keyframes, so seeking that clock puts the entire scene at
an exact moment. Same input, same bytes out, every time.

Usage:
  python3 content/_film.py content/cortex-film-01.html
  python3 content/_film.py content/cortex-film-01.html --fps 30 --no-audio
  python3 content/_film.py content/cortex-film-01.html --vo-only     # just build the voiceover

Duration and beat marks are read from the HTML itself (see FILM-META below), so the
page stays the single source of truth and the renderer never needs editing per episode.

Voiceover: set ELEVENLABS_API_KEY and ELEVEN_VOICE_ID in the environment. Without them
the film still renders, silent, and the beat timings stay exactly as authored.
"""
import argparse, base64, functools, json, os, pathlib, re, subprocess, sys, urllib.request, urllib.error

# Renders take minutes and usually run detached, where stdout is a pipe and Python buffers
# it into silence. Flush every line so progress is actually visible while it works.
print = functools.partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRUB = CONTENT / "_scrub.py"


def ffmpeg_bin() -> str:
    """Prefer a system ffmpeg, fall back to the imageio-ffmpeg wheel."""
    for cand in ("ffmpeg", "/usr/bin/ffmpeg", "/usr/local/bin/ffmpeg"):
        try:
            subprocess.run([cand, "-version"], capture_output=True, check=True)
            return cand
        except (OSError, subprocess.CalledProcessError):
            pass
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("no ffmpeg: pip install imageio-ffmpeg")


# ---------------------------------------------------------------- film metadata

def read_meta(html: pathlib.Path) -> dict:
    """Pull the FILM-META json block out of the page.

    The page declares its own duration, canvas and narration, e.g.

        /* FILM-META {"duration":26,"w":1080,"h":1920,
                      "beats":[{"t":0.0,"vo":"Research eats the first hour."}, ...]} */
    """
    m = re.search(r"/\*\s*FILM-META\s*(\{.*?\})\s*\*/", html.read_text(), re.S)
    if not m:
        sys.exit(f"{html.name}: no FILM-META block found")
    meta = json.loads(m.group(1))
    meta.setdefault("w", 1080)
    meta.setdefault("h", 1920)
    meta.setdefault("beats", [])
    return meta


# ---------------------------------------------------------------- voiceover

def build_vo(meta: dict, out_mp3: pathlib.Path) -> pathlib.Path | None:
    """Generate the narration with ElevenLabs. Returns None when unconfigured.

    Each beat is spoken as its own request so the audio can be laid down on the exact
    beat mark the page declares. That keeps picture and voice locked together: the
    visual never waits on a sentence that ran long, and a re-timed beat only needs a
    re-render, not a re-record.
    """
    key = os.environ.get("ELEVENLABS_API_KEY")
    voice = os.environ.get("ELEVEN_VOICE_ID")
    beats = [b for b in meta["beats"] if b.get("vo")]
    if not (key and voice):
        print("  vo     SKIP (ELEVENLABS_API_KEY / ELEVEN_VOICE_ID not set) -> silent film")
        return None
    if not beats:
        print("  vo     SKIP (no narrated beats)")
        return None

    model = os.environ.get("ELEVEN_MODEL", "eleven_multilingual_v2")
    tmp = out_mp3.parent / "_vo_parts"
    tmp.mkdir(exist_ok=True)
    parts = []
    for i, b in enumerate(beats):
        part = tmp / f"b{i:02d}.mp3"
        if not part.exists():
            req = urllib.request.Request(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
                data=json.dumps({
                    "text": b["vo"],
                    "model_id": model,
                    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75,
                                       "style": 0.0, "use_speaker_boost": True},
                }).encode(),
                headers={"xi-api-key": key, "Content-Type": "application/json"},
            )
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    part.write_bytes(r.read())
            except urllib.error.HTTPError as e:
                print(f"  vo     FAIL beat {i}: HTTP {e.code} {e.read()[:200]!r} -> silent film")
                return None
        parts.append((b["t"], part))
        print(f"  vo     beat {i} @ {b['t']:>5.1f}s  {b['vo'][:52]}")

    # Lay every clip onto one silent bed at its beat mark.
    ff = ffmpeg_bin()
    cmd = [ff, "-y", "-f", "lavfi", "-t", str(meta["duration"]),
           "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"]
    for _, p in parts:
        cmd += ["-i", str(p)]
    chains, mixes = [], ["[0:a]"]
    for i, (t, _) in enumerate(parts, start=1):
        chains.append(f"[{i}:a]adelay={int(t*1000)}|{int(t*1000)}[d{i}]")
        mixes.append(f"[d{i}]")
    filt = ";".join(chains) + ";" + "".join(mixes) + \
        f"amix=inputs={len(parts)+1}:normalize=0:duration=first[a]"
    cmd += ["-filter_complex", filt, "-map", "[a]", "-c:a", "libmp3lame",
            "-b:a", "192k", str(out_mp3)]
    subprocess.run(cmd, capture_output=True, check=True)
    return out_mp3


# ---------------------------------------------------------------- frame capture

def chromium_path() -> str | None:
    """Locate a preinstalled Chromium. Returns None to let Playwright use its own.

    Sandboxes ship a browser build that rarely matches the pip-installed Playwright's
    pinned revision, and re-downloading is blocked, so point at whatever is on disk.
    """
    if os.environ.get("PW_CHROMIUM"):
        return os.environ["PW_CHROMIUM"]
    import glob
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/chrome-headless-shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None


def _open_stage(p, html: pathlib.Path, meta: dict):
    """Launch a browser on the film and return (browser, page, #film locator)."""
    exe = chromium_path()
    if exe:
        print(f"  chrome {exe}")
    b = p.chromium.launch(executable_path=exe,
                          args=["--force-color-profile=srgb", "--disable-lcd-text",
                                "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": meta["w"], "height": meta["h"]},
                    device_scale_factor=1)
    pg.goto(html.resolve().as_uri())
    pg.wait_for_timeout(1200)              # webfonts
    pg.evaluate("document.fonts.ready")
    return b, pg, pg.locator("#film")


def seek(pg, t_s: float) -> None:
    """Park every animation on the page at the same wall-clock moment."""
    pg.evaluate("t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; })",
                t_s * 1000.0)


def grab_still(html: pathlib.Path, meta: dict, t_s: float, png: pathlib.Path) -> None:
    """One frame, for checking a beat's composition without paying for a full render."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b, pg, stage = _open_stage(p, html, meta)
        seek(pg, t_s)
        stage.screenshot(path=str(png))
        b.close()


def render(html: pathlib.Path, meta: dict, fps: int, out: pathlib.Path,
           audio: pathlib.Path | None, lossless: bool = False) -> None:
    from playwright.sync_api import sync_playwright

    # PNG encoding dominates the render (863ms vs 113ms per frame measured at 1080x1920),
    # and the frames are only ever an intermediate on the way into h264, so JPEG is the
    # default. The paper texture carries 5% noise, which dithers the gradients and keeps
    # them from banding. --png is there for a pristine master.
    shot = {"type": "png"} if lossless else {"type": "jpeg", "quality": 95}
    total = int(round(meta["duration"] * fps))
    ff = ffmpeg_bin()
    vcmd = [ff, "-y", "-f", "image2pipe", "-framerate", str(fps), "-i", "-"]
    if audio:
        vcmd += ["-i", str(audio)]
    vcmd += ["-c:v", "libx264", "-preset", "slow", "-crf", "18",
             "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
    if audio:
        vcmd += ["-c:a", "aac", "-b:a", "192k", "-shortest"]
    vcmd.append(str(out))

    proc = subprocess.Popen(vcmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                            stderr=subprocess.PIPE)
    import time
    with sync_playwright() as p:
        b, pg, stage = _open_stage(p, html, meta)
        got = pg.evaluate("document.getAnimations().length")
        if not got:
            print("  WARN   page declares no animations - output will be a still")
        print(f"  frames {total} @ {fps}fps  ({got} animations on the master clock)")

        t0 = time.time()
        for i in range(total):
            seek(pg, i / fps)
            proc.stdin.write(stage.screenshot(**shot))
            if i and i % 60 == 0:
                rate = (time.time() - t0) / i
                print(f"         {i:>4}/{total}  t={i/fps:5.2f}s  "
                      f"{rate*1000:.0f}ms/frame  eta {(total-i)*rate:.0f}s")
        b.close()

    proc.stdin.close()
    if proc.wait() != 0:
        sys.exit(f"ffmpeg failed:\n{proc.stderr.read().decode()[-2000:]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--out")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--vo-only", action="store_true")
    ap.add_argument("--still", type=float, metavar="SEC",
                    help="write a single PNG of that moment and exit (design iteration)")
    ap.add_argument("--to", type=float, metavar="SEC",
                    help="stop the render early (timing probe on a long film)")
    ap.add_argument("--png", action="store_true",
                    help="lossless intermediate frames (8x slower, for a master export)")
    a = ap.parse_args()

    html = pathlib.Path(a.html)
    if not html.exists():
        sys.exit(f"missing {html}")
    meta = read_meta(html)
    out = pathlib.Path(a.out) if a.out else html.with_suffix(".mp4")

    print(f"FILM   {html.name}  {meta['w']}x{meta['h']}  {meta['duration']}s")

    if a.still is not None:
        png = out.with_name(f"{html.stem}-t{a.still:g}s.png")
        grab_still(html, meta, a.still, png)
        print(f"  OK     {png}")
        return

    vo = None if a.no_audio else build_vo(meta, html.with_name(html.stem + "-vo.mp3"))
    if a.vo_only:
        print(f"  vo     {'written' if vo else 'not built'}")
        return

    if a.to:
        meta = dict(meta, duration=min(a.to, meta["duration"]))
        print(f"  probe  rendering first {meta['duration']}s only")
    render(html, meta, a.fps, out, vo, lossless=a.png)
    if SCRUB.exists():                      # CLAUDE.md 28: never ship an unscrubbed export
        subprocess.run([sys.executable, str(SCRUB), str(out)], capture_output=True)
    mb = out.stat().st_size / 1e6
    print(f"  OK     {out}  {mb:.1f} MB  {'narrated' if vo else 'SILENT'}")


if __name__ == "__main__":
    main()
