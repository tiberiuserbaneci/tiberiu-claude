#!/usr/bin/env python3
# Replace the MEDIA of existing vault rows (rebuild flow: same row, new slides - no duplicates).
# Uploads a fresh R2 dir per deck and UPDATEs media/thumb_key/name-timestamp on the matched row.
import os, sys, json, time, glob, urllib.request, ssl

ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()

def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method)
    r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=120) as resp: return resp.read()

def r2put(key,path):
    for att in range(5):
        try:
            req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",open(path,"rb").read(),"image/png")
            return
        except Exception as e:
            if att==4: raise
            time.sleep(2**att)

def d1(sql):
    import urllib.error
    for att in range(6):
        try:
            out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps({"sql":sql}).encode(),"application/json"))
            break
        except urllib.error.HTTPError as e:
            if e.code!=429 or att==5: raise
            time.sleep(3*2**att)
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

def esc(s): return s.replace("'","''")

# slug -> (vault label prefix, tt dir, ig dir)
DECKS={
 "solostack":  "THE SOLO STACK 4:5",        "stopsoftware":"STOP PAYING FOR SOFTWARE",
 "systems":    "SYSTEMS NOT EMPLOYEES",      "leadmachine": "THE LEAD MACHINE",
 "agency":     "A FULL AGENCY ONE CLAUDE",   "agentchatbot":"AN AGENT NOT A CHATBOT",
 "levels":     "SEVEN LEVELS OF ULTRON",     "onepersonrev":"THE 1-PERSON REVENUE STACK",
 "contentteam":"THE CONTENT TEAM",           "onepersonco": "THE ONE-PERSON COMPANY",
}
# + the 20 IG Scraped adaptations (titles from adapt_specs)
import importlib.util as _iu
_s=_iu.spec_from_file_location("_AS","/home/user/tiberiu-claude/content/_hitl-src/adapt_specs.py")
_AS=_iu.module_from_spec(_s); _s.loader.exec_module(_AS)
DECKS.update({d["slug"]:d["title"] for d in _AS.ALL})

if __name__=="__main__":
    slugs=sys.argv[1:] or list(DECKS)
    ts=time.strftime("%Y-%m-%d %H:%M"); dirid=str(int(time.time()))
    for slug in slugs:
        label=DECKS[slug]
        for suffix,chan,ddir in [("(TikTok 3D)","tt",f"scratchpad/{slug}_tt"),("(Instagram)","ig",f"scratchpad/{slug}_ig")]:
            rows=d1(f"SELECT id,name FROM vault_items WHERE owner='{OWNER}' AND name LIKE 'Review%{esc(label)}%{suffix.replace('(','').replace(')','')})%'")
            if not rows:
                rows=d1(f"SELECT id,name FROM vault_items WHERE owner='{OWNER}' AND name LIKE 'Review · {esc(label)} {suffix}%'")
            if not rows: print("MISS", label, suffix); continue
            rid=rows[0]["id"]
            pngs=sorted(glob.glob(f"{ddir}/s*.png"), key=lambda f:int(''.join(c for c in os.path.basename(f) if c.isdigit())))
            keys=[]
            for i,f in enumerate(pngs,1):
                k=f"imports/pm/{slug}-v2{chan}-{dirid}/{i:02d}.png"; r2put(k,f); keys.append(k)
            media=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
            name=f"Review · {label} {suffix} · {ts}"
            d1(f"UPDATE vault_items SET media='{esc(media)}', thumb_key='{keys[0]}', name='{esc(name)}' WHERE id='{rid}'")
            print("OK ", name, f"({len(keys)} media)")
    print("DONE")
