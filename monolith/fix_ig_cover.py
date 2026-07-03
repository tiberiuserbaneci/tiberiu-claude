#!/usr/bin/env python3
# Fix IG Scraped covers: slide 1 must be a TRANSPARENT overlay (operator). Regenerate cover_ig per slug
# (transparent 1350), compose transparent 1920 (paste at OY, no solid bg), overwrite the R2 object at the
# row's existing media[0] key. No new rows. Usage: python3 fix_ig_cover.py [slug ...]  (default: all)
import os, sys, json, io, re, time, ssl, urllib.request, importlib.util
from PIL import Image
ROOT="/home/user/tiberiu-claude"; HS=f"{ROOT}/content/_hitl-src"
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
BUCKET="ultron-reels"; CA="/root/.ccr/ca-bundle.crt"
W,H,CARD_H=1080,1920,1350; OY=(H-CARD_H)//2
ctx=ssl.create_default_context(cafile=CA)
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method); r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    return urllib.request.urlopen(r,context=ctx,timeout=180).read()
def d1(sql):
    out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps({"sql":sql}).encode(),"application/json"))
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]
def r2put(key,data):
    # raw key (matches push_adapted.py); quoting the slashes would land on a different object
    for a in range(5):
        try: req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",data,"image/png"); return
        except Exception:
            if a==4: raise
            time.sleep(2**a)

def render_cover_1350(slug,out):
    bf=f"{HS}/build_{slug}.py"
    if not os.path.exists(bf): return False
    sys.argv=["build_ed45.py",bf,slug]
    spec=importlib.util.spec_from_file_location(f"ed_{slug}_{int(time.time()*1000)%100000}",f"{HS}/build_ed45.py")
    ed=importlib.util.module_from_spec(spec); spec.loader.exec_module(ed)
    ed.cover_ig(out)  # transparent 1080x1350
    return True

def make_1920(src):
    card=Image.open(src).convert("RGBA")
    canvas=Image.new("RGBA",(W,H),(0,0,0,0))
    canvas.alpha_composite(card,(0,OY))
    b=io.BytesIO(); canvas.save(b,"PNG"); return b.getvalue(), canvas.split()[3].getextrema()[0]

rows=d1(f"SELECT id,name,media FROM vault_items WHERE owner='{OWNER}' AND tags LIKE '%IG Scraped%' ORDER BY created_at DESC")
only=set(sys.argv[1:])
done=[]; skip=[]
tmp=f"{ROOT}/scratchpad/_covfix.png"
for r in rows:
    m=json.loads(r["media"]); k=m[0]["key"]
    if m[0].get("type")=="video": skip.append((r["name"][:30],"video")); continue
    mm=re.search(r"imports/pm/([a-z0-9]+)-(?:v2ig|igc1|ig)-",k)
    slug=mm.group(1) if mm else None
    if not slug: skip.append((k[-30:],"no-slug")); continue
    if only and slug not in only: continue
    if not render_cover_1350(slug,tmp): skip.append((slug,"no-build")); continue
    data,amin=make_1920(tmp)
    if amin>=250: skip.append((slug,"not-transparent?!")); continue
    r2put(k,data); done.append(slug)
    print(f"fixed {slug:16} -> {k[-40:]} (amin={amin})")
print("\nDONE fixed:",len(done)); print("skipped:",skip)
