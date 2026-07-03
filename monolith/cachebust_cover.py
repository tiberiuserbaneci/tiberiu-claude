#!/usr/bin/env python3
# The transparent cover is already in R2 at the SAME key, so Monolith/browser serve the CACHED opaque
# copy. Fix: write the transparent cover under a NEW key (cachebust) and point media[0]+thumb_key to it.
# Usage: python3 cachebust_cover.py [slug ...]   (default: all IG Scraped)
import os, sys, json, io, re, time, ssl, urllib.request, importlib.util
from PIL import Image
ROOT="/home/user/tiberiu-claude"; HS=f"{ROOT}/content/_hitl-src"
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
BUCKET="ultron-reels"; CA="/root/.ccr/ca-bundle.crt"
W,H,CARD_H=1080,1920,1350; OY=(H-CARD_H)//2
BUST=str(int(time.time()))
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
    for a in range(5):
        try: req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",data,"image/png"); return
        except Exception:
            if a==4: raise
            time.sleep(2**a)
def esc(s): return s.replace("'","''")
BUILD={"agentchatbot":"agentnotchatbot"}  # slug -> build file name override
def render_1920(slug):
    bfslug=BUILD.get(slug,slug); bf=f"{HS}/build_{bfslug}.py"
    if not os.path.exists(bf): return None
    sys.argv=["build_ed45.py",bf,slug]
    spec=importlib.util.spec_from_file_location(f"ed_{slug}_{int(time.time()*1000)%100000}",f"{HS}/build_ed45.py")
    ed=importlib.util.module_from_spec(spec); spec.loader.exec_module(ed)
    tmp=f"{ROOT}/scratchpad/_cb.png"; ed.cover_ig(tmp)
    c=Image.open(tmp).convert("RGBA"); canvas=Image.new("RGBA",(W,H),(0,0,0,0)); canvas.alpha_composite(c,(0,OY))
    if canvas.split()[3].getextrema()[0]>=250: return None
    b=io.BytesIO(); canvas.save(b,"PNG"); return b.getvalue()

rows=d1(f"SELECT id,name,media,thumb_key FROM vault_items WHERE owner='{OWNER}' AND tags LIKE '%IG Scraped%'")
only=set(sys.argv[1:]); done=[]; skip=[]
for r in rows:
    m=json.loads(r["media"]); k=m[0]["key"]
    if m[0].get("type")=="video": continue
    mm=re.search(r"imports/pm/([a-z0-9]+)-(?:v2ig|igc1|ig)-",k)
    slug=mm.group(1) if mm else None
    if not slug: skip.append((k[-28:],"no-slug")); continue
    if only and slug not in only: continue
    data=render_1920(slug)
    if not data: skip.append((slug,"no-build/opaque")); continue
    newkey=re.sub(r"/01\.png$", f"/01-t{BUST}.png", k)
    r2put(newkey,data)
    m[0]["key"]=newkey
    d1(f"UPDATE vault_items SET media='{esc(json.dumps(m))}', thumb_key='{esc(newkey)}' WHERE id='{r['id']}'")
    done.append(slug); print(f"cachebust {slug:16} -> {newkey[-42:]}")
print("\nDONE:",len(done),"| skip:",skip)
