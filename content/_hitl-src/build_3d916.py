#!/usr/bin/env python3
# 9:16 (1080x1920) page for the 3D-Vertex carousels. Reuses the EXISTING 3D model images
# (no Vertex regen) - crops + alpha-keys + grounds them in a fixed zone, with 1920 chrome.
# Usage: python3 build_3d916.py <model_dir_name> <out_dir_name>   e.g. models operator2_9
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import build_slides as B
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
W,H,MX=1080,1920,72
BG=B.BG; WHITE=B.WHITE; CORAL=B.CORAL; MUTED=B.MUTED; N=B.N
ULOGO="/home/user/tiberiu-claude/content/ultron-logo.png"; GEN=f"{TE}/claude_official.png"
ZONE=(90,888,928,1290)   # CROSS-CHANNEL standard: content within y[300,1450] x[90,930] (TikTok + IG)

def crop_obj(im):
    a=np.asarray(im.convert("RGB")).astype(int); diff=np.abs(a-np.array([25,25,25])).sum(2)
    ys,xs=np.where(diff>40)
    if len(xs)==0: return im.convert("RGBA")
    pad=8; x0=max(0,int(xs.min())-pad); x1=min(im.width,int(xs.max())+pad); y0=max(0,int(ys.min())-pad); y1=min(im.height,int(ys.max())+pad)
    crop=im.convert("RGB").crop((x0,y0,x1,y1)); c=np.asarray(crop).astype(int); d2=np.abs(c-np.array([25,25,25])).sum(2)
    alpha=np.clip((d2-30)*14,0,255).astype("uint8")
    return Image.fromarray(np.dstack([np.asarray(crop).astype("uint8"),alpha]),"RGBA")

def place_in_zone(base,el):
    zx0,zy0,zx1,zy1=ZONE; pad=8; zw,zh=zx1-zx0-2*pad, zy1-zy0-2*pad
    r=min(zw/el.width, zh/el.height); nw,nh=max(1,int(el.width*r)),max(1,int(el.height*r))
    el=el.resize((nw,nh),Image.LANCZOS); ox=zx0+pad+(zw-nw)//2; oy=zy0+pad+(zh-nh)//2
    al=el.split()[3]; shmask=Image.new("L",base.size,0); shmask.paste(al,(ox,oy+30))
    shmask=shmask.filter(ImageFilter.GaussianBlur(42)).point(lambda v:int(v*0.5))
    base.alpha_composite(Image.merge("RGBA",(Image.new("L",base.size,0),)*3+(shmask,)))
    base.alpha_composite(el,(ox,oy))

def ghost(base,num):                                  # big page number, FREE + INSIDE the top safe band (y>300, x<950)
    f=B.dm(900,270); layer=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(layer)
    tw=dl.textlength(num,font=f); dl.text((916-tw,316),num,font=f,fill=(56,55,52,255))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(5)))

def progress(d,page,n):
    x0,x1=90,928; y=1352; h=7                          # inside the cross-channel band (y<1450, x<930)
    d.rounded_rectangle([x0,y,x1,y+h],radius=4,fill=B.TRACK)
    d.rounded_rectangle([x0,y,x0+int((x1-x0)*page/n),y+h],radius=4,fill=CORAL)
    f=B.mono(26); lbl=f"{page:02d} / {n:02d}"; lw=d.textlength(lbl,font=f); d.text((928-lw,y-46),lbl,font=f,fill=MUTED)

def footer(base,page,n):
    d=ImageDraw.Draw(base); lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS)
    base.alpha_composite(lg,(90,1330)); f=B.mono(30); d.text((154,1340),"51ultron.com",font=f,fill=CORAL)
    f2=B.mono(26); lbl=f"{page:02d} / {n:02d}"; lw=d.textlength(lbl,font=f2); d.text((928-lw,1342),lbl,font=f2,fill=MUTED)

def swipe(base):
    bw,bh=252,78; bx=(W-bw)//2; by=1316                # raised into the cross-channel band (clears IG caption block)
    sh=Image.new("RGBA",(bw+60,bh+60),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([30,34,30+bw,34+bh],radius=bh//2,fill=(200,100,63,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(15)),(bx-30,by-30))
    btn=Image.new("RGBA",(bw,bh),(0,0,0,0)); ImageDraw.Draw(btn).rounded_rectangle([0,0,bw-1,bh-1],radius=bh//2,fill=(200,100,63,255))
    base.alpha_composite(btn,(bx,by)); d=ImageDraw.Draw(base); f=B.dm(800,37)
    lbl="Swipe"; lw=d.textlength(lbl,font=f); gap=16; aw=32; tx=bx+(bw-(lw+gap+aw))/2; ty=by+(bh-44)/2
    d.text((tx,ty),lbl,font=f,fill=WHITE); ay=by+bh/2; ax0=tx+lw+gap; ax1=ax0+aw
    d.line([(ax0,ay),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay-11),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay+11),(ax1,ay)],fill=WHITE,width=5)

def cover_logo(base):
    mk=Image.open(GEN).convert("RGBA"); mk.thumbnail((150,150),Image.LANCZOS); base.alpha_composite(mk,(MX,340))

def build(n,MF,OUT):
    s=B.SPECS[n]; base=Image.new("RGBA",(W,H),BG+(255,))
    if s["role"]=="cover": cover_logo(base)
    else: place_in_zone(base,crop_obj(Image.open(f"{MF}/m{n}.png")))
    ghost(base,s["num"]); d=ImageDraw.Draw(base)
    if s.get("eyebrow"): B.ls_text(d,(MX,468),s["eyebrow"],B.mono(28),CORAL,4); y=532   # within cross-channel band
    elif s["role"]=="cover": y=556
    else: y=500
    hsize=104 if s["role"]=="cover" else 92; hf=B.dm(900,hsize); lh=hsize+(18 if s["role"]=="cover" else 12)
    for line in s["head"]: B.seg_line(d,MX,y,line,hf); y+=lh
    y+=16
    if s.get("sub"): d.text((MX,y),s["sub"],font=B.dm(500,34),fill=MUTED); y+=54
    if s.get("body"): B.draw_body(d,MX,y,s["body"],W-2*MX)
    if s["role"]=="cover": swipe(base)
    elif s["role"]=="last": footer(base,n,N)
    else: progress(d,n,N)
    o=f"{OUT}/s{n}.png"; base.convert("RGB").save(o); return o

if __name__=="__main__":
    md=sys.argv[1]; od=sys.argv[2]; MF=f"{TE}/roll3/{md}"; OUT=f"{TE}/roll3/{od}"; os.makedirs(OUT,exist_ok=True)
    for n in range(1,N+1): build(n,MF,OUT); print("built",n)
    ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
    cols=4;rows=2;sc=300;sh=int(sc*H/W)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{od}_montage.png"); print("montage",od)
