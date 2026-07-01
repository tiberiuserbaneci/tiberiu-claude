#!/usr/bin/env python3
# EDITORIAL 4:5 (1080x1350) renderer - TikTok/IG photo-carousel top-performer format (S9).
# Kills the 9:16 empty bands: ~112px side padding (extra left breathing room), NO 300/330 safe
# insets, big dark-premium objects that fill the frame, plus a per-slide SUBHOOK (the why / one
# more fact). Reuses an imported material's COVER/CONTENT/CTA/CLOSE + engine helpers.
# CONTENT item: (eyebrow, hook, [subhook], object, fill)  - subhook optional (5-tuple).
# Usage: python3 build_ed45.py <build_module.py> <outprefix>
import importlib.util, os, sys
import numpy as np
from PIL import Image, ImageDraw
def load(p):
    s=importlib.util.spec_from_file_location("MAT",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
MAT=load(sys.argv[1]); OUT=sys.argv[2]
T2=MAT.T2
COVER,CONTENT,CTA=T2.COVER,T2.CONTENT,T2.CTA
CLOSE=getattr(T2,"CLOSE",dict(l1="Save this",l2="for later",q="Which first?"))
dm,mono=T2.dm,T2.mono
WHITE,CORAL,MUTED,BG,TRACK,GHOST=T2.WHITE,T2.CORAL,T2.MUTED,T2.BG,T2.TRACK,T2.GHOST
INK=(206,206,199)   # sub-hook ink (brighter than MUTED)
ULOGO,CLAUDE_SUN=T2.ULOGO,T2.CLAUDE_SUN
crop_obj,fit_hook,seg_line,ls_text,seg_center=T2.crop_obj,T2.fit_hook,T2.seg_line,T2.ls_text,T2.seg_center
# ---- SAFE ZONES (1080x1350 TikTok/IG photo carousel) ----
# left  112  (extra breathing room, operator)   right 112 -> object x ~[112,968], clear of edge
# top   ~60  (status bar)                        bottom ~100 (caption band); progress sits above it
W,H,MX=1080,1350,112

def dots(base):
    d=ImageDraw.Draw(base)
    for y in range(0,H,30):
        for x in range(0,W,30): d.point((x,y),fill=(31,26,24))
def ghost(base,num):
    d=ImageDraw.Draw(base); f=dm(900,112)   # smaller + higher so it clears the sub-hook line
    d.text((W-MX-d.textlength(num,font=f),58),num,font=f,fill=GHOST)
def progress(d,page,n):
    x0,x1=MX,W-MX; yb=H-56; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=CORAL)
def footer(base):
    d=ImageDraw.Draw(base); y=H-70
    lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((44,44),Image.LANCZOS); base.alpha_composite(lg,(MX,y-8))
    d.text((MX+58,y),"ULTRON",font=mono(26),fill=WHITE)
    u="51ultron.com"; f=dm(900,30); d.text((W-MX-d.textlength(u,font=f),y-4),u,font=f,fill=WHITE)
def wrap(d,text,font,maxw,maxlines=2):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines[:maxlines]

OBJ_CY=762; OBJ_H=636; OBJ_MAXW=904   # every object: WHOLE (uncut), sized by the dense TABLET (not the glow), centred -> equal
def _tbox(d,thr=55,dens=80):
    # bbox of the WHOLE tablet (dense region), incl. its dark lower half; the diffuse drop-glow is
    # not dense enough to survive the column/row filter, so it is excluded from sizing.
    m=d>thr; cols=np.where(m.sum(0)>dens)[0]; rows=np.where(m.sum(1)>dens)[0]
    if len(cols) and len(rows): return int(cols.min()),int(rows.min()),int(cols.max()),int(rows.max())
    ys,xs=np.where(d>40); return int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())
def place_obj(base,objpath,fill=1.0):
    arr=np.asarray(Image.open(objpath).convert("RGB")).astype(int); H0,W0=arr.shape[:2]
    cs=np.concatenate([arr[:48,:48].reshape(-1,3),arr[:48,-48:].reshape(-1,3),arr[-48:,:48].reshape(-1,3),arr[-48:,-48:].reshape(-1,3)])
    bg=np.median(cs,0); d=np.abs(arr-bg).sum(2)
    tx0,ty0,tx1,ty1=_tbox(d)                               # the whole tablet
    pad=42; cx0,cy0=max(0,tx0-pad),max(0,ty0-pad); cx1,cy1=min(W0,tx1+pad),min(H0,ty1+pad)
    alpha=np.clip((d-16)*18,0,255).astype("uint8")         # near-opaque: dark lower half stays solid; far bg drops out
    el=Image.fromarray(np.dstack([arr.astype("uint8"),alpha]),"RGBA").crop((cx0,cy0,cx1,cy1))
    tw,th=tx1-tx0,ty1-ty0; r=min(OBJ_MAXW/tw, OBJ_H/th)*fill   # SIZE by the tablet -> equal across slides
    el=el.resize((max(1,int(el.width*r)),max(1,int(el.height*r))),Image.LANCZOS)
    tcx=((tx0+tx1)/2-cx0)*r; tcy=((ty0+ty1)/2-cy0)*r          # tablet centre inside the scaled crop
    base.alpha_composite(el,(int(W/2-tcx), int(OBJ_CY-tcy)))  # tablet centre -> identical X/Y every slide
def body(base,eyebrow,head,sub,foot,objpath,page,n,fill):
    ghost(base,f"{page:02d}"); d=ImageDraw.Draw(base)
    ls_text(d,(MX,66),eyebrow,mono(27),CORAL,4)
    s=min(fit_hook(d,head,W-2*MX,start=64,floor=46),60); hf=dm(900,s); y=108
    for ln in head: seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    y+=32   # clear gap between hook and sub-hook
    if sub:
        sf=dm(500,31)
        for ln in wrap(d,sub,sf,W-2*MX): d.text((MX,y),ln,font=sf,fill=INK); y+=41
    place_obj(base,objpath,fill)
    if foot:   # the idea line under the object (fills the lower space)
        ff=dm(800,34); fw=int(d.textlength("".join(t for t,_ in foot),font=ff))
        seg_line(d,(W-fw)//2,H-176,foot,ff)
    progress(d,page,n)

def cover_tt(base):
    ghost(base,"01"); d=ImageDraw.Draw(base)
    s=fit_hook(d,COVER["head"],W-2*MX,start=76); hf=dm(900,s); y=352
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=int(s*1.18)
    T2.place_in_zone(base, Image.open(CLAUDE_SUN).convert("RGBA"), (410,740,670,1050))
    txt="Swipe"; f=dm(900,34); tw=int(d.textlength(txt,font=f)); aw=int(d.textlength("  →",font=f)); pw=tw+aw+80; ph=76; px=(W-pw)//2; py=H-186
    d.rounded_rectangle([px,py,px+pw,py+ph],radius=ph//2,fill=CORAL)
    d.text((px+40,py+ph//2-24),txt+"  →",font=f,fill=(26,15,10))

def cover_ig(out):
    SS=2; w,h,mx=W*SS,H*SS,MX*SS
    base=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(base)
    s=76*SS
    while s>52*SS:
        hf=dm(900,s)
        if max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in COVER["head"])<=w-2*mx: break
        s-=2*SS
    hf=dm(900,s); y=300*SS
    for ln in COVER["head"]:
        tw=sum(d.textlength(t,font=hf) for t,_ in ln); seg_line(d,(w-tw)//2,y,ln,hf); y+=int(s*1.14)
    def orb():
        im=Image.open(ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
        m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq,sq],fill=255); s2.putalpha(m); return s2
    logos=[Image.open(CLAUDE_SUN).convert("RGBA"), orb()]
    L=190*SS; SLOT=150*SS
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    nn=len(logos); x=(w-(L*nn+SLOT*(nn-1)))//2; cy=y+120*SS
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<nn-1:
            px=x+L+SLOT//2; ph,pt=22*SS,5*SS
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=T2.BOOK+(255,)); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=T2.BOOK+(255,))
        x+=L+SLOT
    base.resize((W,H),Image.LANCZOS).save(out)

def closing(base,handle,page,n):
    ghost(base,f"{page:02d}"); d=ImageDraw.Draw(base)
    ls_text(d,(MX,356),"SAVE THIS",mono(28),CORAL,4)
    hf=dm(900,76); y=424
    for ln in [CLOSE["l1"],CLOSE["l2"]]: d.text((MX,y),ln,font=hf,fill=WHITE); y+=int(76*1.1)
    d.text((MX,y+10),CLOSE["q"],font=dm(500,33),fill=MUTED)
    py=y+92; txt=f"{handle}   →"; f=dm(800,42); tw=int(d.textlength(txt,font=f)); pw=tw+80; ph=90
    d.rounded_rectangle([MX,py,MX+pw,py+ph],radius=ph//2,fill=CORAL); d.text((MX+40,py+ph//2-28),txt,font=f,fill=(22,13,8))
    lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS); base.alpha_composite(lg,(MX,H-160))
    d.text((MX+64,H-150),handle,font=mono(30),fill=CORAL)

def unpack(item):
    eb,head=item[0],item[1]
    sub=item[2] if len(item)>4 else None
    foot=item[3] if len(item)>5 else None
    return eb,head,sub,foot,item[-2],item[-1]

def deck(outdir, overlay):
    os.makedirs(outdir,exist_ok=True)
    for f in os.listdir(outdir):
        if f.startswith("s") and f.endswith(".png"): os.remove(os.path.join(outdir,f))
    slides=[("cover",)]+[("mid",c) for c in CONTENT]
    slides+=[("close","@tiberiu.ai"),("close","@51ultron")] if not overlay else [("last",CTA)]
    n=len(slides)
    for i,sl in enumerate(slides,1):
        if sl[0]=="cover":
            if overlay: cover_ig(f"{outdir}/s{i}.png"); continue
            base=Image.new("RGBA",(W,H),BG+(255,)); dots(base); cover_tt(base); base.convert("RGB").save(f"{outdir}/s{i}.png"); continue
        base=Image.new("RGBA",(W,H),BG+(255,)); dots(base)
        if sl[0]=="close": closing(base,sl[1],i,n)
        elif sl[0]=="last":
            eb,head,objp,fill=CTA[0],CTA[1],CTA[-2],CTA[-1]; ghost(base,f"{i:02d}"); d=ImageDraw.Draw(base)
            ls_text(d,(MX,356),eb,mono(28),CORAL,4)
            s=fit_hook(d,head,W-2*MX,start=76,floor=54); hf=dm(900,s); y=424
            for ln in head: seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
            T2.place_in_zone(base, crop_obj(Image.open(objp)), (MX,690,W-MX,1120), fill=fill)
            d.text((MX,1150),"Follow for one AI system for founders every day.",font=dm(700,28),fill=WHITE); footer(base)
        else:
            eb,head,sub,foot,objp,fill=unpack(sl[1]); body(base,eb,head,sub,foot,objp,i,n,fill)
        base.convert("RGB").save(f"{outdir}/s{i}.png")
    return n

if __name__=="__main__":
    a=deck(f"{T2.OUTBASE}/{OUT}_tt",False); b=deck(f"{T2.OUTBASE}/{OUT}_ig",True)
    print("tt",a,"ig",b)
