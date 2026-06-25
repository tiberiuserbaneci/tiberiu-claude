#!/usr/bin/env python3
# Reupload a 9:16 build to an existing vault item's R2 keys + git (no Vertex, no vault insert).
# Usage: python3 reupload_916.py <src_dir> <prefix>   e.g. operator2_9 operator-stack
import os,sys,subprocess
from PIL import Image
SP="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad"; TE=f"{SP}/te-gen"; REPO="/home/user/tiberiu-claude"
sys.path.insert(0,TE)
for ln in open(f"{SP}/cfenv"):
    ln=ln.strip()
    if ln.startswith("export "): ln=ln[7:]
    if "=" in ln and not ln.startswith("#"):
        k,v=ln.split("=",1); os.environ[k.strip()]=v.strip().strip('"').strip("'")
from finish import r2put
src,prefix=sys.argv[1],sys.argv[2]
SRC=f"{TE}/roll3/{src}"; SHIP=f"{TE}/roll3/{prefix}-ship9"; os.makedirs(SHIP,exist_ok=True)
GITD=f"{REPO}/content/services-rollout/{prefix}"; os.makedirs(GITD,exist_ok=True)
for i in range(1,9):
    im=Image.open(f"{SRC}/s{i}.png").convert("RGB").resize((1080,1920),Image.LANCZOS)
    o=f"{SHIP}/{i:02d}.png"; im.save(o)
    subprocess.run(["python3",f"{REPO}/content/_scrub.py",o],capture_output=True)
    k=f"imports/pm/{prefix}/{i:02d}.png"; assert r2put(k,o),f"R2 fail {k}"
    subprocess.run(["cp",o,f"{GITD}/slide-{i}.png"],check=True)
print("reuploaded",prefix,"(9:16, same vault item)")
