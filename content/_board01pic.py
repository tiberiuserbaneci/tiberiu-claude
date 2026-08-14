#!/usr/bin/env python3
"""Composite the reveal PICTURE for "people who use ChatGPT vs people who use Claude".

1080x1080 EXACTLY (operator: "designul tb sa fie 1080x1080px tu adaugi restul pentru format 3:4").
FLAT WHITE, ONE COLOUR ("backgroundul tb sa fie intr o singura culoare alb"): #FFFFFF everywhere,
no cream, no dot grid, no card fills. The ARK crops are lifted to pure white so they leave no
visible rectangle on it (see the .prop filter).

WHAT IS ON IT. Two columns of things a FOUNDER actually types, as quotes, because a quote is a
person and a feature label is a spec sheet (operator: "featurerurile sunt slabe de cacat nu fac
scroll stop"). The split is surface vs depth, both sides competent: ChatGPT makes the go-to-market
surface, Claude does the deep work on the business itself.

ON ICP, NOT ON ENGINEERS. Operator: "noua ne trebuie alte use caseuri virale cu care sa atinga
ICP ul nostru", and CLAUDE.md 30 bans dev internals outright ("nu mai pune linii de cod ... te
indepartezi de ICP"). So the right column is NOT refactor / open the PR / fix the test: it is the
founder-facing depth - every support ticket, a call turned into a proposal, the client portal.

WHERE THE PARTS COME FROM (operator's pick): the compose bars are HTML mockups so the typed text
is exact and legible, the two props are cropped out of the ARK plate (byteplus-prompt.md) which is
already pure white and on palette, and the logos are the real SVGs in content/assets/icons.

MARGINS ("atentie la margini"): the card is full bleed, so the frame's rails are the card's rails.
Everything lives inside 70..950 and the render asserts it rather than trusting the layout.

    python3 content/_board01pic.py   # -> content/ig/chatgpt-vs-claude/picture.png
"""
import base64, glob, pathlib, re

REPO = pathlib.Path(__file__).resolve().parent.parent
IC = REPO / "content/assets/icons"
DIR = REPO / "content/ig/chatgpt-vs-claude"
RAW = DIR / "picture-raw.jpg"
OUT_HTML = REPO / "content/_board01pic.html"
OUT = DIR / "picture.png"

SAFE_L, SAFE_R = 70, 950
MID = 510                                  # optical centre of the safe box, where the rule sits
COL_W = 400                                # 70..470 and 550..950, symmetric about MID

# the two props, measured off the 2048px ARK plate
SRC = 2048
LEFT_CROP = (198, 601, 899, 1498)          # the calm light chat panel
RIGHT_CROP = (1166, 601, 1890, 1498)       # the dark working panel with the rising arrow

# what a founder types. One line each, short enough to stay on one line at 38px.
LEFT_COMPOSE = "name my SaaS"
LEFT_QUOTES = ["write my launch post", "make the hero image", "10 subject lines",
               "fix my cold email"]
RIGHT_COMPOSE = "read all my tickets"
RIGHT_QUOTES = ["write the proposal", "build the client portal", "audit my onboarding",
                "summarise the call"]


def svg(name):
    s = (IC / name).read_text()
    s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
    s = re.sub(r'\swidth="[^"]*"', "", s)
    return re.sub(r'\sheight="[^"]*"', "", s)


def prop(crop, w):
    """One ARK panel, cropped out of the plate and scaled to w."""
    x0, y0, x1, y1 = crop
    k = w / (x1 - x0)
    return (f'<div class="prop" style="width:{w}px;height:{round((y1 - y0) * k)}px">'
            f'<img src="{PLATE_URI}" style="width:{round(SRC * k)}px;'
            f'left:-{round(x0 * k)}px;top:-{round(y0 * k)}px"></div>')


def quotes(items, side):
    return "".join(f'<div class="q {side}">&ldquo;{t}&rdquo;</div>' for t in items)


def compose(text, side):
    """A compose bar mockup. Ours, drawn here, not a screenshot of anybody's product."""
    send = ('<span class="send r"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
            'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M12 19V5M5 12l7-7 7 7"/></svg></span>')
    chip = '<span class="chip">Opus 5</span>' if side == "r" else ""
    return (f'<div class="cmp"><span class="plus">+</span>'
            f'<span class="cmp-t">{text}</span>{chip}{send}</div>')


PLATE_URI = "data:image/jpeg;base64," + base64.b64encode(RAW.read_bytes()).decode()


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--ink:#111111;--muted:#6E6A61;--book:#C84623;--bar:#2A2A28;--hair:rgba(17,17,17,.13)}}
*{{margin:0;padding:0;box-sizing:border-box}}
#art{{width:1080px;height:1080px;background:#FFFFFF;position:relative;overflow:hidden;
  font-family:'DM Sans',sans-serif}}
.rule{{position:absolute;left:{MID}px;top:34px;bottom:34px;width:1px;background:var(--hair)}}
.col{{position:absolute;top:34px;bottom:34px;width:{COL_W}px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:19px}}
.col.l{{left:{SAFE_L}px}} .col.r{{left:{SAFE_R - COL_W}px}}
/* the head: the real logo and the model name, small, so the column is anchored */
.hd{{display:flex;align-items:center;gap:10px;height:38px}}
.hd .lg{{width:30px;height:30px;display:inline-flex}}
.hd .lg svg{{width:100%;height:100%}}
.hd.l .lg{{color:var(--ink)}}
.hd .nm{{font-weight:900;font-size:25px;letter-spacing:-.5px;color:var(--ink)}}
/* the compose bar mockup */
.cmp{{width:100%;height:82px;border-radius:22px;background:var(--bar);
  display:flex;align-items:center;gap:11px;padding:0 12px 0 18px;
  box-shadow:0 6px 18px rgba(17,17,17,.13)}}
.plus{{color:rgba(255,255,255,.5);font-size:25px;font-weight:400;line-height:1;flex-shrink:0}}
.cmp-t{{flex:1;color:#FAFAF7;font-size:22px;font-weight:500;letter-spacing:-.3px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.chip{{flex-shrink:0;font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.06em;
  color:rgba(250,250,247,.72);background:rgba(250,250,247,.11);
  padding:6px 10px;border-radius:8px}}
.send{{flex-shrink:0;width:42px;height:42px;border-radius:50%;display:flex;
  align-items:center;justify-content:center}}
.send svg{{width:21px;height:21px}}
.col.l .send{{background:#4A4A46}}
.col.r .send{{background:var(--book)}}
/* the quotes: what the person actually types */
.q{{width:100%;font-size:33px;font-weight:800;letter-spacing:-1px;line-height:1.14;
  color:var(--ink);text-align:center;white-space:nowrap}}
.q.r{{color:var(--ink)}}
/* the prop, cropped out of the ARK plate */
.prop{{position:relative;overflow:hidden;flex-shrink:0}}
/* THE PLATE'S PAPER IS 254, THE CANVAS IS 255, AND THAT 1 LEVEL IS A VISIBLE RECTANGLE.
   Measured, not guessed: the crop's paper reads (254,254,254) everywhere except where the
   object's own shadow falls. Lifting the crop by 0.6% clips its paper to pure white and leaves
   the dark panel (26) and the real shadows where they are, so the prop sits on the sheet with
   no edge instead of in a faintly tinted box. */
.prop img{{position:absolute;display:block;filter:brightness(1.006)}}
.spacer{{flex:1;min-height:0}}
</style></head>
<body><div id="art">
  <div class="rule"></div>
  <div class="col l">
    {compose(LEFT_COMPOSE, 'l')}
    <div class="q l">&ldquo;{LEFT_QUOTES[0]}&rdquo;</div>
    {prop(LEFT_CROP, COL_W)}
    {quotes(LEFT_QUOTES[1:], 'l')}
  </div>
  <div class="col r">
    {compose(RIGHT_COMPOSE, 'r')}
    <div class="q r">&ldquo;{RIGHT_QUOTES[0]}&rdquo;</div>
    {prop(RIGHT_CROP, COL_W)}
    {quotes(RIGHT_QUOTES[1:], 'r')}
  </div>
</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri()); pg.wait_for_timeout(700)
        bad = pg.evaluate("""([L,R])=>[...document.querySelectorAll('.q,.cmp,.hd,.prop')]
            .map(e=>{const r=e.getBoundingClientRect();
              return {t:(e.textContent||'prop').trim().slice(0,22),
                      l:Math.round(r.left),r:Math.round(r.right)};})
            .filter(o=>o.l<L-1||o.r>R+1)""", [SAFE_L, SAFE_R])
        wrapped = pg.evaluate("""()=>[...document.querySelectorAll('.q')]
            .filter(e=>e.getBoundingClientRect().height>52)
            .map(e=>e.textContent.trim())""")
        pg.locator("#art").screenshot(path=str(OUT))
        b.close()
    print(f"  outside {SAFE_L}..{SAFE_R}: {bad if bad else 'nothing'}")
    print(f"  wrapped quotes: {wrapped if wrapped else 'none'}")


if __name__ == "__main__":
    OUT_HTML.write_text(html())
    render()
    print("rendered", OUT.relative_to(REPO))
