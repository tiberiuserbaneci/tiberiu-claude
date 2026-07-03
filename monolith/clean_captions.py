#!/usr/bin/env python3
# operator 2026-07-03: strip the "reply to the first 20" promise + the "it's in my bio" redirect
# from every caption (we want max comments; no TikTok bio link yet).
import os, json, re, time, urllib.request, urllib.error, ssl
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
CA="/root/.ccr/ca-bundle.crt"; ctx=ssl.create_default_context(cafile=CA)
def d1(sql,params=None):
    body={"sql":sql};
    if params is not None: body["params"]=params
    for att in range(6):
        try:
            r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query",data=json.dumps(body).encode(),method="POST")
            r.add_header("Authorization",f"Bearer {TOKEN}"); r.add_header("Content-Type","application/json")
            out=json.loads(urllib.request.urlopen(r,context=ctx,timeout=60).read()); break
        except urllib.error.HTTPError as e:
            if e.code!=429 or att==5: raise
            time.sleep(3*2**att)
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

def clean(c):
    c=c.replace(" and I reply to the first 20","")
    c=re.sub(r"[^.\n]*is in my bio right now, so no waiting on a DM\.\s*","",c)
    c=c.replace("I will send it too,","I will send it,")
    return c

rows=d1(f"SELECT id,caption FROM vault_items WHERE owner='{OWNER}' AND (caption LIKE '%first 20%' OR caption LIKE '%in my bio%')")
print("to clean:",len(rows)); n=0
for r in rows:
    nc=clean(r["caption"])
    if nc!=r["caption"]:
        d1("UPDATE vault_items SET caption=? WHERE id=?",[nc,r["id"]]); n+=1
print("cleaned:",n)
