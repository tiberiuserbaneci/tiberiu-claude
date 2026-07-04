#!/usr/bin/env python3
# Replace an IG Scraped row's FULL media with the rebuilt dense _tt deck (new cachebust keys).
# Slide 1 stays the transparent cover. Usage: python3 push_dense_tt.py <slug> <NAME substring>
import os, sys, json, glob, time, ssl, urllib.request
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
BUCKET="ultron-reels"; CA="/root/.ccr/ca-bundle.crt"; ROOT="/home/user/tiberiu-claude"
ctx=ssl.create_default_context(cafile=CA)
def req(u,m="GET",d=None,ct=None):
    r=urllib.request.Request(u,data=d,method=m); r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    return urllib.request.urlopen(r,context=ctx,timeout=180).read()
def d1(sql):
    o=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps({"sql":sql}).encode(),"application/json"))
    if not o.get("success"): raise RuntimeError(o.get("errors"))
    return o["result"][0]["results"]
def r2put(k,p,ct):
    for a in range(5):
        try: req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{k}","PUT",open(p,"rb").read(),ct); return
        except Exception:
            if a==4: raise
            time.sleep(2**a)
def esc(s): return s.replace("'","''")

slug=sys.argv[1]; namesub=sys.argv[2]
files=sorted(glob.glob(f"{ROOT}/scratchpad/{slug}_tt/s*.png"), key=lambda f:int("".join(c for c in os.path.basename(f) if c.isdigit())))
if not files: raise SystemExit(f"no slides for {slug}")
bust=str(int(time.time()))
keys=[]
for i,f in enumerate(files,1):
    k=f"imports/pm/{slug}-dense-{bust}/{i:02d}.png"; r2put(k,f,"image/png"); keys.append(k)
media=json.dumps([{"key":x,"type":"image","ext":"png","contentType":"image/png"} for x in keys])
rows=d1(f"SELECT id,name FROM vault_items WHERE owner='{OWNER}' AND name LIKE '%{esc(namesub)}%' AND name LIKE '%TikTok%'")
if not rows: raise SystemExit(f"row not found: {namesub}")
rid=rows[0]["id"]
d1(f"UPDATE vault_items SET media='{esc(media)}', thumb_key='{esc(keys[0])}' WHERE id='{rid}'")
print(f"{slug}: TT row '{rows[0]['name']}' -> {len(keys)} dense slides, thumb={keys[0]}")
