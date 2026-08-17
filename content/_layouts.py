#!/usr/bin/env python3
"""Nine ways to show N tools in a 1080x1080 square, same content in every one.

Operator: "in cate feluri se pot afisa aceste 6-8-10 tool uri intr un cadran de 1080x1080 px?"
We have shipped exactly one shape so far (the vertical list), so this is the catalogue.

The content is held IDENTICAL across all nine so the only variable is the form: eight tools, the
last one locked, real brand marks where the repo has them. Each layout trades three things against
each other, and the trade is what to choose on:

    LOGO SIZE  ...  how recognisable each tool is at thumbnail size
    WORDS      ...  whether a description fits, and how long
    DENSITY    ...  how many tools fit before it stops being readable

    python3 content/_layouts.py            # all nine + a contact sheet
    python3 content/_layouts.py list bento # just those
"""
import base64, glob, pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
IC = REPO / "content/assets/icons"
OUT = REPO / "content/layouts"
S = 1080

MARK = {"Notion": "notion", "Perplexity": "perplexity-color", "Canva": "canva-color",
        "Framer": "framer", "Zapier": "zapier", "Cal.com": "caldotcom", "Suno": "suno",
        "Claude": "claude-color"}

# (name, job, one-line description, price for the receipt layout)
TOOLS = [
    ("Perplexity", "research",  "Answers with sources you can check",      "$0"),
    ("Notion",     "docs",      "One place everything lands",              "$10"),
    ("Canva",      "visuals",   "Every asset, without a designer",         "$0"),
    ("Framer",     "site",      "The site, live the same afternoon",        "$15"),
    ("Zapier",     "plumbing",  "Boring, and it never once broke",          "$0"),
    ("Cal.com",    "booking",   "Books the meeting while you sleep",        "$0"),
    ("Suno",       "audio",     "The sound bed, in a minute",               "$8"),
    ("LOCKED",     "the sixth", "Does four of the seven above, in one seat", "$19"),
]


def _strip_root(s: str) -> str:
    """Drop width/height from the ROOT <svg> tag only.

    Stripping them everywhere also hits inner elements, and a clipPath whose <rect width/height>
    are removed clips its whole graphic away: Canva rendered as a blank tile for exactly this
    reason. Only the outer tag needs it, so only the outer tag is touched.
    """
    m = re.match(r"\s*<svg[^>]*>", s)
    if not m:
        return s
    head = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0))
    return head + s[m.end():]


def svg(name):
    slug = MARK.get(name)
    if not slug or not (IC / f"{slug}.svg").exists():
        return None
    s = (IC / f"{slug}.svg").read_text()
    return _strip_root(re.sub(r"<title>.*?</title>", "", s, flags=re.S))


def tile(name, px, radius=None, lg=None):
    """The mark in its container. One helper so every layout shows the same tool the same way."""
    r = radius if radius is not None else round(px * 0.24)
    inner = round(lg if lg else px * 0.55)
    if name == "LOCKED":
        return (f'<span class="tl lk" style="width:{px}px;height:{px}px;border-radius:{r}px;'
                f'font-size:{round(px*0.42)}px">?</span>')
    s = svg(name)
    if s:
        return (f'<span class="tl" style="width:{px}px;height:{px}px;border-radius:{r}px">'
                f'<span class="lg" style="width:{inner}px;height:{inner}px">{s}</span></span>')
    return (f'<span class="tl mono" style="width:{px}px;height:{px}px;border-radius:{r}px;'
            f'font-size:{round(px*0.40)}px">{name[0]}</span>')


def nm(name):
    return "?????" if name == "LOCKED" else name


CSS = """
:root{--ink:#111;--muted:#77736B;--book:#C84623;--hair:rgba(17,17,17,.11);--tile:#F5F4F1}
*{margin:0;padding:0;box-sizing:border-box}
#art{width:1080px;height:1080px;background:#fff;position:relative;overflow:hidden;
  font-family:'DM Sans',sans-serif;padding:56px 70px}
.tl{background:var(--tile);border:1px solid var(--hair);display:inline-flex;
  align-items:center;justify-content:center;flex-shrink:0;overflow:hidden}
.tl .lg{display:flex;color:#1A1A18}.tl .lg svg{width:100%;height:100%}
.tl.mono{font-weight:800;color:#4A4844}
.tl.lk{background:rgba(200,70,35,.08);border-color:rgba(200,70,35,.30);color:var(--book);
  font-weight:800}
.hd{font-family:'DM Mono',monospace;font-size:14px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--muted);margin-bottom:26px}
.hd b{color:var(--book);font-weight:500}
"""


def L_list():
    rows = "".join(
        f'<div class="r{" lk" if n=="LOCKED" else ""}">{tile(n,62)}'
        f'<span class="t"><span class="n">{nm(n)}</span>'
        f'<span class="d">{d}</span></span></div>' for n, j, d, p in TOOLS)
    return f"""<div class="hd">01 <b>THE LIST</b> · logo, name, one line each</div>
<div class="ls">{rows}</div>""", """
.ls{display:flex;flex-direction:column;height:936px}
.r{flex:1;display:flex;align-items:center;gap:20px;border-top:1px solid var(--hair)}
.r:first-child{border-top:none}
.r.lk{background:rgba(200,70,35,.055);border:1px solid rgba(200,70,35,.28);border-radius:12px;
  padding:0 12px;margin-top:4px}
.n{font-size:28px;font-weight:800;letter-spacing:-.5px;display:block}
.r.lk .n{color:var(--book)}
.d{font-size:17px;color:var(--muted);display:block;margin-top:2px}
"""


def L_grid():
    cells = "".join(
        f'<div class="c{" lk" if n=="LOCKED" else ""}">{tile(n,60)}'
        f'<span class="n">{nm(n)}</span><span class="d">{d}</span></div>'
        for n, j, d, p in TOOLS)
    return f"""<div class="hd">02 <b>TWO COLUMNS</b> · half the width, same words</div>
<div class="gr">{cells}</div>""", """
.gr{display:grid;grid-template-columns:1fr 1fr;gap:16px;height:936px}
.c{border:1px solid var(--hair);border-radius:16px;padding:20px;display:flex;
  flex-direction:column;gap:8px;justify-content:center}
.c.lk{background:rgba(200,70,35,.055);border-color:rgba(200,70,35,.28)}
.n{font-size:26px;font-weight:800;letter-spacing:-.5px}
.c.lk .n{color:var(--book)}
.d{font-size:16px;color:var(--muted);line-height:1.25}
"""


def L_wall():
    cells = "".join(f'<div class="c">{tile(n,132)}<span class="n">{nm(n)}</span></div>'
                    for n, j, d, p in TOOLS)
    return f"""<div class="hd">03 <b>THE ICON WALL</b> · biggest logos, no descriptions</div>
<div class="wl">{cells}</div>""", """
.wl{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;height:936px;
  align-content:center;justify-items:center}
.c{display:flex;flex-direction:column;align-items:center;gap:14px}
.n{font-size:25px;font-weight:800;letter-spacing:-.4px}
"""


def L_rank():
    rows = "".join(
        f'<div class="r{" lk" if n=="LOCKED" else ""}"><span class="num">{i:02d}</span>'
        f'{tile(n,54)}<span class="t"><span class="n">{nm(n)}</span>'
        f'<span class="d">{d}</span></span></div>'
        for i, (n, j, d, p) in enumerate(TOOLS, 1))
    return f"""<div class="hd">04 <b>THE RANKING</b> · numerals carry the order</div>
<div class="rk">{rows}</div>""", """
.rk{display:flex;flex-direction:column;height:936px}
.r{flex:1;display:flex;align-items:center;gap:18px;border-top:1px solid var(--hair)}
.r:first-child{border-top:none}
.num{font-family:'DM Mono',monospace;font-size:34px;font-weight:500;color:#D8D4CE;width:62px}
.r.lk .num{color:var(--book)}
.n{font-size:27px;font-weight:800;letter-spacing:-.5px;display:block}
.r.lk .n{color:var(--book)}
.d{font-size:16.5px;color:var(--muted);display:block;margin-top:2px}
"""


def L_bento():
    hero = TOOLS[-1]
    small = "".join(f'<div class="s">{tile(n,50)}<span class="n">{nm(n)}</span></div>'
                    for n, j, d, p in TOOLS[:-1])
    return f"""<div class="hd">05 <b>BENTO</b> · one hero, the rest as supporting cast</div>
<div class="bn"><div class="hero">{tile(hero[0],104)}
  <span class="hn">{nm(hero[0])}</span><span class="hd2">{hero[2]}</span></div>
  <div class="rest">{small}</div></div>""", """
.bn{display:flex;flex-direction:column;gap:16px;height:936px}
.hero{flex:0 0 300px;background:rgba(200,70,35,.06);border:1px solid rgba(200,70,35,.30);
  border-radius:22px;display:flex;flex-direction:column;justify-content:center;gap:14px;
  padding:0 34px}
.hn{font-size:44px;font-weight:800;letter-spacing:-1px;color:var(--book)}
.hd2{font-size:22px;color:#7A5245;font-weight:600}
.rest{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.s{border:1px solid var(--hair);border-radius:14px;display:flex;align-items:center;gap:14px;
  padding:0 18px}
.n{font-size:24px;font-weight:800;letter-spacing:-.4px}
"""


def L_radial():
    import math
    n = len(TOOLS)
    items = []
    for i, (name, j, d, p) in enumerate(TOOLS):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = 380 + 322 * math.cos(a), 380 + 322 * math.sin(a)
        items.append(f'<div class="o" style="left:{x:.0f}px;top:{y:.0f}px">{tile(name,86)}'
                     f'<span class="n">{nm(name)}</span></div>')
    return f"""<div class="hd">06 <b>RADIAL</b> · the ring, for "everything orbits one thing"</div>
<div class="rd"><div class="core">YOU</div>{"".join(items)}</div>""", """
.rd{position:relative;width:760px;height:760px;margin:14px auto 0}
.core{position:absolute;left:380px;top:380px;transform:translate(-50%,-50%);
  width:150px;height:150px;border-radius:50%;background:var(--ink);color:#fff;
  display:flex;align-items:center;justify-content:center;
  font-family:'DM Mono',monospace;font-size:19px;letter-spacing:.16em}
.o{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;
  align-items:center;gap:7px;width:170px}
.o .tl{border-radius:22px}
.n{font-size:19px;font-weight:800;letter-spacing:-.3px;text-align:center}
"""


def L_receipt():
    rows = "".join(
        f'<div class="r{" lk" if n=="LOCKED" else ""}">{tile(n,38,10)}'
        f'<span class="n">{nm(n)}</span><span class="j">{j}</span>'
        f'<span class="p">{p}</span></div>' for n, j, d, p in TOOLS)
    total = sum(int(p.strip("$")) for _, _, _, p in TOOLS)
    return f"""<div class="hd">07 <b>THE RECEIPT</b> · the money angle, itemised</div>
<div class="rc">{rows}<div class="tot"><span>TOTAL, PER MONTH</span><span>${total}</span></div>
</div>""", """
.rc{border:2px solid var(--ink);border-radius:16px;padding:26px 30px;height:900px;
  display:flex;flex-direction:column}
.r{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1px dashed var(--hair)}
.n{font-size:25px;font-weight:800;letter-spacing:-.4px;flex:1}
.r.lk .n{color:var(--book)}
.j{font-family:'DM Mono',monospace;font-size:14px;color:var(--muted);letter-spacing:.1em;
  text-transform:uppercase}
.p{font-family:'DM Mono',monospace;font-size:24px;font-weight:500;width:96px;text-align:right}
.tot{display:flex;justify-content:space-between;align-items:center;padding-top:22px;
  font-family:'DM Mono',monospace;font-size:23px;letter-spacing:.1em;font-weight:500}
.tot span:last-child{color:var(--book);font-size:34px}
"""


def L_phone():
    cells = "".join(f'<div class="a">{tile(n,148,34)}<span class="n">{nm(n)}</span></div>'
                    for n, j, d, p in TOOLS)
    return f"""<div class="hd">08 <b>HOME SCREEN</b> · reads as a phone, instantly familiar</div>
<div class="ph"><div class="scr">{cells}</div></div>""", """
.ph{display:flex;justify-content:center}
.scr{width:820px;height:880px;border-radius:52px;background:#F0EEE9;
  border:1px solid var(--hair);padding:56px 44px;
  display:grid;grid-template-columns:repeat(3,1fr);gap:34px 30px;align-content:start;
  justify-items:center}
.a{display:flex;flex-direction:column;align-items:center;gap:11px}
.a .tl{background:#fff}
.n{font-size:20px;font-weight:700;letter-spacing:-.3px}
"""


def L_pipe():
    steps = "".join(
        f'<div class="st{" lk" if n=="LOCKED" else ""}">{tile(n,52)}'
        f'<span class="n">{nm(n)}</span><span class="j">{j}</span></div>'
        f'{"" if i == len(TOOLS)-1 else "<span class=ar>&rarr;</span>"}'
        for i, (n, j, d, p) in enumerate(TOOLS))
    return f"""<div class="hd">09 <b>THE PIPELINE</b> · order matters, each hands to the next</div>
<div class="pp">{steps}</div>""", """
.pp{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:26px 14px;
  height:936px;align-content:space-evenly}
.st{display:flex;align-items:center;gap:13px;border:1px solid var(--hair);border-radius:16px;
  padding:20px 22px}
.st.lk{background:rgba(200,70,35,.06);border-color:rgba(200,70,35,.30)}
.n{font-size:27px;font-weight:800;letter-spacing:-.4px}
.st.lk .n{color:var(--book)}
.j{font-family:'DM Mono',monospace;font-size:13px;color:var(--muted);letter-spacing:.1em;
  text-transform:uppercase}
.ar{font-size:30px;color:#CFCBC4}
"""


LAYOUTS = {"list": L_list, "grid": L_grid, "wall": L_wall, "rank": L_rank, "bento": L_bento,
           "radial": L_radial, "receipt": L_receipt, "phone": L_phone, "pipe": L_pipe}


def build(key, pg):
    body, css = LAYOUTS[key]()
    html = (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="assets/fonts.css"><style>{CSS}{css}</style></head>'
            f'<body><div id="art">{body}</div></body></html>')
    p = REPO / f"content/_layout-{key}.html"; p.write_text(html)
    pg.goto(p.as_uri()); pg.wait_for_timeout(320)
    out = OUT / f"{list(LAYOUTS).index(key)+1:02d}-{key}.png"
    pg.locator("#art").screenshot(path=str(out))
    return out


if __name__ == "__main__":
    keys = sys.argv[1:] or list(LAYOUTS)
    OUT.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    made = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": S, "height": S}, device_scale_factor=1)
        for k in keys:
            made.append(build(k, pg)); print(" ", made[-1].name)
        b.close()
    if len(made) > 3:                       # a contact sheet so nine can be compared at once
        from PIL import Image
        cell, gap = 350, 10
        sheet = Image.new("RGB", (cell*3 + gap*4, cell*3 + gap*4), (232, 230, 226))
        for i, f in enumerate(made[:9]):
            im = Image.open(f).resize((cell, cell))
            sheet.paste(im, (gap + (i % 3)*(cell+gap), gap + (i//3)*(cell+gap)))
        sheet.save(OUT / "00-contact-sheet.png")
        print("  00-contact-sheet.png")
