#!/usr/bin/env python3
# Parametric 3D builder for the new batch (code / projects / skills / chat). Same centered-cover spec as
# build_agentsprod_3d: ONE 3D content set, IG 3D = overlay (transparent) centered cover, TikTok 3D = normal
# (opaque) centered cover with the 3D Claude mark on top. 10pp each (cover + 8 content + CTA). Usage:
#   python3 build_one.py <material>
import os, sys, shutil
from PIL import Image, ImageDraw
import build_slides as B
import build_3d916 as T
co=lambda s:(s,B.CORAL); wo=lambda s:(s,B.WHITE)
TE=T.TE; LIB="/home/user/tiberiu-claude/content/_templates/tiktok/lib"

CFG={
 "code":dict(logo="matte", eyebrow="CLAUDE CODE", cover=[[wo("Not autocomplete.")],[co("A coding agent.")]],
   sub="It plans, edits and tests inside your project, then opens the change for review.",
   content=[
    ("START",[[wo("Type one line.")],[co("It starts.")]],"start"),
    ("MEMORY",[[wo("It reads your repo,")],[co("remembers it.")]],"init"),
    ("PLAN FIRST",[[wo("It plans")],[co("before it edits.")]],"plan"),
    ("LET IT RUN",[[wo("It edits, tests,")],[co("fixes itself.")]],"run"),
    ("RESUME",[[wo("Pick up any")],[co("past session.")]],"resume"),
    ("ONE ASK",[[wo("Ask in English.")],[co("It ships.")]],"proof"),
    ("WHY",[[wo("A teammate,")],[co("not a toy.")]],"why"),
    ("THE LOOP",[[wo("Start. Describe.")],[co("Review.")]],"loop"),
   ], cta=("GET THE SETUP",[[wo("Comment "),co("CODE")],[wo("for the setup.")]],"cta")),
 "projects":dict(logo="glossy", eyebrow="CLAUDE PROJECTS", cover=[[wo("Stop re-explaining")],[co("your business.")]],
   sub="Set your rules, docs and context once. Every chat starts smart.",
   content=[
    ("THE PAIN",[[wo("You type context")],[co("into every chat.")]],"pain"),
    ("SET ONCE",[[wo("Set it once.")],[co("It remembers.")]],"setonce"),
    ("KNOWLEDGE",[[wo("Drop your docs.")],[co("It reads them.")]],"knowledge"),
    ("MEMORY",[[wo("It keeps")],[co("what you did.")]],"activity"),
    ("THREE INPUTS",[[wo("Rules. Docs.")],[co("Context.")]],"three"),
    ("BEFORE vs AFTER",[[wo("Same ask,")],[co("on brand first try.")]],"beforeafter"),
    ("NAME IT",[[wo("Name it after")],[co("the job.")]],"name"),
    ("EVERY OUTPUT",[[wo("One setup,")],[co("every output.")]],"everywhere"),
   ], cta=("GET THE TEMPLATE",[[wo("Comment "),co("PROJECTS")],[wo("for the template.")]],"cta")),
 "skills":dict(logo="metal", eyebrow="THE SKILL CATALOG", cover=[[wo("7 agents.")],[co("71 skills.")]],
   sub="One box fronts a whole specialist team. You call them by name or just describe the job.",
   content=[
    ("THE CATALOG",[[wo("One box.")],[co("A whole team.")]],"stats"),
    ("RESEARCH",[[wo("It researches")],[co("any account.")]],"cortex"),
    ("OUTBOUND",[[wo("It finds buyers,")],[co("writes the email.")]],"specter"),
    ("DEALS",[[wo("It preps")],[co("every call.")]],"striker"),
    ("CONTENT",[[wo("It writes")],[co("in your voice.")]],"pulse"),
    ("CODE",[[wo("It builds")],[co("and ships.")]],"sentinel"),
    ("ADS + LEGAL",[[wo("It runs ads,")],[co("reviews contracts.")]],"amplify"),
    ("HOW IT RUNS",[[wo("You ask.")],[co("It routes.")]],"how"),
   ], cta=("GET THE CATALOG",[[wo("Comment "),co("SKILLS")],[wo("for the catalog.")]],"cta")),
 "chat":dict(logo="glossy", eyebrow="ONE CHAT BOX", cover=[[wo("My whole GTM")],[co("in one chat.")]],
   sub="Eight habits moved every GTM job into one AI chat box, with one memory underneath.",
   content=[
    ("ONE BOX",[[wo("One box,")],[co("not twelve tabs.")]],"onebox"),
    ("SLASH IT",[[wo("Slash the agent")],[co("that owns it.")]],"slash"),
    ("PICK A TIER",[[wo("Spend deep")],[co("only when earned.")]],"tier"),
    ("MEMORY",[[wo("It loads context")],[co("before you type.")]],"memory"),
    ("UPLOAD ONCE",[[wo("Files become")],[co("context.")]],"upload"),
    ("BACKGROUND",[[wo("Long jobs run")],[co("in the background.")]],"background"),
    ("FORK IT",[[wo("Branch without")],[co("losing the thread.")]],"fork"),
    ("SEND IT",[[wo("Send the session,")],[co("not a screenshot.")]],"share"),
   ], cta=("GET THE CHEATSHEET",[[wo("Comment "),co("CHAT")],[wo("for the cheatsheet.")]],"cta")),
}

M=sys.argv[1]; C=CFG[M]
MODELS=f"{TE}/roll3/models_{M}"; CTA=f"{MODELS}/cta.png"
T.LOGO3D=f"{LIB}/claude-logo-3d-{C['logo']}.png"; T.CENTER_COVER=True
COVER=dict(role="cover",eyebrow=C["eyebrow"],head=C["cover"],sub=C["sub"]); CONTENT=C["content"]; CTA_SLIDE=C["cta"]

def build_ig_cover(out,head):
    import numpy as np
    SS=2; W,H,MX=T.W*SS,T.H*SS,T.MX*SS
    base=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
    L=190*SS; SLOT=150*SS; BOOK=(204,120,92,255)
    def orb():
        im=Image.open(T.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        s=max(c.size); sq=Image.new("RGBA",(s,s),(0,0,0,0)); sq.alpha_composite(c,((s-c.width)//2,(s-c.height)//2))
        m=Image.new("L",(s,s),0); ImageDraw.Draw(m).ellipse([0,0,s,s],fill=255); sq.putalpha(m); return sq
    logos=[Image.open(T.GEN).convert("RGBA"),orb()]
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    n=len(logos); x=(W-(L*n+SLOT*(n-1)))//2; cy=540*SS
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<n-1:
            px=x+L+SLOT//2; ph,pt=22*SS,5*SS
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=BOOK); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=BOOK)
        x+=L+SLOT
    cw=W-2*MX; hsize=84*SS
    while hsize>64*SS:
        hf=B.dm(900,hsize)
        if max(d.textlength("".join(s[0] for s in ln),font=hf) for ln in head)<=cw: break
        hsize-=2*SS
    if COVER.get("eyebrow"):
        ew=B.ls_width(d,COVER["eyebrow"],B.mono(28*SS),4*SS); B.ls_text(d,((W-ew)//2,820*SS),COVER["eyebrow"],B.mono(28*SS),B.CORAL,4*SS)
    hf=B.dm(900,hsize); lh=96*SS; y=884*SS
    for ln in head:
        tw=sum(d.textlength(t,font=hf) for t,_ in ln); xx=(W-tw)//2
        for t,c in ln: d.text((xx,y),t,font=hf,fill=c); xx+=d.textlength(t,font=hf)
        y+=lh
    base.resize((T.W,T.H),Image.LANCZOS).save(out)

def src_for(key): return CTA if key=="cta" else f"{MODELS}/{key}.png"

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

tt=build_variant(8, f"{TE}/roll3/{M}_3d_tt", overlay=False)
ig=build_variant(8, f"{TE}/roll3/{M}_3d_ig", overlay=True)
print(M,"TikTok 3D:",tt," IG:",ig)
for od,name in [(f"{M}_3d_tt",f"{M}3d_tt"),(f"{M}_3d_ig",f"{M}3d_ig")]:
    N=len(os.listdir(f"{TE}/roll3/{od}"))-1
    ims=[Image.open(f"{TE}/roll3/{od}/s{i}.png") for i in range(1,N+1)]
    cols=5; rows=(N+cols-1)//cols; sc=220; sh=int(sc*1920/1080)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{name}_montage.png")
print("montages done")
