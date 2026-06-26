#!/usr/bin/env python3
# TikTok 3D (Model B) - HUMAN GATE. Reuses build_3d916's 9:16 pager with HITL content + HITL models.
import os
from PIL import Image
import build_slides as B
import build_3d916 as T
co=lambda s:(s,B.CORAL); wo=lambda s:(s,B.WHITE)
HITL={
1:dict(role="cover",num="01",head=[[wo("Your AI can send,")],[wo("charge and delete.")],[co("Mine asks first.")]],sub="It runs the busywork. It stops before anything it cannot undo."),
2:dict(role="mid",num="02",eyebrow="THE GATE",head=[[wo("It stops before")],[co("it ships.")]],body=[("It drafts the work and runs it, then pauses at every step that leaves the building.",0)]),
3:dict(role="mid",num="03",eyebrow="WHAT NEEDS A YES",head=[[co("7 moves")],[wo("that need your yes.")]]),
4:dict(role="mid",num="04",eyebrow="THE DECISION",head=[[wo("Approve, decline,")],[co("or pick a path.")]]),
5:dict(role="mid",num="05",eyebrow="EDIT FIRST",head=[[wo("Change it before")],[co("it ships.")]],body=[("Edit the action on the card, then approve the version you actually want.",0)]),
6:dict(role="mid",num="06",eyebrow="THE RULE",head=[[wo("Before the action.")],[co("Never after.")]],body=[("An approval after the fact is theatre. The gate sits before the irreversible step.",0)]),
7:dict(role="mid",num="07",eyebrow="THE RECORD",head=[[wo("Every yes")],[co("is logged.")]]),
8:dict(role="last",num="08",eyebrow="GET THE SETUP",head=[[wo("Comment "),co("GATE")],[wo("I will send it.")]],body=[("The exact human-gate setup I run my company on. Follow for one AI system for founders every day.",0)]),
}
B.SPECS=HITL

def build_ig_cover(out):
    # Transparent IG overlay: BIG hook only (no subhook), STATIC flat Claude logo (not the 3D one),
    # no corner number, no swipe. Designed to sit over a short reel video.
    from PIL import ImageDraw
    W,H,MX=T.W,T.H,T.MX
    base=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
    head=HITL[1]["head"]; cw=W-2*MX
    hsize=116                                              # largest hook that still fits the width
    while hsize>72:
        hf=B.dm(900,hsize)
        if max(d.textlength("".join(s[0] for s in line),font=hf) for line in head)<=cw: break
        hsize-=2
    hf=B.dm(900,hsize); lh=hsize+16; y=404
    for line in head: B.seg_line(d,MX,y,line,hf); y+=lh
    # 4 AI logos in a row under the hook, equal size: Claude, Gemini, ChatGPT, Ultron
    import numpy as np
    LOGOD=f"{T.TE}/logos"; L=160; SLOT=76; BOOK=(204,120,92,255)
    def ultron_orb():
        im=Image.open(T.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36)                                 # crop tight to the sphere (drop the black)
        c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        s=max(c.size); sq=Image.new("RGBA",(s,s),(0,0,0,0)); sq.alpha_composite(c,((s-c.width)//2,(s-c.height)//2))
        m=Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse([0,0,s,s],fill=255); sq.putalpha(m)
        return sq
    logos=[Image.open(T.GEN).convert("RGBA"),
           Image.open(f"{LOGOD}/gemini.png").convert("RGBA"),
           Image.open(f"{LOGOD}/openai.png").convert("RGBA"),
           ultron_orb()]
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    n=len(logos); x=(W-(L*n+SLOT*(n-1)))//2; ly=int(y)+62; cy=ly+L//2
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<n-1:                                              # book "+" between logos
            px=x+L+SLOT//2; ph,pt=23,5
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=BOOK); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=BOOK)
        x+=L+SLOT
    base.save(out)

MF=f"{T.TE}/roll3/models_hitl"; OUT=f"{T.TE}/roll3/hitl_3d_9"; os.makedirs(OUT,exist_ok=True)
for n in range(1,9): T.build(n,MF,OUT); print("built",n)
# Instagram variant: slide 1 = transparent overlay (hook + 3D logo only, no corner number, no swipe),
# laid over a short reel video; slides 2-8 identical to the TikTok 3D set.
import shutil
IGOUT=f"{T.TE}/roll3/hitl_ig_3d"; os.makedirs(IGOUT,exist_ok=True)
build_ig_cover(f"{IGOUT}/s1.png"); print("built IG s1 (transparent overlay: big hook + static logo)")
for n in range(2,9): shutil.copy(f"{OUT}/s{n}.png", f"{IGOUT}/s{n}.png")
ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,9)]
cols=4;rows=2;sc=300;sh=int(sc*1920/1080)
st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
st.save(f"{T.TE}/hitl_3d_montage.png"); print("montage saved")
