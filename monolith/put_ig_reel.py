#!/usr/bin/env python3
# Surgically replace slide 1 of the eyes IG row with the Veo reel video (keep slides 2-10 as images).
import os, json, time, urllib.request, urllib.error, ssl
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
SP="/home/user/tiberiu-claude/scratchpad/covers"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method); r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=180) as resp: return resp.read()
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

rows=d1(f"SELECT id,name,media,thumb_key FROM vault_items WHERE owner='{OWNER}' AND name LIKE 'Review%WIRE ITS EYES%Instagram)%'")
if not rows: raise SystemExit("IG row not found")
r=rows[0]; rid=r["id"]; media=json.loads(r["media"]); print("current slides:",len(media))
did=str(int(time.time()))
vkey=f"imports/pm/eyes-igreel-{did}/01.mp4"; tkey=f"imports/pm/eyes-igreel-{did}/thumb.png"
r2put(vkey,f"{SP}/ig_reel_intro.mp4","video/mp4")
r2put(tkey,f"{SP}/ig_reel_frame.png","image/png")
media[0]={"key":vkey,"type":"video","ext":"mp4","contentType":"video/mp4"}
d1(f"UPDATE vault_items SET media='{esc(json.dumps(media))}', thumb_key='{tkey}' WHERE id='{rid}'")
print("OK slide 1 -> reel video; slides 2-10 unchanged; thumb=frame")
