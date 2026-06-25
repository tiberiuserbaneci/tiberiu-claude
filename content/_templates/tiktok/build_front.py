#!/usr/bin/env python3
# New carousel "operator-front": FRONT-ON elements, each cropped and framed into ONE fixed zone
# on every slide (consistent, no text overlap). Chrome reused from build_slides; orange = hook orange.
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import build_slides as B
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
MF=f"{TE}/roll3/models_front"; MK=f"{TE}/roll3/models/claude_mark.png"; OUT=f"{TE}/roll3/operator_front"; os.makedirs(OUT,exist_ok=True)
W,H,MX=B.W,B.H,B.MX; BG=B.BG; WHITE=B.WHITE; CORAL=B.CORAL; MUTED=B.MUTED; N=B.N
ZONE=(48,500,1032,1205)   # fixed focal frame (big, lower): same on every content slide

def crop_obj(im):
    a=np.asarray(im.convert("RGB")).astype(int)
    diff=np.abs(a-np.array([25,25,25])).sum(2)
    ys,xs=np.where(diff>40)                       # bbox of the clearly-non-charcoal UI panel
    if len(xs)==0: return im.convert("RGBA")
    pad=8
    x0=max(0,int(xs.min())-pad); x1=min(im.width,int(xs.max())+pad)
    y0=max(0,int(ys.min())-pad); y1=min(im.height,int(ys.max())+pad)
    crop=im.convert("RGB").crop((x0,y0,x1,y1))
    c=np.asarray(crop).astype(int); d2=np.abs(c-np.array([25,25,25])).sum(2)
    alpha=np.clip((d2-30)*14,0,255).astype("uint8")   # charcoal bg + soft shadow -> transparent; UI panel -> opaque
    return Image.fromarray(np.dstack([np.asarray(crop).astype("uint8"),alpha]),"RGBA")

def place_in_zone(base,el):
    zx0,zy0,zx1,zy1=ZONE; pad=8
    zw,zh=zx1-zx0-2*pad, zy1-zy0-2*pad
    r=min(zw/el.width, zh/el.height); nw,nh=max(1,int(el.width*r)),max(1,int(el.height*r))
    el=el.resize((nw,nh),Image.LANCZOS)
    ox=zx0+pad+(zw-nw)//2; oy=zy0+pad+(zh-nh)//2
    # grounding fade: a soft shadow shaped like the element, offset down + blurred (so it doesn't look "thrown in")
    al=el.split()[3]
    shmask=Image.new("L",base.size,0); shmask.paste(al,(ox,oy+26))
    shmask=shmask.filter(ImageFilter.GaussianBlur(38)).point(lambda v:int(v*0.5))
    shadow=Image.merge("RGBA",(Image.new("L",base.size,0),Image.new("L",base.size,0),Image.new("L",base.size,0),shmask))
    base.alpha_composite(shadow)
    base.alpha_composite(el,(ox,oy))

def frame(base):
    pass   # INVISIBLE frame: elements occupy the same fixed ZONE on every slide, but no border/box is drawn

def cover_logo(base):
    mk=Image.open(f"{TE}/claude_logo_genuine.png").convert("RGBA")   # genuine Claude sunburst
    mk.thumbnail((142,142),Image.LANCZOS)
    base.alpha_composite(mk,(MX,54))

def build(n):
    s=B.SPECS[n]
    base=Image.new("RGBA",(W,H),BG+(255,))
    if s["role"]=="cover":
        cover_logo(base)
    else:
        frame(base)
        place_in_zone(base,crop_obj(Image.open(f"{MF}/m{n}.png")))
    B.ghost(base,s["num"])
    d=ImageDraw.Draw(base)
    if s.get("eyebrow"):
        ef=B.mono(28); B.ls_text(d,(MX,138),s["eyebrow"],ef,CORAL,4); y=198   # titles lowered a touch
    elif s["role"]=="cover": y=452
    else: y=162
    hsize=104 if s["role"]=="cover" else 78
    hf=B.dm(900,hsize); lh=hsize+(16 if s["role"]=="cover" else 10)
    for line in s["head"]:
        B.seg_line(d,MX,y,line,hf); y+=lh
    y+=14
    if s.get("sub"):
        sf=B.dm(500,34); d.text((MX,y),s["sub"],font=sf,fill=MUTED); y+=50
    if s.get("body"):
        B.draw_body(d,MX,y,s["body"],W-2*MX)
    if s["role"]=="cover": B.swipe(base)
    elif s["role"]=="last": B.footer(d,n,N)
    else: B.progress(d,n,N)
    out=f"{OUT}/s{n}.png"; base.convert("RGB").save(out); return out

if __name__=="__main__":
    import sys
    only=[int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(1,N+1)
    for n in only: build(n); print("built",n)
    ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1) if os.path.exists(f"{OUT}/s{i}.png")]
    if len(ims)==N:
        cols=4;rows=2;sc=330;sh=int(sc*H/W)
        st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
        for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
        st.save(f"{TE}/operator_front_montage.png"); print("montage saved")
