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
    if "*/" in m.group(1):
        sys.exit(f"{html.name}: FILM-META contains '*/', which closes the CSS comment early "
                 f"and silently drops the whole :root block. Use | as a separator.")
    meta = json.loads(m.group(1))
    meta.setdefault("w", 1080)
    meta.setdefault("h", 1920)
    meta.setdefault("beats", [])
    return meta


# ---------------------------------------------------------------- voiceover

def build_vo(meta: dict, out_mp3: pathlib.Path) -> tuple[pathlib.Path, list[float], float] | None:
    """Narrate the film as one unbroken take. Returns (mp3, beat marks, duration).

    The beats are spoken in a single request rather than one clip per beat. Stitched clips
    each carry their own lead-in and tail silence, which adds up to roughly a second of dead
    air across six cuts and makes the narration sound assembled. One take also lets the voice
    carry its own prosody across sentence boundaries.

    The picture then follows the voice instead of the other way round: character-level
    timestamps say when each beat's sentence actually begins, and those become the beat marks
    the page animates on. A sentence that runs long moves its cut with it, so the visual for a
    line can never appear before the line is spoken.
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

    # Character offset where each beat's line starts inside the joined script.
    script, starts = "", []
    for b in beats:
        starts.append(len(script))
        script += b["vo"] + " "
    script = script.strip()
    words = len(script.split())

    model = os.environ.get("ELEVEN_MODEL", "eleven_multilingual_v2")
    cache = out_mp3.with_suffix(".align.json")
    if cache.exists():
        payload = json.loads(cache.read_text())
        if payload.get("script") != script:
            payload = None                       # script edited, re-record
    else:
        payload = None

    if payload is None:
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps",
            data=json.dumps({
                "text": script,
                "model_id": model,
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75,
                                   "style": 0.0, "use_speaker_boost": True},
            }).encode(),
            headers={"xi-api-key": key, "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                payload = json.loads(r.read())
        except urllib.error.HTTPError as e:
            print(f"  vo     FAIL HTTP {e.code} {e.read()[:200]!r} -> silent film")
            return None
        payload["script"] = script
        cache.write_text(json.dumps(payload))

    out_mp3.write_bytes(base64.b64decode(payload["audio_base64"]))
    al = payload.get("alignment") or {}
    cstart = al.get("character_start_times_seconds") or []
    cend = al.get("character_end_times_seconds") or []
    if not cstart:
        print("  vo     WARN no alignment returned, keeping authored beat marks")
        return out_mp3, [b["t"] for b in beats], meta["duration"]

    marks = [round(cstart[min(i, len(cstart) - 1)], 2) for i in starts]
    spoken = round(cend[-1], 2)
    print(f"  vo     one take, {words} words in {spoken:.1f}s "
          f"({words/spoken:.2f} w/s, {words/spoken*60:.0f} wpm)")
    for i, (m, b) in enumerate(zip(marks, beats)):
        gap = m - round(cend[max(0, starts[i] - 2)], 2) if i else 0.0
        print(f"         beat {i+1} @ {m:>5.2f}s  (gap {gap:+.2f}s)  {b['vo'][:46]}")
    return out_mp3, marks, spoken


# ---------------------------------------------------------------- frame capture

def words_from(alignment: dict) -> list[tuple[str, float, float]]:
    """Character timings -> (word, start, end). The voice is the only clock that matters."""
    chars = alignment.get("characters") or []
    st = alignment.get("character_start_times_seconds") or []
    en = alignment.get("character_end_times_seconds") or []
    out, cur, start, last = [], "", None, 0.0
    for c, cs, ce in zip(chars, st, en):
        if c.isspace():
            if cur:
                out.append((cur, start, last))
            cur, start = "", None
        else:
            if not cur:
                start = cs
            cur += c
            last = ce
    if cur:
        out.append((cur, start, last))
    return out


# Words that only glue a sentence together. They stay small and quiet so the words that
# carry the meaning can be enormous, which is the whole difference between a caption track
# and kinetic typography.
GLUE = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on", "at", "for", "with", "is", "are",
    "was", "it", "its", "you", "your", "they", "their", "them", "that", "this", "what", "so",
    "then", "all", "i", "will", "be", "do", "does", "into", "from", "as", "but", "not", "no",
    "up", "out", "if", "by", "my", "we", "our", "he", "she", "who", "already", "just",
}

# Premium motion identity (motion-design skill): elegant, controlled, zero overshoot.
# Heavier words get longer, more emphasized entrances; glue drifts in and gets out of the way.
# duration, easing var, entrance keyframes to cycle through
WEIGHT = {
    "fn":   (0.22, "var(--eStd)",  ("kRise",)),
    "mid":  (0.34, "var(--eStd)",  ("kRise", "kLeft", "kRight")),
    "key":  (0.48, "var(--eEmph)", ("kDrop", "kPop")),
    "hero": (0.72, "var(--eEmph)", ("kBlur",)),          # dramatic reveal territory
}


def weigh(word: str, accents: set[str]) -> str:
    """How much visual weight this word has earned in the line."""
    bare = word.strip(".,:;!?'\"").lower()
    if bare in accents:
        return "hero"
    if bare in GLUE or len(bare) <= 2:
        return "fn"
    if word.strip(".,:;").isupper() or len(bare) >= 8 or any(c.isdigit() for c in bare):
        return "key"
    return "mid"


def chunk_words(words, max_words=4, max_chars=26):
    """Group spoken words into caption-sized phrases.

    Breaking after clause punctuation keeps a chunk from straddling a pause, which is what
    makes an auto-caption feel machine made.
    """
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        text = " ".join(x[0] for x in cur)
        ends_clause = w[0][-1] in ".,:;"
        if len(cur) >= max_words or len(text) >= max_chars or ends_clause:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    return chunks


def build_captions(meta: dict, words: list, hook_end: float,
                   cta_at: float | None = None) -> tuple[str, str]:
    """Return (DOM html, CSS) for the full-screen hook and the word-synced subtitles.

    Two jobs the reference clip splits. The opening sentence is the whole frame, because the
    first three seconds decide whether anyone sees the rest. Everything after it drops into
    the lower band and reveals word by word on the voice, replacing the static headline that
    used to sit there restating what the narration had just said.
    """
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    css, dom = [], []

    # ---- hook: the opening sentence, filling the safe band, one word at a time ----
    spec = meta.get("hook") or ""
    hook_words = [w for w in words if w[1] < hook_end]
    hold = float(meta.get("hook_hold", 0.15))
    out_at = (hook_words[-1][2] + hold) if hook_words else hook_end

    lines, i = [], 0
    for raw_line in spec.split("|"):
        toks = [t for t in raw_line.strip().split(" ") if t]
        row = []
        for tok in toks:
            if i < len(hook_words):
                row.append((hook_words[i], tok.startswith("*")))
                i += 1
        if row:
            lines.append(row)

    accents = {a.strip(".,:;!?").lower() for a in (meta.get("accent") or [])}
    dom.append('<div id="hook" class="hk"><div class="hk-in">')
    n = 0
    for li, row in enumerate(lines):
        dom.append(f'<div class="hk-l {("", "I", "R")[li % 3]}">')
        for (word, ws, _we), accent in row:
            n += 1
            w = "hero" if accent else weigh(word, accents)
            dur, ease, entrances = WEIGHT[w]
            kf = entrances[n % len(entrances)]
            dom.append(f'<span class="hw {w}{" a" if accent else ""} hw{n}">{esc(word)}</span>')
            anim = [f"{kf} {dur:.2f}s {ease} both {ws:.2f}s"]
            if accent:
                # secondary motion: the highlighter chases the word in rather than arriving
                # with it, and the tracking settles after it lands
                anim.append(f"hkbar .28s var(--eStd) both {ws + .07:.2f}s")
                anim.append(f"kTrack .55s var(--eStd) both {ws:.2f}s")
            css.append(f".hw{n}{{animation:{','.join(anim)}}}")
        dom.append("</div>")
    dom.append("</div></div>")
    # push-in across the hook, then clear the frame for the visuals
    css.append(f".hk-in{{animation:hkpush {max(out_at, .1):.2f}s linear both 0s}}")
    css.append(f".hk{{animation:hkout .38s ease-in forwards {out_at:.2f}s}}")

    # ---- subtitles: everything after the hook, in the lower band ----
    # The hook covers the caption band too, so nothing may appear underneath it until the
    # push-out has finished, and nothing may run under the CTA card, whose own type already
    # says the words being spoken.
    hook_clear = out_at + .40
    rest = [w for w in words if w[1] >= hook_end]
    if cta_at:
        rest = [w for w in rest if w[1] < cta_at]
    dom.append('<div id="subs" class="sb">')
    for ci, chunk in enumerate(chunk_words(rest), start=1):
        c_in = max(chunk[0][1] - .10, hook_clear if ci == 1 else 0)
        nxt = None
        flat = [w for w in rest if w[1] > chunk[-1][1]]
        if flat:
            nxt = flat[0][1]
        # clear the frame a fade before the next chunk arrives, or two are legible at once
        c_out = min(nxt - .26, chunk[-1][2] + .40) if nxt else chunk[-1][2] + .40
        c_out = max(c_out, c_in + .30)
        # exits accelerate away and run shorter than entrances: what arrives matters more
        css.append(f".ck{ci}{{animation:scin .22s var(--eStd) both {c_in:.2f}s,"
                   f"ckout .14s var(--eExit) forwards {c_out:.2f}s}}")
        # anchor cycles so the eye is not pinned to one margin for 25 seconds
        dom.append(f'<div class="ck {"LIRC"[ci % 4]} ck{ci}">')
        for word, ws, _we in chunk:
            n += 1
            w = weigh(word, accents)
            dur, ease, entrances = WEIGHT[w]
            kf = entrances[n % len(entrances)]
            dom.append(f'<span class="sw {w} sw{n}">{esc(word)}</span>')
            anim = [f"{kf} {dur:.2f}s {ease} both {ws:.2f}s"]
            if w in ("key", "mid"):
                # read-along highlight: lands in book orange as it is spoken, settles to ink
                anim.append(f"sbs .30s linear forwards {ws + dur:.2f}s")
                css.append(f".sw{n}{{color:var(--book);animation:{','.join(anim)}}}")
            else:
                css.append(f".sw{n}{{animation:{','.join(anim)}}}")
        dom.append("</div>")
    dom.append("</div>")
    return "".join(dom), "".join(css)


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


def _open_stage(p, html: pathlib.Path, meta: dict, marks: list[float] | None = None,
                captions: tuple[str, str] | None = None):
    """Launch a browser on the film and return (browser, page, #film locator).

    `marks` overwrites the page's --b1..--bN beat clock with times measured from the
    voiceover, so every cut lands on the word that motivates it.
    """
    exe = chromium_path()
    if exe:
        print(f"  chrome {exe}")
    b = p.chromium.launch(executable_path=exe,
                          args=["--force-color-profile=srgb", "--disable-lcd-text",
                                "--font-render-hinting=none"])
    pg = b.new_page(viewport={"width": meta["w"], "height": meta["h"]},
                    device_scale_factor=1)
    pg.goto(html.resolve().as_uri())
    if captions:
        dom, css = captions
        pg.evaluate("""({dom, css}) => {
            const band = document.getElementById('capband');
            const wrap = document.createElement('div');
            wrap.innerHTML = dom;
            // the hook overlays the whole frame, the subtitles live in the lower band
            const hook = wrap.querySelector('#hook');
            if (hook) document.getElementById('film').appendChild(hook);
            const subs = wrap.querySelector('#subs');
            if (subs && band) band.appendChild(subs);
            const s = document.createElement('style');
            s.textContent = css;
            document.head.appendChild(s);
        }""", {"dom": dom, "css": css})
    if marks:
        pg.evaluate("""ms => {
            const r = document.documentElement;
            ms.forEach((t, i) => r.style.setProperty(`--b${i+1}`, `${t}s`));
        }""", marks)
        print("  clock  " + "  ".join(f"b{i+1}={t:g}s" for i, t in enumerate(marks)))
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
           audio: pathlib.Path | None, lossless: bool = False,
           marks: list[float] | None = None,
           captions: tuple[str, str] | None = None) -> None:
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
        b, pg, stage = _open_stage(p, html, meta, marks, captions)
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

    built = None if a.no_audio else build_vo(meta, html.with_name(html.stem + "-vo.mp3"))
    if a.vo_only:
        print(f"  vo     {'written' if built else 'not built'}")
        return

    vo = marks = captions = None
    if built:
        # The take, not the storyboard, sets the length: run to the last word plus a beat
        # to let the CTA land, so the film never outlives the narration or clips it.
        vo, marks, spoken = built
        meta = dict(meta, duration=round(spoken + 0.7, 2))
        print(f"  length {meta['duration']}s (spoken {spoken}s + 0.7s tail)")

        cache = html.with_name(html.stem + "-vo.align.json")
        if meta.get("hook") and cache.exists():
            words = words_from(json.loads(cache.read_text()).get("alignment") or {})
            # The hook runs to the end of the opening sentence: it is the one line that has
            # to land, so it owns the frame until it is finished being said.
            hook_end = next((w[2] for w in words if w[0].endswith(".")), 2.5) + 0.05
            # the CTA beat draws its own COMMENT CORTEX, so captions stop there
            captions = build_captions(meta, words, hook_end,
                                      cta_at=marks[-1] if marks else None)
            n_hook = sum(1 for w in words if w[1] < hook_end)
            print(f"  caps   hook {n_hook} words to {hook_end:.2f}s, "
                  f"{len(words) - n_hook} words captioned after")

    if a.to:
        meta = dict(meta, duration=min(a.to, meta["duration"]))
        print(f"  probe  rendering first {meta['duration']}s only")
    render(html, meta, a.fps, out, vo, lossless=a.png, marks=marks, captions=captions)
    if SCRUB.exists():                      # CLAUDE.md 28: never ship an unscrubbed export
        subprocess.run([sys.executable, str(SCRUB), str(out)], capture_output=True)
    mb = out.stat().st_size / 1e6
    print(f"  OK     {out}  {mb:.1f} MB  {'narrated' if vo else 'SILENT'}")


if __name__ == "__main__":
    main()
