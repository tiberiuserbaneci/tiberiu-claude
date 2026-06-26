#!/usr/bin/env python3
# Push the JOBS 9:16 set (TikTok 2D, TikTok 3D, Instagram) to the Monolith vault as Review,
# then re-sort so every Posted item sinks below every non-Posted (Posted-after-Review).
# The existing 4:5 "Review Jobs" item is left untouched.
import os,sys,json,time,uuid,subprocess
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
REPO="/home/user/tiberiu-claude"; O="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; SCRUB=f"{REPO}/content/_scrub.py"
for ln in open(f"{SP}/cfenv"):
    ln=ln.strip()
    if ln.startswith("export "): ln=ln[7:]
    if "=" in ln and not ln.startswith("#"):
        k,v=ln.split("=",1); os.environ[k.strip()]=v.strip().strip('"').strip("'")
sys.path.insert(0,TE)
from finish import r2put, esc

def wr(sql,parse=False):
    cmd=["npx","--yes","wrangler@latest","d1","execute","opencut-vault","--remote","--json","--command",sql]
    r=subprocess.run(cmd,capture_output=True,text=True,env=os.environ)
    if r.returncode!=0: print("WR ERR",r.returncode,(r.stderr or "")[-300:]); return None
    if parse:
        try: return json.loads(r.stdout)[0]["results"]
        except Exception as e: print("parse err",e,(r.stdout or "")[-200:]); return None
    return True

cap=open(f"{REPO}/content/jobs-tiktok-caption.md").read().split("\n---\n",1)[1].strip()
ts=time.strftime("%Y-%m-%d %H:%M",time.localtime())
mats=[
 dict(slug="jobs-tt-2d",tag="TikTok",label="JOBS 9:16 (TikTok 2D)",dir=f"{TE}/roll3/jobs_docs",n=8),
 dict(slug="jobs-tt-3d",tag="TikTok",label="JOBS 9:16 (TikTok 3D)",dir=f"{TE}/roll3/jobs_3d_tt",n=8),
 dict(slug="jobs-ig",tag="Instagram",label="JOBS 9:16 (Instagram)",dir=f"{TE}/roll3/jobs_3d_ig",n=10),
]
base=int(time.time()*1000)
for idx,m in enumerate(mats):
    keys=[]
    for i in range(1,m["n"]+1):
        f=f"{m['dir']}/s{i}.png"
        subprocess.run(["python3",SCRUB,f],capture_output=True)
        k=f"imports/pm/{m['slug']}/{i:02d}.png"; assert r2put(k,f),f"R2 fail {k}"; keys.append(k)
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    name=f"Review · {m['label']} · {ts}"
    vid=str(uuid.uuid5(uuid.NAMESPACE_URL,f"{m['tag'].lower()}-{m['slug']}-{ts}"))
    created=base+(len(mats)-idx)*1000; tags=json.dumps([m["tag"]])
    sql=("INSERT INTO vault_items (id,owner,kind,name,source,duration_sec,thumb_key,thumb_url,media,tags,created_at,caption) VALUES ("
         f"'{vid}','{O}','carousel','{esc(name)}','generated',NULL,'{keys[0]}',NULL,'{esc(cmedia)}','{esc(tags)}',{created},'{esc(cap)}');")
    print(("OK   " if wr(sql) else "FAIL ")+m["tag"]+" / "+m["slug"]+f"  ({len(keys)} media)  "+name)

# SORT: Posted after Review
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
floor=min(int(r["c"]) for r in nonp)
posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
if posted:
    cases=[f"WHEN '{p['id']}' THEN {floor-(r+1)*1000}" for r,p in enumerate(posted)]
    inlist=",".join(f"'{p['id']}'" for p in posted)
    ok=wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({inlist});")
    print(f"SORT {'OK' if ok else 'FAIL'}: sank {len(posted)} Posted below {len(nonp)} non-Posted")
top=wr(f"SELECT name FROM vault_items WHERE owner='{O}' ORDER BY created_at DESC LIMIT 6;",parse=True)
print("TOP:"); [print("  ",r["name"][:60]) for r in (top or [])]
