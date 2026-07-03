#!/usr/bin/env python3
# Cover variant B - Vertex photoreal hero for WIRE ITS EYES + coded hook overlay.
import os,json,base64,time,requests
from PIL import Image, ImageDraw, ImageFont
SP="/home/user/tiberiu-claude/scratchpad"; CA="/root/.ccr/ca-bundle.crt"
P="project-c28b1276-8b53-430a-a7a"
URL=f"https://aiplatform.googleapis.com/v1/projects/{P}/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent"
info=json.load(open(f"{SP}/adc.json"))
def token(): return requests.post("https://oauth2.googleapis.com/token",data={"client_id":info["client_id"],"client_secret":info["client_secret"],"refresh_token":info["refresh_token"],"grant_type":"refresh_token"},verify=CA,timeout=30).json()["access_token"]

PROMPT=("A cinematic photoreal 3D render, portrait 4:5, on a COMPLETELY FLAT near-black #191919 background. "
 "A single glowing amber-orange abstract EYE-ORB sealed inside a dark translucent glass sphere, floating, "
 "centred, dramatic single warm rim light from upper-left, deep shadow, volumetric glow, faint concentric "
 "energy rings around the orb, a thin horizontal scan-line of light across it. Luxurious, editorial, minimal, "
 "warm copper-and-charcoal palette ONLY (no blue, no green, no neon). Lots of negative space around the object. "
 "Photographic depth of field, subtle film grain. NO text, NO logos, NO watermark, one object only.")

def gen():
    body={"contents":[{"role":"user","parts":[{"text":PROMPT}]}],
      "generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}}
    for att in range(7):
        try:
            r=requests.post(URL,headers={"Authorization":f"Bearer {token()}","Content-Type":"application/json"},json=body,verify=CA,timeout=300)
            if r.status_code==429: print("429 wait",att); time.sleep(20*(att+1)); continue
            r.raise_for_status(); out=r.json(); c=out.get("candidates") or []
            for p2 in ((c[0].get("content") or {}).get("parts") or []):
                if "inlineData" in p2:
                    open(f"{SP}/covers/vertex_raw.png","wb").write(base64.b64decode(p2["inlineData"]["data"])); print("OK raw"); return True
            print("empty",att); time.sleep(8)
        except Exception as e: print("err",att,str(e)[:120]); time.sleep(8)
    return False

def compose():
    W,H=1080,1350
    bg=Image.open(f"{SP}/covers/vertex_raw.png").convert("RGB").resize((W,H))
    d=ImageDraw.Draw(bg,"RGBA")
    F="/home/user/tiberiu-claude/content/assets"
    hf=ImageFont.truetype(f"{F}/DMSans-900.ttf",78); mf=ImageFont.truetype(f"{F}/DMMono-500.ttf",26)
    # top scrim for hook legibility
    sc=Image.new("RGBA",(W,360),(0,0,0,0)); sd=ImageDraw.Draw(sc)
    for i in range(360): sd.line([(0,i),(W,i)],fill=(12,10,9,int(150*(1-i/360))))
    bg.paste(Image.alpha_composite(Image.new("RGBA",(W,360),(0,0,0,0)),sc).convert("RGB") if False else bg.crop((0,0,W,360)),(0,0))
    bg=bg.convert("RGBA"); bg.alpha_composite(sc,(0,0))
    d=ImageDraw.Draw(bg)
    d.text((70,120),"YOUR AI IS BLIND",font=hf,fill=(250,250,247))
    d.text((70,210),"BY DEFAULT.",font=hf,fill=(212,162,127))
    # bottom scrim + swipe
    sc2=Image.new("RGBA",(W,300),(0,0,0,0)); s2=ImageDraw.Draw(sc2)
    for i in range(300): s2.line([(0,i),(W,i)],fill=(12,10,9,int(150*i/300)))
    bg.alpha_composite(sc2,(0,H-300))
    d.text((70,H-150),"Wire its eyes.  swipe -->",font=mf,fill=(230,225,215))
    bg.convert("RGB").save(f"{SP}/covers/cover_B.png"); print("composed cover_B")

if __name__=="__main__":
    if gen(): compose()
