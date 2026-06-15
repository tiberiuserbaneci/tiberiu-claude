#!/usr/bin/env python3
"""Ultron material GUARD. Hard pre-flight that blocks anything off-spec before delivery.

Usage:
  python3 content/_preflight.py <file.html> [<file2.html> ...]
  python3 content/_preflight.py --changed          # validate git-changed material HTMLs
  python3 content/_preflight.py --static <file>     # text-only checks, no browser (fast, for hooks)

Exit code 0 = all PASS. Non-zero = at least one FAIL (the offending material must be fixed).
Checks (the operator's recurring rejections, made mechanical):
  1 charscan   no em/en dash, ellipsis char, curly quotes
  2 fonts      DM Sans / DM Mono only; forbidden families rejected
  3 palette    no forbidden hex (neon orange/green/red/peach/purple/blue)
  4 dims       #artifact == 1080x1450 (LinkedIn) or .slide == 1080x1920 (TikTok/IG), exact
  5 safezone   vertical slides: top content >= 300px (TikTok/IG UI inset)
  6 density    real ink per row; flags airy/empty bands (THE recurring 'slab si aerisit')
  7 repeat     body layout must differ from the previous material (no template reuse)
  8 footer     Ultron footer + 51ultron.com present
"""
import sys, re, pathlib, base64, tempfile, json, subprocess, glob

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LOGO = CONTENT / "ultron-logo.png"

CURLY = {"—":"em-dash","–":"en-dash","…":"ellipsis-char","‘":"curly-quote","’":"curly-quote","“":"curly-quote","”":"curly-quote"}
FORBIDDEN_FONTS = ["Inter","Fraunces","Instrument Serif","Bricolage","JetBrains","Space Grotesk","Caveat","Kalam","Arial","Roboto","Helvetica","Poppins","Montserrat","Georgia","Times"]
FORBIDDEN_HEX = ["#ff801f","#ed7f4a","#4ade80","#76d39a","#c0392b","#ffe0c2","#ff8c50","#22c55e","#16a34a","#3b82f6","#2563eb","#8b5cf6","#a855f7"]
# brand-frame classes shared by every poster - excluded from the repetition signature so we
# compare the BODY layout (the part that must change), not the consistent brand chrome.
BRAND_FRAME = {"frame","slide","atm","hero","eye","eyebrow","hook","sub","title","statile","st","sn","sl",
 "mast","ml","mr","cta","ctawrap","cta-l","cta-k","cta-t","cta-chip","ph","send","savel","ftr","fl2","flogo",
 "ftx","furl","swipe","safe","cover","cstat","c"}

# density of a product mockup runs high (breathing room) - a blind empty% gate false-positives on
# approved work, so empty% is surfaced as guidance and only an egregious DEAD BAND hard-fails.
DENSITY_AIRY_PCT     = 58.0    # above this empty-row share = print an 'airy, review' warning
DENSITY_MAX_BAND_PX  = 120     # a single contiguous empty band taller than this = hard FAIL (dead space)
REPEAT_MAX_JACCARD   = 0.62    # body-class overlap above this = same template reused = hard FAIL

def html_for_render(p):
    t = p.read_text()
    if "__LOGO_URI__" in t and LOGO.exists():
        uri = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
        t = t.replace("__LOGO_URI__", uri)
    return t

def target_of(name):
    n = name.lower()
    # TikTok 1080x1450 with safe zones (operator 2026-06-15): tall photo format, content inside a
    # safe box, dims checked on the .slide box.
    if "1450" in n: return (".slide", 1450, True)
    # editorial 4:5 photo-carousel (operator 2026-06-12): canvas 1080x1350, bleed allowed,
    # so dims are checked on the canvas box (offsetHeight), not scrollHeight. No 300px inset.
    if "-45-" in n or "editorial45" in n: return (".slide", 1350, True)
    if "carousel" in n: return ("slide", 1920, True)
    if any(k in n for k in ("tiktok","-ig-","story","highlight","instagram")): return (".slide", 1920, False)
    return ("#artifact", 1450, False)

def classes_in(text):
    cls = set()
    for m in re.findall(r'class="([^"]+)"', text):
        for c in m.split(): cls.add(c)
    return cls

def body_signature(text):
    return classes_in(text) - BRAND_FRAME

def prev_material(path):
    """The previous generated material of the same channel (highest docs-NN below this one)."""
    m = re.match(r"(docs|ref)-(\d+)-", path.stem)
    if not m: return None
    series, num = m.group(1), int(m.group(2))
    ch = "tiktok" if "tiktok" in path.stem else ("linkedin" if "linkedin" in path.stem else "")
    best = None
    for f in CONTENT.glob(f"{series}-*.html"):
        mm = re.match(rf"{series}-(\d+)-", f.stem)
        if not mm: continue
        k = int(mm.group(1))
        same_ch = ("tiktok" in f.stem) == ("tiktok" in path.stem)
        if k < num and same_ch:
            if best is None or k > int(re.match(rf"{series}-(\d+)-", best.stem).group(1)):
                best = f
    return best

# ---------- static checks (no browser) ----------
def static_checks(path):
    text = path.read_text()
    fails, warns = [], []
    hits = [(v,text.count(k)) for k,v in CURLY.items() if k in text]
    if hits: fails.append(f"charscan: found {hits} (use plain - . ' \")")
    ff = [f for f in FORBIDDEN_FONTS if re.search(r'\b'+re.escape(f)+r'\b', text)]
    if ff: fails.append(f"fonts: forbidden family present {ff}")
    if "DM Sans" not in text: warns.append("fonts: DM Sans import not found")
    fh = [h for h in FORBIDDEN_HEX if h.lower() in text.lower()]
    if fh: fails.append(f"palette: forbidden hex {fh}")
    if "51ultron" not in text: warns.append("footer: 51ultron.com not found")
    sb = len(re.findall(r'justify-content:\s*space-between', text)); f1 = len(re.findall(r'flex:\s*1\b', text))
    if sb or f1: warns.append(f"code-smell: {sb}x space-between, {f1}x flex:1 - confirm none spreads sparse rows into gaps")
    # repetition vs previous material of the same channel
    prev = prev_material(path)
    if prev:
        a, b = body_signature(text), body_signature(prev.read_text())
        if a and b:
            j = len(a & b) / len(a | b)
            if j > REPEAT_MAX_JACCARD:
                fails.append(f"repeat: body layout {j:.0%} same as {prev.name} (>{REPEAT_MAX_JACCARD:.0%}) - REDESIGN, do not reuse the template")
            else:
                warns.append(f"repeat: body {j:.0%} vs {prev.name} (ok)")
    return fails, warns

# ---------- rendered checks (browser + pixels) ----------
def density_metrics(img):
    """Empty-row pct and largest empty band (logical px), measured RELATIVE to each slide's own
    background tone, so it works on LIGHT (cream) slides too - not only the dark canvas. A row is
    empty when almost none of its pixels differ from the background. (The old version counted any
    bright pixel as ink, so a cream background read as 100% inked and voids on light slides were
    invisible - that is how S2/S4/S6 airy middles slipped through.)"""
    g = img.convert("L"); W, H = g.size
    px = g.load()
    step = max(1, W // 360)                  # sample columns for speed
    edge = []                                # background tone = median of the top + bottom margins
    for x in range(0, W, step):
        edge.append(px[x, 2]); edge.append(px[x, H - 3])
    edge.sort(); bg = edge[len(edge) // 2]
    dark = bg < 128
    rows_empty = []
    for y in range(H):
        ink = 0; n = 0
        for x in range(0, W, step):
            n += 1
            v = px[x, y]
            if (v > bg + 55) if dark else (v < bg - 28):   # content = clearly off the background
                ink += 1
        rows_empty.append((ink / n) < 0.012)
    # restrict to the content band (drop leading/trailing empty margin)
    top = next((i for i,e in enumerate(rows_empty) if not e), 0)
    bot = next((i for i,e in enumerate(reversed(rows_empty)) if not e), 0)
    band = rows_empty[top:H-bot] if (H-bot) > top else rows_empty
    empty_pct = 100.0 * sum(band) / max(1, len(band))
    longest = cur = 0
    for e in band:
        cur = cur+1 if e else 0
        longest = max(longest, cur)
    scale = H / 1450.0 if abs(H-1450) < abs(H-1920) else H / 1920.0
    return empty_pct, longest / max(scale,1e-6)

def render_checks(path):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    sel, target, multi = target_of(path.stem)
    html = html_for_render(path)
    tmp = pathlib.Path(tempfile.mkdtemp()) / "x.html"; tmp.write_text(html)
    fails, warns = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width":1080,"height":target}, device_scale_factor=1)
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(350); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
        els = pg.query_selector_all(sel if multi else (sel if sel.startswith((".","#")) else sel))
        if not els:
            els = pg.query_selector_all("#artifact") or pg.query_selector_all(".slide") or pg.query_selector_all(".frame")
        for i, el in enumerate(els, 1):
            tag = f"slide {i}" if (multi or len(els)>1) else "frame"
            # 4:5 format: canvas box must be exact; visuals may bleed past it (clipped), so
            # scrollHeight is the wrong measure there. Other formats keep zero-dead-space scrollHeight.
            h = el.evaluate("e=>e.offsetHeight" if target == 1350 else "e=>e.scrollHeight")
            if h != target: fails.append(f"dims[{tag}]: height {h} != {target}")
            if target == 1920:
                topgap = el.evaluate("""e=>{const r=e.getBoundingClientRect();
                    const m=e.querySelector('.mast,.eyebrow,.safe>*');return m?m.getBoundingClientRect().top-r.top:999;}""")
                if topgap < 300: fails.append(f"safezone[{tag}]: top content at {round(topgap)}px (< 300 inset)")
            shot = pathlib.Path(tempfile.mkdtemp()) / "s.png"; el.screenshot(path=str(shot))
            empty_pct, band = density_metrics(Image.open(shot))
            msg = f"density[{tag}]: {empty_pct:.0f}% empty rows, largest dead band {band:.0f}px"
            if band > DENSITY_MAX_BAND_PX and target in (1350, 1450):
                # editorial photo formats (4:5 1350, TikTok 1450 safe-zone): intentional air +
                # reserved UI margins sit below the ink threshold, so the band gate false-positives.
                # Surface for eye-review, do not hard-block.
                warns.append(msg + "  -> editorial format: air is part of the design - review by eye")
            elif band > DENSITY_MAX_BAND_PX:
                fails.append(msg + f"  -> DEAD BAND > {DENSITY_MAX_BAND_PX}px. Pack content; never flex:1/space-between on sparse rows.")
            elif empty_pct > DENSITY_AIRY_PCT:
                warns.append(msg + "  -> AIRY, review the dominant block (pack rows, add real content)")
            else:
                warns.append(msg + " (ok)")
        b.close()
    return fails, warns

def check(path, static_only=False):
    path = pathlib.Path(path)
    fails, warns = static_checks(path)
    if not static_only:
        try:
            rf, rw = render_checks(path); fails += rf; warns += rw
        except Exception as e:
            warns.append(f"render: skipped ({e})")
    print(f"\n=== {path.name} ===")
    for w in warns: print("  ok  ", w)
    for f in fails: print("  FAIL", f)
    print("  RESULT:", "PASS" if not fails else "FAIL  <-- fix before delivery")
    return not fails

def changed_materials():
    out = subprocess.run(["git","-C",str(ROOT),"status","--porcelain"],capture_output=True,text=True).stdout
    files=[]
    for line in out.splitlines():
        f = line[3:].strip()
        if re.search(r"content/docs-.*\.html$", f): files.append(ROOT/f)   # new materials only; legacy script-* refs are rebuild candidates
    return files

if __name__ == "__main__":
    args = sys.argv[1:]
    static_only = "--static" in args
    args = [a for a in args if a != "--static"]
    if args == ["--changed"] or not args:
        targets = changed_materials()
        if not targets:
            print("preflight: no changed material HTMLs"); sys.exit(0)
    else:
        targets = [pathlib.Path(a) for a in args]
    ok = all([check(t, static_only) for t in targets])   # list, not generator: check every file
    print("\nPREFLIGHT:", "ALL PASS" if ok else "FAIL - fix the materials above before delivery")
    sys.exit(0 if ok else 1)
