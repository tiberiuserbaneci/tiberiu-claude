#!/usr/bin/env python3
"""Film 16: the skill file. A better cut of the operator's own BREAKDOWN reference.

WHY THIS ONE, OUT OF THE FIVE. Measured 2026-08-12 with `_reelscan.py`:

    reel            ink      motion   dead frames
    v1 VISION       0.0506   0.0894   32%
    v2 EYES         0.0490   0.0752   11%
    v3 ROUTE        0.0454   0.0386   23%
    v4 BREAKDOWN    0.0404   0.0663   37%     <- lowest ink, worst dead share
    v5 VISION b     0.0600   0.0895   32%
    our film-12     0.0965   0.0566    2%

v4 is the weakest of the set on both numbers that matter, and it is beatable with arithmetic
rather than with taste: our own films already run twice its coverage at a twentieth of its
dead frames. What we lose to all five is MOTION, so that is the number this film is built
against - target 0.08, not "not dead".

WHAT V4 GOT RIGHT AND THIS KEEPS. The subject is a real Claude capability, the objects are
real software rather than diagrams, the frame carries a handle and a series label and nothing
else, and the CTA promises a file.

WHAT V4 GOT WRONG AND THIS FIXES.
  - It cuts between separate objects, so each cut passes through a frame holding neither. Six
    of its samples are dead at exactly those seams. This film never cuts: it is ONE session
    window that fills up, so coverage rises monotonically by construction (the episode 05
    lesson, applied to somebody else's format).
  - It spends 0 to 6 seconds on one held caption over a nearly static app icon, and 15 to 19
    seconds on a thin bar with two labels. Both are the airy block CLAUDE.md 27.9 rejects.
  - It shows the skill path but never the FILE, which is the one thing a viewer would have to
    see to go and do this. Here the frontmatter is on screen.

EVERY FACT ON SCREEN IS VERIFIED AGAINST THE LIVE DOCS (CLAUDE.md 31, 2026-08-12):
  ~/.claude/skills/<name>/SKILL.md          personal skill location
  .claude/skills/<name>/SKILL.md            project skill location
  name / description / allowed-tools        the frontmatter fields
  the directory name becomes /<name>        how it is invoked
  the body loads only when the skill is used, so reference material costs nothing until then
  yt-dlp --write-auto-subs --skip-download  pulls captions without downloading the video

No fabricated counts. The only quantity spoken is "two hours of talking", which is the input,
not a measured result.

Build:  python3 content/_skillfilm.py
Voice:  source <scratchpad>/eleven.env    (never in the repo, PARALLEL-SESSION 4)
Render: python3 content/_film.py content/skill-film-16.html
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "content" / "skill-film-16.html"


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


# The take sets the cuts, so these are authored marks only - `_film.py` overwrites --b1..--b6
# with the measured word times before rendering.
META = {
    "duration": 28, "w": 1080, "h": 1920, "fps": 30,
    "hook": True,
    "accent": ["BREAKDOWN", "command", "timestamped", "file"],
    "beats": [
        {"t": 0, "vo": "You paste a link, and Claude tells you it cannot open the video."},
        {"t": 4.4, "vo": "One folder inside your Claude directory changes that."},
        {"t": 8.0, "vo": "A skill is just a file: a name, a description, and the instructions you "
               "would have typed anyway."},
        {"t": 13.4, "vo": "The folder name becomes the command, and the body stays out of context "
               "until the second you use it."},
        {"t": 19.0, "vo": "Under it, yt-dlp pulls the captions off the video with no API key and no "
               "account, so two hours of talking arrives timestamped."},
        {"t": 25.4, "vo": "Comment BREAKDOWN and the file is in your DMs."},
    ],
    "zones": ["bot", "bot", "bot", "bot", "bot", "bot"],
}


def page() -> str:
    fonts = load("_fonts").embedded_css()
    import json
    meta = json.dumps(META)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>CLAUDE SKILLS 01 - THE FILE</title>
<style>{fonts}
/* FILM-META {meta} */
:root{{
  --paper:#EFE9DF; --paper2:#E6DFD2;
  --ink:#191713; --ink70:rgba(25,23,19,.70); --ink44:rgba(25,23,19,.44);
  --ink22:rgba(25,23,19,.22); --ink12:rgba(25,23,19,.12);
  --win:#181613; --win2:#211E19;
  --iv:#F6F2EA; --iv62:rgba(246,242,234,.62); --iv34:rgba(246,242,234,.34);
  --iv14:rgba(246,242,234,.14);
  --book:#C84623; --bookl:#E0774F; --kraft:#D4A27F;
  --e:cubic-bezier(.4,0,.2,1); --eE:cubic-bezier(.05,.7,.1,1);
  --b1:0s; --b2:4.4s; --b3:8.0s; --b4:13.4s; --b5:19.0s; --b6:25.4s;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;display:flex;justify-content:center}}
#film{{position:relative;width:1080px;height:1920px;overflow:hidden;
  background:var(--paper);color:var(--ink)}}

/* ONE GROUND for the whole film. Paper, a warm bloom, a hairline grid and grain, all inside
   one painted layer so the blurs rasterise once instead of on all 840 frames. */
.bg{{position:absolute;inset:0;z-index:0;contain:paint}}
.bg::before{{content:'';position:absolute;inset:-12%;
  background:radial-gradient(ellipse 58% 38% at 14% 3%,rgba(200,70,35,.13) 0%,transparent 62%),
    radial-gradient(ellipse 56% 40% at 92% 96%,rgba(25,23,19,.10) 0%,transparent 64%)}}
.grid{{position:absolute;inset:0;opacity:.5;
  background-image:linear-gradient(var(--ink12) 1px,transparent 1px),
    linear-gradient(90deg,var(--ink12) 1px,transparent 1px);background-size:120px 120px}}
.noise{{position:absolute;inset:0;opacity:.42;
  background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='150' height='150'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/>\
<feColorMatrix type='saturate' values='0'/></filter>\
<rect width='150' height='150' filter='url(%23n)' opacity='.45'/></svg>")}}

.safe{{position:absolute;top:300px;left:104px;right:152px;bottom:330px;z-index:6;
  display:flex;flex-direction:column}}

/* CLAUDE.md 31: a series label, never a company. The handle is the only identity. */
.mast{{flex-shrink:0;display:flex;justify-content:space-between;align-items:baseline;
  font-family:'DM Mono',monospace;font-weight:500;font-size:21px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--ink44)}}
.mast em{{color:var(--book);font-style:normal}}
.stage{{flex:1;min-height:0;position:relative;margin-top:22px}}
.capband{{position:absolute;inset:0;z-index:7;pointer-events:none}}
.foot{{flex-shrink:0;padding-top:20px;font-family:'DM Mono',monospace;font-weight:500;
  font-size:21px;letter-spacing:.26em;color:var(--ink44)}}

/* THE SESSION. One window, filling from the top, anchored so new lines push the stack up.
   It never cuts and nothing is ever removed, so coverage only rises: the defect that put six
   dead samples into the reference is impossible here rather than guarded against.
   330px is reserved at the foot for the caption band (300px plus the sheet's own drift). */
.win{{position:absolute;left:0;right:0;top:0;bottom:330px;border-radius:22px;
  background:var(--win);overflow:hidden;
  box-shadow:inset 0 0 0 2px rgba(246,242,234,.10),0 40px 80px -40px rgba(25,23,19,.55);
  animation:winpush 28s var(--e) both 0s}}
.tb{{display:flex;align-items:center;gap:11px;padding:20px 24px;background:var(--win2);
  border-bottom:1px solid var(--iv14)}}
.tb i{{width:13px;height:13px;border-radius:50%;background:var(--iv14);display:block}}
.tb i:first-child{{background:var(--book)}}
.tb span{{margin-left:12px;font-family:'DM Mono',monospace;font-weight:500;font-size:19px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--iv34)}}
.body{{position:absolute;left:0;right:0;top:62px;bottom:0;padding:22px 28px 24px;
  display:flex;flex-direction:column;gap:11px;font-family:'DM Mono',monospace;
  font-weight:400;font-size:24px;line-height:1.38;color:var(--iv62)}}
/* A BLOCK GROWS, IT DOES NOT FADE IN PLACE. Fading a line into a slot that was already
   reserved changes a few hundred pixels and leaves the rest of the frame identical; the
   sampler saw five of every six frames unchanged and read 0.0087 motion. A terminal does not
   work that way, and neither does this now: each block opens from zero height and pushes the
   whole stack, so one arrival changes the whole window. `grid-template-rows` 0fr to 1fr is
   what animates to an unknown height without hardcoding one, so the copy can change without
   re-measuring anything. */
.blk{{display:grid;grid-template-rows:0fr;opacity:0}}
.blk>.in{{overflow:hidden;min-height:0}}
@keyframes grow{{from{{grid-template-rows:0fr;opacity:0}}
  to{{grid-template-rows:1fr;opacity:1}}}}
.pr{{color:var(--iv)}}
.pr b{{color:var(--book);font-weight:500;margin-right:12px}}
.no{{color:var(--bookl)}}
.dim{{color:var(--iv34)}}
.ok{{color:var(--kraft)}}

/* the file, as a real card inside the session */
.card{{border-radius:14px;background:rgba(246,242,234,.05);
  box-shadow:inset 0 0 0 1.5px var(--iv14);padding:16px 20px;
  display:flex;flex-direction:column;gap:7px}}
.card .fn{{font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:var(--iv34);
  margin-bottom:5px}}
.card .k{{color:var(--kraft)}}
.card .v{{color:var(--iv)}}
.rule{{height:1px;background:var(--iv14);margin:2px 0}}
.chips{{display:flex;gap:12px;flex-wrap:wrap}}
.chip{{font-size:21px;letter-spacing:.1em;padding:7px 15px;border-radius:999px;
  color:var(--bookl);box-shadow:inset 0 0 0 1.5px rgba(224,119,79,.40)}}
.chip.q{{color:var(--iv34);box-shadow:inset 0 0 0 1.5px var(--iv14)}}
.ts{{display:flex;gap:18px}}
.ts u{{text-decoration:none;color:var(--book);flex-shrink:0}}

/* THE ASK is the last thing the session prints, not a card laid over a dimmed frame.
   Retiring the picture to put the CTA on it is the coverage collapse CLAUDE.md 30 forbids. */
.cta{{margin-top:auto;border-radius:16px;background:rgba(200,70,35,.13);
  box-shadow:inset 0 0 0 2px rgba(200,70,35,.42);padding:18px 22px;
  display:flex;align-items:center;justify-content:space-between;gap:20px}}
.cta .kw{{font-family:'Anton',sans-serif;font-size:54px;line-height:.92;letter-spacing:-1px;
  text-transform:uppercase;color:var(--book)}}
.cta .kw em{{display:block;font-family:'DM Mono',monospace;font-size:20px;font-weight:500;
  letter-spacing:.24em;color:var(--iv34);font-style:normal;margin-bottom:6px}}
.cta .to{{text-align:right;font-size:21px;letter-spacing:.1em;color:var(--iv62);
  flex-shrink:0}}

@keyframes winpush{{from{{transform:scale(1)}}to{{transform:scale(1.012)}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(18px)}}
  to{{opacity:1;transform:translateY(0)}}}}
@keyframes tick{{from{{opacity:0}}to{{opacity:1}}}}

/* Each block arrives on its own beat and STAYS. One animation per element: a second rule on
   the same element replaces the first rather than extending it, which is the trap recorded in
   FILM-SERIES.md and the reason six ledger slots never filled on episode 05. */
.k1{{animation:grow .62s var(--eE) both calc(var(--b1) + .35s)}}
.k2{{animation:grow .62s var(--eE) both calc(var(--b1) + 2.30s)}}
.k3{{animation:grow .62s var(--eE) both calc(var(--b2) + .30s)}}
.k4{{animation:grow .62s var(--eE) both calc(var(--b3) + .25s)}}
.k5{{animation:grow .62s var(--eE) both calc(var(--b3) + 1.60s)}}
.k6{{animation:grow .62s var(--eE) both calc(var(--b3) + 2.90s)}}
.k7{{animation:grow .62s var(--eE) both calc(var(--b4) + .30s)}}
.k8{{animation:grow .62s var(--eE) both calc(var(--b4) + 2.20s)}}
.k9{{animation:grow .62s var(--eE) both calc(var(--b5) + .30s)}}
.k10{{animation:grow .62s var(--eE) both calc(var(--b5) + 1.70s)}}
.k11{{animation:grow .62s var(--eE) both calc(var(--b5) + 3.10s)}}
.k12{{animation:grow .62s var(--eE) both calc(var(--b5) + 4.40s)}}
.k13{{animation:grow .70s var(--eE) both calc(var(--b6) + .20s)}}

/* THE CAPTION RAIL, AUTHORED RATHER THAN MEASURED. `_film.py` normally builds these from the
   voiceover's character timestamps and injects them into #capband, but api.elevenlabs.io is
   refused by the agent proxy from this environment (403 on the CONNECT tunnel, verified
   2026-08-12), so the take cannot be recorded here. These lines sit on the authored beat clock
   instead, in their own #authcap so a real take can be dropped in later without touching them:
   delete this element and the injected #subs takes over.

   One animation per line, its duration the beat's own span, with the in and the out as
   keyframes inside it. Two rules on one element would replace each other rather than
   sequence, which is the trap in FILM-SERIES.md that emptied six ledger slots on episode 05. */
#authcap{{position:absolute;left:0;right:0;bottom:0;height:300px;z-index:8;
  display:flex;align-items:flex-end;justify-content:center;pointer-events:none}}
#authcap p{{position:absolute;bottom:0;width:100%;text-align:center;opacity:0;
  font-family:'DM Sans',sans-serif;font-weight:900;font-size:54px;line-height:1.16;
  letter-spacing:-1.2px;color:var(--ink)}}
#authcap em{{color:var(--book);font-style:normal}}
@keyframes capin{{0%{{opacity:0;transform:translateY(16px)}}
  9%{{opacity:1;transform:translateY(0)}}
  86%{{opacity:1;transform:translateY(0)}}
  100%{{opacity:0;transform:translateY(-10px)}}}}
.c1{{animation:capin calc(var(--b2) - var(--b1)) var(--e) both var(--b1)}}
.c2{{animation:capin calc(var(--b3) - var(--b2)) var(--e) both var(--b2)}}
.c3{{animation:capin calc(var(--b4) - var(--b3)) var(--e) both var(--b3)}}
.c4{{animation:capin calc(var(--b5) - var(--b4)) var(--e) both var(--b4)}}
.c5{{animation:capin calc(var(--b6) - var(--b5)) var(--e) both var(--b5)}}

/* MOTION IS DISCRETE, NOT A DRIFT. Measured on the first cut: 0.0087 motion and 67 percent
   dead samples, against 0.066 to 0.089 on the five references. The cause was arithmetic, not
   taste - sixteen events across twenty eight seconds is one change every 1.75s, and the
   sampler looks every 0.25s, so five of every six frames were identical to the one before.
   A slow continuous drift does not fix it either: 18px over 28s is 0.16px between samples,
   which is nothing. What registers is something genuinely changing, so the session behaves
   like a session - the caret blinks, the commands type, and the caption arrives a word at a
   time. All three are true to the object rather than decoration added to satisfy a metric. */
.car{{display:inline-block;width:13px;height:26px;margin-left:6px;vertical-align:-4px;
  background:var(--book);animation:blink 1.02s steps(1) infinite}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
.type{{display:inline-block;overflow:hidden;white-space:nowrap;vertical-align:bottom;
  width:0}}
@keyframes typ{{from{{width:0}}to{{width:var(--w)}}}}
.t1{{--w:15.2em;animation:typ 1.05s steps(19) both calc(var(--b1) + .40s)}}
.t2{{--w:23.4em;animation:typ 1.30s steps(26) both calc(var(--b4) + .35s)}}

/* the caption arrives word by word. The words only ever fade IN; the paragraph owns the fade
   OUT, so no element carries two animations and neither replaces the other. */
#authcap p{{animation-name:capout;animation-timing-function:var(--e);animation-fill-mode:both}}
@keyframes capout{{0%,86%{{opacity:1}}100%{{opacity:0;transform:translateY(-10px)}}}}
#authcap w{{display:inline-block;opacity:0;animation:wordin .34s var(--eE) both}}
@keyframes wordin{{from{{opacity:0;transform:translateY(13px)}}
  to{{opacity:1;transform:translateY(0)}}}}
.c1w0{{animation-delay:calc(var(--b1) + 0.30s)}}
.c1w1{{animation-delay:calc(var(--b1) + 0.47s)}}
.c1w2{{animation-delay:calc(var(--b1) + 0.64s)}}
.c1w3{{animation-delay:calc(var(--b1) + 0.81s)}}
.c1w4{{animation-delay:calc(var(--b1) + 0.98s)}}
.c2w0{{animation-delay:calc(var(--b2) + 0.30s)}}
.c2w1{{animation-delay:calc(var(--b2) + 0.47s)}}
.c2w2{{animation-delay:calc(var(--b2) + 0.64s)}}
.c2w3{{animation-delay:calc(var(--b2) + 0.81s)}}
.c3w0{{animation-delay:calc(var(--b3) + 0.30s)}}
.c3w1{{animation-delay:calc(var(--b3) + 0.47s)}}
.c3w2{{animation-delay:calc(var(--b3) + 0.64s)}}
.c3w3{{animation-delay:calc(var(--b3) + 0.81s)}}
.c3w4{{animation-delay:calc(var(--b3) + 0.98s)}}
.c3w5{{animation-delay:calc(var(--b3) + 1.15s)}}
.c4w0{{animation-delay:calc(var(--b4) + 0.30s)}}
.c4w1{{animation-delay:calc(var(--b4) + 0.47s)}}
.c4w2{{animation-delay:calc(var(--b4) + 0.64s)}}
.c4w3{{animation-delay:calc(var(--b4) + 0.81s)}}
.c4w4{{animation-delay:calc(var(--b4) + 0.98s)}}
.c4w5{{animation-delay:calc(var(--b4) + 1.15s)}}
.c5w0{{animation-delay:calc(var(--b5) + 0.30s)}}
.c5w1{{animation-delay:calc(var(--b5) + 0.47s)}}
.c5w2{{animation-delay:calc(var(--b5) + 0.64s)}}
.c5w3{{animation-delay:calc(var(--b5) + 0.81s)}}
.c5w4{{animation-delay:calc(var(--b5) + 0.98s)}}
</style></head>
<body>
<div id="film">
  <div class="bg"><div class="grid"></div><div class="noise"></div></div>

  <div class="safe">
    <div class="mast"><span>Claude skills <em>&middot;</em> 01</span><span>the file</span></div>

    <div class="stage">
      <div class="win">
        <div class="tb"><i></i><i></i><i></i><span>claude</span></div>
        <div class="body">

          <div class="blk k1"><div class="in pr"><b>&gt;</b><span class="type t1">summarise this talk</span><span class="car"></span></div></div>
          <div class="blk k2"><div class="in no">I cannot open video. Paste the transcript and I will read it.</div></div>

          <div class="blk k3"><div class="in dim">~/.claude/<span class="ok">skills</span>/youtube/SKILL.md</div></div>

          <div class="blk k4 card">
            <span class="fn">SKILL.md</span>
            <span><span class="k">name:</span> <span class="v">youtube</span></span>
            <span><span class="k">description:</span> <span class="v">read a video by its captions</span></span>
            <span><span class="k">allowed-tools:</span> <span class="v">Bash Read</span></span>
          </div>
          <div class="blk k6 chips"><span class="chip">/youtube</span>
            <span class="chip q">body loads only when used</span></div>

          <div class="blk k7"><div class="in pr"><b>$</b><span class="type t2">yt-dlp --write-auto-subs</span></div></div>
          <div class="blk k8"><div class="in ok">captions written</div></div>

          <div class="blk k9"><div class="in ts"><u>00:00</u><span>cold open, names the stakes</span></div></div>
          <div class="blk k10"><div class="in ts"><u>12:40</u><span>the actual argument starts</span></div></div>
          <div class="blk k11"><div class="in ts"><u>41:05</u><span>the part everyone quotes</span></div></div>

          <div class="blk k13 cta">
            <span class="kw"><em>Comment</em>Breakdown</span>
            <span class="to">the file<br>&rarr; your DMs</span>
          </div>
        </div>
      </div>
      <div class="capband" id="capband"></div>
      <div id="authcap">
        <p class="c1"><w class='c1w0'>Claude</w> <w class='c1w1'>cannot</w> <w class='c1w2'>open</w> <w class='c1w3'>the</w> <w class='c1w4'><em>video</em>.</w></p>
        <p class="c2"><w class='c2w0'>One</w> <w class='c2w1'><em>folder</em></w> <w class='c2w2'>changes</w> <w class='c2w3'>that.</w></p>
        <p class="c3"><w class='c3w0'>A</w> <w class='c3w1'>skill</w> <w class='c3w2'>is</w> <w class='c3w3'>just</w> <w class='c3w4'>a</w> <w class='c3w5'><em>file</em>.</w></p>
        <p class="c4"><w class='c4w0'>The</w> <w class='c4w1'>folder</w> <w class='c4w2'>name</w> <w class='c4w3'>is</w> <w class='c4w4'>the</w> <w class='c4w5'><em>command</em>.</w></p>
        <p class="c5"><w class='c5w0'>No</w> <w class='c5w1'>API</w> <w class='c5w2'>key.</w> <w class='c5w3'>No</w> <w class='c5w4'><em>account</em>.</w></p>
      </div>
    </div>

    <div class="foot">@tiberiu.ai</div>
  </div>
</div>
</body></html>
"""


if __name__ == "__main__":
    OUT.write_text(page())
    words = sum(len(b["vo"].split()) for b in META["beats"])
    print(f"built  {OUT.relative_to(REPO)}")
    print(f"  {len(META['beats'])} beats, {words} words, "
          f"{words / META['duration']:.1f} w/s authored over {META['duration']}s")
