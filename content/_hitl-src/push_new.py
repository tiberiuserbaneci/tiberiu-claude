#!/usr/bin/env python3
# Push the 5 NEW converted materials: TikTok 3D (10pp) + IG 3D (10pp) per material, Review status, then sort.
# Each material shares its 8 content objects; covers differ (normal vs overlay). Reuses the source caption.
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
    r=subprocess.run(["npx","--yes","wrangler@latest","d1","execute","opencut-vault","--remote"]+(["--json"] if parse else [])+["--command",sql],capture_output=True,text=True,env=os.environ)
    if r.returncode!=0: print("WR ERR",(r.stderr or "")[-160:]); return None
    if parse:
        try: return json.loads(r.stdout)[0]["results"]
        except: return None
    return True
def caption(f):
    p=f"{REPO}/content/{f}"
    if not os.path.exists(p): return ""
    t=open(p).read()
    return (t.split("\n---\n",1)[1].strip() if "\n---\n" in t else t.strip())
# (slug, LABEL, caption file, tt dir, ig dir)
MATS=[
 ("agentsprod","AGENTS PROD 9:16","agents-prod-tiktok-caption.md","agentsprod_3d_tt","agentsprod_3d_ig"),
 ("code","CLAUDE CODE 9:16","claude-code-start-editorial45-caption.md","code_3d_tt","code_3d_ig"),
 ("projects","CLAUDE PROJECTS 9:16","claude-projects-editorial45-caption.md","projects_3d_tt","projects_3d_ig"),
 ("skills","SKILLS 9:16","docs-12-skills-tiktok-caption.md","skills_3d_tt","skills_3d_ig"),
 ("chat","CHAT HABITS 9:16","chat-habits-45-tiktok-caption.md","chat_3d_tt","chat_3d_ig"),
]
ts=sys.argv[1] if len(sys.argv)>1 else "2026-06-26 19:00"
base=int(time.time()*1000); idx=0
sel=sys.argv[2:] if len(sys.argv)>2 else [m[0] for m in MATS]
for slug,label,capf,ttd,igd in MATS:
    if slug not in sel: continue
    cap=caption(capf)
    for tag,suffix,d in [("TikTok","(TikTok 3D)",ttd),("Instagram","(Instagram)",igd)]:
        dd=f"{TE}/roll3/{d}"
        if not os.path.isdir(dd): print("MISSING dir",dd); continue
        n=len([f for f in os.listdir(dd) if f.startswith("s") and f.endswith(".png")])
        keys=[]
        for i in range(1,n+1):
            f=f"{dd}/s{i}.png"; subprocess.run(["python3",SCRUB,f],capture_output=True)
            k=f"imports/pm/{slug}-{suffix.strip('()').replace(' ','').lower()}/{i:02d}.png"; assert r2put(k,f),f"R2 {k}"; keys.append(k)
        cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
        name=f"Review · {label} {suffix} · {ts}"; vid=str(uuid.uuid5(uuid.NAMESPACE_URL,f"{tag.lower()}-{slug}-{suffix}-{ts}"))
        created=base-idx*1000; idx+=1; tags=json.dumps([tag])
        sql=("INSERT INTO vault_items (id,owner,kind,name,source,duration_sec,thumb_key,thumb_url,media,tags,created_at,caption) VALUES ("
             f"'{vid}','{O}','carousel','{esc(name)}','generated',NULL,'{keys[0]}',NULL,'{esc(cmedia)}','{esc(tags)}',{created},'{esc(cap)}');")
        print(("OK   " if wr(sql) else "FAIL ")+f"{slug} {suffix}  ({len(keys)} media)")
# sort posted under review
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
if nonp:
    floor=min(int(r["c"]) for r in nonp)
    posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
    if posted:
        cases=[f"WHEN '{p['id']}' THEN {floor-(r+1)*1000}" for r,p in enumerate(posted)]
        wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({','.join(chr(39)+p['id']+chr(39) for p in posted)});")
        print(f"SORT: sank {len(posted)} Posted")
print("PUSH NEW DONE")
