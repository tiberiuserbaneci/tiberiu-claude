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
ZONE=(90,888,928,1290)   # legacy default; build() now uses an adaptive zone that fills the band
LOGO3D="/home/user/tiberiu-claude/content/_templates/tiktok/lib/claude-logo-3d-glossy.png"  # cover hero (3D Claude)

def crop_obj(im):
    # EDGE crop: the panel (even its dark frame/bevel) has SHARP edges; the soft drop-shadow and the
    # faint full-frame vignette are SMOOTH. So bound the object by its edge-gradient, not by brightness
    # or bright-pixel density. A dark panel body is nearly as dark as the bg, so density/brightness crops
    # sliced the frame and bevels. The full extent of the edge-bearing rows/cols IS the whole panel - text
    # may cluster on one side (e.g. a checklist) with the opposite frame edge far across an empty interior,
    # so take the plain min..max of edge lines, never the "largest run" (that sliced off the far frame).
    # Image-border artifacts (the 1px diff at row/col 0 and the last row/col) are the only strays, and the
    # 2px border zeroing below removes them - the vignette is smooth so it never trips the gradient mask.
    g=np.asarray(im.convert("L")).astype(float)
    gx=np.abs(np.diff(g,axis=1,prepend=g[:,:1])); gy=np.abs(np.diff(g,axis=0,prepend=g[:1,:]))
    em=(gx+gy)>10; em[:2,:]=em[-2:,:]=em[:,:2]=em[:,-2:]=False    # sharp panel edges only; kill image-border artifacts
    col=em.sum(0).astype(float); row=em.sum(1).astype(float)
    if col.max()==0 or row.max()==0: return im.convert("RGBA")
    cx=np.where(col>col.max()*0.04)[0]; ry=np.where(row>row.max()*0.04)[0]   # full span of edge-bearing lines = whole panel
    pad=16; x0=max(0,int(cx.min())-pad); x1=min(im.width,int(cx.max())+pad); y0=max(0,int(ry.min())-pad); y1=min(im.height,int(ry.max())+pad)
    crop=im.convert("RGB").crop((x0,y0,x1,y1)); c=np.asarray(crop).astype(int); d2=np.abs(c-np.array([25,25,25])).sum(2)
    alpha=np.clip((d2-30)*14,0,255).astype("uint8")               # key the charcoal bg out so the grounding shadow follows the silhouette
    return Image.fromarray(np.dstack([np.asarray(crop).astype("uint8"),alpha]),"RGBA")

def place_in_zone(base,el,zone):
    zx0,zy0,zx1,zy1=zone; pad=4; zw,zh=zx1-zx0-2*pad, zy1-zy0-2*pad
    r=min(zw/el.width, zh/el.height); nw,nh=max(1,int(el.width*r)),max(1,int(el.height*r))
    el=el.resize((nw,nh),Image.LANCZOS); ox=zx0+pad+(zw-nw)//2; oy=zy0+pad+(zh-nh)//2
    al=el.split()[3]; shmask=Image.new("L",base.size,0); shmask.paste(al,(ox,oy+30))
    shmask=shmask.filter(ImageFilter.GaussianBlur(42)).point(lambda v:int(v*0.5))
    base.alpha_composite(Image.merge("RGBA",(Image.new("L",base.size,0),)*3+(shmask,)))
    base.alpha_composite(el,(ox,oy))

def ghost(base,num):                                  # SMALL top-right corner watermark; sits ABOVE the headline so titles never touch it
    f=B.dm(900,150); layer=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(layer)
    tw=dl.textlength(num,font=f); dl.text((922-tw,298),num,font=f,fill=(54,53,50,255))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(4)))

def progress(d,page,n):
    x0,x1=90,928; y=1352; h=7                          # inside the cross-channel band (y<1450, x<930)
    d.rounded_rectangle([x0,y,x1,y+h],radius=4,fill=B.TRACK)
    d.rounded_rectangle([x0,y,x0+int((x1-x0)*page/n),y+h],radius=4,fill=CORAL)
    # page-number label removed (the corner watermark already shows it) - bar only

def footer(base,page,n):
    d=ImageDraw.Draw(base); lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS)
    base.alpha_composite(lg,(90,1330)); f=B.mono(30); d.text((154,1340),"51ultron.com",font=f,fill=CORAL)

def swipe(base):
    bw,bh=252,78; bx=(W-bw)//2; by=1360                # lower so it clears the cover logo (still inside the band)
    sh=Image.new("RGBA",(bw+60,bh+60),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([30,34,30+bw,34+bh],radius=bh//2,fill=(200,100,63,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(15)),(bx-30,by-30))
    btn=Image.new("RGBA",(bw,bh),(0,0,0,0)); ImageDraw.Draw(btn).rounded_rectangle([0,0,bw-1,bh-1],radius=bh//2,fill=(200,100,63,255))
    base.alpha_composite(btn,(bx,by)); d=ImageDraw.Draw(base); f=B.dm(800,37)
    lbl="Swipe"; lw=d.textlength(lbl,font=f); gap=16; aw=32; tx=bx+(bw-(lw+gap+aw))/2; ty=by+(bh-44)/2
    d.text((tx,ty),lbl,font=f,fill=WHITE); ay=by+bh/2; ax0=tx+lw+gap; ax1=ax0+aw
    d.line([(ax0,ay),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay-11),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay+11),(ax1,ay)],fill=WHITE,width=5)

def cover_logo(base):
    mk=Image.open(GEN).convert("RGBA"); mk.thumbnail((150,150),Image.LANCZOS); base.alpha_composite(mk,(MX,340))

def build(n,MF,OUT,transparent=False):
    s=B.SPECS[n]; base=Image.new("RGBA",(W,H),(0,0,0,0) if transparent else BG+(255,)); d=ImageDraw.Draw(base)
    cover=s["role"]=="cover"; last=s["role"]=="last"
    if not transparent: ghost(base,s["num"])              # corner watermark (skipped for the IG overlay cover)
    # --- text block at the top of the safe band (clears the watermark) ---
    # FIXED positions on EVERY slide so the 0.5s reel-flip has no visual jump:
    # eyebrow at 476, headline at 540 (size 84, 2 lines), 3D element zone top at 758.
    if s.get("eyebrow"): B.ls_text(d,(MX,476),s["eyebrow"],B.mono(28),CORAL,4)
    y=540; hf=B.dm(900,84); lh=96
    for line in s["head"]: B.seg_line(d,MX,y,line,hf); y+=lh
    elt_bottom=1238 if last else 1326   # only the thin progress bar sits below now
    src=LOGO3D if cover else f"{MF}/m{n}.png"
    place_in_zone(base,crop_obj(Image.open(src)),(88,758,942,elt_bottom))  # wider band -> bigger element
    # --- chrome ---
    if cover:
        if not transparent: swipe(base)                   # IG overlay cover: no swipe (sits over a video)
    elif last:
        d.text((MX,1258),"Follow for one AI system for founders every day.",font=B.dm(700,29),fill=WHITE)
        footer(base,n,N)
    else: progress(d,n,N)
    o=f"{OUT}/s{n}.png"; (base if transparent else base.convert("RGB")).save(o); return o

if __name__=="__main__":
    md=sys.argv[1]; od=sys.argv[2]; MF=f"{TE}/roll3/{md}"; OUT=f"{TE}/roll3/{od}"; os.makedirs(OUT,exist_ok=True)
    for n in range(1,N+1): build(n,MF,OUT); print("built",n)
    ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
    cols=4;rows=2;sc=300;sh=int(sc*H/W)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{od}_montage.png"); print("montage",od)
