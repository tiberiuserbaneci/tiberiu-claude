#!/usr/bin/env python3
"""Build the FREE-column AI-tools directory as the reveal picture (CLAUDE.md 32/33).

Operator: no initials (they read amateur), real COLOR logos, only 3 per row, bigger, and a
distinct colour nuance per category. So this is 7 categories x 3 tools = 21, every tile a real
brand logo. Thirteen carry their true brand colours; the genuinely-monochrome marks (ChatGPT,
CapCut, Pika, Ideogram, Suno, ElevenLabs, NotebookLM, Semantic Scholar, Luma) are tinted to the
category colour so every tile reads coloured. Logos are vendored from @lobehub/icons (npm),
simple-icons (npm) and svgl (Canva), because Seedream mangles real logos and the renderer cannot
fetch a CDN.

    python3 content/_freetools.py       # builds html + renders content/ig/free-tools/picture.png
"""
import pathlib, re, subprocess, sys, glob

REPO = pathlib.Path(__file__).resolve().parent.parent
ICONS = REPO / "content/assets/icons"
OUT_HTML = REPO / "content/free-tools-directory.html"
OUT_PIC = REPO / "content/ig/free-tools/picture.png"

# category -> (accent colour, [ (name, svg-file, recolor?) ]).  recolor=True paints the mark in
# the accent (a monochrome brand mark); False keeps the svg's own brand colours.
# Four categories only (operator 2026-08-13: dropped WRITING, CODING, RESEARCH), so the icons can
# be big and the category labels visible - the seven-row version rendered both too small.
CATS = [
    ("VIDEO", "#4C5FAF", [
        ("CapCut", "capcut.svg", True), ("Pika Labs", "pika.svg", True),
        ("Luma", "luma-color.svg", True)]),
    ("IMAGE", "#8A4E9C", [
        ("DALL-E", "dalle-color.svg", False), ("Ideogram", "ideogram.svg", True),
        ("Stable Diffusion", "stability-color.svg", False)]),
    ("VOICE & AUDIO", "#B7791F", [
        ("Suno", "suno.svg", True), ("ElevenLabs", "elevenlabs.svg", True),
        ("Udio", "udio-color.svg", False)]),
    ("DESIGN", "#3E6D8E", [
        ("Canva", "canva-color.svg", False), ("Figma", "figma-color.svg", False),
        ("MS Designer", "microsoft-color.svg", False)]),
]


def mark(fname: str, recolor: bool, accent: str) -> str:
    svg = (ICONS / fname).read_text()
    svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
    if recolor:
        svg = re.sub(r'fill="(currentColor|#000000|#000|black|#1A1A1A|#1a1a1a)"',
                     f'fill="{accent}"', svg)
    return svg


def tile(name, fname, recolor, accent):
    return (f'<div class="tile"><div class="chip">{mark(fname, recolor, accent)}</div>'
            f'<div class="nm">{name}</div></div>')


def row(label, accent, tools):
    tiles = "".join(tile(n, f, r, accent) for n, f, r in tools)
    tint = accent + "14"
    return (f'<div class="cat" style="--acc:{accent};--tint:{tint}">'
            f'<div class="lab">{label}</div>'
            f'<div class="row">{tiles}</div></div>')


def build_html():
    body = "".join(row(l, a, t) for l, a, t in CATS)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:1080px;height:1093px;background:#FFFFFF;padding:26px 30px;
  display:flex;flex-direction:column;gap:18px;font-family:'DM Sans',sans-serif}}
/* each category is its own tinted band, so the category is unmistakable and its colour reads */
.cat{{flex:1;background:var(--tint);border-radius:26px;padding:18px 26px 22px;
  display:flex;flex-direction:column;min-height:0}}
/* the label is a solid colour pill, big, not a faint mono line that vanished on a phone */
.lab{{align-self:flex-start;background:var(--acc);color:#fff;
  font-family:'DM Sans',sans-serif;font-weight:800;font-size:17px;letter-spacing:.06em;
  text-transform:uppercase;padding:7px 16px;border-radius:999px;margin-bottom:6px}}
/* icons big and close together: centred, fixed tiles, a modest gap, not stretched edge to edge */
.row{{flex:1;display:flex;justify-content:center;align-items:center;gap:44px;min-height:0}}
.tile{{width:196px;display:flex;flex-direction:column;align-items:center;gap:12px}}
.chip{{width:132px;height:132px;border-radius:30px;background:#fff;
  border:1px solid rgba(23,23,23,.06);box-shadow:0 3px 14px rgba(23,23,23,.06);
  display:flex;align-items:center;justify-content:center}}
.chip svg{{width:80px;height:80px;display:block}}
.nm{{font-size:23px;font-weight:700;color:#191919;text-align:center;line-height:1.1;
  letter-spacing:-.3px}}
</style></head>
<body><div class="card">{body}</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next((h for p in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",)
                for h in sorted(glob.glob(p))), None)
    OUT_PIC.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1093}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri())
        pg.wait_for_timeout(900)
        pg.locator(".card").screenshot(path=str(OUT_PIC))
        b.close()


if __name__ == "__main__":
    OUT_HTML.write_text(build_html())
    print(f"built  {OUT_HTML.relative_to(REPO)}")
    render()
    print(f"rendered  {OUT_PIC.relative_to(REPO)}")
