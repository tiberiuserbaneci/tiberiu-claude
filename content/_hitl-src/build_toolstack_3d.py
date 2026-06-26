#!/usr/bin/env python3
# Jobs 3D: TikTok (8 slides) + Instagram (10 slides, transparent overlay cover).
# Reuses build_3d916's pager, the Jobs Vertex objects, the reusable OPERATOR CTA pill,
# and the 3D Claude logo. No per-material CTA generation.
import os, shutil
from PIL import Image, ImageDraw
import build_slides as B
import build_3d916 as T
co=lambda s:(s,B.CORAL); wo=lambda s:(s,B.WHITE)
TE=T.TE; LIB="/home/user/tiberiu-claude/content/_templates/tiktok/lib"
JOBS=f"{TE}/roll3/models_toolstack"; CTA=f"{TE}/roll3/cta3d/cta-operator.png"
T.LOGO3D=f"{LIB}/claude-logo-3d-glossy.png"   # vary the cover logo (HITL used glossy)

COVER=dict(role="cover",eyebrow="YOUR WHOLE STACK",head=[[wo("Nine apps by hand.")],[co("Now one chat.")]],
           sub="One message runs the research, the CRM, the email, the calendar and the billing.")
# (eyebrow, head, object-key) - first 6 -> TikTok 8, all 8 -> IG 10
CONTENT=[
 ("THE BEFORE",[[wo("Nine apps.")],[co("Nine tabs.")]],"before"),
 ("THE MOTION",[[wo("One message.")],[co("The whole motion.")]],"motion"),
 ("THE APPS",[[wo("Every app,")],[co("one chat.")]],"apps"),
 ("ONE MESSAGE",[[wo("Say it once.")],[co("It runs.")]],"onemsg"),
 ("THE HUB",[[wo("One chat")],[co("runs them all.")]],"hub"),
 ("THE GATE",[[wo("Except the")],[co("irreversible.")]],"gate"),
 ("THE COUNT",[[wo("Ninety-two")],[co("actions.")]],"count"),
 ("ONE PLACE",[[wo("No tenth tool.")],[co("One chat.")]],"onechat"),
]
CTA_SLIDE=("GET THE STACK",[[wo("Your whole stack,")],[co("one chat.")]],"cta")

def build_ig_cover(out,head):
    import numpy as np
    SS=2; W,H,MX=T.W*SS,T.H*SS,T.MX*SS                 # render 2x then downscale -> crisp text + logos
    base=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
    cw=W-2*MX; hsize=84*SS
    while hsize>64*SS:
        hf=B.dm(900,hsize)
        if max(d.textlength("".join(s[0] for s in ln),font=hf) for ln in head)<=cw: break
        hsize-=2*SS
    if COVER.get("eyebrow"): B.ls_text(d,(MX,340*SS),COVER["eyebrow"],B.mono(28*SS),B.CORAL,4)
    hf=B.dm(900,hsize); lh=96*SS; y=404*SS               # over-video intro cover -> top-anchored, NOT centered mid-slide
    for ln in head: B.seg_line(d,MX,y,ln,hf); y+=lh
    L=200*SS; SLOT=156*SS; BOOK=(204,120,92,255)        # wide gap: logo  +  logo
    def orb():
        im=Image.open(T.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        s=max(c.size); sq=Image.new("RGBA",(s,s),(0,0,0,0)); sq.alpha_composite(c,((s-c.width)//2,(s-c.height)//2))
        m=Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse([0,0,s,s],fill=255); sq.putalpha(m); return sq
    logos=[Image.open(T.GEN).convert("RGBA"),orb()]     # Claude + Ultron only
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    n=len(logos); x=(W-(L*n+SLOT*(n-1)))//2; cy=720*SS       # logos tucked under the hook in the top third, not floating
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<n-1:
            px=x+L+SLOT//2; ph,pt=23*SS,5*SS
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=BOOK); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=BOOK)
        x+=L+SLOT
    base.resize((T.W,T.H),Image.LANCZOS).save(out)

def src_for(key):
    return CTA if key=="cta" else f"{JOBS}/{key}.png"

def build_variant(n_content, outdir, overlay):
    os.makedirs(outdir,exist_ok=True); md=f"{outdir}/_models"; os.makedirs(md,exist_ok=True)
    slides=[("COVER",COVER["head"],None,"cover")]
    for eb,head,key in CONTENT[:n_content]: slides.append((eb,head,key,"mid"))
    eb,head,key=CTA_SLIDE; slides.append((eb,head,key,"last"))
    SPECS={};
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

tt=build_variant(6, f"{TE}/roll3/toolstack_3d_tt", overlay=False)   # TikTok: cover + 6 content + CTA = 8
ig=build_variant(8, f"{TE}/roll3/toolstack_3d_ig", overlay=True)    # IG: overlay cover + 8 content + CTA = 10
print("TikTok 3D slides:",tt," IG slides:",ig)
# montages
for od,name in [("toolstack_3d_tt","toolstack3d_tt"),("toolstack_3d_ig","toolstack3d_ig")]:
    N=len(os.listdir(f"{TE}/roll3/{od}"))-1  # minus _models
    ims=[Image.open(f"{TE}/roll3/{od}/s{i}.png") for i in range(1,N+1)]
    cols=5; rows=(N+cols-1)//cols; sc=220; sh=int(sc*1920/1080)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{name}_montage.png")
print("montages done")
