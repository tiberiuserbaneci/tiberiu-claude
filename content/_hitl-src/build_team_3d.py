#!/usr/bin/env python3
# THE TEAM - 9:16 (1080x1920) 3D carousel, TikTok + Instagram.
# Self-contained (no dead session paths): fonts from content/assets, objects from content/_hitl-src,
# pills/logos from _templates/tiktok/lib. Same 10-slide deck on both channels; ONLY slide 1 differs
# (IG = transparent overlay cover, TikTok = normal opaque cover). Architecture = the proven "FEATURE
# DROP" winner (modules/billing). Anchors locked per analysis/reel-carousel-design.md (fast-flip).
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT="/home/user/tiberiu-claude"
ASSETS=f"{ROOT}/content/assets"; OBJ=f"{ROOT}/content/_hitl-src"; LIB=f"{ROOT}/content/_templates/tiktok/lib"
OUTBASE=f"{ROOT}/scratchpad"
W,H,MX=1080,1920,90
BG=(25,25,25); WHITE=(250,250,247); CORAL=(200,100,63); MUTED=(154,154,146); GHOST=(54,53,50); TRACK=(60,59,57)
BOOK=(204,120,92)
ULOGO=f"{ROOT}/content/ultron-logo.png"           # Ultron sphere
CLAUDE_SUN=f"{OBJ}/claude_official.png"            # Claude sunburst (cover)
LOGO3D=f"{LIB}/claude-logo-3d-matte.png"           # TikTok cover 3D Claude mark

def dm(w,px):
    m={900:"DMSans-900",800:"DMSans-800",700:"DMSans-700",500:"DMSans-500"}
    return ImageFont.truetype(f"{ASSETS}/{m.get(w,'DMSans-700')}.ttf",px)
def mono(px,med=True): return ImageFont.truetype(f"{ASSETS}/{'DMMono-500' if med else 'DMMono-400'}.ttf",px)
def ls_text(d,xy,s,font,fill,ls):
    x,y=xy
    for ch in s: d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+ls
    return x
def seg_line(d,x,y,segs,font):
    for txt,col in segs: d.text((x,y),txt,font=font,fill=col); x+=d.textlength(txt,font=font)
    return x
def seg_center(d,y,segs,font):
    tw=sum(d.textlength(t,font=font) for t,_ in segs); x=(W-tw)//2
    for t,c in segs: d.text((x,y),t,font=font,fill=c); x+=d.textlength(t,font=font)

def crop_obj(im):
    a=np.asarray(im.convert("RGB")).astype(int); h,w=a.shape[:2]; area=h*w
    cs=np.concatenate([a[:48,:48].reshape(-1,3),a[:48,-48:].reshape(-1,3),a[-48:,:48].reshape(-1,3),a[-48:,-48:].reshape(-1,3)])
    bg=np.median(cs,0).astype(int); diff=np.abs(a-bg).sum(2); bbox=None
    for thr in (120,100,80,65,52,42,34,28,22):
        ys,xs=np.where(diff>thr)
        if len(xs)==0: continue
        b=(int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max()))
        if (b[2]-b[0])*(b[3]-b[1])<=0.93*area: bbox=b
        else: break
    if bbox is None: return im.convert("RGBA")
    pad=18; x0=max(0,bbox[0]-pad); y0=max(0,bbox[1]-pad); x1=min(w,bbox[2]+pad); y1=min(h,bbox[3]+pad)
    crop=im.convert("RGB").crop((x0,y0,x1,y1)); c=np.asarray(crop).astype(int); d2=np.abs(c-bg).sum(2)
    alpha=np.clip((d2-16)*18,0,255).astype("uint8")
    return Image.fromarray(np.dstack([np.asarray(crop).astype("uint8"),alpha]),"RGBA")

def place_in_zone(base,el,zone,fill=1.0):
    zx0,zy0,zx1,zy1=zone; pad=6; zw,zh=zx1-zx0-2*pad, zy1-zy0-2*pad
    solid=el.split()[3].point(lambda v:255 if v>140 else 0); pb=solid.getbbox() or (0,0,el.width,el.height)
    pw,ph=max(1,pb[2]-pb[0]),max(1,pb[3]-pb[1]); r=min(zw/pw, zh/ph)*fill
    el=el.resize((max(1,int(el.width*r)),max(1,int(el.height*r))),Image.LANCZOS)
    solid=el.split()[3].point(lambda v:255 if v>140 else 0); pb=solid.getbbox() or (0,0,el.width,el.height)
    pcx=(pb[0]+pb[2])/2; pcy=(pb[1]+pb[3])/2
    cx=W//2; cy=(zy0+zy1)//2; ox=int(round(cx-pcx)); oy=int(round(cy-pcy))
    al=el.split()[3]; shmask=Image.new("L",base.size,0); shmask.paste(al,(ox,oy+30))
    shmask=shmask.filter(ImageFilter.GaussianBlur(42)).point(lambda v:int(v*0.5))
    base.alpha_composite(Image.merge("RGBA",(Image.new("L",base.size,0),)*3+(shmask,)))
    base.alpha_composite(el,(ox,oy))

def ghost(base,num):
    f=dm(900,150); layer=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(layer)
    tw=dl.textlength(num,font=f); dl.text((922-tw,298),num,font=f,fill=GHOST+(255,))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(4)))

def progress(d,page,n):
    x0,x1=90,928; y=1352; h=7
    d.rounded_rectangle([x0,y,x1,y+h],radius=4,fill=TRACK)
    d.rounded_rectangle([x0,y,x0+int((x1-x0)*page/n),y+h],radius=4,fill=CORAL)

def footer(base):
    d=ImageDraw.Draw(base); lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS)
    base.alpha_composite(lg,(90,1330)); d.text((154,1340),"51ultron.com",font=mono(30),fill=CORAL)

def swipe(base):
    bw,bh=252,78; bx=(W-bw)//2; by=1360
    sh=Image.new("RGBA",(bw+60,bh+60),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([30,34,30+bw,34+bh],radius=bh//2,fill=(200,100,63,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(15)),(bx-30,by-30))
    btn=Image.new("RGBA",(bw,bh),(0,0,0,0)); ImageDraw.Draw(btn).rounded_rectangle([0,0,bw-1,bh-1],radius=bh//2,fill=(200,100,63,255))
    base.alpha_composite(btn,(bx,by)); d=ImageDraw.Draw(base); f=dm(800,37)
    lbl="Swipe"; lw=d.textlength(lbl,font=f); gap=16; aw=32; tx=bx+(bw-(lw+gap+aw))/2; ty=by+(bh-44)/2
    d.text((tx,ty),lbl,font=f,fill=WHITE); ay=by+bh/2; ax0=tx+lw+gap; ax1=ax0+aw
    d.line([(ax0,ay),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay-11),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay+11),(ax1,ay)],fill=WHITE,width=5)

def fit_hook(d,head,maxw,start=84,floor=58):
    s=start
    while s>floor:
        hf=dm(900,s)
        if max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=maxw: break
        s-=2
    return s

# ---- content ----
co=lambda s:(s,CORAL); wo=lambda s:(s,WHITE)
COVER=dict(head=[[wo("I run a company of seven.")],[co("I work alone.")]])   # no eyebrow on the cover (rule)
V=f"{OBJ}/models_team/v3"   # varied forms, one material system (congruence != uniformity)
# (eyebrow, head, object, fill) - fill varies object footprint so sizes differ slide to slide
CONTENT=[
 ("CORTEX",   [[wo("One researches")],[co("the account.")]], f"{V}/cortex.png",  0.92),
 ("SPECTER",  [[wo("One writes")],[co("the outreach.")]],    f"{V}/specter.png", 0.96),
 ("STRIKER",  [[wo("One works")],[co("the deal.")]],         f"{V}/striker.png", 0.99),
 ("PULSE",    [[wo("One posts")],[co("in your voice.")]],    f"{V}/pulse.png",   0.95),
 ("SENTINEL", [[wo("One ships")],[co("the code.")]],         f"{V}/sentinel.png",0.93),
 ("THE GATE", [[wo("You approve")],[co("every move.")]],     f"{V}/gate.png",    0.62),
 ("THE TEAM", [[wo("Seven of them,")],[co("one chat.")]],    f"{V}/team.png",    0.82),
 ("HOW",      [[wo("Each one")],[co("a slash away.")]],      f"{V}/how.png",     0.84),
]
CTA=("GET THE TEAM", [[wo("Your team,")],[co("in your chat.")]], f"{LIB}/cta3d-operator.png", 0.92)

def body_slide(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base)
    ghost(base, f"{page:02d}")
    ls_text(d,(MX,476),eyebrow,mono(28),CORAL,4)
    s=fit_hook(d,head,W-2*MX,start=84,floor=64); hf=dm(900,s); lh=int(s*1.14); y=540   # auto-fit guard: stays 84 unless a line would overflow
    for ln in head: seg_line(d,MX,y,ln,hf); y+=lh
    elt_bottom=1238 if last else 1326
    place_in_zone(base, crop_obj(Image.open(objpath)), (88,758,942,elt_bottom), fill=fill)
    if last:
        d.text((MX,1258),"Follow for one AI system for founders every day.",font=dm(700,29),fill=WHITE)
        footer(base)
    else:
        progress(d,page,n)

def cover_tt(base, n):
    # NO eyebrow on the cover (rule). Hook centered in the middle, 3D Claude mark below, per S30.
    d=ImageDraw.Draw(base)
    ghost(base,"01")
    s=fit_hook(d,COVER["head"],W-2*MX,start=84); hf=dm(900,s); lh=int(s*1.18); y=640
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=lh
    place_in_zone(base, crop_obj(Image.open(LOGO3D)), (380,900,700,1260))
    swipe(base)

def cover_ig(out):
    SS=2; w,h,mx=W*SS,H*SS,MX*SS
    base=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(base)
    s=84*SS
    while s>58*SS:
        hf=dm(900,s)
        if max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in COVER["head"])<=w-2*mx: break
        s-=2*SS
    hf=dm(900,s); lh=int(s*1.14); y=404*SS   # no eyebrow on the cover (rule)
    for ln in COVER["head"]: seg_line(d,mx,y,ln,hf); y+=lh
    # Claude sunburst + Ultron sphere, tucked under the hook
    L=200*SS; SLOT=156*SS
    def orb():
        im=Image.open(ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
        m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq,sq],fill=255); s2.putalpha(m); return s2
    logos=[Image.open(CLAUDE_SUN).convert("RGBA"), orb()]
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    nn=len(logos); x=(w-(L*nn+SLOT*(nn-1)))//2; cy=760*SS
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, cy-im.height//2))
        if i<nn-1:
            px=x+L+SLOT//2; ph,pt=23*SS,5*SS
            d.rectangle([px-ph,cy-pt,px+ph,cy+pt],fill=BOOK+(255,)); d.rectangle([px-pt,cy-ph,px+pt,cy+ph],fill=BOOK+(255,))
        x+=L+SLOT
    base.resize((W,H),Image.LANCZOS).save(out)

def deck(outdir, overlay):
    os.makedirs(outdir,exist_ok=True)
    slides=[("cover",)]+[("mid",c) for c in CONTENT]+[("last",CTA)]
    n=len(slides)
    for i,sl in enumerate(slides,1):
        if sl[0]=="cover":
            if overlay: cover_ig(f"{outdir}/s{i}.png"); continue
            base=Image.new("RGBA",(W,H),BG+(255,)); cover_tt(base,n)
            base.convert("RGB").save(f"{outdir}/s{i}.png"); continue
        eb,head,objp,fill=sl[1]
        base=Image.new("RGBA",(W,H),BG+(255,))
        body_slide(base,eb,head,objp,i,n,last=(sl[0]=="last"),fill=fill)
        base.convert("RGB").save(f"{outdir}/s{i}.png")
    return n

def montage(outdir,name,n):
    ims=[Image.open(f"{outdir}/s{i}.png") for i in range(1,n+1)]
    cols=5; rows=(n+cols-1)//cols; sc=216; sh=int(sc*H/W)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{OUTBASE}/{name}_montage.jpg")

if __name__=="__main__":
    ntt=deck(f"{OUTBASE}/team_tt", overlay=False)
    nig=deck(f"{OUTBASE}/team_ig", overlay=True)
    montage(f"{OUTBASE}/team_tt","team_tt",ntt)
    montage(f"{OUTBASE}/team_ig","team_ig",nig)
    print("TikTok slides:",ntt," IG slides:",nig)
