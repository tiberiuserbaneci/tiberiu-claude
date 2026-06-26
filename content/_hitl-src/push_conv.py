#!/usr/bin/env python3
# Generic push for a converted material: TikTok 3D + Instagram (no 2D/LinkedIn), Review status, sort.
# Usage: python3 push_conv.py <slug> <Label> <caption-md> <tt_dir> <ig_dir>
import os,sys,json,time,uuid,subprocess
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
REPO="/home/user/tiberiu-claude"; O="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"; SCRUB=f"{REPO}/content/_scrub.py"
for ln in open(f"{SP}/cfenv"):
    ln=ln.strip().removeprefix("export ")
    if "=" in ln and not ln.startswith("#"):
        k,v=ln.split("=",1); os.environ[k.strip()]=v.strip().strip('"').strip("'")
sys.path.insert(0,TE)
from finish import r2put, esc
def wr(sql,parse=False):
    r=subprocess.run(["npx","--yes","wrangler@latest","d1","execute","opencut-vault","--remote","--json","--command",sql],capture_output=True,text=True,env=os.environ)
    if r.returncode!=0: print("WR ERR",(r.stderr or "")[-200:]); return None
    if parse:
        try: return json.loads(r.stdout)[0]["results"]
        except: return None
    return True
slug,label,capmd,ttdir,igdir=sys.argv[1:6]
cap=open(f"{REPO}/content/{capmd}").read().split("\n---\n",1)[1].strip()
ts=time.strftime("%Y-%m-%d %H:%M",time.localtime())
mats=[dict(slug=f"{slug}-tt-3d",tag="TikTok",label=f"{label} (TikTok 3D)",dir=f"{TE}/roll3/{ttdir}",n=8),
      dict(slug=f"{slug}-ig",tag="Instagram",label=f"{label} (Instagram)",dir=f"{TE}/roll3/{igdir}",n=10)]
base=int(time.time()*1000)
for idx,m in enumerate(mats):
    keys=[]
    for i in range(1,m["n"]+1):
        f=f"{m['dir']}/s{i}.png"; subprocess.run(["python3",SCRUB,f],capture_output=True)
        k=f"imports/pm/{m['slug']}/{i:02d}.png"; assert r2put(k,f),f"R2 fail {k}"; keys.append(k)
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    name=f"Review · {m['label']} · {ts}"; vid=str(uuid.uuid5(uuid.NAMESPACE_URL,f"{m['tag'].lower()}-{m['slug']}-{ts}"))
    created=base+(len(mats)-idx)*1000; tags=json.dumps([m["tag"]])
    sql=("INSERT INTO vault_items (id,owner,kind,name,source,duration_sec,thumb_key,thumb_url,media,tags,created_at,caption) VALUES ("
         f"'{vid}','{O}','carousel','{esc(name)}','generated',NULL,'{keys[0]}',NULL,'{esc(cmedia)}','{esc(tags)}',{created},'{esc(cap)}');")
    print(("OK   " if wr(sql) else "FAIL ")+m["slug"]+f"  ({len(keys)} media)")
# sort
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
floor=min(int(r["c"]) for r in nonp)
posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
if posted:
    cases=[f"WHEN '{p['id']}' THEN {floor-(r+1)*1000}" for r,p in enumerate(posted)]
    wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({','.join(chr(39)+p['id']+chr(39) for p in posted)});")
    print(f"SORT: sank {len(posted)} Posted")
