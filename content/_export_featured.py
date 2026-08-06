#!/usr/bin/env python3
"""Export LinkedIn Featured cards (1200x627) from the featured-*.html materials.

Renders at device_scale_factor=2 (2400x1254) then LANCZOS-downsamples to EXACTLY
1200x627, so the delivered file is the standard Featured size but retina-sharp.
Verifies the canvas box is 1200x627 before shooting, then runs content/_scrub.py
(CLAUDE.md 28) so nothing tool-related survives in the PNG metadata.

Usage: python3 content/_export_featured.py [content/featured-XX-*.html ...]
"""
import sys, base64, pathlib, tempfile, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LOGO = CONTENT / "ultron-logo.png"
W, H = 1200, 627


def render(src: pathlib.Path) -> pathlib.Path:
    from playwright.sync_api import sync_playwright
    from PIL import Image

    html = src.read_text()
    if "__LOGO_URI__" in html:
        if not LOGO.exists():
            sys.exit(f"missing logo: {LOGO}")
        uri = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
        html = html.replace("__LOGO_URI__", uri)
    tmp = pathlib.Path(tempfile.mkdtemp()) / "x.html"
    tmp.write_text(html)

    raw = pathlib.Path(tempfile.mkdtemp()) / "raw.png"
    with sync_playwright() as p:
        # the sandbox ships a pinned Chromium; never run "playwright install" here
        chrome = pathlib.Path("/opt/pw-browsers/chromium")
        b = p.chromium.launch(executable_path=str(chrome) if chrome.exists() else None)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(1800)
        pg.eval_on_selector("body", "e=>e.style.padding='0'")
        pg.eval_on_selector(".scaler>.canvas", "e=>e.style.transform='none'")
        el = pg.query_selector("#artifact")
        box = el.evaluate("e=>[e.offsetWidth,e.offsetHeight,e.scrollHeight]")
        if box[0] != W or box[1] != H or box[2] != H:
            b.close()
            sys.exit(f"{src.name}: canvas {box[0]}x{box[1]} scrollH {box[2]} != {W}x{H}")
        el.screenshot(path=str(raw))
        b.close()

    out = CONTENT / (src.stem.replace("-linkedin", "") + ".png")
    img = Image.open(raw).convert("RGB")
    if img.size != (W, H):
        img = img.resize((W, H), Image.LANCZOS)
    img.save(out)
    subprocess.run([sys.executable, str(CONTENT / "_scrub.py"), str(out)], check=True)
    print(f"  {out.name}  {Image.open(out).size}  {out.stat().st_size//1024}KB")
    return out


if __name__ == "__main__":
    args = sys.argv[1:] or sorted(str(p) for p in CONTENT.glob("featured-*-linkedin.html"))
    for a in args:
        render(pathlib.Path(a))
