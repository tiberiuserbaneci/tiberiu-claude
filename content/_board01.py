#!/usr/bin/env python3
"""Board 01 - ChatGPT vs Claude, which one for which job. 1080x1350 (4:5 feed).

Two columns of real, verified best-at use cases (sources: llm-stats / zapier, 2026). Ultron is
slotted as one row on the Claude side - the founder-GTM use case built on Claude (operator override
of CLAUDE.md 31 for this comparison series: position beside known tools = borrowed credibility).

    python3 content/_board01.py   # -> content/boards/01-chatgpt-vs-claude.png
"""
import pathlib, re, base64, glob

REPO = pathlib.Path(__file__).resolve().parent.parent
IC = REPO / "content/assets/icons"
OUT_HTML = REPO / "content/_board01.html"
OUT = REPO / "content/boards/01-chatgpt-vs-claude.png"

# left = ChatGPT, right = Claude. (label, detail)
GPT = [
    ("Image generation", "posters, mockups, product shots"),
    ("Voice mode", "hands-free, real conversation"),
    ("Live web browsing", "answers with today's data"),
    ("Deep research", "long multi-source reports"),
    ("Computer use", "drives your browser and apps"),
    ("Custom GPTs", "build your own mini assistants"),
    ("Everyday tasks", "the fast, all-purpose default"),
]
CLAUDE = [
    ("Coding", "Claude Code ships multi-file, ~95% accurate"),
    ("Long documents", "200K context, a whole book at once"),
    ("Writing that sounds human", "nuanced tone, fewer hallucinations"),
    ("Artifacts", "build apps and docs inside the chat"),
    ("Careful reasoning", "follows long, complex instructions"),
    ("Projects", "a private knowledge base per client"),
    ("Data analysis", "reads your spreadsheets, finds the pattern"),
]


def svg(name, color=None):
    s = (IC / name).read_text()
    s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
    s = re.sub(r'\swidth="[^"]*"', "", s); s = re.sub(r'\sheight="[^"]*"', "", s)
    return s


def ultron_disc():
    b64 = base64.b64encode((REPO / "content/ultron-logo.png").read_bytes()).decode()
    return f'<img class="uimg" src="data:image/png;base64,{b64}">'


def rows(items, side):
    out = []
    for label, detail in items:
        if label == "__ULTRON__":
            out.append(
                f'<div class="row ult"><div class="mk">{ultron_disc()}</div>'
                f'<div class="rt"><div class="rl">Founder GTM <span class="tag">via Ultron</span></div>'
                f'<div class="rd">{detail}</div></div></div>')
        else:
            out.append(
                f'<div class="row"><div class="mk {side}"></div>'
                f'<div class="rt"><div class="rl">{label}</div>'
                f'<div class="rd">{detail}</div></div></div>')
    return "".join(out)


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--slate:#191919;--card:#201F1E;--ivory:#FAFAF7;--book:#CC785C;--kraft:#D4A27F;
  --cloud:#919180;--ink70:rgba(250,250,247,.72);--ink46:rgba(250,250,247,.46);
  --rule:rgba(250,250,247,.10);}}
*{{margin:0;padding:0;box-sizing:border-box}}
#art{{width:1080px;height:1350px;background:var(--slate);padding:50px 54px 38px;
  display:flex;flex-direction:column;font-family:'DM Sans',sans-serif;position:relative;overflow:hidden}}
#art::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:radial-gradient(rgba(204,120,92,.05) 1.2px,transparent 1.3px);background-size:26px 26px}}
.mast,.body,.verdict,.ftr{{position:relative;z-index:1}}
.mast{{display:flex;justify-content:space-between;align-items:center;
  font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.2em;color:var(--ink46);
  text-transform:uppercase;padding-bottom:16px}}
.mast .s{{color:var(--book)}}
.title{{font-family:'DM Sans',sans-serif;font-weight:900;font-size:72px;letter-spacing:-1.5px;
  color:var(--ivory);line-height:1.0;margin-top:4px}}
.title .c{{color:var(--book)}} .title .v{{color:var(--ink46);font-weight:800}}
.sub{{font-size:22px;font-weight:500;color:var(--ink70);margin-top:12px;letter-spacing:-.2px}}
.body{{flex:1;display:flex;gap:0;margin-top:22px;min-height:0}}
.col{{flex:1;display:flex;flex-direction:column;min-height:0}}
.col.l{{padding-right:30px}} .col.r{{padding-left:30px}}
.chead{{display:flex;align-items:center;gap:11px;padding-bottom:10px;margin-bottom:12px;
  border-bottom:2px solid transparent}}
.chead.l{{border-image:linear-gradient(90deg,var(--cloud),transparent) 1}}
.chead.r{{border-image:linear-gradient(90deg,var(--book),transparent) 1}}
.chead .lg{{width:32px;height:32px;display:inline-flex}}
.chead .lg svg{{width:100%;height:100%}}
.chead.l .lg{{color:var(--ivory)}}
.chead .nm{{font-weight:900;font-size:26px;letter-spacing:-.5px;color:var(--ivory)}}
.chead .bf{{margin-left:auto;font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink46)}}
.rows{{display:flex;flex-direction:column;gap:10px;flex:1;min-height:0}}
.row{{flex:1;display:flex;gap:13px;align-items:center;padding:0 15px;
  background:rgba(250,250,247,.028);border:1px solid var(--rule);border-radius:11px}}
.mk{{width:13px;height:13px;border-radius:50%;flex-shrink:0}}
.mk.l{{background:var(--cloud);box-shadow:0 0 0 4px rgba(145,145,128,.12)}}
.mk.r{{background:var(--book);box-shadow:0 0 0 4px var(--book-lo,rgba(204,120,92,.12))}}
.rl{{font-weight:800;font-size:20.5px;color:var(--ivory);letter-spacing:-.3px;line-height:1.12}}
.rd{{font-size:15px;color:var(--ink70);margin-top:2px;line-height:1.25}}
/* center divider + VS */
.divwrap{{width:0;position:relative}}
.vline{{position:absolute;left:0;top:54px;bottom:0;width:1px;background:var(--rule)}}
.vs{{position:absolute;left:-26px;top:2px;width:52px;height:52px;border-radius:50%;
  background:var(--card);border:1px solid var(--rule);display:flex;align-items:center;
  justify-content:center;font-family:'DM Mono',monospace;font-weight:500;font-size:15px;
  letter-spacing:.05em;color:var(--ivory)}}
/* verdict band */
.verdict{{margin-top:16px;display:flex;align-items:center;gap:16px;
  background:rgba(204,120,92,.08);border:1px solid rgba(204,120,92,.30);
  border-radius:14px;padding:16px 20px}}
.verdict .chip{{flex-shrink:0;font-family:'DM Mono',monospace;font-size:12px;font-weight:500;
  letter-spacing:.14em;text-transform:uppercase;color:#1a0f0a;background:var(--book);
  padding:8px 12px;border-radius:6px}}
.verdict .vt{{font-size:19px;font-weight:600;color:var(--ivory);line-height:1.32;letter-spacing:-.2px}}
.verdict .vt b{{color:var(--book);font-weight:800}}
.ftr{{display:flex;justify-content:space-between;align-items:center;padding-top:16px;
  margin-top:14px;border-top:1px solid var(--rule);
  font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.16em;text-transform:uppercase}}
.ftr .h{{color:var(--ivory)}} .ftr .k{{color:var(--ink46)}}
</style></head>
<body><div id="art">
  <div class="mast"><span>AI STACK <span class="s">/</span> 01</span><span>WHICH TOOL WINS WHICH JOB</span></div>
  <div class="title">ChatGPT <span class="v">vs</span> <span class="c">Claude</span></div>
  <div class="sub">Same 20 dollars a month. Different jobs. Here is who wins each.</div>
  <div class="body">
    <div class="col l">
      <div class="chead l"><span class="lg">{svg('openai.svg')}</span><span class="nm">ChatGPT</span><span class="bf">best for</span></div>
      <div class="rows">{rows(GPT,'l')}</div>
    </div>
    <div class="divwrap"><div class="vline"></div><div class="vs">VS</div></div>
    <div class="col r">
      <div class="chead r"><span class="lg">{svg('claude-color.svg')}</span><span class="nm">Claude</span><span class="bf">best for</span></div>
      <div class="rows">{rows(CLAUDE,'r')}</div>
    </div>
  </div>
  <div class="verdict"><span class="chip">The rule</span>
    <span class="vt">Create and search on <b>ChatGPT</b>. Build and write on <b>Claude</b>. The founders who actually ship keep both and let each do the job it wins.</span></div>
  <div class="ftr"><span class="h">@tiberiu.ai</span><span class="k">save this before you renew either one</span></div>
</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri()); pg.wait_for_timeout(700)
        h = pg.evaluate("()=>document.getElementById('art').scrollHeight")
        pg.locator("#art").screenshot(path=str(OUT))
        b.close()
        print("scrollHeight", h)


if __name__ == "__main__":
    OUT_HTML.write_text(html())
    render()
    print("rendered", OUT.relative_to(REPO))
