#!/usr/bin/env python3
# Cachebust the 5 corrected materials: re-upload TikTok-3D + IG-3D under fresh keys and UPDATE the existing
# vault rows' media + thumb so the app shows the viral-hook / fixed-cover / no-dashboard versions. Then sort.
import os,sys,json,time,subprocess
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
v=int(time.time())
# (slug, dir, n, name LIKE)
M=[]
for slug,label in [("agentsprod","AGENTS PROD 9:16"),("code","CLAUDE CODE 9:16"),("projects","CLAUDE PROJECTS 9:16"),("skills","SKILLS 9:16"),("chat","CHAT HABITS 9:16")]:
    M.append((f"{slug}-tt",f"{slug}_3d_tt",10,f"Review · {label} (TikTok 3D)%"))
    M.append((f"{slug}-ig",f"{slug}_3d_ig",10,f"Review · {label} (Instagram)%"))
ok=0
for slug,d,n,like in M:
    dd=f"{TE}/roll3/{d}"; keys=[]
    for i in range(1,n+1):
        f=f"{dd}/s{i}.png"
        if not os.path.exists(f): print("MISSING",f); break
        subprocess.run(["python3",SCRUB,f],capture_output=True)
        k=f"imports/pm/{slug}-{v}/{i:02d}.png"; assert r2put(k,f),f"R2 {k}"; keys.append(k)
    if len(keys)!=n: print("SKIP",slug); continue
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    good=wr(f"UPDATE vault_items SET media='{esc(cmedia)}', thumb_key='{keys[0]}' WHERE owner='{O}' AND name LIKE '{like}';")
    ok+=bool(good); print(("OK   " if good else "FAIL ")+f"{slug}  ({len(keys)})  <- {like}")
print(f"--- cachebust {ok}/{len(M)} ---")
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
if nonp:
    floor=min(int(r["c"]) for r in nonp)
    posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
    if posted:
        cases=[f"WHEN '{p['id']}' THEN {floor-(r+1)*1000}" for r,p in enumerate(posted)]
        wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({','.join(chr(39)+p['id']+chr(39) for p in posted)});")
        print(f"SORT: sank {len(posted)} Posted")
print("REPUSH NEW DONE")
