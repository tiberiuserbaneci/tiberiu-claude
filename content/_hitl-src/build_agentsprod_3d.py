#!/usr/bin/env python3
# agents-prod 3D: ONE 3D content set, two covers. IG 3D = overlay (transparent) cover + 8 content + CTA = 10pp.
# TikTok 3D = normal (opaque) cover + same 8 content + CTA = 10pp. Cover title CENTERED in the middle (both).
# TikTok cover is Claude-forward (3D Claude mark on top). Founder-facing content, no code (source was engineer-heavy).
import os, shutil
from PIL import Image, ImageDraw
import build_slides as B
import build_3d916 as T
co=lambda s:(s,B.CORAL); wo=lambda s:(s,B.WHITE)
TE=T.TE; LIB="/home/user/tiberiu-claude/content/_templates/tiktok/lib"
MODELS=f"{TE}/roll3/models_agentsprod"; CTA=f"{MODELS}/cta.png"
T.LOGO3D=f"{LIB}/claude-logo-3d-extruded.png"   # normal-cover 3D Claude mark (vary per material)
T.CENTER_COVER=True                              # normal TikTok cover: title centered in the middle

COVER=dict(role="cover",eyebrow="AI AGENTS",head=[[wo("Works in the demo.")],[co("Dies on real users.")]],
           sub="A demo agent impresses once. A production agent survives real users, bad inputs and dead APIs.")
# (eyebrow, head, object-key) - all 8 used by BOTH IG and TikTok (10pp each)
CONTENT=[
 ("DEMO vs PROD",[[wo("A demo agent.")],[co("A real one.")]],"compare"),
 ("THE CHECKLIST",[[wo("Six things")],[co("must be true.")]],"checklist"),
 ("THE BRAIN",[[wo("Right model")],[co("for each job.")]],"model"),
 ("WHEN TOOLS FAIL",[[wo("Tools fail.")],[co("It recovers.")]],"tools"),
 ("MEMORY",[[wo("It remembers")],[co("across sessions.")]],"memory"),
 ("THE TRACE",[[wo("Every run,")],[co("fully traced.")]],"trace"),
 ("THE GATE",[[wo("Risky actions")],[co("wait for you.")]],"gate"),
 ("THE EVAL",[[wo("Tested like")],[co("software.")]],"eval"),
]
CTA_SLIDE=("GET THE CHECKLIST",[[wo("Comment "),co("AGENTS")],[wo("for the checklist.")]],"cta")

def build_ig_cover(out,head):
    import numpy as np
    SS=2; W,H,MX=T.W*SS,T.H*SS,T.MX*SS                 # render 2x then downscale -> crisp text + logos
    base=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
    # hook CENTERED on top, no eyebrow / no sub-hook
    cw=W-2*MX; hsize=84*SS
    while hsize>64*SS:
        hf=B.dm(900,hsize)
        if max(d.textlength("".join(s[0] for s in ln),font=hf) for ln in head)<=cw: break
        hsize-=2*SS
    hf=B.dm(900,hsize); lh=96*SS; y=700*SS
    for ln in head:
        tw=sum(d.textlength(t,font=hf) for t,_ in ln); xx=(W-tw)//2
        for t,c in ln: d.text((xx,y),t,font=hf,fill=c); xx+=d.textlength(t,font=hf)
        y+=lh
    # Claude + Ultron logos BELOW the hook
    L=190*SS; SLOT=150*SS; BOOK=(204,120,92,255)
    def orb():
        im=Image.open(T.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        s=max(c.size); sq=Image.new("RGBA",(s,s),(0,0,0,0)); sq.alpha_composite(c,((s-c.width)//2,(s-c.height)//2))
        m=Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse([0,0,s,s],fill=255); sq.putalpha(m); return sq
    logos=[Image.open(T.GEN).convert("RGBA"),orb()]
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    n=len(logos); x=(W-(L*n+SLOT*(n-1)))//2; cy=1040*SS
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<n-1:
            px=x+L+SLOT//2; ph,pt=22*SS,5*SS
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=BOOK); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=BOOK)
        x+=L+SLOT
    base.resize((T.W,T.H),Image.LANCZOS).save(out)

def src_for(key):
    return CTA if key=="cta" else f"{MODELS}/{key}.png"

def build_variant(n_content, outdir, overlay):
    os.makedirs(outdir,exist_ok=True); md=f"{outdir}/_models"; os.makedirs(md,exist_ok=True)
    slides=[("COVER",COVER["head"],None,"cover")]
    for eb,head,key in CONTENT[:n_content]: slides.append((eb,head,key,"mid"))
    eb,head,key=CTA_SLIDE; slides.append((eb,head,key,"last"))
    SPECS={}
    for i,(eb,head,key,role) in enumerate(slides,1):
        SPECS[i]=dict(role=role,num=f"{i:02d}",head=head)
        if role=="cover": SPECS[i]["eyebrow"]=COVER.get("eyebrow","")
        elif eb: SPECS[i]["eyebrow"]=eb
        if key: shutil.copy(src_for(key), f"{md}/m{i}.png")
    B.SPECS=SPECS; T.N=len(slides)
    for i,(eb,head,key,role) in enumerate(slides,1):
        if role=="cover" and overlay: build_ig_cover(f"{outdir}/s{i}.png", head)
        else: T.build(i, md, outdir)
    return len(slides)

tt=build_variant(8, f"{TE}/roll3/agentsprod_3d_tt", overlay=False)   # TikTok: normal cover + 8 + CTA = 10
ig=build_variant(8, f"{TE}/roll3/agentsprod_3d_ig", overlay=True)    # IG: overlay cover + 8 + CTA = 10
print("TikTok 3D slides:",tt," IG slides:",ig)
for od,name in [("agentsprod_3d_tt","agentsprod3d_tt"),("agentsprod_3d_ig","agentsprod3d_ig")]:
    N=len(os.listdir(f"{TE}/roll3/{od}"))-1
    ims=[Image.open(f"{TE}/roll3/{od}/s{i}.png") for i in range(1,N+1)]
    cols=5; rows=(N+cols-1)//cols; sc=220; sh=int(sc*1920/1080)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{name}_montage.png")
print("montages done")
