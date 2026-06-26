#!/usr/bin/env python3
# Cachebust re-push of every FIXED material: re-upload slides under fresh version-tagged R2 keys and
# UPDATE the existing vault rows' media + thumb so the app shows the corrected (uncropped, repositioned)
# versions. 6 TikTok-3D + 6 IG sets + the Maps LinkedIn image. Then re-run the Posted-after-Review sort.
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
    if r.returncode!=0: print("WR ERR",(r.stderr or "")[-200:]); return None
    if parse:
        try: return json.loads(r.stdout)[0]["results"]
        except: return None
    return True
v=int(time.time())  # version tag -> fresh keys -> app cache busts
# (roll3 dir, slide count, name LIKE, key slug)
M9=[
 ("maps_3d_tt",8,"Review · MAPS 9:16 (TikTok 3D)%","maps-tt3d"),
 ("maps_3d_ig",10,"Review · MAPS 9:16 (Instagram)%","maps-ig"),
 ("routing_3d_tt",8,"Review · ROUTING 9:16 (TikTok 3D)%","routing-tt3d"),
 ("routing_3d_ig",10,"Review · ROUTING 9:16 (Instagram)%","routing-ig"),
 ("toolstack_3d_tt",8,"Review · TOOL STACK 9:16 (TikTok 3D)%","toolstack-tt3d"),
 ("toolstack_3d_ig",10,"Review · TOOL STACK 9:16 (Instagram)%","toolstack-ig"),
 ("modules_3d_tt",8,"Review · MODULES 9:16 (TikTok 3D)%","modules-tt3d"),
 ("modules_3d_ig",10,"Review · MODULES 9:16 (Instagram)%","modules-ig"),
 ("jobs_3d_tt",8,"Review · JOBS 9:16 (TikTok 3D)%","jobs-tt3d"),
 ("jobs_3d_ig",10,"Review · JOBS 9:16 (Instagram)%","jobs-ig"),
 ("hitl_3d_tt",8,"Posted · HUMAN GATE (TikTok 3D)%","hitl-tt3d"),
 ("hitl_3d_ig",8,"Review · HUMAN GATE (IG 3D overlay)%","hitl-ig"),
]
ok=0
for d,n,like,slug in M9:
    keys=[]
    for i in range(1,n+1):
        f=f"{TE}/roll3/{d}/s{i}.png"
        if not os.path.exists(f): print("MISSING",f); break
        subprocess.run(["python3",SCRUB,f],capture_output=True)
        k=f"imports/pm/{slug}-{v}/{i:02d}.png"; assert r2put(k,f),f"R2 fail {k}"; keys.append(k)
    if len(keys)!=n: print("SKIP (count)",slug); continue
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    sql=f"UPDATE vault_items SET media='{esc(cmedia)}', thumb_key='{keys[0]}' WHERE owner='{O}' AND name LIKE '{like}';"
    good=wr(sql); ok+=bool(good); print(("OK   " if good else "FAIL ")+f"{slug}  ({len(keys)} media)  <- {like}")
# Maps LinkedIn (single image)
lf=f"{REPO}/content/maps-linkedin.png"; subprocess.run(["python3",SCRUB,lf],capture_output=True)
lk=f"imports/pm/maps-li-{v}/01.png"; assert r2put(lk,lf),"R2 fail LI"
lmedia=json.dumps([{"key":lk,"type":"image","ext":"png","contentType":"image/png"}])
good=wr(f"UPDATE vault_items SET media='{esc(lmedia)}', thumb_key='{lk}' WHERE owner='{O}' AND name LIKE 'Review · MAPS scraper (LinkedIn)%';")
ok+=bool(good); print(("OK   " if good else "FAIL ")+"maps-linkedin  (1 media)")
print(f"--- cachebust updated {ok}/{len(M9)+1} entries ---")
# Posted-after-Review sort: sink every Posted% item below the lowest non-Posted created_at
nonp=wr(f"SELECT created_at c FROM vault_items WHERE owner='{O}' AND name NOT LIKE 'Posted%' AND created_at IS NOT NULL;",parse=True)
floor=min(int(r["c"]) for r in nonp)
posted=wr(f"SELECT id FROM vault_items WHERE owner='{O}' AND name LIKE 'Posted%' ORDER BY created_at DESC;",parse=True)
if posted:
    cases=[f"WHEN '{p['id']}' THEN {floor-(r+1)*1000}" for r,p in enumerate(posted)]
    wr(f"UPDATE vault_items SET created_at = CASE id {' '.join(cases)} END WHERE id IN ({','.join(chr(39)+p['id']+chr(39) for p in posted)});")
    print(f"SORT: sank {len(posted)} Posted below Review")
print("DONE")
