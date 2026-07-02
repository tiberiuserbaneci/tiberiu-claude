#!/usr/bin/env python3
# Push a 9:16 carousel material (TikTok deck + IG deck) into the Monolith vault.
# Self-contained: R2 PUT + D1 INSERT via the Cloudflare REST API (no wrangler, no dead paths).
# Env (source scratchpad/cfenv): CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID.
# Usage:
#   python3 monolith/push_material.py --slug theteam --label "THE TEAM 9:16" \
#       --tt scratchpad/team_tt --ig scratchpad/team_ig --caption content/team-3d-tiktok-caption.md
import os, sys, json, time, uuid, glob, argparse, urllib.request, ssl

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
    req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/r2/buckets/{BUCKET}/objects/{key}",
        "PUT",open(path,"rb").read(),"image/png"); return True

def d1(sql):
    body=json.dumps({"sql":sql}).encode()
    out=json.loads(req(f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{DBID}/query","POST",body,"application/json"))
    if not out.get("success"): raise RuntimeError(out.get("errors"))
    return out["result"][0]["results"]

def esc(s): return s.replace("'","''")
def caption_of(p):
    t=open(p).read(); return (t.split("\n---\n",1)[1].strip() if "\n---\n" in t else t.strip())

def top_base():
    # Browse sorts created_at DESC; restamp_sort inflates existing rows ABOVE the real epoch, so a
    # raw time.time() stamp sinks new items to the bottom (the recurring "unde sunt" bug). Stamp new
    # items ABOVE the current max so a fresh push always lands at the TOP of the Review list.
    m=d1(f"SELECT MAX(created_at) AS m FROM vault_items WHERE owner='{OWNER}'")[0]["m"] or int(time.time()*1000)
    return int(m)+600000   # 10 min of headroom above the current top

def push_deck(slug, label, suffix, tag, ddir, cap, ts, idx, dirid, base):
    pngs=sorted(glob.glob(f"{ddir}/s*.png"), key=lambda f:int(''.join(c for c in os.path.basename(f) if c.isdigit())))
    keys=[]
    chan=suffix.strip("()").replace(" ","").lower()
    for i,f in enumerate(pngs,1):
        k=f"imports/pm/{slug}-{chan}-{dirid}/{i:02d}.png"; r2put(k,f); keys.append(k)
    media=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    name=f"Review · {label} {suffix} · {ts}"
    vid=str(uuid.uuid5(uuid.NAMESPACE_URL,f"{tag.lower()}-{slug}-{suffix}-{ts}"))
    created=base-idx*60000; tags=json.dumps([tag])   # above current max, newest-first, restamp-safe spacing
    d1("INSERT INTO vault_items (id,owner,kind,name,source,duration_sec,thumb_key,thumb_url,media,tags,created_at,caption) VALUES ("
       f"'{vid}','{OWNER}','carousel','{esc(name)}','generated',NULL,'{keys[0]}',NULL,'{esc(media)}','{esc(tags)}',{created},'{esc(cap)}');")
    return name, len(keys)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--slug",required=True); ap.add_argument("--label",required=True)
    ap.add_argument("--tt",required=True); ap.add_argument("--ig",required=True)
    ap.add_argument("--caption",required=True); ap.add_argument("--ts",default=time.strftime("%Y-%m-%d %H:%M"))
    a=ap.parse_args()
    cap=caption_of(a.caption); dirid=str(int(time.time())); base=top_base()
    for idx,(suffix,tag,ddir) in enumerate([("(TikTok 3D)","TikTok",a.tt),("(Instagram)","Instagram",a.ig)]):
        name,n=push_deck(a.slug,a.label,suffix,tag,ddir,cap,a.ts,idx,dirid,base)
        print(f"OK  {name}  ({n} media)")
    print("DONE")
