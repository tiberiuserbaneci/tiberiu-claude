#!/usr/bin/env python3
# Bump the Tier-3 rebuilt materials (eyes + the 10 batch) to the top of the vault:
# give their rows the highest created_at, then restamp keeps them first (non-posted DESC).
import os, json, time, urllib.request, urllib.error, ssl
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
CA="/root/.ccr/ca-bundle.crt"; ctx=ssl.create_default_context(cafile=CA)
def d1(sql,params=None):
    body={"sql":sql}
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
def esc(s): return s.replace("'","''")

# desired top order (newest first): eyes, then the batch of 10
TITLES=["WIRE ITS EYES","THE AI OPERATING SYSTEM","PROMPTS ARE DEAD, LOOPS RUN","THE COMPLETE AI BODY",
 "5 SIGNS YOU NEED AI NOW","THE 500K CONTENT DESK","STUCK AT LEVEL ONE","THE HIDDEN SKILLS",
 "THE CAROUSEL COMMAND","HOW REAL AGENTS ARE BUILT","60 MINUTES TO AN OPERATOR"]
base=9_000_000_000_000; step=1000; i=0
for tt in TITLES:
    for suf in ("(TikTok 3D)","(Instagram)"):
        rows=d1(f"SELECT id,name FROM vault_items WHERE owner='{OWNER}' AND name LIKE 'Review%{esc(tt)}%{esc(suf)}%'")
        for r in rows:
            d1(f"UPDATE vault_items SET created_at={base-i*step} WHERE id='{r['id']}'"); i+=1
            print("bumped",r["name"][:52])
print("bumped",i,"rows to top")
