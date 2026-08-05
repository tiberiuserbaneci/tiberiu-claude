#!/usr/bin/env python3
"""Render a slide deck to PNGs and a PDF carousel at exact canvas size.

Same discipline as the film renderer: the page is the source of truth, the export never
guesses. Each `.slide` is screenshotted at its own box, so a slide that is not exactly
1080x1920 shows up as a wrong-sized file rather than as a silently letterboxed upload.

Usage:
  python3 content/_carousel.py content/paper-01-chat.html
  python3 content/_carousel.py content/paper-*.html --pdf-only
  python3 content/_carousel.py content/paper-01-chat.html --check   # geometry only, no files
"""
import argparse, functools, glob, pathlib, subprocess, sys

print = functools.partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRUB = CONTENT / "_scrub.py"


def chromium_path():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None


def render(html: pathlib.Path, out_dir: pathlib.Path, check_only=False, w=1080, h=1920):
    from playwright.sync_api import sync_playwright
    exe = chromium_path()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": 900}, device_scale_factor=1)
        pg.goto(f"file://{html.resolve()}")
        pg.wait_for_timeout(1400)
        pg.evaluate("document.fonts.ready")
        n = pg.locator(".slide").count()
        if n == 0:
            sys.exit(f"{html.name}: no .slide elements")

        bad = pg.evaluate("""([w,h]) => [...document.querySelectorAll('.slide')]
            .map((s,i)=>({i:i+1, w:Math.round(s.scrollWidth), h:Math.round(s.scrollHeight)}))
            .filter(s=>s.w!==w||s.h!==h)""", [w, h])
        if bad:
            for s in bad:
                print(f"  DIM  slide {s['i']:02d} is {s['w']}x{s['h']}, expected {w}x{h}")
            b.close()
            sys.exit(f"{html.name}: {len(bad)} slide(s) off canvas")

        # anything painted outside the safe box will be cropped by the app UI
        spill = pg.evaluate("""() => {
            const out=[];
            document.querySelectorAll('.slide').forEach((s,i)=>{
              const r=s.getBoundingClientRect();
              s.querySelectorAll('.safe *').forEach(e=>{
                const b=e.getBoundingClientRect();
                if(!b.width||!b.height) return;
                const top=b.top-r.top, bot=r.bottom-b.bottom,
                      left=b.left-r.left, right=r.right-b.right;
                if(top<299||bot<329||left<69||right<129)
                  out.push({i:i+1, cls:(e.className||'').toString().slice(0,24),
                            top:Math.round(top), bot:Math.round(bot),
                            left:Math.round(left), right:Math.round(right)});
              });
            });
            return out.slice(0,6);
        }""")
        if spill:
            for s in spill:
                print(f"  SAFE slide {s['i']:02d} .{s['cls']} t{s['top']} b{s['bot']} "
                      f"l{s['left']} r{s['right']}")
        print(f"  {html.name:28} {n} slides  all {w}x{h}"
              + ("" if not spill else f"  ({len(spill)} outside the safe box)"))
        if check_only:
            b.close()
            return []

        out_dir.mkdir(parents=True, exist_ok=True)
        pngs = []
        for i in range(n):
            f = out_dir / f"{html.stem}-{i+1:02d}.png"
            pg.locator(".slide").nth(i).screenshot(path=str(f))
            pngs.append(f)
        b.close()
    return pngs


def to_pdf(pngs, dest: pathlib.Path):
    """One page per slide, page box equal to the image box. No resampling, no margins."""
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in pngs]
    ims[0].save(dest, save_all=True, append_images=ims[1:], resolution=72.0)
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decks", nargs="+")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=str(CONTENT / "paper"))
    a = ap.parse_args()
    out_dir = pathlib.Path(a.out)
    for d in a.decks:
        html = pathlib.Path(d)
        pngs = render(html, out_dir, check_only=a.check)
        if a.check or not pngs:
            continue
        pdf = to_pdf(pngs, out_dir / f"{html.stem}.pdf")
        subprocess.run([sys.executable, str(SCRUB), str(pdf)], check=False,
                       capture_output=True)
        for p in pngs:
            subprocess.run([sys.executable, str(SCRUB), str(p)], check=False,
                           capture_output=True)
        print(f"  -> {pdf.name}  ({len(pngs)} pages, scrubbed)")


if __name__ == "__main__":
    main()
