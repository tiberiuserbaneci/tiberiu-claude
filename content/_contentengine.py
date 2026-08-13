#!/usr/bin/env python3
"""Build the "30-day content engine" picture: a real copy-paste prompt + proof of its output.

Operator, on the pretty-but-useless research hub: "de ce l as salva? ... e o reclama pura la
chatgpt. ce sa fac eu cu el?" The fix is a TOOL, not a poster: the frame carries a real prompt a
founder pastes into ChatGPT to get a month of content, and the output is shown so the value is
provable at a glance. The full engine (angle sub-prompts, a swipe file, a template) is the DM.

Built in HTML because the prompt has to be exact and legible - ARK mangles a paragraph of text.

    python3 content/_contentengine.py   # -> content/ig/content-engine/picture.png
"""
import pathlib, re, glob

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT_HTML = REPO / "content/content-engine-pic.html"
OUT_PIC = REPO / "content/ig/content-engine/picture.png"
INK = "#171717"

PROMPT_LINES = [
    ('b', "Act as my content strategist."),
    ('n', "Niche: [your niche]    Voice: [blunt, expert]"),
    ('gap', ""),
    ('b', "Plan my next 30 days. For each day give:"),
    ('a', "a scroll-stop hook, 12 words max"),
    ('a', "the format: carousel, reel or single"),
    ('a', "the one idea the post teaches"),
    ('gap', ""),
    ('b', "Rotate 5 angles: story, how-to, myth-bust,"),
    ('b', "list, hot take.  No emojis."),
]

# a few sample output cells to prove it returns real posts, the rest just carry the day number
SAMPLES = {1: "The mistake killing your reach",
           9: "Steal my 3-tab workflow",
           17: "Nobody says this out loud",
           26: "I deleted 4 tools. Here is why"}


def chatgpt_mark(px: int) -> str:
    svg = (REPO / "content/assets/icons/openai.svg").read_text()
    svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
    svg = re.sub(r'\swidth="[^"]*"', "", svg); svg = re.sub(r'\sheight="[^"]*"', "", svg)
    return f'<span class="ico" style="width:{px}px;height:{px}px">{svg}</span>'


def prompt_html() -> str:
    rows = []
    for kind, txt in PROMPT_LINES:
        if kind == 'gap':
            rows.append('<div class="pgap"></div>')
        elif kind == 'a':
            rows.append(f'<div class="pl"><span class="ar">&rarr;</span>{txt}</div>')
        elif kind == 'b':
            rows.append(f'<div class="pl st">{txt}</div>')
        else:
            rows.append(f'<div class="pl">{txt}</div>')
    return "".join(rows)


def grid_html() -> str:
    cells = []
    for d in range(1, 31):
        s = SAMPLES.get(d)
        if s:
            cells.append(f'<div class="cell hot"><div class="dn">DAY {d}</div>'
                         f'<div class="hk">{s}</div></div>')
        else:
            cells.append(f'<div class="cell"><div class="dn">DAY {d}</div></div>')
    return "".join(cells)


def build_html() -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
.card{{width:1080px;height:1093px;background:#FFFFFF;padding:30px 40px;
  display:flex;flex-direction:column;font-family:'DM Sans',sans-serif}}
.eyebrow{{font-family:'DM Mono',monospace;font-size:14px;font-weight:500;letter-spacing:.22em;
  color:#C84623;text-transform:uppercase;margin-bottom:14px}}
/* the prompt, styled like a chat input you paste into */
.prompt{{background:#F6F4F0;border:1px solid rgba(23,23,23,.09);border-radius:22px;
  padding:22px 26px;box-shadow:0 4px 20px rgba(23,23,23,.05)}}
.phead{{display:flex;align-items:center;gap:10px;padding-bottom:14px;margin-bottom:16px;
  border-bottom:1px solid rgba(23,23,23,.08)}}
.ico{{display:inline-flex}} .ico svg{{width:100%;height:100%;color:#171717}}
.phead b{{font-size:19px;font-weight:800;color:#171717}}
.phead .tag{{margin-left:auto;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;
  color:#8a8a83;text-transform:uppercase}}
.pl{{font-size:26px;line-height:1.42;color:#2a2a28;letter-spacing:-.2px}}
.pl.st{{color:#171717;font-weight:600}}
.pl .ar{{color:#C84623;font-weight:800;margin-right:10px}}
.pgap{{height:14px}}
/* the bridge */
.bridge{{display:flex;align-items:center;justify-content:center;gap:12px;margin:16px 0 14px}}
.bridge .ln{{flex:1;height:1px;background:rgba(23,23,23,.12)}}
.bridge .t{{font-family:'DM Mono',monospace;font-size:14px;font-weight:500;letter-spacing:.14em;
  color:#171717;text-transform:uppercase}}
.bridge .t b{{color:#C84623}}
/* the output: 30 days, proof it fills a month */
.grid{{flex:1;display:grid;grid-template-columns:repeat(6,1fr);grid-auto-rows:1fr;gap:10px;min-height:0}}
.cell{{background:#F6F4F0;border:1px solid rgba(23,23,23,.06);border-radius:12px;
  padding:9px 10px;display:flex;flex-direction:column;overflow:hidden}}
.cell .dn{{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.1em;color:#9a9a92}}
.cell.hot{{background:rgba(200,70,35,.09);border-color:rgba(200,70,35,.3);grid-column:span 2}}
.cell.hot .dn{{color:#C84623}}
.cell.hot .hk{{font-size:17px;font-weight:700;color:#171717;line-height:1.12;margin-top:3px;
  letter-spacing:-.2px}}
</style></head>
<body><div class="card">
  <div class="eyebrow">Paste this into ChatGPT &rarr;</div>
  <div class="prompt">
    <div class="phead">{chatgpt_mark(26)}<b>ChatGPT</b><span class="tag">content engine</span></div>
    {prompt_html()}
  </div>
  <div class="bridge"><span class="ln"></span><span class="t">it returns <b>30 days</b> of posts</span><span class="ln"></span></div>
  <div class="grid">{grid_html()}</div>
</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next((h for p in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",)
                for h in sorted(glob.glob(p))), None)
    OUT_PIC.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1093}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri()); pg.wait_for_timeout(800)
        pg.locator(".card").screenshot(path=str(OUT_PIC))
        b.close()


if __name__ == "__main__":
    OUT_HTML.write_text(build_html())
    print(f"built  {OUT_HTML.relative_to(REPO)}")
    render()
    print(f"rendered  {OUT_PIC.relative_to(REPO)}")
