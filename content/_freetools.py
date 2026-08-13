#!/usr/bin/env python3
"""Build the FREE-column AI-tools directory as the reveal picture (CLAUDE.md 32/33).

Operator brief: a video from the free column of the "Free vs Paid AI Tools" infographic, free
side only, hook = bait. Seedream mangles real brand logos, so the picture is built in HTML with
the ten logos that survive in simple-icons rendered monochrome, and the rest as two-letter
charcoal monograms, so 35 marks read as one consistent icon set on white.

    python3 content/_freetools.py            # builds html + renders content/ig/free-tools/picture.png
"""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
ICONS = REPO / "content/assets/icons"
OUT_HTML = REPO / "content/free-tools-directory.html"
OUT_PIC = REPO / "content/ig/free-tools/picture.png"

# (name, icon-slug-or-None, monogram).  Slug -> content/assets/icons/<slug>.svg (monochrome).
CATS = [
    ("WRITING", [
        ("ChatGPT", None, "GT"), ("Claude", "claude", None), ("Gemini", "googlegemini", None),
        ("Copy.ai", None, "co"), ("Writesonic", None, "Ws")]),
    ("VIDEO", [
        ("CapCut", None, "Cc"), ("Canva Video", None, "Cv"), ("Pika Labs", None, "Pk"),
        ("InVideo", None, "iV"), ("Luma AI", None, "Lu")]),
    ("IMAGE", [
        ("DALL-E", None, "DE"), ("Leonardo AI", None, "Le"), ("Craiyon", None, "Cr"),
        ("MS Designer", None, "MD"), ("Ideogram", None, "Id")]),
    ("CODING", [
        ("GitHub Copilot", "githubcopilot", None), ("Replit AI", "replit", None),
        ("Codeium", None, "Cd"), ("Colab AI", "googlecolab", None), ("Loveable", None, "Lv")]),
    ("VOICE & AUDIO", [
        ("Suno AI", "suno", None), ("Udio", None, "Ud"), ("Descript", None, "Ds"),
        ("ElevenLabs", "elevenlabs", None), ("Murf AI", None, "Mu")]),
    ("RESEARCH", [
        ("Perplexity", "perplexity", None), ("NotebookLM", None, "NL"),
        ("Semantic Scholar", "semanticscholar", None), ("Consensus", None, "Cs"),
        ("ChatGPT Search", None, "CS")]),
    ("DESIGN", [
        ("Canva", None, "Cv"), ("MS Designer", None, "MD"), ("Figma AI", "figma", None),
        ("Autodraw", None, "Ad"), ("Pixicout", None, "Px")]),
]

INK = "#171717"


def mark(slug: str | None, mono: str | None) -> str:
    if slug:
        svg = (ICONS / f"{slug}.svg").read_text()
        svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
        svg = svg.replace("<svg ", f'<svg fill="{INK}" ', 1)
        svg = re.sub(r'\swidth="[^"]*"', "", svg)
        svg = re.sub(r'\sheight="[^"]*"', "", svg)
        return f'<span class="ic logo">{svg}</span>'
    return f'<span class="ic mono">{mono}</span>'


def tile(name: str, slug: str | None, mono: str | None) -> str:
    return (f'<div class="tile"><div class="chip">{mark(slug, mono)}</div>'
            f'<div class="nm">{name}</div></div>')


def row(label: str, tools: list) -> str:
    tiles = "".join(tile(*t) for t in tools)
    return (f'<div class="cat"><div class="lab"><span>{label}</span><i></i></div>'
            f'<div class="row">{tiles}</div></div>')


def build_html() -> str:
    body = "".join(row(l, t) for l, t in CATS)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:1080px;height:1093px;background:#FFFFFF;
  padding:26px 40px 22px;display:flex;flex-direction:column;
  font-family:'DM Sans',sans-serif;position:relative}}
.cat{{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0}}
.cat+.cat{{border-top:1px solid rgba(23,23,23,.07)}}
.lab{{display:flex;align-items:center;gap:12px;margin-bottom:10px}}
.lab span{{font-family:'DM Mono',monospace;font-size:12px;font-weight:500;
  letter-spacing:.20em;color:#C84623;text-transform:uppercase;white-space:nowrap}}
.lab i{{flex:1;height:1px;background:rgba(200,70,35,.22)}}
.row{{display:flex;gap:14px}}
.tile{{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;min-width:0}}
.chip{{width:58px;height:58px;border-radius:15px;background:#F1EFEA;
  display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.ic.logo svg{{width:30px;height:30px;display:block}}
.ic.mono{{font-family:'DM Sans',sans-serif;font-weight:800;font-size:22px;color:{INK};
  letter-spacing:-.5px}}
.nm{{font-size:14.5px;font-weight:600;color:{INK};text-align:center;line-height:1.15;
  letter-spacing:-.2px}}
</style></head>
<body><div class="card">{body}</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    import glob
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
