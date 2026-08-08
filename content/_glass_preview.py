#!/usr/bin/env python3
"""Preview of the new carousel type: the LEDGER, in glass, black and white.

A different mechanic from every deck shipped so far. Those put one object and one line on a
slide, so slide 4 tells you nothing about slide 6 and no single slide is worth saving. Here
the whole system is on EVERY slide - seven rows, always visible - and the slide expands one
of them. The reader keeps the map while getting the detail, which is what makes a single
screenshot worth keeping, and the collapsed rows are the reason to swipe.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
GL = load("_glass")
LOGO = GL.logo_b64()
W, H = GL.W, GL.H

# Every row carries a HOOK for its own slide, the job, the mechanism, and the artifact it
# actually hands back. Four real things per row, because a panel with a title and one line in
# it is the airy block the operator rejects on sight.
ROWS = [
    ("01", "Nine tabs, or one brief",
     "Research the company before the call",
     "Who they are, who actually signs, and what changed this quarter. Ranked, not listed.",
     "hands back  ->  one page, sources attached"),
    ("02", "Templates with a name in them do not work",
     "Write the first email from what they posted",
     "One specific trigger from something real they said. The ask is a question, not a CTA.",
     "hands back  ->  a draft you would have sent"),
    ("03", "The polite reply is the objection",
     "Answer the objection you would have walked past",
     "The soft line in the reply you read as interest. It is the one that decides the deal.",
     "hands back  ->  the reply, and what it costs to get wrong"),
    ("04", "You were going to sign it anyway",
     "Read the contract before you sign it",
     "It flags what is not standard and drafts the redline in your own words, not boilerplate.",
     "hands back  ->  a redline. You sign, it does not"),
    ("05", "One input, the whole week",
     "Turn one input into the week of posts",
     "In your voice, from your own numbers, formatted per channel and per time zone.",
     "hands back  ->  scheduled, waiting on your approval"),
    ("06", "Most of the bill is the wrong tier",
     "Pick the model the job actually needs",
     "A lookup does not need the expensive one. Hard judgement does. It decides per turn.",
     "hands back  ->  the same answer, for less"),
    ("07", "Quiet is not alive",
     "Tell you which deals are real",
     "Nobody says no any more, they go quiet, and quiet reads as alive on every board.",
     "hands back  ->  a ranked list, and where Monday goes"),
]


def mast(right):
    return (f"<div class='mast'><span class='mono'>ULTRON <em>/</em> AI FOR FOUNDERS</span>"
            f"<span class='mono'>{right}</span></div>")


def foot():
    return (f"<div class='foot'><img src='data:image/png;base64,{LOGO}'>"
            f"<span>51ULTRON<em>.</em>COM</span></div>")


def cover():
    # the whole system is on the cover too, as slivers - the promise is countable at a glance
    slivers = "".join(
        f"<div class='sl g flat'><span class='rn mono'>{n}</span>"
        f"<span class='st'>{job}</span></div>" for n, _, job, _, _ in ROWS)
    return f"""<div class="slide">
  <div class="field"><i class="f1"></i><i class="f2"></i><i class="f3"></i></div>
  <div class="grain"></div>
  <div class="safe">
    {mast("01 / 09")}
    <div class="cv">
      <div class="cv-eye mono">Most founders use Claude like a search engine</div>
      <div class="cv-h disp">7 jobs it<br>should be doing<br><em>instead</em></div>
      <div class="cv-sl">{slivers}</div>
      <div class="g cv-chip"><span class="mono">Swipe</span>
        <span class="cv-chip-b">Comment JOBS and I will send all seven</span></div>
    </div>
    {foot()}
  </div>
</div>"""


def ledger(active: int, idx: str):
    rows = []
    for i, (n, hook, job, body, art) in enumerate(ROWS):
        on = (i == active)
        rows.append(
            f"<div class='row g{' flat' if not on else ''}{' on' if on else ''}'>"
            f"<span class='rn mono'>{n}</span>"
            f"<span class='rt'>{job}</span>"
            + (f"<span class='rb'>{body}</span><span class='ra mono'>{art}</span>" if on else "")
            + "</div>")
    return f"""<div class="slide">
  <div class="field"><i class="f1"></i><i class="f2"></i><i class="f3"></i></div>
  <div class="grain"></div>
  <div class="safe">
    {mast(idx)}
    <div class="lg-h disp">{ROWS[active][1]}</div>
    <div class="lg">{''.join(rows)}</div>
    {foot()}
  </div>
</div>"""


EXTRA = f"""
.cv{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:24px}}
.cv-eye{{font-size:22px;color:var(--ink70);letter-spacing:.13em;line-height:1.4}}
.cv-h{{font-size:94px;color:var(--ink)}}
.cv-h em{{color:var(--acc);font-style:normal}}
.cv-sl{{display:flex;flex-direction:column;gap:7px}}
.sl{{display:grid;grid-template-columns:60px 1fr;align-items:center;
  padding:11px 22px;border-radius:15px}}
.sl .rn{{font-size:18px;color:var(--ink45)}}
.sl .st{{font-size:23px;font-weight:600;color:var(--ink70)}}
.cv-chip{{align-self:stretch;display:flex;align-items:center;gap:18px;
  padding:20px 30px;border-radius:20px}}
.cv-chip .mono{{font-size:19px;color:var(--acc)}}
.cv-chip-b{{font-size:25px;font-weight:700;color:var(--ink)}}

.lg-h{{flex-shrink:0;font-size:54px;margin:22px 0 20px;color:var(--ink)}}
.lg-h em{{color:var(--acc);font-style:normal}}
.lg{{flex:1;min-height:0;display:flex;flex-direction:column;gap:11px}}
.row{{flex:1;display:grid;grid-template-columns:74px 1fr;column-gap:6px;
  align-items:center;align-content:center;padding:14px 26px;border-radius:22px}}
.row .rn{{font-size:21px;color:var(--ink45)}}
.row .rt{{font-size:26px;font-weight:700;color:var(--ink70);line-height:1.24}}
.row.on{{flex:3.1;align-content:center;padding:30px 28px}}
.row.on .rn{{font-size:25px;color:var(--acc)}}
.row.on .rt{{font-size:41px;font-weight:800;color:var(--ink);letter-spacing:-.5px;
  line-height:1.14}}
.row.on .rb{{grid-column:2;font-size:27px;font-weight:500;color:var(--ink70);
  line-height:1.4;margin-top:13px}}
.row.on .ra{{grid-column:2;font-size:19px;letter-spacing:.10em;color:var(--acc);
  margin-top:18px;padding-top:15px;border-top:1px solid var(--rim2)}}
"""

for theme in ("black", "white"):
    body = cover() + ledger(3, "05 / 09")
    html = GL.shell(theme, FONTS, body, f"glass ledger {theme}").replace(
        "</style>", EXTRA + "</style>")
    out = REPO / f"content/glass-ledger-{theme}.html"
    out.write_text(html)
    print(f"{out}  {len(html):,} chars")
