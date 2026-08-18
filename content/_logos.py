#!/usr/bin/env python3
"""Install a local brand mark library, so a material never needs the network.

The renderer has no internet (18): every mark a poster or a film inlines has to be
a file on disk. This builds two tiers.

  content/assets/logos/     THE LIBRARY, offline and complete
      mono/<slug>.svg       Simple Icons, one path, monochrome, brand hex in the index
      ai/<name>.svg         Lobe icons, the AI model marks, colour and mono variants
      color/<slug>.svg      full colour official artwork, for the tools we actually name
      png/<slug>-<n>.png    raster exports, brand colour and white, for a video editor
      logos.json            index: title, slug, brand hex, which files exist, source

  content/assets/icons/     THE WORKING SET, what the material scripts read
      <slug>.svg            resolved mono mark
      <slug>-color.svg      resolved colour mark

Two tiers because a material wants one obvious file per tool and the library wants
everything. The working set keeps the naming the existing scripts already expect,
so _stack.py and _layouts.py pick the new marks up with no change.

Sources, all four reachable through the agent proxy (measured 2026-08-17):

  | key  | source                          | what it is                    | licence |
  |------|---------------------------------|-------------------------------|---------|
  | si   | simple-icons (npm tarball)      | 3453 mono marks + brand hex   | CC0     |
  | lobe | @lobehub/icons-static-svg (npm) | 903 AI model marks, colour    | MIT     |
  | gil  | gilbarbara/logos (raw.github)   | official full colour artwork  | CC0     |
  | dash | homarr-labs/dashboard-icons     | app marks, colour             | MIT     |

The icon FILES are freely licensed. The TRADEMARKS are not: a third party mark in a
commercial piece needs the operator's say so (18), which the tool stack materials have.

    python3 content/_logos.py --sync              refresh the source cache
    python3 content/_logos.py --install           library + working set
    python3 content/_logos.py --png 1024          raster exports for video
    python3 content/_logos.py --sheet             contact sheet of the working set
    python3 content/_logos.py --find granola      search all four sources
    python3 content/_logos.py --report            what is installed, what is missing
"""
from __future__ import annotations

import argparse
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
CACHE = REPO / ".logocache"
LIB = REPO / "content/assets/logos"
WORK = REPO / "content/assets/icons"

RAW = "https://raw.githubusercontent.com"
GIL = f"{RAW}/gilbarbara/logos/main/logos"
DASH = f"{RAW}/homarr-labs/dashboard-icons/main/svg"
NPM = "https://registry.npmjs.org"

# Every tool we have put on a card or expect to, mapped to the slug that resolves it.
# The value is the resolution key, not the display name: ChatGPT and Codex are both OpenAI.
SUITE: dict[str, str] = {
    # models and assistants
    "Claude": "claude", "Claude Code": "claude", "Claude Cowork": "claude",
    "ChatGPT": "openai", "Codex": "openai", "Gemini": "gemini",
    "Nano Banana 2": "gemini", "NotebookLM": "notebooklm", "Veo 3.1": "google",
    "DeepSeek": "deepseek", "Grok": "grok", "Mistral": "mistral", "Qwen": "qwen",
    "Llama": "ollama", "Perplexity": "perplexity", "Copilot": "githubcopilot",
    "Manus": "manus", "Kimi": "kimi", "Cohere": "cohere",
    # build
    "Cursor": "cursor", "Windsurf": "windsurf", "Replit": "replit", "Lovable": "lovable",
    "v0": "v0", "Vercel": "vercel", "Supabase": "supabase", "Railway": "railway",
    "GitHub": "github", "Zed": "zedindustries", "VS Code": "vscode",
    "Warp": "warp", "Raycast": "raycast", "Postman": "postman",
    # design and media
    "Figma": "figma", "Framer": "framer", "Webflow": "webflow", "Miro": "miro",
    "Excalidraw": "excalidraw", "Midjourney": "midjourney", "Ideogram": "ideogram",
    "Recraft": "recraft", "Krea": "krea", "Flux": "flux", "Runway": "runway",
    "Luma": "luma", "Pika": "pika", "Kling": "kling", "Sora": "sora",
    "CapCut": "capcut", "ElevenLabs": "elevenlabs", "Suno": "suno", "Descript": "descript",
    "Canva": "canva",   # not in any of the four; the real mark was fetched earlier, kept local
    # write, think, remember
    "Notion": "notion", "Obsidian": "obsidian", "Linear": "linear", "Todoist": "todoist",
    "Asana": "asana", "Trello": "trello", "ClickUp": "clickup", "Airtable": "airtable",
    "Loom": "loom", "Zoom": "zoom", "Slack": "slack", "Substack": "substack",
    "Typeform": "typeform", "Calendly": "calendly", "Cal.com": "caldotcom",
    # money and ops
    "Stripe": "stripe", "Ramp": "ramp", "Brex": "brex", "QuickBooks": "quickbooks",
    "Xero": "xero", "Gusto": "gusto", "Twilio": "twilio", "Resend": "resend",
    # sales
    "HubSpot": "hubspot", "Pipedrive": "pipedrive", "Salesforce": "salesforce",
    "Intercom": "intercom", "Intercom Fin": "intercom",
    "Zapier": "zapier", "Make": "make",
    # Simple Icons' "fathom" is usefathom.com, the analytics company. The Fathom in our stacks
    # is the meeting notetaker, a different company, so it gets no mark rather than a wrong one.
    "Fathom Analytics": "fathom",
    # measure
    "PostHog": "posthog", "Mixpanel": "mixpanel", "Amplitude": "amplitude",
    "Sentry": "sentry", "Datadog": "datadog", "Plausible": "plausible",
    # channels
    "LinkedIn": "linkedin", "Instagram": "instagram", "TikTok": "tiktok",
    "YouTube": "youtube", "X": "x", "Reddit": "reddit", "Discord": "discord",
    "Telegram": "telegram", "WhatsApp": "whatsapp", "Gmail": "gmail",
    "Outlook": "microsoftoutlook",
}

# Vector marks that exist in none of the four sources, checked 2026-08-17. These are the
# newest AI startups; every one of them renders as a monogram tile until the operator drops
# a real file in. A hand drawn approximation was tried once and rejected on sight, correctly.
NO_MARK = [
    "Attio", "Beehiiv", "Bolt", "Clay", "Deel", "Dropcontact", "Elicit",
    "FigJam", "Fireflies", "Gamma", "Granola", "Gumloop", "Height", "Heygen",
    "Higgsfield", "Hunter", "Instantly", "Lemlist", "Limitless", "Lindy", "Mem",
    "Mercury", "Metricool", "Motion", "Otter", "Outreach", "Readwise", "Reclaim",
    "Rippling", "Salesloft", "Shortwave", "Smartlead", "Superhuman", "Superwhisper",
    "Synthesia", "Tana", "Whimsical", "Wispr Flow",
    # A mark for the wrong company is worse than no mark, and it is the first thing a reader
    # who uses the product notices. Both of these resolve to a different company:
    "Apollo",          # gilbarbara "apollostack" is Apollo GraphQL, not Apollo.io the sales tool
    "Fathom",          # see Fathom Analytics above; the notetaker is a different company
]


def get(url: str, timeout: int = 40) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def npm_tarball(pkg: str) -> bytes:
    meta = json.loads(get(f"{NPM}/{pkg}"))
    ver = meta["dist-tags"]["latest"]
    name = pkg.split("/")[-1]
    return get(f"{NPM}/{pkg}/-/{name}-{ver}.tgz")


def sync(force: bool = False) -> None:
    """Pull the four sources into the cache. Cheap, about 9 MB, and gitignored."""
    CACHE.mkdir(exist_ok=True)
    for pkg, dest in (("simple-icons", "si"), ("@lobehub/icons-static-svg", "lobe")):
        d = CACHE / dest
        if d.exists() and not force:
            print(f"  {dest:<5} cached ({len(list((d / 'icons').glob('*.svg')))} svg)")
            continue
        print(f"  {dest:<5} downloading {pkg}")
        blob = npm_tarball(pkg)
        shutil.rmtree(d, ignore_errors=True)
        d.mkdir(parents=True)
        with tarfile.open(fileobj=io.BytesIO(blob)) as tf:
            for m in tf.getmembers():
                parts = m.name.split("/", 1)
                if len(parts) < 2 or not m.isfile():
                    continue
                tgt = d / parts[1]
                tgt.parent.mkdir(parents=True, exist_ok=True)
                src = tf.extractfile(m)
                if src:
                    tgt.write_bytes(src.read())
        print(f"        {len(list((d / 'icons').glob('*.svg')))} svg")
    for url, dest in ((f"{RAW}/gilbarbara/logos/main/logos.json", "gil.json"),
                      (f"{RAW}/homarr-labs/dashboard-icons/main/tree.json", "dash.json")):
        p = CACHE / dest
        if p.exists() and not force:
            print(f"  {dest:<9} cached")
            continue
        p.write_bytes(get(url))
        print(f"  {dest:<9} fetched")


def norm(t: str) -> str:
    t = t.lower()
    for a, b in ((".", ""), ("+", "plus"), ("&", "and"), ("'", ""), (" ", ""),
                 ("-", ""), ("_", "")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]", "", t)


def indexes() -> dict:
    """Read the cached sources into lookup tables keyed by normalised slug."""
    si_json = CACHE / "si/data/simple-icons.json"
    si_raw = json.loads(si_json.read_text()) if si_json.exists() else []
    if isinstance(si_raw, dict):
        si_raw = si_raw.get("icons", [])
    si = {}
    for e in si_raw:
        title, hexv = e.get("title", ""), e.get("hex")
        for k in {e.get("slug"), norm(title)}:
            if k:
                si.setdefault(norm(k), {"title": title, "hex": hexv})

    lobe: dict[str, list[str]] = {}
    ldir = CACHE / "lobe/icons"
    if ldir.exists():
        for f in sorted(os.listdir(ldir)):
            if f.endswith(".svg"):
                base = re.sub(r"-(color|text|brand|combine)$", "", f[:-4])
                lobe.setdefault(norm(base), []).append(f)

    gil: dict[str, list[str]] = {}
    gp = CACHE / "gil.json"
    if gp.exists():
        for e in json.loads(gp.read_text()):
            for f in e.get("files", []):
                for k in (e.get("shortname", ""), e.get("name", "")):
                    if k:
                        gil.setdefault(norm(k), [])
                        if f not in gil[norm(k)]:
                            gil[norm(k)].append(f)

    dash: dict[str, str] = {}
    dp = CACHE / "dash.json"
    if dp.exists():
        for f in json.loads(dp.read_text()).get("svg", []):
            dash.setdefault(norm(f[:-4]), f)
    return {"si": si, "lobe": lobe, "gil": gil, "dash": dash}


def valid_svg(b: bytes) -> bool:
    """An HTML error page and an empty wrapper both have to fail here, not at render time."""
    if not b or len(b) < 60:
        return False
    s = b[:4000].decode("utf-8", "replace").lstrip()
    if not s.startswith("<svg") and "<svg" not in s[:200]:
        return False
    body = b.decode("utf-8", "replace")
    return bool(re.search(r"<(path|circle|rect|polygon|polyline|ellipse|g|use|image)\b", body))


def is_stub(b: bytes) -> bool:
    """True for a file that is structurally a valid svg but carries no mark.

    Lobe's zapier-color.svg is 198 bytes holding one 21 character path: every structural check
    passed and it rendered on the card as a small orange dash. So the gate measures drawing,
    not validity. Measured on the real files this has to let through:

        stub  zapier-color   198 b   21 ink   1 element   <- the one to reject
        real  framer (gil)   405 b   95 ink   1 element
        real  trello (gil)   829 b    0 ink   3 elements  <- geometry in rects, no path data
        real  clickup (dash)1520 b  197 ink   2 elements

    A single element, almost no path data and a tiny file together mean a stub. Any one of the
    three being healthy is enough to accept, which is why the test is an AND.
    """
    body = b.decode("utf-8", "replace")
    ink = sum(len(m) for m in re.findall(r'\sd="([^"]*)"', body))
    ink += sum(len(m) for m in re.findall(r'\spoints="([^"]*)"', body))
    els = len(re.findall(r"<(path|circle|rect|polygon|polyline|ellipse|line|use|image)\b", body))
    return els <= 1 and ink < 60 and len(b) < 320


def aspect(b: bytes) -> float:
    """Width over height off the viewBox. A tile is square, so this decides what fits it."""
    m = re.search(r'viewBox="([\d.eE+\-\s,]+)"', b.decode("utf-8", "replace"))
    if not m:
        return 1.0
    v = [float(x) for x in re.split(r"[\s,]+", m.group(1).strip()) if x]
    return v[2] / v[3] if len(v) >= 4 and v[3] else 1.0


WIDE = 2.0


def pick_color(slug: str, idx: dict) -> tuple[bytes, str, bool] | None:
    """Full colour artwork, best source first. Colour is what makes a stack read as real.

    Square wins over wide. Eight brands resolved to their WORDMARK on the first pass
    (Pipedrive 4.4:1, Webflow 4.0, Zapier 3.7, HubSpot 3.4, Mixpanel 3.1, Gusto 2.6, Flux 2.5,
    Stripe 2.4). Dropped into an 84px square tile a 4:1 wordmark is 21px tall and unreadable,
    which is a worse defect than no mark at all. A wordmark is only returned when nothing
    square exists, and it comes back flagged so the material can give it a wide slot.
    """
    k = norm(slug)
    ok = lambda b: valid_svg(b) and not is_stub(b)
    fallback: tuple[bytes, str, bool] | None = None

    def offer(b: bytes, src: str):
        nonlocal fallback
        if not ok(b):
            return None
        if aspect(b) <= WIDE:
            return b, src, False
        if fallback is None:
            fallback = (b, src, True)
        return None

    for name in idx["lobe"].get(k, []):
        if name.endswith("-color.svg"):
            r = offer((CACHE / "lobe/icons" / name).read_bytes(), f"lobe:{name}")
            if r:
                return r
    if k in idx["gil"]:
        for n in sorted(idx["gil"][k], key=lambda n: (0 if "-icon" in n else 1, len(n))):
            try:
                b = get(f"{GIL}/{n}")
            except Exception:
                continue
            r = offer(b, f"gil:{n}")
            if r:
                return r
    if k in idx["dash"]:
        try:
            r = offer(get(f"{DASH}/{idx['dash'][k]}"), f"dash:{idx['dash'][k]}")
            if r:
                return r
        except Exception:
            pass
    for name in idx["lobe"].get(k, []):
        if not name.endswith(("-text.svg", "-brand.svg", "-combine.svg")):
            r = offer((CACHE / "lobe/icons" / name).read_bytes(), f"lobe:{name}")
            if r:
                return r
    return fallback


def pick_mono(slug: str, idx: dict) -> tuple[bytes, str, str | None] | None:
    """Monochrome single path plus the official brand hex, which only Simple Icons carries."""
    k = norm(slug)
    if k in idx["si"]:
        p = CACHE / "si/icons" / f"{k}.svg"
        if not p.exists():
            cand = list((CACHE / "si/icons").glob(f"{k}*.svg"))
            p = cand[0] if cand else p
        if p.exists():
            b = p.read_bytes()
            if valid_svg(b):
                return b, f"si:{p.name}", idx["si"][k].get("hex")
    return None


def install(idx: dict) -> dict:
    for d in (LIB / "mono", LIB / "ai", LIB / "color", WORK):
        d.mkdir(parents=True, exist_ok=True)

    # the library, copied wholesale so a later --add never needs the network
    n_mono = n_ai = 0
    sidir = CACHE / "si/icons"
    if sidir.exists():
        for f in os.listdir(sidir):
            if f.endswith(".svg"):
                shutil.copyfile(sidir / f, LIB / "mono" / f)
                n_mono += 1
    ldir = CACHE / "lobe/icons"
    if ldir.exists():
        for f in os.listdir(ldir):
            if f.endswith(".svg"):
                shutil.copyfile(ldir / f, LIB / "ai" / f)
                n_ai += 1
    print(f"  library   mono {n_mono}   ai {n_ai}")

    # the working set, one resolved pair per tool
    manifest: dict[str, dict] = {}
    done: dict[str, dict] = {}
    for name, slug in SUITE.items():
        if slug in done:
            manifest[name] = dict(done[slug], slug=slug)
            continue
        entry: dict = {"slug": slug, "hex": None, "mono": None, "color": None, "source": []}
        m = pick_mono(slug, idx)
        if m:
            b, src, hexv = m
            (WORK / f"{slug}.svg").write_bytes(b)
            entry.update(mono=f"{slug}.svg", hex=hexv)
            entry["source"].append(src)
        c = pick_color(slug, idx)
        if c:
            b, src, wide = c
            (LIB / "color" / f"{slug}.svg").write_bytes(b)
            if wide:
                # a wordmark: keep it, name it for what it is, leave the tile to the mono mark
                (WORK / f"{slug}-wordmark.svg").write_bytes(b)
                entry.update(wordmark=f"{slug}-wordmark.svg")
            else:
                (WORK / f"{slug}-color.svg").write_bytes(b)
                entry.update(color=f"{slug}-color.svg")
            entry["source"].append(src)
        # A mark none of the four carry may already be here from an earlier hand fetch.
        # Keep it rather than report a gap we do not have.
        if not entry["source"]:
            for fn, key in ((f"{slug}-color.svg", "color"), (f"{slug}.svg", "mono")):
                if (WORK / fn).exists() and valid_svg((WORK / fn).read_bytes()):
                    entry[key] = fn
                    entry["source"].append(f"local:{fn}")
                    if key == "color":
                        shutil.copyfile(WORK / fn, LIB / "color" / f"{slug}.svg")
        done[slug] = entry
        manifest[name] = entry
        flag = "ok " if (entry["mono"] or entry["color"]) else "MISS"
        print(f"  {flag} {name:<16} {slug:<18} {' '.join(entry['source']) or '-'}")

    for name in NO_MARK:
        manifest.setdefault(name, {"slug": norm(name), "hex": None, "mono": None,
                                   "color": None, "source": [], "note": "no vector mark in any source"})

    (LIB / "logos.json").write_text(json.dumps({
        "built": "content/_logos.py",
        "sources": {
            "si": "simple-icons, CC0, monochrome single path plus official brand hex",
            "lobe": "@lobehub/icons-static-svg, MIT, AI model marks",
            "gil": "gilbarbara/logos, CC0, official full colour artwork",
            "dash": "homarr-labs/dashboard-icons, MIT, app marks",
        },
        "note": "Files are freely licensed. Trademarks are not: a third party mark in a "
                "commercial piece needs the operator's approval per CLAUDE.md 18.",
        "tools": manifest,
    }, indent=1) + "\n")
    return manifest


def measure(png: pathlib.Path) -> tuple[float, float]:
    """Mean luminance of the mark's own pixels, and the aspect of the ink itself.

    Two things a material cannot know from the filename. Luminance: a colour mark is often
    near black artwork (Vercel, Cursor, ChatGPT), which disappears on the slate card, so the
    white variant has to be used instead. Ink aspect: a viewBox says nothing, since Simple
    Icons draws every mark inside a 24x24 square, wordmarks included. Stripe's mark is a wide
    band inside that square and it needs a wide slot, not a tile.
    """
    from PIL import Image

    im = Image.open(png).convert("RGBA")
    a = im.getchannel("A")
    box = a.point(lambda v: 255 if v > 40 else 0).getbbox()
    small = im.resize((96, 96))
    px = [p for p in small.getdata() if p[3] > 40]
    lum = (sum(0.2126 * r + 0.7152 * g + 0.0722 * b for r, g, b, _ in px) / (len(px) * 255)
           if px else 0.0)
    ar = ((box[2] - box[0]) / (box[3] - box[1])) if box and box[3] > box[1] else 1.0
    return lum, ar


def rasterise(manifest: dict, size: int) -> int:
    """PNG at brand colour and in white, for anything outside the HTML pipeline."""
    from playwright.sync_api import sync_playwright

    ch = sorted(pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"))
    out = LIB / "png"
    out.mkdir(parents=True, exist_ok=True)
    jobs = []
    for name, e in manifest.items():
        slug = e["slug"]
        if e.get("color"):
            jobs.append((slug, (WORK / e["color"]).read_text(), None, f"{slug}-{size}.png"))
        elif e.get("mono"):
            svg = (WORK / e["mono"]).read_text()
            hexv = "#" + (e.get("hex") or "FFFFFF")
            jobs.append((slug, svg, hexv, f"{slug}-{size}.png"))
            jobs.append((slug, svg, "#FFFFFF", f"{slug}-{size}-w.png"))
    seen, n = set(), 0
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=str(ch[-1]) if ch else None)
        pg = b.new_page(viewport={"width": size, "height": size})
        for slug, svg, fill, fn in jobs:
            if fn in seen:
                continue
            seen.add(fn)
            svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
            m = re.match(r"\s*<svg[^>]*>", svg)
            if m:
                svg = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)) + svg[m.end():]
            tint = f"svg,svg *{{fill:{fill} !important}}" if fill else ""
            pg.set_content(
                f"<style>html,body{{margin:0;background:transparent}}"
                f"#w{{width:{size}px;height:{size}px;display:flex;align-items:center;"
                f"justify-content:center}}#w svg{{width:88%;height:88%}}{tint}</style>"
                f"<div id='w'>{svg}</div>")
            pg.locator("#w").screenshot(path=str(out / fn), omit_background=True)
            n += 1
        b.close()

    # write the measured luminance back, so a material can pick the readable variant
    for name, e in manifest.items():
        slug = e.get("slug")
        p = out / f"{slug}-{size}.png"
        if p.exists():
            lum, ar = measure(p)
            e["lum"] = round(lum, 3)
            e["dark"] = lum < 0.30          # invisible on the slate card without a white variant
            e["ink_aspect"] = round(ar, 2)
            e["wide_ink"] = ar > 2.0        # a band, not a tile: give it a wide slot
            e["png"] = p.name
            w = out / f"{slug}-{size}-w.png"
            if w.exists():
                e["png_white"] = w.name
    doc = json.loads((LIB / "logos.json").read_text())
    doc["tools"] = manifest
    doc["raster"] = {"size": size, "dir": "content/assets/logos/png"}
    (LIB / "logos.json").write_text(json.dumps(doc, indent=1) + "\n")
    return n


def sheet(manifest: dict) -> pathlib.Path:
    from playwright.sync_api import sync_playwright

    ch = sorted(pathlib.Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"))
    cells = []
    for name, e in sorted(manifest.items()):
        f = e.get("color") or e.get("mono")
        if not f:
            ini = re.sub(r"[^A-Za-z]", "", name)[:1].upper() or "?"
            art = f"<span class='mn'>{ini}</span>"
            cls = "miss"
        else:
            s = (WORK / f).read_text()
            s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
            m = re.match(r"\s*<svg[^>]*>", s)
            if m:
                s = re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)) + s[m.end():]
            art, cls = s, ("col" if e.get("color") else "mono")
            # Black artwork on a slate card is invisible. A light chip behind it is what a real
            # product tile does, and it is what the material has to do too.
            if e.get("color") and e.get("dark"):
                cls += " lt"
        cells.append(f"<div class='c {cls}'><div class='a'>{art}</div>"
                     f"<div class='n'>{name}</div></div>")
    cols = 10
    html = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap');
*{{box-sizing:border-box}}
body{{margin:0;background:#191919;padding:46px;font-family:'DM Mono',monospace}}
h1{{color:#FAFAF7;font-size:23px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 6px}}
p{{color:rgba(250,250,247,.46);font-size:12.5px;letter-spacing:.10em;margin:0 0 30px}}
.g{{display:grid;grid-template-columns:repeat({cols},1fr);gap:14px}}
.c{{background:#262625;border:1px solid rgba(250,250,247,.10);border-radius:12px;
   padding:16px 8px 11px;display:flex;flex-direction:column;align-items:center;gap:10px}}
.a{{width:56px;height:56px;display:flex;align-items:center;justify-content:center}}
.a svg{{width:100%;height:100%}}
.mono .a svg,.mono .a svg *{{fill:#FAFAF7}}
.lt{{background:#FAFAF7;border-color:rgba(25,25,25,.12)}}
.lt .n{{color:rgba(25,25,25,.66)}}
.miss{{border-color:rgba(204,120,92,.32);background:rgba(204,120,92,.07)}}
.mn{{font-size:27px;font-weight:500;color:#CC785C}}
.n{{font-size:9.5px;letter-spacing:.06em;color:rgba(250,250,247,.72);text-align:center;
   line-height:1.25;word-break:break-word}}
.miss .n{{color:#CC785C}}
</style>
<h1>Brand mark library</h1>
<p>{sum(1 for e in manifest.values() if e.get('color'))} colour ·
{sum(1 for e in manifest.values() if e.get('mono') and not e.get('color'))} monochrome ·
{sum(1 for e in manifest.values() if not e.get('mono') and not e.get('color'))} no mark, monogram tile</p>
<div class='g'>{''.join(cells)}</div>"""
    tmp = LIB / "_sheet.html"
    tmp.write_text(html)
    out = LIB / "library-sheet.png"
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=str(ch[-1]) if ch else None)
        pg = b.new_page(viewport={"width": 1500, "height": 900}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(1400)
        pg.screenshot(path=str(out), full_page=True)
        b.close()
    tmp.unlink(missing_ok=True)
    return out


def find(q: str, idx: dict) -> None:
    k = norm(q)
    for src in ("si", "lobe", "gil", "dash"):
        pool = idx[src]
        hit = [x for x in pool if k in x]
        if hit:
            print(f"  {src:<5} {', '.join(sorted(hit)[:14])}")
    if not any(k in idx[s] for s in idx):
        print("  nothing, in any of the four sources")


def report(manifest: dict) -> None:
    col = [n for n, e in manifest.items() if e.get("color")]
    mono = [n for n, e in manifest.items() if e.get("mono") and not e.get("color")]
    miss = [n for n, e in manifest.items() if not e.get("mono") and not e.get("color")]
    print(f"  colour     {len(col)}")
    print(f"  mono only  {len(mono)}   {', '.join(sorted(mono))}")
    print(f"  no mark    {len(miss)}   {', '.join(sorted(miss))}")
    print(f"  library    {len(list((LIB / 'mono').glob('*.svg')))} mono, "
          f"{len(list((LIB / 'ai').glob('*.svg')))} ai, "
          f"{len(list((LIB / 'png').glob('*.png')))} png")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--png", type=int, default=0)
    ap.add_argument("--sheet", action="store_true")
    ap.add_argument("--find")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if not any((a.sync, a.install, a.png, a.sheet, a.find, a.report)):
        ap.print_help()
        return

    if a.sync or a.force or not CACHE.exists():
        print("sync")
        sync(a.force)
    idx = indexes()

    mpath = LIB / "logos.json"
    manifest = json.loads(mpath.read_text())["tools"] if mpath.exists() else {}

    if a.find:
        print(f"find {a.find}")
        find(a.find, idx)
        return
    if a.install:
        print("install")
        manifest = install(idx)
    if a.png:
        print(f"raster {a.png}px")
        print(f"  {rasterise(manifest, a.png)} png written")
    if a.sheet:
        print("sheet")
        print(f"  {sheet(manifest)}")
    if a.report or a.install:
        print("report")
        report(manifest)


if __name__ == "__main__":
    main()
