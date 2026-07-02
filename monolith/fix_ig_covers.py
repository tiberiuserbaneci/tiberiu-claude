#!/usr/bin/env python3
# Inlocuieste DOAR slide 1 (cover) pe randurile IG din vault cu varianta OPACA (operator
# 2026-07-02: overlay-urile transparente ies ALBE pe orice drum direct spre IG - Photos/
# AirDrop/IG aplatizeaza PNG->JPEG pe alb). Uploadeaza s1 nou, patchuieste media[0] + thumb.
# Include si randul Posted THE ONE-PERSON COMPANY (operator: "FIX LA TOATE", testa pe el).
# Usage: python3 fix_ig_covers.py <slug> ...
import os, sys, json, time, ssl, urllib.request, urllib.error
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"; BUCKET="ultron-reels"
ME="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; CA="/root/.ccr/ca-bundle.crt"
ctx=ssl.create_default_context(cafile=CA) if os.path.exists(CA) else ssl.create_default_context()
def req(url,method="GET",data=None,ct=None):
    r=urllib.request.Request(url,data=data,method=method)
    r.add_header("Authorization",f"Bearer {TOKEN}")
    if ct: r.add_header("Content-Type",ct)
    with urllib.request.urlopen(r,context=ctx,timeout=120) as resp: return resp.read()
def r2put(key,path):
    for att in range(5):
        try:
            req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}","PUT",open(path,"rb").read(),"image/png"); return
        except Exception:
            if att==4: raise
            time.sleep(2**att)
def d1(sql,params=None):
    body={"sql":sql}
    if params: body["params"]=params
    for att in range(6):
        try:
            out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",json.dumps(body).encode(),"application/json"))
            break
        except urllib.error.HTTPError as e:
            if e.code!=429 or att==5: raise
            time.sleep(3*2**att)
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

DECKS={
 "solostack":"THE SOLO STACK 4:5","stopsoftware":"STOP PAYING FOR SOFTWARE",
 "systems":"SYSTEMS NOT EMPLOYEES","leadmachine":"THE LEAD MACHINE",
 "agency":"A FULL AGENCY ONE CLAUDE","agentchatbot":"AN AGENT NOT A CHATBOT",
 "levels":"SEVEN LEVELS OF ULTRON","onepersonrev":"THE 1-PERSON REVENUE STACK",
 "contentteam":"THE CONTENT TEAM","onepersonco":"THE ONE-PERSON COMPANY",
}
import importlib.util as _iu
_s=_iu.spec_from_file_location("_AS","/home/user/tiberiu-claude/content/_hitl-src/adapt_specs.py")
_AS=_iu.module_from_spec(_s); _s.loader.exec_module(_AS)
DECKS.update({d["slug"]:d["title"] for d in _AS.ALL})
def esc(s): return s.replace("'","''")

if __name__=="__main__":
    slugs=sys.argv[1:] or list(DECKS)
    dirid=str(int(time.time()))
    for slug in slugs:
        label=DECKS[slug]
        rows=d1(f"SELECT id,name,media FROM vault_items WHERE owner='{ME}' AND name LIKE '%{esc(label)} (Instagram)%'")
        if not rows: print("MISS",label); continue
        p=f"scratchpad/{slug}_ig/s1.png"
        key=f"imports/pm/{slug}-igc1-{dirid}/01.png"; r2put(key,p)
        for r in rows:
            media=json.loads(r["media"]); media[0]={"key":key,"type":"image","ext":"png","contentType":"image/png"}
            d1("UPDATE vault_items SET media=?, thumb_key=? WHERE id=?",[json.dumps(media),key,r["id"]])
            print("OK",r["name"][:64])
    print("DONE")
