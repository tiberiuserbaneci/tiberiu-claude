#!/usr/bin/env python3
# Finalize rollout carousels: footer -> resize 1080x1350 -> scrub -> R2 -> vault (update Review rows
# to the new carousel) -> stage to content/ for git. Resumable. Run after rollout.py generates slides.
import os,sys,json,subprocess,uuid,time,glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import requests
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
REPO="/home/user/tiberiu-claude"
O="x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3"
tok=os.environ["CLOUDFLARE_API_TOKEN"]; acct=os.environ["CLOUDFLARE_ACCOUNT_ID"]; ca="/root/.ccr/ca-bundle.crt"
BUCKET="ultron-reels"
MAN=json.load(open(f"{TE}/rollout_manifest.json"))["items"]
ORANGE=(232,84,43)
def fontload(px):
    f=ImageFont.truetype(f"{TE}/DMSans-VF.ttf",px)
    try: f.set_variation_by_axes([800])
    except Exception:
        try: f.set_variation_by_name("Bold")
        except Exception: pass
    return f
def footer_resize_scrub(src,out):
    im=Image.open(src).convert("RGB").resize((1080,1350),Image.LANCZOS)
    d=ImageDraw.Draw(im); px=int(1080*0.026); f=fontload(px); T="51ultron.com"; ls=int(px*0.04)
    ws=[d.textlength(c,font=f) for c in T]; tot=sum(ws)+ls*(len(T)-1); x=(1080-tot)/2; y=1350-int(1350*0.045)
    for c,w in zip(T,ws): d.text((x,y),c,font=f,fill=ORANGE); x+=w+ls
    im.save(out)
    subprocess.run(["python3",f"{REPO}/content/_scrub.py",out],capture_output=True)
def r2put(key,path,ct):
    data=open(path,"rb").read()
    for a in range(5):
        r=requests.put(f"https://api.cloudflare.com/client/v4/accounts/{acct}/r2/buckets/{BUCKET}/objects/{key}",data=data,headers={"Authorization":f"Bearer {tok}","Content-Type":ct},verify=ca,timeout=300)
        if r.status_code in (200,201): return True
        time.sleep(1.5*(a+1))
    print("  R2 FAIL",key,r.status_code); return False
def wexec(cmd):
    subprocess.run(["npx","--yes","wrangler@latest","d1","execute","opencut-vault","--remote","--command",cmd],capture_output=True,text=True)
def caption(it):
    h=it["hook"].replace("/","\n").strip()
    return (f"Comment {it['kw']} and I will send you the Ultron setup.\n\n{h}\n\n"
            "One ask, and Ultron runs the whole service for you.\n\n#claude #ai #founder #startup #buildinpublic")
def esc(x): return x.replace("'","''")
def prefix(row): return row.replace(" Infographic","").strip()

done=0
for it in MAN:
    slug=it["slug"]; src=f"{TE}/roll/{slug}"
    if len(glob.glob(f"{src}/s*.png"))<5: print("skip(not ready)",slug); continue
    shipd=f"{TE}/rollship/{slug}"; os.makedirs(shipd,exist_ok=True)
    gitd=f"{REPO}/content/services-rollout/{slug}"; os.makedirs(gitd,exist_ok=True)
    keys=[]
    for i in range(1,6):
        out=f"{shipd}/{i:02d}.png"; footer_resize_scrub(f"{src}/s{i}.png",out)
        k=f"imports/pm/rollout-{slug}/{i:02d}.png"; r2put(k,out,"image/png"); keys.append(k)
        subprocess.run(["cp",out,f"{gitd}/slide-{i}.png"])
    cap=caption(it); open(f"{gitd}/caption.md","w").write(cap)
    cmedia=json.dumps([{"key":k,"type":"image","ext":"png","contentType":"image/png"} for k in keys])
    pfx=prefix(it["row"])
    wexec(f"UPDATE vault_items SET kind='carousel', media='{esc(cmedia)}', thumb_key='{keys[0]}', thumb_url=NULL, duration_sec=NULL, caption='{esc(cap)}' WHERE owner='{O}' AND tags='[\"TikTok\"]' AND name LIKE '{esc(pfx)}%' AND name LIKE 'Review%';")
    done+=1; print(f"[{done}] {slug} -> vault updated ({len(keys)} imgs)")
print(f"FINALIZE DONE: {done} carousels shipped to vault + staged to content/services-rollout/")
