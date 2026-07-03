#!/usr/bin/env python3
# Replace an Instagram vault row's media with a SINGLE motion-reel video (the whole IG deliverable
# is one reel, not a carousel). Usage: put_reel.py <slug-tag> <LABEL substring> <reel.mp4> <thumb.png>
# e.g. put_reel.py aios "THE AI OPERATING SYSTEM" scratchpad/reel_aios.mp4 scratchpad/reel_aios_thumb.png
import os, json, time, urllib.request, urllib.error, ssl, sys
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method); r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=300) as resp: return resp.read()
def r2put(key,path,ct):
    for att in range(5):
        try: req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",open(path,"rb").read(),ct); return
        except Exception as e:
            if att==4: raise
            time.sleep(2**att)
def d1(sql):
    for att in range(6):
        try:
            out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps({"sql":sql}).encode(),"application/json")); break
        except urllib.error.HTTPError as e:
            if e.code!=429 or att==5: raise
            time.sleep(3*2**att)
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]
def esc(s): return s.replace("'","''")

slug,label,reel,thumb=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
rows=d1(f"SELECT id,name,media,thumb_key FROM vault_items WHERE owner='{OWNER}' AND name LIKE '%{esc(label)}%' AND name LIKE '%Instagram)%'")
if not rows: raise SystemExit(f"IG row not found for label: {label}")
r=rows[0]; rid=r["id"]; print("row:",r["name"])
old=json.loads(r["media"]); print("old media items:",len(old))
did=str(int(time.time()))
vkey=f"imports/pm/{slug}-igreel-{did}/reel.mp4"; tkey=f"imports/pm/{slug}-igreel-{did}/thumb.png"
r2put(vkey,reel,"video/mp4"); r2put(tkey,thumb,"image/png")
media=[{"key":vkey,"type":"video","ext":"mp4","contentType":"video/mp4"}]
d1(f"UPDATE vault_items SET media='{esc(json.dumps(media))}', thumb_key='{tkey}' WHERE id='{rid}'")
print(f"OK {slug} IG -> single reel video; thumb=frame; key={vkey}")
