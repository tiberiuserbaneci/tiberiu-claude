#!/usr/bin/env python3
"""Portal scanner: builds content/portal/manifest.json from everything in content/.
Renders thumbnails for reference HTMLs, zips carousels, parses caption files.
Merges with the existing manifest so posted/analytics/crosspost state is preserved."""
import json, re, pathlib, zipfile, datetime, subprocess, struct
ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
PORTAL = CONTENT / "portal"
THUMBS = PORTAL / "thumbs"
ZIPS = PORTAL / "zips"
for d in (PORTAL, THUMBS, ZIPS, CONTENT / "analytics"):
    d.mkdir(parents=True, exist_ok=True)
MANIFEST = PORTAL / "manifest.json"

VARIANTS = {"journey","tiles","panel","dashboard","hub","org","radar","roster","cheatsheet","overview"}
def is_variant(tok): return tok in VARIANTS or re.fullmatch(r"v\d+", tok) is not None

def channel_of(name):
    if "linkedin" in name: return "linkedin"
    if "tiktok" in name: return "tiktok"
    if re.search(r"(-ig-|story|highlight|instagram)", name): return "instagram"
    return "linkedin"

def material_id(name):
    """Group key: carousels by slide, linkedin/single by trailing variant/version."""
    if "carousel" in name:
        return name.split("-carousel")[0] + "-tiktok-carousel"
    toks = name.split("-")
    while len(toks) > 2 and is_variant(toks[-1]):
        toks.pop()
    return "-".join(toks)

def slug_prefix(mid):
    """docs-05-jobs-linkedin -> docs-05-jobs ; docs-05-jobs-tiktok-carousel -> docs-05-jobs"""
    for ch in ("-tiktok","-linkedin","-ig","-instagram"):
        if ch in mid: return mid.split(ch)[0]
    return mid

def parse_caption(md_path):
    if not md_path.exists(): return {}
    t = md_path.read_text()
    def section(*names):
        for n in names:
            m = re.search(r"##\s*"+re.escape(n)+r"\b(.*?)(?=\n##\s|\n---|\Z)", t, re.S|re.I)
            if m: return m.group(1).strip().lstrip("(").strip()
        return ""
    cap = section("CAPTION","PRIMARY")
    return {"caption": cap, "alt": section("ALT TEXT","ALT"), "first_comment": section("FIRST COMMENT")}

def find_caption(prefix, channel):
    cands = []
    if channel == "tiktok":
        cands = [f"{prefix}-tiktok-caption.md"]
    else:
        cands = [f"{prefix}-caption.md", f"{prefix}-copy.md", f"{prefix}-linkedin-caption.md"]
    for c in cands:
        p = CONTENT / c
        if p.exists(): return parse_caption(p)
    return {}

def title_from(mid):
    # docs-05-jobs-linkedin -> "Background Jobs"; pretty-ish from slug
    s = slug_prefix(mid)
    s = re.sub(r"^docs-\d+-", "", s); s = re.sub(r"^ref-\d+-", "", s)
    return s.replace("-", " ").title()

def git_date(path):
    try:
        out = subprocess.run(["git","log","-1","--format=%cs","--",str(path)], cwd=ROOT,
                             capture_output=True, text=True, timeout=10).stdout.strip()
        return out or datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()

# ---- material dimensions (corner badge in the portal) ----
KNOWN_LOGICAL = {(1080, 1450), (1080, 1920)}
def png_size(path):
    """Read width/height straight from the PNG IHDR header (no Pillow needed)."""
    try:
        b = open(path, "rb").read(26)
        if b[:8] == b"\x89PNG\r\n\x1a\n" and b[12:16] == b"IHDR":
            return struct.unpack(">II", b[16:24])
    except Exception:
        pass
    return None
def html_canvas_size(path):
    """Pull the canvas size out of a reference poster's CSS (the box is always 1080 wide)."""
    try:
        t = path.read_text(errors="ignore")
    except Exception:
        return None
    m = re.search(r"width:\s*1080px\s*;\s*height:\s*(\d+)px", t)   # .poster / .canvas / .slide, any name
    if m:
        return (1080, int(m.group(1)))
    for sel in (r"\.canvas", r"\.poster", r"\.slide", r"\.frame", r"#artifact"):
        m = re.search(sel + r"\s*\{[^}]*?width:\s*(\d+)px[^}]*?height:\s*(\d+)px", t, re.S)
        if m:
            return (int(m.group(1)), int(m.group(2)))
    return None
def fmt_dims(wh):
    """'1080x1920' native, or '2160x2900 (1080x1450 @2x)' for a 2x export."""
    if not wh:
        return ""
    w, h = wh
    if (w, h) in KNOWN_LOGICAL:
        return f"{w}x{h}"
    if w % 2 == 0 and h % 2 == 0 and (w // 2, h // 2) in KNOWN_LOGICAL:
        return f"{w}x{h} ({w // 2}x{h // 2} @2x)"
    return f"{w}x{h}"

# ---- gather generated materials (docs-*, ref-*) from PNGs ----
mats = {}
pngs = [p for p in CONTENT.glob("*.png") if p.name != "ultron-logo.png" and not p.name.startswith("script-")]
for p in sorted(pngs):
    name = p.stem
    mid = material_id(name)
    ch = channel_of(name)
    typ = "carousel" if "carousel" in name else "single"
    m = mats.setdefault(mid, {"id": mid, "channel": ch, "type": typ, "files": [], "source":"generated"})
    m["files"].append("content/"+p.name)

materials = []
for mid, m in mats.items():
    files = sorted(m["files"])
    typ = m["type"]; ch = m["channel"]
    if typ == "carousel":
        slides = files
        preview = slides[0]
        zpath = ZIPS / (mid + ".zip")
        with zipfile.ZipFile(zpath, "w") as z:
            for i, f in enumerate(slides, 1):
                z.write(ROOT / f, arcname=f"{mid}-{i:02d}.png")
        download = "content/portal/zips/" + zpath.name
        nslides = len(slides)
    else:
        # pick newest as preview, rest are alternates
        files_sorted = sorted(files, key=lambda f: (ROOT/f).stat().st_mtime, reverse=True)
        preview = files_sorted[0]; download = preview; slides=[]; nslides=1; zpath=None
    dim_src = slides[0] if typ == "carousel" else preview
    dims = fmt_dims(png_size(ROOT / dim_src))
    cap = find_caption(slug_prefix(mid), ch)
    materials.append({
        "id": mid, "title": title_from(mid),
        "channel": ch, "type": typ, "slides": nslides, "dims": dims,
        "preview": preview, "download": download,
        "files": files, "variants": [pathlib.Path(f).stem.split(mid.replace('content/',''))[-1].strip('-') for f in files] if typ!="carousel" else [],
        "caption": cap.get("caption",""), "alt": cap.get("alt",""), "first_comment": cap.get("first_comment",""),
        "generated_date": git_date(ROOT/preview), "source": "generated",
        "status": "ready", "posted": False, "posted_date": None,
        "analytics": None, "crossposts": []
    })

# ---- references (script-*.html / logos-reference.html) -> thumbnails ----
ref_htmls = sorted(CONTENT.glob("script-*.html")) + sorted(CONTENT.glob("logos-reference.html"))
refs = []
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for h in ref_htmls:
            mid = h.stem
            thumb = THUMBS / (mid + ".png")
            if not thumb.exists():
                try:
                    pg = b.new_page(viewport={"width":1080,"height":1500})
                    pg.goto(h.as_uri(), wait_until="load", timeout=8000)
                    pg.wait_for_timeout(700)
                    pg.evaluate("document.body.style.zoom='0.42'")
                    pg.wait_for_timeout(150)
                    el = pg.query_selector("#artifact,.canvas,.frame,.slide") or pg.query_selector("body")
                    el.screenshot(path=str(thumb))
                    pg.close()
                except Exception as e:
                    print("thumb fail", mid, e)
            refs.append((mid, thumb))
        b.close()
except Exception as e:
    print("playwright unavailable:", e)
    refs = [(h.stem, THUMBS/(h.stem+".png")) for h in ref_htmls]

for mid, thumb in refs:
    ch = channel_of(mid)
    rwh = html_canvas_size(CONTENT / (mid + ".html")) or ((1080, 1450) if ch == "linkedin" else (1080, 1920))
    materials.append({
        "id": mid, "title": title_from(mid).replace("Script","Script "),
        "channel": ch, "type": "single", "slides": 1, "dims": fmt_dims(rwh),
        "preview": "content/portal/thumbs/"+thumb.name if thumb.exists() else None,
        "download": "content/"+mid+".html", "files": ["content/"+mid+".html"], "variants": [],
        "caption": "", "alt": "", "first_comment": "",
        "generated_date": git_date(CONTENT/(mid+".html")), "source": "reference",
        "status": "needs-revision", "posted": False, "posted_date": None,
        "analytics": None, "crossposts": []
    })

# ---- merge with existing manifest: preserve state, deletions, and cross-post clones ----
state_keys = ("posted","posted_date","analytics","analytics_uploaded","crossposts","status")
old_doc = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
old = {m["id"]: m for m in old_doc.get("materials", [])}
deleted = old_doc.get("deleted", [])
deleted_ids = {d["id"] for d in deleted}

# drop anything the operator removed from the portal (source files stay on disk, recoverable via Restore)
materials = [m for m in materials if m["id"] not in deleted_ids]

for m in materials:
    o = old.get(m["id"])
    if o:
        for k in state_keys:
            if k in o and not (k == "status" and m["source"] == "reference"):
                m[k] = o[k]

# re-attach cross-post clones (not file-backed): refresh their assets from the origin, keep their own channel + state
by_id = {m["id"]: m for m in materials}
present = set(by_id)
for o in old.values():
    if o.get("source") == "crosspost" and o["id"] not in present and o["id"] not in deleted_ids:
        origin = by_id.get(o.get("origin"))
        if origin:
            for k in ("preview","download","files","slides","type","caption","alt","first_comment","dims"):
                if k in origin:
                    o[k] = origin[k]
            materials.append(o)

manifest = {"generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
            "counts": {"total": len(materials),
                       "generated": sum(1 for m in materials if m["source"]=="generated"),
                       "reference": sum(1 for m in materials if m["source"]=="reference"),
                       "crosspost": sum(1 for m in materials if m["source"]=="crosspost")},
            "deleted": deleted,
            "materials": sorted(materials, key=lambda m:(m["source"]!="generated", m["channel"], m["id"]))}
MANIFEST.write_text(json.dumps(manifest, indent=2))
print(f"manifest: {manifest['counts']}  -> {MANIFEST}")
