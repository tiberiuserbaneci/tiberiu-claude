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
CATS = [
    ("WRITING", "#C0553A", [
        ("ChatGPT", "openai.svg", True), ("Claude", "claude-color.svg", False),
        ("Gemini", "gemini-color.svg", False)]),
    ("VIDEO", "#4C5FAF", [
        ("CapCut", "capcut.svg", True), ("Pika Labs", "pika.svg", True),
        ("Luma", "luma-color.svg", True)]),
    ("IMAGE", "#8A4E9C", [
        ("DALL-E", "dalle-color.svg", False), ("Ideogram", "ideogram.svg", True),
        ("Stable Diffusion", "stability-color.svg", False)]),
    ("CODING", "#1F8A70", [
        ("GitHub Copilot", "copilot-color.svg", False), ("Replit", "replit-color.svg", False),
        ("Colab", "colab-color.svg", False)]),
    ("VOICE & AUDIO", "#B7791F", [
        ("Suno", "suno.svg", True), ("ElevenLabs", "elevenlabs.svg", True),
        ("Udio", "udio-color.svg", False)]),
    ("RESEARCH", "#C0413F", [
        ("Perplexity", "perplexity-color.svg", False), ("NotebookLM", "notebooklm.svg", True),
        ("Semantic Scholar", "semanticscholar.svg", True)]),
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
    tint, hair = accent + "14", accent + "33"
    return (f'<div class="cat" style="--acc:{accent};--tint:{tint};--hair:{hair}">'
            f'<div class="lab"><span>{label}</span><i></i></div>'
            f'<div class="row">{tiles}</div></div>')


def build_html():
    body = "".join(row(l, a, t) for l, a, t in CATS)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:1080px;height:1093px;background:#FFFFFF;padding:24px 34px 20px;
  display:flex;flex-direction:column;font-family:'DM Sans',sans-serif}}
.cat{{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0}}
.cat+.cat{{border-top:1px solid rgba(23,23,23,.06)}}
.lab{{display:flex;align-items:center;gap:12px;margin-bottom:9px}}
.lab span{{font-family:'DM Mono',monospace;font-size:12.5px;font-weight:500;
  letter-spacing:.2em;color:var(--acc);text-transform:uppercase;white-space:nowrap}}
.lab i{{flex:1;height:1px;background:var(--hair)}}
.row{{display:flex;gap:20px}}
.tile{{flex:1;display:flex;flex-direction:column;align-items:center;gap:9px;min-width:0}}
.chip{{width:86px;height:86px;border-radius:22px;background:var(--tint);
  border:1px solid var(--hair);display:flex;align-items:center;justify-content:center}}
.chip svg{{width:50px;height:50px;display:block}}
.nm{{font-size:19px;font-weight:600;color:#191919;text-align:center;line-height:1.12;
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
