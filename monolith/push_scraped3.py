#!/usr/bin/env python3
# Push an adapted "IG Scraped 3" material: UPDATE the existing source row with the IG deck (1920),
# and INSERT a paired TikTok 3D row (1350). Both tagged ["IG Scraped 3"]. Title read from build_{slug}.py.
# Usage: python3 push_scraped2.py <slug> <row_id>
import os, sys, json, glob, time, ssl, re, urllib.request, uuid
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
BUCKET="ultron-reels"; CA="/root/.ccr/ca-bundle.crt"; ROOT="/home/user/tiberiu-claude"
ctx=ssl.create_default_context(cafile=CA)
def req(u,m="GET",d=None,ct=None):
    r=urllib.request.Request(u,data=d,method=m); r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    return urllib.request.urlopen(r,context=ctx,timeout=180).read()
def d1(sql,params=None):
    b={"sql":sql}
    if params is not None: b["params"]=params
    o=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps(b).encode(),"application/json"))
    if not o.get("success"): raise RuntimeError(o.get("errors"))
    return o["result"][0]["results"]
def r2put(k,p):
    for a in range(5):
        try: req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{k}","PUT",open(p,"rb").read(),"image/png"); return
        except Exception:
            if a==4: raise
            time.sleep(2**a)
def esc(s): return s.replace("'","''")
def upload(slug,kind,bust):
    files=sorted(glob.glob(f"{ROOT}/scratchpad/{slug}_{kind}/s*.png"), key=lambda f:int("".join(c for c in os.path.basename(f) if c.isdigit())))
    keys=[]
    for i,f in enumerate(files,1):
        k=f"imports/pm/{slug}-s3{kind}-{bust}/{i:02d}.png"; r2put(k,f); keys.append(k)
    media=json.dumps([{"key":x,"type":"image","ext":"png","contentType":"image/png"} for x in keys])
    return media,keys

slug=sys.argv[1]; row_id=sys.argv[2]
title=""
try:
    src=open(f"{ROOT}/content/_hitl-src/build_{slug}.py").read()
    m=re.search(r'TITLE\s*=\s*[\'"]([^\'"]+)[\'"]',src); title=m.group(1) if m else slug.upper()
except Exception: title=slug.upper()
bust=str(int(time.time()))
ig_media,ig_keys=upload(slug,"ig",bust)
d1(f"UPDATE vault_items SET media='{esc(ig_media)}', thumb_key='{esc(ig_keys[0])}', name='Review · {esc(title)} (Instagram)' WHERE id='{esc(row_id)}'")
print(f"{slug}: IG row updated -> {len(ig_keys)} slides")
time.sleep(3)
tt_media,tt_keys=upload(slug,"tt",bust)
# reuse the source row's created_at minus 1 so the TT row sits right under its IG pair
ca=d1(f"SELECT created_at FROM vault_items WHERE id='{esc(row_id)}'")[0]["created_at"]
vid=str(uuid.uuid4())
d1("INSERT INTO vault_items (id,owner,kind,name,source,media,thumb_key,tags,created_at,caption) VALUES (?,?,?,?,?,?,?,?,?,?)",
   [vid,OWNER,"carousel",f"Review · {title} (TikTok 3D)","ig-scraped-3",tt_media,tt_keys[0],'["IG Scraped 3"]',ca-1,""])
print(f"{slug}: TT row inserted -> {len(tt_keys)} slides | title='{title}'")
