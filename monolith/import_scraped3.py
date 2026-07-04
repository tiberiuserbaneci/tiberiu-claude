#!/usr/bin/env python3
# "IG Scraped 3" category: 100 FRESH Catalin carousels to modify next.
# Dedup: (a) by source media-key across ALL prior batches (batch-2 keys from ig2_map.json + any
# key already imported this run), (b) a light topic-phrase blocklist built from the 109 titles we
# already adapted (batches 1+2) so we do not re-import an identical hook. Draws across every Catalin
# carousel pool, prefers rows with a real hook. Re-runnable (wipes prior IG Scraped 3 rows first).
import os, json, ssl, re, urllib.request, uuid
ACCT=os.environ["CLOUDFLARE_ACCOUNT_ID"]; TOKEN=os.environ["CLOUDFLARE_API_TOKEN"]
DBID="16afa4b2-a2ae-46d1-af4a-41e75836d95b"
CAT="Doho2J2linQZYPsXsR95HWJPCr7XaMVA"; OWNER="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
ROOT="/home/user/tiberiu-claude"
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
def d1(sql,params=None):
    body={"sql":sql}
    if params is not None: body["params"]=params
    r=urllib.request.Request(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query",data=json.dumps(body).encode(),method="POST")
    r.add_header("Authorization",f"Bearer {TOKEN}"); r.add_header("Content-Type","application/json")
    o=json.loads(urllib.request.urlopen(r,context=ctx,timeout=90).read())
    if not o.get("success"): raise RuntimeError(o.get("errors"))
    return o["result"][0]["results"]

# wipe any prior IG Scraped 3 rows (re-runnable)
d1(f"DELETE FROM vault_items WHERE owner='{OWNER}' AND tags LIKE '%IG Scraped 3%'")

# --- source keys already consumed (batch 2) ---
USED=set()
try:
    for o in json.load(open(f"{ROOT}/scratchpad/ig2_map.json")):
        if o.get("key"): USED.add(o["key"])
except Exception: pass

# --- topic blocklist from the 109 titles we already adapted (batches 1+2) ---
STOP=set("the a an of to in on for not and or vs is are you your it its one two three four five six "
         "seven ten now day with without no how what why they them their we our from into out up".split())
def keywords(text):
    words=re.findall(r"[a-z0-9]+", (text or "").lower())
    return {w for w in words if len(w)>=4 and w not in STOP}
BLOCK=[]  # list of keyword-sets, one per covered title
try:
    for t in json.load(open(f"{ROOT}/scratchpad/existing_titles.json")):
        t=re.sub(r"·.*$","",t)  # drop date suffix
        k=keywords(t)
        if k: BLOCK.append(k)
except Exception: pass
# manual phrase blocks (batch-1/2 source topics)
DUP=["forgets everything the second","agentic os","prompt after prompt","prompt engineering is dead",
 "took your entire body","5 signs your business needs ai","$500k/year content","wtf is a loop",
 "free claude code resources","stops at level one","low effort content","16 claude skills nobody",
 "/carousel command","paying a designer to build car","spending too much on claude code","cut costs",
 "5 agent architectures","set up claude code in one hour","dont need to be technical",
 "a bunch were","5 that businesses","24 things every claude power user","board of advisor",
 "burned mailboxes","ghosted by your cold emails","single overworked chatbot","org chart",
 "replaced a $300k","replaced my meta ads","higgsfield","most developers are using claude code like a chatbot",
 "paste text in, get text back","most ai agents finish a task and forget","7 claude skills every content creator",
 "10 skills. one claude. a full agency","double your output with these 5 ai agents","hold you by the shoulders",
 "learn from your own","build an ai agent company","paperclip"]

EMOJI=re.compile("["+"\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"+"]",flags=re.UNICODE)
CTA=re.compile(r'(comment\s+[""\']?\w+.*?|want the complete\s+\w+.*?|save this.*?|drop\s+/?\w+.*?|dm me.*?)([.!?\n]|$)',re.IGNORECASE)
def hook(name,cap):
    for src in (cap or "",name or ""):
        s=EMOJI.sub("",src); s=re.sub(r'#\w+',' ',s); s=CTA.sub(' ',s)
        s=re.sub(r'[.·]{2,}',' ',s); s=re.sub(r'\s+',' ',s).strip(" .·-""\"'")
        for part in re.split(r'(?<=[.!?]) ',s):
            p=part.strip(" .·-""\"'")
            if len(p)>=14: return p[:60].strip()
    return None
def isdup(name,cap,h):
    blob=((name or "")+" "+(cap or "")).lower()
    if any(p in blob for p in DUP): return True
    # keyword-overlap against covered titles: >=2 shared distinctive words == same topic
    hk=keywords(h or name or "")
    if not hk: return False
    for bset in BLOCK:
        if len(hk & bset)>=2: return True
    return False

POOLS=["Vertex Set 2","Vertex 2 · 1355","CTW Format","Vertex 1920","Vertex 1355","Next WIPF","Next WIP"]
rows=[]
for tag in POOLS:
    rows+=d1(f"SELECT id,name,media,caption FROM vault_items WHERE owner='{CAT}' AND tags='[\"{tag}\"]' AND kind='carousel' ORDER BY created_at DESC")

base=9_420_000_000_000; made=0; seenkey=set(); mapping=[]
for require_hook in (True, False):
    for r in rows:
        if made>=100: break
        try: k0=json.loads(r['media'])[0]['key']
        except Exception: continue
        if k0 in USED or k0 in seenkey: continue
        h=hook(r['name'],r['caption'])
        if require_hook and not h: continue
        if isdup(r['name'],r['caption'],h): continue
        seenkey.add(k0)
        nm=f"Review · {h} (IG Scraped 3)" if h else f"Review · IG3 source {made+1:02d} (IG Scraped 3)"
        vid=str(uuid.uuid4()); ca=base-made*1000
        d1("INSERT INTO vault_items (id,owner,kind,name,source,media,thumb_key,tags,created_at,caption) VALUES (?,?,?,?,?,?,?,?,?,?)",
           [vid,OWNER,"carousel",nm,"ig-scraped-3",r['media'],k0,'["IG Scraped 3"]',ca,r.get('caption') or ""])
        mapping.append({"row_id":vid,"vault_name":nm,"key":k0,"media":r['media'],"has_hook":bool(h),"topic":h or ""})
        made+=1; print(f"{made:3d}  {(h or nm)[:60]}")
    if made>=100: break
json.dump(mapping, open(f"{ROOT}/scratchpad/ig3_map.json","w"), indent=0)
print(f"\nIMPORTED {made} fresh sources into 'IG Scraped 3'  (wrote scratchpad/ig3_map.json)")
