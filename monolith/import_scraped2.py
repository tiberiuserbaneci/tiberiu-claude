#!/usr/bin/env python3
# "IG Scraped 2" category: 50 FRESH Catalin carousels (Vertex Set 2) to modify next, deduped against
# the batch-1 topics already built. Prefers rows with a real hook; names from the caption hook.
import os, json, ssl, re, urllib.request, uuid
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"
CAT="Doho2J2linQZYPsXsR95HWJPCr7XaMVA"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
def d1(sql,params=None):
    body={"sql":sql}
    if params is not None: body["params"]=params
    r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query",data=json.dumps(body).encode(),method="POST")
    r.add_header("Authorization",f"Bearer {TOKEN}"); r.add_header("Content-Type","application/json")
    o=json.loads(urllib.request.urlopen(r,context=ctx,timeout=90).read())
    if not o.get("success"): raise RuntimeError(o.get("errors"))
    return o["result"][0]["results"]

# wipe any prior IG Scraped 2 rows (re-runnable)
d1(f"DELETE FROM vault_items WHERE owner='{OWNER}' AND tags LIKE '%IG Scraped 2%'")

# batch-1 topics already built -> skip Catalin rows that match these
DUP=["forgets everything the second","agentic os","prompt after prompt","prompt engineering is dead",
 "took your entire body","5 signs your business needs ai","$500k/year content","wtf is a loop",
 "free claude code resources","stops at level one","low effort content","16 claude skills nobody",
 "/carousel command","paying a designer to build car","spending too much on claude code","cut costs",
 "5 agent architectures","set up claude code in one hour","don’t need to be technical","dont need to be technical",
 "actually checked them","a bunch were","5 that businesses","24 things every claude power user",
 "board of advisor","burned mailboxes","ghosted by your cold emails","single overworked chatbot",
 "one business idea and 2 hours","sales agents","org chart","replaced a $300k","replaced my meta ads",
 "replaced my $2","higgsfield","most developers are using claude code like a chatbot","paste text in, get text back",
 "most ai agents finish a task and forget","7 claude skills every content creator","10 skills. one claude. a full agency",
 "double your output with these 5 ai agents","hold you by the shoulders","learn from your own"]
EMOJI=re.compile("["+"\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"+"]",flags=re.UNICODE)
CTA=re.compile(r'(comment\s+[“"\']?\w+.*?|want the complete\s+\w+.*?|save this.*?|drop\s+/?\w+.*?|dm me.*?)([.!?\n]|$)',re.IGNORECASE)
def hook(name,cap):
    for src in (cap or "",name or ""):
        s=EMOJI.sub("",src); s=re.sub(r'#\w+',' ',s); s=CTA.sub(' ',s)
        s=re.sub(r'[.·]{2,}',' ',s); s=re.sub(r'\s+',' ',s).strip(" .·-“”\"'")
        # first meaningful sentence
        m=re.split(r'(?<=[.!?]) ',s)
        for part in m:
            p=part.strip(" .·-“”\"'")
            if len(p)>=14: return p[:60].strip()
    return None
def isdup(name,cap):
    blob=((name or "")+" "+(cap or "")).lower()
    return any(p in blob for p in DUP)

rows=d1(f"SELECT id,name,media,caption FROM vault_items WHERE owner='{CAT}' AND tags='[\"Vertex Set 2\"]' AND kind='carousel' ORDER BY created_at DESC")
base=9_460_000_000_000; made=0; seenkey=set()
# pass 1: rows with a real hook (not a CTA-only name), deduped; pass 2: fill from the rest
for require_hook in (True, False):
    for r in rows:
        if made>=50: break
        try: k0=json.loads(r['media'])[0]['key']
        except Exception: continue
        if k0 in seenkey: continue
        if isdup(r['name'],r['caption']): continue
        h=hook(r['name'],r['caption'])
        if require_hook and not h: continue
        seenkey.add(k0)
        nm=f"Review · {h} (IG Scraped 2)" if h else f"Review · IG2 source {made+1:02d} (IG Scraped 2)"
        vid=str(uuid.uuid4()); ca=base-made*1000
        d1("INSERT INTO vault_items (id,owner,kind,name,source,media,thumb_key,tags,created_at,caption) VALUES (?,?,?,?,?,?,?,?,?,?)",
           [vid,OWNER,"carousel",nm,"ig-scraped-2",r['media'],k0,'["IG Scraped 2"]',ca,r.get('caption') or ""])
        made+=1; print(f"{made:2d}  {(h or nm)[:60]}")
    if made>=50: break
print(f"\nIMPORTED {made} fresh sources into 'IG Scraped 2'")
