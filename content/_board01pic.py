#!/usr/bin/env python3
"""Reveal PICTURE for board 01 - ChatGPT vs Claude, for BUILDERS. 1080x1093, light.

This is the picture that goes inside the 7s reveal (content/_reveal.py, CLAUDE.md 32), not a
standalone poster: the reveal band carries the operator's title, this carries the payoff. Light
paper, because the reveal takes the band colour from the picture's mode and sets black hook text
on it - a dark picture makes the hook vanish.

Use cases are in the builder / solo-founder zone (operator: "use case urile ... tb sa fie in zona
de builder, solo-founder"), not generic consumer features.

    python3 content/_board01pic.py   # -> content/boards/01-pic.png
"""
import pathlib, re, glob

REPO = pathlib.Path(__file__).resolve().parent.parent
IC = REPO / "content/assets/icons"
OUT_HTML = REPO / "content/_board01pic.html"
OUT = REPO / "content/boards/01-pic.png"

GPT = [
    ("Product visuals", "mockups and ad images, no designer"),
    ("Live market research", "size a niche in minutes"),
    ("Voice brainstorming", "think out loud, hands-free"),
    ("Custom GPTs", "wrap your repeatable workflows"),
    ("Ad and landing copy", "test ten angles fast"),
    ("Everyday ops", "the quick all-rounder"),
]
CLAUDE = [
    ("Build your MVP", "Claude Code ships real features"),
    ("Ship a landing page", "Artifacts, live inside the chat"),
    ("Your whole launch", "emails and posts that sound human"),
    ("Read the whole codebase", "200K context, nothing dropped"),
    ("Analyze user feedback", "find the pattern in the data"),
    ("Client knowledge base", "a private Project per account"),
]


def svg(name):
    s = (IC / name).read_text()
    s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
    s = re.sub(r'\swidth="[^"]*"', "", s); s = re.sub(r'\sheight="[^"]*"', "", s)
    return s


def rows(items, side):
    out = []
    for label, detail in items:
        out.append(
            f'<div class="row"><div class="mk {side}"></div>'
            f'<div class="rt"><div class="rl">{label}</div>'
            f'<div class="rd">{detail}</div></div></div>')
    return "".join(out)


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--cream:#F5F1EA;--card:#FFFFFF;--ink:#171717;--muted:#6E6A61;--book:#C84623;
  --rule:rgba(23,23,23,.10);}}
*{{margin:0;padding:0;box-sizing:border-box}}
#art{{width:1080px;height:1093px;background:var(--cream);padding:44px 46px;
  display:flex;flex-direction:column;font-family:'DM Sans',sans-serif;position:relative;overflow:hidden}}
#art::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:radial-gradient(rgba(23,23,23,.045) 1.1px,transparent 1.2px);background-size:26px 26px}}
.body{{position:relative;z-index:1;flex:1;display:flex;min-height:0}}
.col{{flex:1;display:flex;flex-direction:column;min-height:0}}
.col.l{{padding-right:28px}} .col.r{{padding-left:28px}}
.chead{{display:flex;align-items:center;gap:11px;padding-bottom:11px;margin-bottom:12px;
  border-bottom:2px solid transparent}}
.chead.l{{border-image:linear-gradient(90deg,var(--ink),transparent) 1}}
.chead.r{{border-image:linear-gradient(90deg,var(--book),transparent) 1}}
.chead .lg{{width:33px;height:33px;display:inline-flex}}
.chead .lg svg{{width:100%;height:100%}}
.chead.l .lg{{color:var(--ink)}}
.chead .nm{{font-weight:900;font-size:27px;letter-spacing:-.5px;color:var(--ink)}}
.chead .bf{{margin-left:auto;font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--muted)}}
.rows{{display:flex;flex-direction:column;gap:10px;flex:1;min-height:0}}
.row{{flex:1;display:flex;gap:12px;align-items:center;padding:0 15px;
  background:var(--card);border:1px solid var(--rule);border-radius:12px;
  box-shadow:0 1px 3px rgba(23,23,23,.04)}}
.mk{{width:12px;height:12px;border-radius:50%;flex-shrink:0}}
.mk.l{{background:var(--ink);box-shadow:0 0 0 4px rgba(23,23,23,.08)}}
.mk.r{{background:var(--book);box-shadow:0 0 0 4px rgba(200,70,35,.12)}}
.rl{{font-weight:800;font-size:20.5px;color:var(--ink);letter-spacing:-.3px;line-height:1.12}}
.rd{{font-size:14.5px;color:var(--muted);margin-top:2px;line-height:1.22}}
.divwrap{{width:0;position:relative;z-index:2}}
.vline{{position:absolute;left:0;top:52px;bottom:0;width:1px;background:var(--rule)}}
.vs{{position:absolute;left:-25px;top:2px;width:50px;height:50px;border-radius:50%;
  background:var(--cream);border:1px solid var(--rule);display:flex;align-items:center;
  justify-content:center;font-family:'DM Mono',monospace;font-weight:500;font-size:14px;
  letter-spacing:.05em;color:var(--ink);box-shadow:0 2px 8px rgba(23,23,23,.06)}}
</style></head>
<body><div id="art">
  <div class="body">
    <div class="col l">
      <div class="chead l"><span class="lg">{svg('openai.svg')}</span><span class="nm">ChatGPT</span><span class="bf">a builder uses</span></div>
      <div class="rows">{rows(GPT,'l')}</div>
    </div>
    <div class="divwrap"><div class="vline"></div><div class="vs">VS</div></div>
    <div class="col r">
      <div class="chead r"><span class="lg">{svg('claude-color.svg')}</span><span class="nm">Claude</span><span class="bf">a builder uses</span></div>
      <div class="rows">{rows(CLAUDE,'r')}</div>
    </div>
  </div>
</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1093}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri()); pg.wait_for_timeout(700)
        pg.locator("#art").screenshot(path=str(OUT))
        b.close()


if __name__ == "__main__":
    OUT_HTML.write_text(html())
    render()
    print("rendered", OUT.relative_to(REPO))
