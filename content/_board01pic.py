#!/usr/bin/env python3
"""The reveal PICTURE for "people who use ChatGPT vs people who use Claude". 1080x1080, white.

WHY THIS WAS REBUILT. v2 put two ARK panels and eight quotes on a sheet and the operator was
right about it: "de ce plm as salva cacatul asta". Quotes like "write my launch post" are vibes.
They teach nothing, they route nothing, and nobody saves a mood board. CLAUDE.md 34 exists for
exactly this and it was broken twice.

SO THIS IS A ROUTING TABLE, NOT A COMPARISON. Twelve real jobs, each sent to the model that wins
it, each naming the CAPABILITY that decides it. That is the save reason: a founder keeps having
tasks and keeps having to pick. The bottom rule is the thing they actually memorise.

NO IMPORTED GRAPHICS (operator: "nu mai pune nici un element grafic pe el si construieste tu
vizualele si textul"). Every mark here is drawn from type and rules: the numerals carry the
rhythm, the hairlines carry the structure, the accent carries the side. No ARK plate, no icon,
no illustration.

THE HEADER AND FOOTER STAY ("headerul si footerul par ok") - they live in _reveal.py, which puts
"People who use / ChatGPT | Claude" in the band and the follow line in the 108px strip.

FACTS ARE CHECKED, NOT RECALLED (CLAUDE.md 31). The capability names and the 200K context were
verified against the live web this session; nothing here is a number I made up.

    python3 content/_board01pic.py   # -> content/ig/chatgpt-vs-claude/picture.png
"""
import glob, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
DIR = REPO / "content/ig/chatgpt-vs-claude"
OUT_HTML = REPO / "content/_board01pic.html"
OUT = DIR / "picture.png"

SAFE_L, SAFE_R = 70, 950
MID = 510
COL_W = 400

# EVERY ROW CARRIES A DRAWN GLYPH (operator: "am nevoie si de ceva vizual recognoscibil care sa
# te faca sa salvezi"). Icons are what turn a list into a reference card: the eye finds the row
# it needs without reading the others, which is the behaviour a saved cheatsheet gets used for.
# They are drawn here as plain stroked paths, not imported from anywhere.
ICONS = {
    "image":  '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.6"/>'
              '<path d="M20.5 16.5L15 11l-6 6"/>',
    "mic":    '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/>'
              '<path d="M12 18v3"/>',
    "globe":  '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
              '<path d="M12 3c2.6 3 2.6 15 0 18c-2.6-3-2.6-15 0-18z"/>',
    "cursor": '<path d="M5 3l13.5 7.8-5.8 1.4L9.6 18z"/>',
    "bot":    '<rect x="4" y="7" width="16" height="12" rx="3"/><circle cx="9.5" cy="13" r="1.1"/>'
              '<circle cx="14.5" cy="13" r="1.1"/><path d="M12 3.5V7"/>',
    "brief":  '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/>'
              '<path d="M14 3v5h5"/><path d="M8.5 13h7M8.5 17h4.5"/>',
    "table":  '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9.5h18M9.5 9.5V20"/>',
    "stack":  '<rect x="7" y="2.5" width="13" height="16" rx="2"/>'
              '<path d="M3.5 6.5V19a2.5 2.5 0 0 0 2.5 2.5h10.5"/><path d="M10.5 7h6M10.5 11h6"/>',
    "window": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>'
              '<circle cx="6.4" cy="6.5" r=".9"/><path d="M7 13.5h7M7 16.5h4"/>',
    "cube":   '<path d="M12 2.5l8.5 4.8v9.4L12 21.5l-8.5-4.8V7.3z"/>'
              '<path d="M12 12l8.5-4.7M12 12v9.5M12 12L3.5 7.3"/>',
    "pen":    '<path d="M12.5 20.5H21"/>'
              '<path d="M16.6 3.4a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "lock":   '<path d="M3 7.5a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
              '<circle cx="12" cy="14" r="1.9"/><path d="M12 15.9v2.1"/>',
    "check":  '<path d="M9.5 6H20M9.5 12H20M9.5 18H20"/>'
              '<path d="M3 6l1.6 1.6L7.6 4.6M3 12l1.6 1.6L7.6 10.6M3 18l1.6 1.6L7.6 16.6"/>',
    "shield": '<path d="M12 21.5s7.5-3.8 7.5-9.5V5.2L12 2.5 4.5 5.2v6.8c0 5.7 7.5 9.5 7.5 9.5z"/>'
              '<path d="M8.8 12l2.2 2.2 4.2-4.2"/>',
}

# (the job a founder has, the capability that decides it, the glyph)
LEFT = [
    ("An image for the ad", "Claude generates none", "image"),
    ("Hands-free thinking", "voice mode, while you drive", "mic"),
    ("What changed this week", "live web, with sources", "globe"),
    ("Click through a site for you", "computer use", "cursor"),
    ("A reusable team assistant", "a custom GPT", "bot"),
    ("A multi-source brief", "deep research", "brief"),
    ("A photo turned into data", "vision, then a table", "table"),
]
RIGHT = [
    ("A 300-page doc in one go", "200K context, no chunking", "stack"),
    ("A working page in the chat", "Artifacts", "window"),
    ("Your product, actually built", "Claude Code", "cube"),
    ("Copy nobody clocks as AI", "the writing model", "pen"),
    ("One private space per client", "Projects", "lock"),
    ("A 20-step brief, followed", "instruction following", "check"),
    ("A check you can trust", "fewer hallucinations", "shield"),
]

RULE = ("If the output is a picture or a click, send it left. "
        "If it is a document, a build or a decision, send it right.")


def rows(items, side):
    out = []
    for job, why, key in items:
        out.append(
            f'<div class="row"><span class="ic {side}">'
            f'<svg viewBox="0 0 24 24">{ICONS[key]}</svg></span>'
            f'<span class="tx"><span class="job">{job}</span>'
            f'<span class="why">{why}</span></span></div>')
    return "".join(out)


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--ink:#111111;--muted:#77736B;--book:#C84623;--hair:rgba(17,17,17,.11)}}
*{{margin:0;padding:0;box-sizing:border-box}}
#art{{width:1080px;height:1080px;background:#FFFFFF;position:relative;overflow:hidden;
  font-family:'DM Sans',sans-serif}}
.rule{{position:absolute;left:{MID}px;top:26px;bottom:196px;width:1px;background:var(--hair)}}
.col{{position:absolute;top:26px;width:{COL_W}px;bottom:196px;
  display:flex;flex-direction:column}}
.col.l{{left:{SAFE_L}px}} .col.r{{left:{SAFE_R - COL_W}px}}
/* one mono line naming what the column is FOR, so the table is usable without the band */
.cap{{font-family:'DM Mono',monospace;font-size:14px;font-weight:500;letter-spacing:.2em;
  text-transform:uppercase;color:var(--muted);padding-bottom:13px;flex-shrink:0}}
.col.r .cap{{color:var(--book)}}
/* the rows carry the whole picture: numerals for rhythm, hairlines for structure */
.row{{flex:1;display:flex;align-items:center;gap:15px;border-top:1px solid var(--hair)}}
.ic{{flex-shrink:0;width:38px;height:38px;display:flex;align-items:center;justify-content:center}}
.ic svg{{width:34px;height:34px;fill:none;stroke-width:1.7;
  stroke-linecap:round;stroke-linejoin:round}}
.ic.l svg{{stroke:#2B2B29}} .ic.r svg{{stroke:var(--book)}}
/* THE VS, on the rule, between the two columns. It sits in the gutter (470..550) so it never
   touches a row, and its own white ground breaks the hairline instead of crossing it. */
.vs{{position:absolute;left:{MID}px;top:455px;transform:translate(-50%,-50%);
  width:66px;height:66px;border-radius:50%;background:#FFFFFF;
  border:2px solid var(--ink);display:flex;align-items:center;justify-content:center;
  font-family:'DM Mono',monospace;font-size:21px;font-weight:500;letter-spacing:.04em;
  color:var(--ink)}}
.tx{{display:flex;flex-direction:column;gap:3px;min-width:0}}
.job{{font-size:26px;font-weight:800;letter-spacing:-.6px;color:var(--ink);line-height:1.1}}
.why{{font-size:17px;font-weight:500;color:var(--muted);line-height:1.15;letter-spacing:-.1px}}
/* THE TAKEAWAY. The one line a founder can memorise, which is the reason to save the frame. */
.take{{position:absolute;left:{SAFE_L}px;width:{SAFE_R - SAFE_L}px;bottom:34px;
  border:2px solid var(--ink);border-radius:16px;padding:22px 26px;
  display:flex;align-items:center;gap:20px}}
.take .kb{{flex-shrink:0;font-family:'DM Mono',monospace;font-size:13px;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;color:#FFFFFF;background:var(--ink);
  padding:9px 13px;border-radius:7px}}
.take .tt{{font-size:25px;font-weight:700;color:var(--ink);line-height:1.26;letter-spacing:-.5px}}
.take .tt b{{color:var(--book);font-weight:800}}
</style></head>
<body><div id="art">
  <div class="rule"></div>
  <div class="vs">VS</div>
  <div class="col l"><div class="cap">Send it here</div>{rows(LEFT,'l')}</div>
  <div class="col r"><div class="cap">Send it here</div>{rows(RIGHT,'r')}</div>
  <div class="take"><span class="kb">The rule</span>
    <span class="tt">Output is a <b>picture</b> or a <b>click</b>, send it left.
      Output is a <b>document</b>, a <b>build</b> or a <b>decision</b>, send it right.</span></div>
</div></body></html>"""


def render():
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
        pg.goto(OUT_HTML.as_uri()); pg.wait_for_timeout(600)
        bad = pg.evaluate("""([L,R])=>[...document.querySelectorAll('.job,.why,.tt,.cap')]
            .map(e=>{const r=e.getBoundingClientRect();
              return {t:e.textContent.trim().slice(0,20),
                      l:Math.round(r.left),r:Math.round(r.right)};})
            .filter(o=>o.l<L-1||o.r>R+1)""", [SAFE_L, SAFE_R])
        wrap = pg.evaluate("""()=>[...document.querySelectorAll('.job')]
            .filter(e=>e.getBoundingClientRect().height>34).map(e=>e.textContent)""")
        pg.locator("#art").screenshot(path=str(OUT))
        b.close()
    print(f"  outside {SAFE_L}..{SAFE_R}: {bad if bad else 'nothing'}")
    print(f"  wrapped jobs: {wrap if wrap else 'none'}")


if __name__ == "__main__":
    OUT_HTML.write_text(html())
    render()
    print("rendered", OUT.relative_to(REPO))
