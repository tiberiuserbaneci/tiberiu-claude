#!/usr/bin/env python3
"""The nine layouts, each built into the operator's 4:5 reveal frame.

Frame taken verbatim off the attached reveal.html and NOT re-derived. Every number below is
his, including the ones I would have chosen differently:

    1080 x 1350                    total, 4:5
      0    - 180    BAND      dark gradient #1c1c1c to #2b2b2b, hook 42/800 x2 + sub 29/700
      180  + 3px    EDGE      #111
      180  - 1350   PICTURE   1170 tall, the layout lives here
      1180          CTA PILL  floats on the picture, white glass, 27/700, keyword in #EA580C
      veil over the PICTURE only, 0.982 to 0, 4.2s linear, band never dims
      FILM-META duration 7.0, fps 30

The picture is where the reference has a photograph and we have a tool stack instead. Ground is
the reference's own #f6f8fc, so a black brand mark reads and a white one does not: the mark
resolver below picks the variant by the measured luminance in logos.json rather than by name.

The layout SHAPES come from content/_layouts.py, imported rather than copied, so the catalogue
and the materials cannot drift apart. Two adjustments are made to each:
  - the catalogue header (01 THE LIST, etc) is stripped; it labels a specimen, not a material
  - the body height is rescaled from the square's 936 to this frame's 920, which is what is
    left of 1170 after 56 top and 194 bottom, the bottom being the clearance for the CTA pill

    python3 content/_reveal9.py                  # all nine
    python3 content/_reveal9.py list phone       # just those
    python3 content/_reveal9.py --follow         # reference footer instead of the comment CTA
    python3 content/_reveal9.py --shots          # also render a still of each
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "content/ig/reveal9"
LOGOS = REPO / "content/assets/logos/logos.json"

W, H = 1080, 1350
BAND_H, EDGE_H, PIC_H = 180, 3, 1170
PIC_TOP = BAND_H
CTA_TOP = 1180
PAD_TOP, PAD_BOT, PAD_X = 56, 194, 70
BODY_H = PIC_H - PAD_TOP - PAD_BOT          # 920
DUR, FPS, VEIL, ALPHA0 = 7.0, 30, 4.2, 0.982

# (name, job, one line, price). Every tool appears in exactly one material: the audience is on
# Instagram and a repeated stack is what makes a set skippable (CLAUDE.md 30). Only the hidden
# row repeats. Claude, ChatGPT and Gemini are three posts apart for the same reason.
SPECS: dict[str, dict] = {
    "list": {
        "l1": "7 TOOLS THAT KEEP", "l2": "YOUR WEEK MOVING",
        "sub": "(they carry the days you cannot)", "kw": "WEEK",
        "tools": [
            ("Claude", "thinking", "First draft of anything, in your voice", "$0"),
            ("Notion", "the desk", "One page where the week actually lives", "$10"),
            ("Linear", "the work", "What is next, without asking anyone", "$8"),
            ("Cal.com", "the diary", "Books the call while you are asleep", "$0"),
            ("Loom", "the update", "Three minutes of video beats a meeting", "$0"),
            ("Slack", "the noise", "Kept in one room, out of your head", "$0"),
            ("Zapier", "the glue", "The handoffs nobody has to remember", "$20"),
            ("LOCKED", "the eighth", "Runs the six above from one place", "$19"),
        ]},
    "grid": {
        "l1": "8 APPS THAT REPLACED", "l2": "MY WHOLE STACK",
        "sub": "(you can cancel the rest tonight)", "kw": "STACK",
        "tools": [
            ("Perplexity", "research", "Answers you can check the source of", "$0"),
            ("Figma", "design", "The screen before anyone builds it", "$0"),
            ("Canva", "posts", "Every asset, without a designer", "$0"),
            ("Webflow", "the site", "Live the same afternoon you wrote it", "$14"),
            ("Stripe", "getting paid", "The only invoice you have to send", "$0"),
            ("Ramp", "spending", "Every card, one screen, no receipts lost", "$0"),
            ("Gmail", "the inbox", "Where the day arrives whether you like it", "$0"),
            ("LOCKED", "the eighth", "Does the four above talk to each other", "$19"),
        ]},
    "wall": {
        "l1": "THE 9 AI MODELS", "l2": "I ACTUALLY OPEN",
        "sub": "(everything else I could delete today)", "kw": "MODELS",
        "tools": [
            ("Grok", "fast takes", "Reads the room in real time", "$0"),
            ("DeepSeek", "cheap reasoning", "Costs almost nothing to think out loud", "$0"),
            ("Mistral", "in Europe", "Runs where the data has to stay", "$0"),
            ("Qwen", "long context", "Eats a whole quarter of documents", "$0"),
            ("Llama", "on my laptop", "No bill and nothing leaves the machine", "$0"),
            ("Kimi", "the long read", "Finishes a book and answers about it", "$0"),
            ("Manus", "does the task", "Goes and does it instead of describing it", "$0"),
            ("Copilot", "in the editor", "Finishes the line before you type it", "$10"),
            ("Cohere", "for retrieval", "Finds the one paragraph that matters", "$0"),
            ("LOCKED", "the tenth", "Picks which of these nine gets the job", "$19"),
        ]},
    "rank": {
        "l1": "I RANKED THE 10 AI", "l2": "TOOLS I PAY FOR",
        "sub": "(number three is the one nobody expects)", "kw": "RANKED",
        "tools": [
            ("ChatGPT", "01", "The one I open before the coffee", "$20"),
            ("Midjourney", "02", "Pictures nobody can tell I did not shoot", "$10"),
            ("ElevenLabs", "03", "My own voice, on days I have no time", "$5"),
            ("Descript", "04", "Cuts the video by editing the words", "$12"),
            ("Raycast", "05", "Every app is two keys away now", "$0"),
            ("Obsidian", "06", "Notes that are still mine in ten years", "$0"),
            ("Airtable", "07", "The spreadsheet that grew up", "$20"),
            ("HubSpot", "08", "Remembers the deals I would forget", "$0"),
            ("Miro", "09", "Where the messy thinking is allowed", "$0"),
            ("Todoist", "10", "The list that survives a bad week", "$4"),
            ("LOCKED", "00", "Ranks these ten for the job in front of you", "$19"),
        ]},
    "bento": {
        "l1": "7 APPS AND ONE", "l2": "I WILL NOT NAME",
        "sub": "(the unnamed one does half the work)", "kw": "EIGHTH",
        "tools": [
            ("Cursor", "writing code", "Writes the boring 80 percent", "$20"),
            ("Replit", "trying things", "An idea running before lunch", "$0"),
            ("Vercel", "shipping", "Live in the time a deploy used to take", "$0"),
            ("Supabase", "the data", "A real database without a database person", "$0"),
            ("GitHub", "the history", "Every version of every mistake", "$0"),
            ("Sentry", "what broke", "Tells me before the customer does", "$0"),
            ("PostHog", "what they did", "The truth about how it is used", "$0"),
            ("LOCKED", "the eighth", "The one that decides what to build next", "$19"),
        ]},
    "radial": {
        "l1": "THIS IS WHAT ONE", "l2": "FOUNDER LOOKS LIKE NOW",
        "sub": "(eight apps and nobody else in the building)", "kw": "SOLO",
        "tools": [
            ("Gemini", "asks", "Reads what I never had time to read", "$0"),
            ("Excalidraw", "thinks", "The napkin that does not get thrown out", "$0"),
            ("Recraft", "draws", "Brand assets that match each other", "$0"),
            ("Lovable", "builds", "A working page from a sentence", "$0"),
            ("Typeform", "listens", "Asks the market instead of guessing", "$0"),
            ("Intercom", "answers", "Handles the questions I have answered before", "$0"),
            ("Xero", "books", "The month closes without me", "$15"),
            ("Amplitude", "measures", "Which of this actually moved anything", "$0"),
            ("LOCKED", "runs it", "Sits in the middle and hands off the work", "$19"),
        ]},
    "receipt": {
        "l1": "MY WHOLE COMPANY COSTS", "l2": "LESS THAN ONE HIRE",
        "sub": "(here is the itemised bill)", "kw": "BILL",
        "tools": [
            ("Substack", "the audience", "Where the writing lands", "$0"),
            ("Plausible", "the numbers", "Traffic without the creepy part", "$9"),
            ("Framer", "the site", "Redesigned on a Sunday", "$5"),
            ("Brex", "the card", "Spend that shows up categorised", "$0"),
            ("QuickBooks", "the books", "So the accountant stops calling", "$30"),
            ("Mixpanel", "the funnel", "Where people quietly give up", "$0"),
            ("Calendly", "the calls", "No more what time works for you", "$0"),
            ("CapCut", "the video", "Cut on a phone in a car park", "$0"),
            ("LOCKED", "the last line", "Replaces four rows above it", "$19"),
        ]},
    "phone": {
        "l1": "MY PHONE RUNS", "l2": "A WHOLE COMPANY",
        "sub": "(nine apps, no staff, no office)", "kw": "PHONE",
        "tools": [
            ("Instagram", "reach", "Where strangers meet the work", "$0"),
            ("TikTok", "reach", "The one that still surprises me", "$0"),
            ("YouTube", "depth", "For the people who want the long version", "$0"),
            ("LinkedIn", "buyers", "Where the money actually reads", "$0"),
            ("X", "signal", "What is happening before it is news", "$0"),
            ("Reddit", "truth", "What people say when no brand is watching", "$0"),
            ("Discord", "the room", "The hundred who care most", "$0"),
            ("WhatsApp", "the deal", "Where it closes, every time", "$0"),
            ("Telegram", "the crew", "The three people I actually build with", "$0"),
            ("LOCKED", "the tenth", "Posts to all nine and reads back what worked", "$19"),
        ]},
    "pipe": {
        "l1": "ONE LEAD, EIGHT APPS", "l2": "AND ZERO ME",
        "sub": "(each one hands the work to the next)", "kw": "CHAIN",
        "tools": [
            ("Outlook", "it lands", "A stranger asks a question", "$0"),
            ("Make", "it routes", "Nobody has to notice it arrived", "$9"),
            ("Salesforce", "it is logged", "The record writes itself", "$25"),
            ("NotebookLM", "it is briefed", "Everything we know, on one page", "$0"),
            ("Resend", "it replies", "In four minutes, not four days", "$0"),
            ("Twilio", "it follows up", "A text, because email is a graveyard", "$0"),
            ("Zoom", "it meets", "The only part I show up for", "$0"),
            ("Trello", "it moves", "Nothing sits still without someone noticing", "$0"),
            ("LOCKED", "it closes", "The eight above, without the wiring", "$19"),
        ]},
}


def marks() -> dict:
    """Tool name to icon filename, decided by the MEASURED luminance, not by the name.

    The picture ground is #f6f8fc. A near white mark disappears on it exactly the way a near
    black one disappears on the slate card, so the colour variant is used unless it is too
    light, and then the monochrome one is, which inherits the dark ink colour.
    """
    if not LOGOS.exists():
        return {}
    doc = json.loads(LOGOS.read_text())["tools"]
    out = {}
    for name, e in doc.items():
        if e.get("color") and (e.get("lum") or 0) < 0.82:
            out[name] = e["color"][:-4]
        elif e.get("mono"):
            out[name] = e["mono"][:-4]
    return out


def layouts_module():
    spec = importlib.util.spec_from_file_location("lay", REPO / "content/_layouts.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def fonts() -> str:
    p = REPO / "content/assets/fonts.css"
    return p.read_text() if p.exists() else ""


def frame(key: str, body: str, css: str, follow: bool) -> str:
    s = SPECS[key]
    cta = (f'Follow <span class="kw">@tiberiu.ai</span> for daily AI stacks' if follow else
           f'Comment <span class="kw">{s["kw"]}</span> for the full stack')
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>reveal {key} 4:5 {W}x{H}</title>
<style>
/* FILM-META {{"duration":{DUR},"w":{W},"h":{H},"fps":{FPS},"beats":[]}} */
{fonts()}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
body {{ background: #000; display: flex; justify-content: center;
  font-family: 'DM Sans', sans-serif; }}
#film {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #000 }}
.card {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; z-index: 1 }}

.band {{
  position: absolute; left: 0; top: 0; width: {W}px; height: {BAND_H}px;
  background: linear-gradient(to bottom, #1c1c1c, #2b2b2b); z-index: 5;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px;
}}
.band .l1, .band .l2 {{ font-weight: 800; font-size: 42px; line-height: 1.08;
  letter-spacing: -0.9px; color: #FFFFFF; white-space: nowrap }}
.band .sub {{ font-weight: 700; font-size: 29px; line-height: 1.15; letter-spacing: -0.4px;
  color: #FFFFFF; margin-top: 5px; white-space: nowrap }}

.edge {{ position: absolute; left: 0; right: 0; top: {BAND_H}px; height: {EDGE_H}px;
  background: #111; z-index: 6; pointer-events: none }}
.pic {{ position: absolute; left: 0; top: {PIC_TOP}px; width: {W}px; height: {PIC_H}px;
  background: #f6f8fc; z-index: 1; overflow: hidden }}

.cta-btn {{
  position: absolute; left: 50%; transform: translateX(-50%); top: {CTA_TOP}px;
  background: rgba(255,255,255,0.90);
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  border: 2px solid #FFFFFF;
  box-shadow: 0 12px 28px rgba(15,23,42,0.14), 0 4px 10px rgba(15,23,42,0.08),
    inset 0 1px 1px rgba(255,255,255,0.95);
  border-radius: 999px; padding: 15px 42px;
  display: flex; align-items: center; justify-content: center; z-index: 3;
}}
.cta-btn .txt {{ font-weight: 700; font-size: 27px; line-height: 1; color: #0F172A;
  letter-spacing: -0.3px; white-space: nowrap }}
.cta-btn .kw {{ color: #EA580C; font-weight: 800; margin: 0 6px }}

.veil {{ position: absolute; left: 0; top: {PIC_TOP}px; width: {W}px; height: {PIC_H}px;
  background: #000; opacity: {ALPHA0}; z-index: 4; pointer-events: none;
  animation: up {VEIL}s linear forwards 0s }}
@keyframes up {{ from {{ opacity: {ALPHA0} }} to {{ opacity: 0 }} }}

/* the layout, in the picture */
#art {{ width: {W}px; height: {PIC_H}px; background: #f6f8fc; position: relative;
  overflow: hidden; padding: {PAD_TOP}px {PAD_X}px {PAD_BOT}px }}
{css}
</style></head>
<body>
<div id="film">
  <div class="card">
    <div class="band">
      <span class="l1">{s['l1']}</span>
      <span class="l2">{s['l2']}</span>
      <span class="sub">{s['sub']}</span>
    </div>
    <div class="edge"></div>
    <div class="pic"><div id="art">{body}</div></div>
    <div class="cta-btn"><span class="txt">{cta}</span></div>
    <div class="veil"></div>
  </div>
</div>
</body></html>
"""


def radial_material(L):
    """The ring, with the hidden tool in the CORE instead of a ninth seat on the circle.

    The catalogue version spreads all N evenly and puts the word YOU in the middle, which is
    right for a specimen where every item is equal. In the material it is wrong twice: nine
    items do not divide a circle the way eight do, so the ring came out visibly uneven, and the
    hidden tool is the whole point of the picture, sitting in the one position that says so.
    Overridden here rather than in _layouts.py, because the catalogue is not wrong, it is
    answering a different question.
    """
    import math

    ring = [t for t in L.TOOLS if t[0] != "LOCKED"]
    core = next((t for t in L.TOOLS if t[0] == "LOCKED"), None)
    n = len(ring)
    items = []
    for i, (name, j, d, p) in enumerate(ring):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = 380 + 320 * math.cos(a), 380 + 320 * math.sin(a)
        items.append(f'<div class="o" style="left:{x:.0f}px;top:{y:.0f}px">{L.tile(name, 96)}'
                     f'<span class="n">{name}</span><span class="j">{j}</span></div>')
    mid = (f'<div class="core"><span class="q">?</span>'
           f'<span class="cn">?????</span><span class="cj">{core[1]}</span></div>'
           if core else '<div class="core"><span class="cn">YOU</span></div>')
    return f'<div class="rd">{mid}{"".join(items)}</div>', """
.rd{position:relative;width:760px;height:760px;margin:80px auto 0}
.core{position:absolute;left:380px;top:380px;transform:translate(-50%,-50%);
  width:214px;height:214px;border-radius:50%;background:rgba(200,70,35,.08);
  border:2px solid rgba(200,70,35,.34);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:2px}
.core .q{font-size:46px;font-weight:800;color:var(--book);line-height:1}
.core .cn{font-size:26px;font-weight:800;color:var(--book);letter-spacing:1px}
.core .cj{font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin-top:3px}
.o{position:absolute;transform:translate(-50%,-50%);display:flex;flex-direction:column;
  align-items:center;gap:8px;width:190px}
.o .tl{border-radius:26px}
.n{font-size:22px;font-weight:800;letter-spacing:-.3px;text-align:center}
.j{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted)}
"""


def build(key: str, L, follow: bool) -> pathlib.Path:
    L.TOOLS = SPECS[key]["tools"]
    body, css = radial_material(L) if key == "radial" else L.LAYOUTS[key]()
    # the catalogue header labels a specimen; a material does not carry one
    body = re.sub(r'<div class="hd">.*?</div>', "", body, count=1, flags=re.S)
    # the square's body heights, rescaled to what this frame leaves
    css = css.replace("936px", f"{BODY_H}px").replace("900px", f"{BODY_H - 36}px")
    css = L.CSS + css
    # #art is declared by the frame, so drop the square's own declaration of it
    css = re.sub(r"#art\{[^}]*\}", "", css, count=1)
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{list(SPECS).index(key) + 1:02d}-{key}.html"
    p.write_text(frame(key, body, css, follow))
    return p


def check(paths: list[pathlib.Path], shots: bool) -> None:
    """The band lines are nowrap: an over long hook is silently clipped, so measure it."""
    from playwright.sync_api import sync_playwright

    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": W, "height": H})
        for f in paths:
            pg.goto(f.as_uri())
            pg.wait_for_timeout(340)
            wide = pg.evaluate(
                "() => ['.l1','.l2','.sub'].map(s => [s, "
                "Math.round(document.querySelector(s).getBoundingClientRect().width)])")
            over = [f"{s} {w}px" for s, w in wide if w > W - 80]
            box = pg.evaluate(
                "() => { const a = document.querySelector('#art');"
                " let m = 0; for (const el of a.querySelectorAll('*')) {"
                "  const r = el.getBoundingClientRect(); if (r.height) m = Math.max(m, r.bottom); }"
                " return Math.round(m); }")
            hit = box > CTA_TOP - 8
            flag = "FAIL" if (over or hit) else "ok  "
            note = (", ".join(over) + (" | content reaches " + str(box) if hit else "")).strip(" |")
            print(f"  {flag} {f.name:<16} band {max(w for _, w in wide)}px   {note}")
            if shots:
                pg.evaluate("() => document.querySelectorAll('.veil')"
                            ".forEach(v => v.style.display = 'none')")
                pg.locator("#film").screenshot(path=str(f.with_suffix(".png")))
        b.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("keys", nargs="*")
    ap.add_argument("--follow", action="store_true",
                    help="the reference footer line instead of the comment CTA")
    ap.add_argument("--shots", action="store_true", help="also write a still of each")
    a = ap.parse_args()

    L = layouts_module()
    L.MARK = marks() or L.MARK
    keys = a.keys or list(SPECS)
    made = [build(k, L, a.follow) for k in keys]
    print(f"built {len(made)} into {OUT}")
    check(made, a.shots)


if __name__ == "__main__":
    main()
