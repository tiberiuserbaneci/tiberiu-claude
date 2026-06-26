#!/usr/bin/env python3
# Push the HUMAN GATE materials to the Monolith vault as Review items, then enforce the
# operator sort: every Posted item sinks below every non-Posted item (Posted after Review).
import os,sys,json,time,uuid,subprocess
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"
REPO="/home/user/tiberiu-claude"; O="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
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
    if r.returncode!=0: print("WR ERR rc",r.returncode,(r.stderr or "")[-400:]); return None
    if parse:
        try: return json.loads(r.stdout)[0]["results"]
        except Exception as e: print("parse err",e,(r.stdout or "")[-300:]); return None
    return True

# --- captions ---
def li_section(name):
    md=open(f"{REPO}/content/hitl-linkedin-caption.md").read()
    return md.split(f"## {name}",1)[1].split("\n---",1)[0].split("\n## ",1)[0].strip()
li_caption=li_section("CAPTION")+"\n\n"+li_section("FIRST COMMENT")
tk_caption=open(f"{REPO}/content/hitl-tiktok-caption.md").read().split("\n---\n",1)[1].strip()

ts=time.strftime("%Y-%m-%d %H:%M",time.localtime())
mats=[
 dict(slug="hitl-linkedin",tag="LinkedIn",label="HUMAN GATE (LinkedIn)",cap=li_caption,
      files=[f"{REPO}/content/hitl-linkedin.png"]),
 dict(slug="hitl-tiktok-2d",tag="TikTok",label="HUMAN GATE (TikTok 2D)",cap=tk_caption,
      files=[f"{REPO}/content/hitl-tiktok-2d-s{i}.png" for i in range(1,9)]),
 dict(slug="hitl-tiktok-3d",tag="TikTok",label="HUMAN GATE (TikTok 3D)",cap=tk_caption,
      files=[f"{REPO}/content/hitl-tiktok-3d-s{i}.png" for i in range(1,9)]),
 dict(slug="hitl-ig-3d",tag="Instagram",label="HUMAN GATE (IG 3D overlay)",cap=tk_caption,
      files=[f"{TE}/roll3/hitl_ig_3d/s{i}.png" for i in range(1,9)]),  # s1 transparent overlay
]
base=int(time.time()*1000)
for idx,m in enumerate(mats):
    keys=[]
    for i,f in enumerate(m["files"],1):
        k=f"imports/pm/{m['slug']}/{i:02d}.png"
        assert r2put(k,f),f"R2 fail {k}"; keys.append(k)
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    name=f"Review · {m['label']} · {ts}"
    vid=str(uuid.uuid5(uuid.NAMESPACE_URL,f"{m['tag'].lower()}-{m['slug']}-{ts}"))
    created=base+(len(mats)-idx)*1000        # LinkedIn highest -> first in its section
    tags=json.dumps([m["tag"]])
    sql=("INSERT INTO vault_items (id,owner,kind,name,source,duration_sec,thumb_key,thumb_url,media,tags,created_at,caption) VALUES ("
         f"'{vid}','{O}','carousel','{esc(name)}','generated',NULL,'{keys[0]}',NULL,'{esc(cmedia)}','{esc(tags)}',{created},'{esc(m['cap'])}');")
    ok=wr(sql)
    print(("OK   " if ok else "FAIL ")+m["tag"]+" / "+m["slug"]+"  ("+str(len(keys))+" media)  "+name)

# --- SORT: Posted after Review (sink every Posted below every non-Posted) ---
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
floor=min(int(r["c"]) for r in nonp)
posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
if posted:
    cases=[]; ids=[]
    for rank,p in enumerate(posted):
        cases.append(f"WHEN '{p['id']}' THEN {floor-(rank+1)*1000}"); ids.append(p["id"])
    inlist=",".join(f"'{i}'" for i in ids)
    ok=wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({inlist});")
    print(f"SORT {'OK' if ok else 'FAIL'}: sank {len(ids)} Posted below {len(nonp)} non-Posted (floor {floor})")

# --- verify top + bottom of the Library ---
top=wr(f"SELECT name FROM vault_items WHERE owner='{O}' ORDER BY created_at DESC LIMIT 8;",parse=True)
bot=wr(f"SELECT name FROM vault_items WHERE owner='{O}' ORDER BY created_at DESC LIMIT 6 OFFSET (SELECT count(*)-6 FROM vault_items WHERE owner='{O}');",parse=True)
print("\nTOP of Library:");  [print("  ",r["name"][:64]) for r in (top or [])]
print("BOTTOM of Library:"); [print("  ",r["name"][:64]) for r in (bot or [])]
