#!/usr/bin/env python3
"""The stack card: one 1080x1350 picture per post. Hook band, tool rows, follow footer.

Operator, 2026-08-14: "executa fiecare postare ... pune si hook ul si follow in format
1080x1350 px ... nu movie - doar poza pentru fiecare postare o vreau ... nu vreau nimic 3d doar
logo uri nume si descriere - toata greutatea materialului o da hook ul si tool urile il fac
salvabil."

So the page is a LIST, not a composition. The hook is the only large thing in the frame and the
body never competes with it: logo, name, engine, one line of what it does. No 3D, no illustration,
no scene.

    1080 x 1350
      0 -  250   BAND     hook line 1 in caps, line 2 in brackets, lower case
      250 + 3    RULE     black, the archive's own separator
    250 - 1242   BODY     the tool rows, or the pyramid's tiers
   1242 - 1350   FOOTER   avatar + the follow line

Tool marks: real brand SVGs where the repo has them, a monogram tile where it does not. Both sit
in the SAME rounded container, which is what stops a mixed set reading as a collage.

    python3 content/_stack.py            # all ten
    python3 content/_stack.py 01 05      # just those
"""
import base64, glob, pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parent.parent
IC = REPO / "content/assets/icons"
OUT_DIR = REPO / "content/ig/stacks"

W, H = 1080, 1350
BAND_H, FOOT_H = 250, 108
PAD = 70                                  # a feed post has no side rail, so the margin is even
BOOK = "#C84623"

# tool -> the svg file that carries its mark, when one exists
MARK = {
    "ChatGPT": "openai", "Codex": "openai", "Claude Code": "claude-color",
    "Claude": "claude-color", "Claude Cowork": "claude-color",
    "Nano Banana 2": "googlegemini", "Gemini": "googlegemini", "Veo 3.1": "google",
    "NotebookLM": "notebooklm", "Notion": "notion", "Perplexity": "perplexity-color",
    "Ideogram": "ideogram", "ElevenLabs": "elevenlabs", "Suno": "suno", "Canva": "canva-color",
    "CapCut": "capcut", "Pika": "pika", "Stripe": "stripe", "Zapier": "zapier",
    "Make": "make", "Obsidian": "obsidian", "Cursor": "cursor", "Framer": "framer",
    "DeepSeek V4 Pro": "deepseek", "Intercom Fin": "intercom", "Cal.com": "caldotcom",
    "Apollo": "apollo", "Fathom": "fathom",
}


def mark(name: str) -> str:
    """A brand svg when we have one, a monogram tile when we do not. Same container either way."""
    slug = MARK.get(name)
    if slug and (IC / f"{slug}.svg").exists():
        s = (IC / f"{slug}.svg").read_text()
        s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
        s = re.sub(r'\s(width|height)="[^"]*"', "", s)
        return f'<span class="tile"><span class="lg">{s}</span></span>'
    initial = re.sub(r"[^A-Za-z]", "", name)[:1].upper() or "?"
    return f'<span class="tile mono">{initial}</span>'


def avatar() -> str:
    for p in (REPO / "content/assets/tiberiu.jpg",
              REPO / "content/assets/tibi poza_profil_instagram_bw_square_1080.jpg"):
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            return f'<img class="av" src="data:image/jpeg;base64,{b64}">'
    return '<span class="av ph"></span>'


def ultron_mark() -> str:
    p = REPO / "content/ultron-logo.png"
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f'<span class="tile ult"><img src="data:image/png;base64,{b64}"></span>'


# ---------------------------------------------------------------- the ten specs
# EVERY HOOK IS THE OPERATOR'S OWN. Operator, 2026-08-14: "ti am dat o lista de 50+ hook uri
# construieste pe alea". I had been writing hooks while sitting on an archive of 61 that had
# already gone viral, which is the whole mistake. These are lifted from it, by position:
#   01 <- 61 "THIS IS HOW 8 TOOLS RUN (my life and business)"
#   02 <- 33 "I HIRED 5 TOOLS FOR $30/MONTH (they replaced $10K in payroll)"
#   03 <- 53 "THE FREEDOM PYRAMID:"   (the archive leaves the bracket empty; the reframe is mine)
#   04 <- 35 "I REPLACED 7 EMPLOYEES (with icons)"    <- and the material IS icons
#   05 <- 20 "I DON'T TRACK DEALS ANYMORE (this app does it for me)"
#   06 <- 48 "MY 4-STEP DAILY SYSTEM (for peace and profit)"
#   07 <- 11 "7 APPS I USE INSTEAD OF MOTIVATION"     <- retargeted to the agency
#   08 <- 43 "I TURNED MY BRAIN INTO A SOFTWARE (6 tools now think for me)"
#   09 <- 51 "MY MOST LOYAL EMPLOYEE" + the bracket from 32 "(they never ask for a raise)"
#   10 <- 47 "I WISH I FOUND THESE 7 APPS (before burning out)"
# The only liberties: adding AI, moving a count to match the stack, and one bracket for 03.
# rows: (tool, engine, what it does FOR THIS use case). The last row is always Ultron.
SPECS = {
"01": dict(
  slug="whole-company",
  l1="THIS IS HOW 8 AI TOOLS RUN", l2="(my life and business)",
  rows=[("ChatGPT","GPT-5.6","The everyday brain. Everything not worth a specialist"),
        ("Claude Code","Claude","Ships the product itself, multi file, from the terminal"),
        ("Granola","Claude or GPT","Sits in every call so you never take a note"),
        ("Wispr Flow","in house","You talk, it types, into whatever app is open"),
        ("Nano Banana 2","Gemini 3.1","Every image, free, inside the Gemini app"),
        ("Veo 3.1","Google","Video with native audio, 4K, portrait"),
        ("Notion","multi","Where all of it lands"),
        ("Ultron","Claude","Research, outbound and deals in one place. Nothing sends without you")]),
"02": dict(
  slug="thirty-dollar-team",
  l1="I HIRED 5 AI TOOLS FOR $30/MONTH", l2="(they replaced $10K in payroll)",
  rows=[("Perplexity","multi","The researcher. Cites sources so you can check it"),
        ("Ideogram","in house","The designer. The one that gets text right in an image"),
        ("Fathom","multi","The notetaker, on a free tier"),
        ("Gumloop","multi","The ops hire. Drag the workflow, it runs daily"),
        ("Ultron","Claude","The SDR and the closer. Finds the account, runs the deal")]),
"04": dict(
  slug="seven-hires",
  l1="I REPLACED 7 EMPLOYEES", l2="(with icons)",
  rows=[("Elicit","multi","The researcher. Reads the papers you never will"),
        ("Claude","Claude","The copywriter. Nobody clocks it as AI"),
        ("Recraft","in house","The designer. Brand assets that stay on brand"),
        ("CapCut","in house","The editor. Cuts, captions, ships"),
        ("Cursor","multi","The developer. Lives in your codebase"),
        ("Reclaim","in house","The assistant. Defends your calendar"),
        ("Ultron","Claude","The SDR and the closer. Two of these seven, in one seat")]),
"05": dict(
  slug="pipeline",
  l1="I DON'T TRACK DEALS ANYMORE", l2="(5 apps do it for me)",
  rows=[("Fireflies","multi","Records the call and writes what was actually agreed"),
        ("Apollo","in house","Finds who is worth talking to"),
        ("Instantly","in house","Sends it and keeps the inbox warm"),
        ("Attio","multi","The board that updates itself"),
        ("Ultron","Claude","Qualifies, handles the objection, drafts the close plan")]),
"06": dict(
  slug="morning",
  l1="MY 4-STEP DAILY AI SYSTEM", l2="(for peace and profit)",
  rows=[("Superwhisper","local","Five minutes of talking and the brain is out"),
        ("NotebookLM","Gemini","Yesterday's material as a briefing you can question"),
        ("Ultron","Claude","The overnight replies, sorted and answered"),
        ("Codex","OpenAI","One thing shipped before the first meeting")]),
"07": dict(
  slug="instead-of-an-agency",
  l1="7 AI APPS I USE INSTEAD OF AN AGENCY", l2="(same work, none of the retainer)",
  rows=[("Gemini","Gemini 3.6","The strategist. Angles, competitors, positioning"),
        ("Gamma","multi","The deck, in a minute"),
        ("Canva","multi","The static assets"),
        ("Higgsfield","multi","The video volume, every model in one place"),
        ("Suno","in house","The sound and the music bed"),
        ("Metricool","none","What actually worked, per channel"),
        ("Ultron","Claude","Writes the posts and the sequences in your voice")]),
"08": dict(
  slug="second-brain",
  l1="I TURNED MY BRAIN INTO A SOFTWARE", l2="(6 tools now think for me)",
  rows=[("Mem","multi","Everything you capture, sorted without you"),
        ("Readwise","multi","Everything you read, resurfaced later"),
        ("Limitless","in house","Everything you said, all day"),
        ("Tana","multi","The structure underneath it"),
        ("DeepSeek V4 Pro","DeepSeek","The cheap pass over all of it, long context"),
        ("Ultron","Claude","Every account and contact, researched once and remembered")]),
"09": dict(
  slug="most-loyal",
  l1="MY MOST LOYAL EMPLOYEE IS AN AI", l2="(they never ask for a raise)",
  rows=[("Zapier","multi","The plumbing. Boring, and it never once broke"),
        ("Cal.com","none","Books the meeting while you sleep"),
        ("Intercom Fin","multi","Answers support at 3am, in your tone"),
        ("Ultron","Claude","Works the pipeline overnight. Nothing sends without you")]),
"10": dict(
  slug="survivors",
  l1="I WISH I FOUND THESE 7 AI APPS", l2="(before burning out)",
  rows=[("Claude Cowork","Claude","The only one that touches your actual files"),
        ("Framer","multi","The site, live the same afternoon"),
        ("Pika","in house","The only video I actually shipped"),
        ("Krea","multi","Images fast enough to iterate on a call"),
        ("Manus","multi","The agent that finished instead of describing"),
        ("Ramp","none","The spend you can finally see"),
        ("Ultron","Claude","Replaced four separate go to market tools, so it stayed")]),
"03": dict(
  slug="freedom-pyramid",
  l1="THE AI FREEDOM PYRAMID", l2="(most founders build it upside down)",
  tiers=[("INCOME", [("Stripe","")]),
         ("LEVERAGE", [("Ultron","Claude"),("Lovable",""),("Clay","")]),
         ("CONTENT", [("Midjourney",""),("Kling 3.0",""),("ElevenLabs","")]),
         ("AUTOMATION", [("Make",""),("Lindy","")]),
         ("PRODUCTIVITY", [("Obsidian",""),("Motion",""),("Otter","")])]),
}


def row_html(tool, engine, desc):
    is_u = tool == "Ultron"
    tile = ultron_mark() if is_u else mark(tool)
    return (f'<div class="row{" ult" if is_u else ""}">{tile}'
            f'<span class="tx"><span class="top"><span class="nm">{tool}</span>'
            f'<span class="chip">{engine}</span></span>'
            f'<span class="ds">{desc}</span></span></div>')


def tier_html(label, tools):
    chips = "".join(
        f'<span class="pchip{" ult" if t == "Ultron" else ""}">'
        f'{ultron_mark() if t == "Ultron" else mark(t)}<span>{t}</span></span>'
        for t, _ in tools)
    return f'<div class="tier"><span class="tlab">{label}</span><span class="tset">{chips}</span></div>'


def page(spec):
    body = ("".join(tier_html(l, ts) for l, ts in spec["tiers"]) if "tiers" in spec
            else "".join(row_html(*r) for r in spec["rows"]))
    n = len(spec.get("rows", spec.get("tiers", [])))
    # A SHORT LIST MUST PACK, NOT STRETCH. With flex:1 a 4 row card gave each row 247px to hold
    # 70px of content, which is the airiness CLAUDE.md 27.9 calls the recurring rejection. So the
    # row height is capped and the group centres, and the contents scale up as the list shortens.
    BODY_H = H - BAND_H - FOOT_H - 3
    row_h = min(BODY_H // max(n, 1), 172)
    tile = 84 if n <= 4 else 72 if n <= 6 else 60
    nm_s = 36 if n <= 4 else 32 if n <= 6 else 27
    ds_s = 21 if n <= 4 else 19.5 if n <= 6 else 17.5
    ch_s = 15 if n <= 6 else 13
    lg_s = round(tile * 0.56)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--ink:#111;--muted:#77736B;--book:{BOOK};--hair:rgba(17,17,17,.11)}}
*{{margin:0;padding:0;box-sizing:border-box}}
#art{{width:{W}px;height:{H}px;background:#fff;position:relative;overflow:hidden;
  font-family:'DM Sans',sans-serif}}
/* THE HOOK. The only large thing in the frame, in the archive's own format:
   caps claim, then the payoff in brackets, lower case. */
.band{{position:absolute;left:0;top:0;width:{W}px;height:{BAND_H}px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:9px;
  padding:0 {PAD}px}}
.h1{{font-size:{52 if len(spec['l1']) < 30 else 44}px;font-weight:800;letter-spacing:-1.2px;
  color:var(--ink);text-align:center;line-height:1.06}}
.h2{{font-size:33px;font-weight:400;letter-spacing:-.5px;color:#3A3A38;text-align:center}}
.edge{{position:absolute;left:0;top:{BAND_H}px;width:{W}px;height:3px;background:#000}}
/* THE BODY */
.body{{position:absolute;left:{PAD}px;right:{PAD}px;top:{BAND_H + 3}px;
  height:{BODY_H}px;display:flex;flex-direction:column;justify-content:center;
  padding:{14 if n > 6 else 20}px 0}}
.row{{height:{row_h}px;flex-shrink:0;display:flex;align-items:center;gap:22px;
  border-top:1px solid var(--hair);padding:0 4px}}
.row:first-child{{border-top:none}}
.tile{{flex-shrink:0;width:{tile}px;height:{tile}px;
  border-radius:16px;background:#F5F4F1;border:1px solid var(--hair);
  display:flex;align-items:center;justify-content:center;overflow:hidden}}
.tile .lg{{width:{lg_s}px;height:{lg_s}px;display:flex;color:#1A1A18}}
.tile .lg svg{{width:100%;height:100%}}
.tile.mono{{font-family:'DM Sans',sans-serif;font-weight:800;
  font-size:{round(tile * 0.44)}px;color:#4A4844;letter-spacing:-.5px}}
.tile.ult{{background:rgba(200,70,35,.08);border-color:rgba(200,70,35,.30)}}
.tile.ult img{{width:100%;height:100%;object-fit:cover}}
.tx{{display:flex;flex-direction:column;gap:3px;flex:1;min-width:0}}
.top{{display:flex;align-items:baseline;gap:12px}}
.nm{{font-size:{nm_s}px;font-weight:800;letter-spacing:-.6px;color:var(--ink);
  white-space:nowrap}}
.chip{{font-family:'DM Mono',monospace;font-size:{ch_s}px;letter-spacing:.06em;
  color:var(--muted);background:#F5F4F1;padding:4px 9px;border-radius:6px;white-space:nowrap}}
.ds{{font-size:{ds_s}px;font-weight:500;color:var(--muted);line-height:1.24}}
/* Ultron reads as different without shouting: warm ground, a hairline, and it closes the list */
.row.ult{{background:rgba(200,70,35,.055);border:1px solid rgba(200,70,35,.28);
  border-radius:14px;padding:0 14px;margin-top:6px}}
.row.ult .nm{{color:var(--book)}}
.row.ult .chip{{color:var(--book);background:rgba(200,70,35,.10)}}
/* THE PYRAMID, the one material that is a shape rather than a list */
/* IT HAS TO READ AS A PYRAMID, NOT AS A TABLE. The first build left-aligned every tier, so one
   chip at the top and three at the bottom all started on the same rail and the shape the hook
   promises never appeared. Centring each tier makes the widening visible: the row IS the tier's
   width, so the silhouette narrows to a point at income. */
.tier{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:9px;border-top:1px solid var(--hair)}}
.tier:first-child{{border-top:none}}
.tlab{{font-family:'DM Mono',monospace;font-size:13px;font-weight:500;letter-spacing:.2em;
  color:var(--muted)}}
.tset{{display:flex;flex-wrap:wrap;gap:11px;justify-content:center}}
.pchip{{display:flex;align-items:center;gap:10px;padding:8px 15px 8px 8px;
  border:1px solid var(--hair);border-radius:12px;background:#FCFBF9;
  font-size:21px;font-weight:700;letter-spacing:-.3px;color:var(--ink)}}
.pchip .tile{{width:38px;height:38px;border-radius:10px}}
.pchip .tile .lg{{width:22px;height:22px}}
.pchip .tile.mono{{font-size:18px}}
.pchip.ult{{background:rgba(200,70,35,.06);border-color:rgba(200,70,35,.28);color:var(--book)}}
/* THE FOOTER */
.foot{{position:absolute;left:0;bottom:0;width:{W}px;height:{FOOT_H}px;
  display:flex;align-items:center;justify-content:center;gap:18px;border-top:1px solid var(--hair)}}
.av{{width:46px;height:46px;border-radius:50%;object-fit:cover;
  box-shadow:0 0 0 2px #fff,0 0 0 4px rgba(200,70,35,.34)}}
.foot .txt{{font-size:25px;font-weight:600;letter-spacing:-.4px;color:#161412;white-space:nowrap}}
</style></head>
<body><div id="art">
  <div class="band"><span class="h1">{spec['l1']}</span><span class="h2">{spec['l2']}</span></div>
  <div class="edge"></div>
  <div class="body">{body}</div>
  <div class="foot">{avatar()}<span class="txt">Follow for more AI tools and productivity hacks</span></div>
</div></body></html>"""


def build(key):
    spec = SPECS[key]
    html_path = REPO / f"content/_stack-{key}.html"
    html_path.write_text(page(spec))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{key}-{spec['slug']}.png"
    from playwright.sync_api import sync_playwright
    exe = next(iter(sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto(html_path.as_uri()); pg.wait_for_timeout(500)
        bad = pg.evaluate("""([L,R])=>[...document.querySelectorAll('.h1,.h2,.nm,.ds,.txt')]
            .map(e=>{const r=e.getBoundingClientRect();
              return {t:e.textContent.trim().slice(0,24),l:Math.round(r.left),r:Math.round(r.right)};})
            .filter(o=>o.l<L-1||o.r>R+1)""", [PAD - 4, W - PAD + 4])
        h = pg.evaluate("()=>document.getElementById('art').scrollHeight")
        pg.locator("#art").screenshot(path=str(out))
        b.close()
    flag = "  SPILL " + str(bad) if bad else ""
    print(f"  {out.name}   {W}x{h}{flag}")
    return out


if __name__ == "__main__":
    keys = sys.argv[1:] or ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
    for k in keys:
        build(k)
