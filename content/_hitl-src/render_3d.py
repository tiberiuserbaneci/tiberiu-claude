#!/usr/bin/env python3
# CODED 3D (no Vertex): take the flat 2.5D app window and render it as a tilted 3D panel with
# thickness (extruded edge), a soft contact shadow and a screen sheen. All PIL. Transparent PNG out.
# Usage: python3 render_3d.py apollo designer developer bill gate ultron gmail_sent hubspot ...
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import importlib.util, os, sys
spec=importlib.util.spec_from_file_location("R25","/home/user/tiberiu-claude/content/_hitl-src/render_25d.py")
R25=importlib.util.module_from_spec(spec); spec.loader.exec_module(R25)
OUT="/home/user/tiberiu-claude/content/_hitl-src/models_solo3d"

def find_coeffs(dst, src):
    A=[]
    for (dx,dy),(sx,sy) in zip(dst,src):
        A.append([dx,dy,1,0,0,0,-sx*dx,-sx*dy]); A.append([0,0,0,dx,dy,1,-sy*dx,-sy*dy])
    res=np.linalg.solve(np.array(A,float), np.array([c for p in src for c in p],float))
    return res.tolist()

def panel_rgba(key):
    im=R25.MOCK[key]().convert("RGBA"); cw,ch=im.size; W,H=1380,940; mx,my=(cw-W)//2,(ch-H)//2
    mask=Image.new("L",(cw,ch),0); ImageDraw.Draw(mask).rounded_rectangle([mx,my,mx+W,my+H],radius=30,fill=255)
    out=Image.new("RGBA",(cw,ch),(0,0,0,0)); out.paste(im,(0,0),mask)
    return out.crop((mx,my,mx+W,my+H))

def make3d(key):
    panel=panel_rgba(key); W,H=panel.size
    CW,CH=int(W*1.46),int(H*1.62)
    px,py=(CW-W)//2,(CH-H)//2-int(H*0.06)
    src=[(px,py),(px+W,py),(px+W,py+H),(px,py+H)]
    padded=Image.new("RGBA",(CW,CH),(0,0,0,0)); padded.paste(panel,(px,py),panel)
    # tilt: right edge recedes (foreshortened + inset), slight vertical squeeze on the right
    dx=int(W*0.075); vy=int(H*0.052)
    dst=[(px+6,py+2),(px+W-dx,py+vy),(px+W-dx,py+H-vy),(px+2,py+H-6)]
    tilt=padded.transform((CW,CH),Image.PERSPECTIVE,find_coeffs(dst,src),Image.BICUBIC)
    a=tilt.split()[3]
    base=Image.new("RGBA",(CW,CH),(0,0,0,0))
    # contact shadow
    sh=Image.new("RGBA",(CW,CH),(0,0,0,0)); sh.paste((0,0,0,150),(0,0),a)
    sh=sh.transform((CW,CH),Image.AFFINE,(1,0,26,0,1,54)).filter(ImageFilter.GaussianBlur(40))
    base.alpha_composite(sh)
    # thickness / extruded edge (dark), offset down-right behind the panel
    for k in range(18,0,-2):
        edge=Image.new("RGBA",(CW,CH),(0,0,0,0)); edge.paste((22,20,19,255),(0,0),a)
        base.alpha_composite(edge.transform((CW,CH),Image.AFFINE,(1,0,k,0,1,int(k*1.15))))
    # the panel
    base.alpha_composite(tilt)
    # sheen: soft diagonal light on the screen
    sheen=Image.new("L",(CW,CH),0); sd=ImageDraw.Draw(sheen)
    sd.polygon([(0,0),(int(CW*0.5),0),(0,int(CH*0.5))],fill=70)
    sheen=Image.fromarray((np.asarray(sheen)*(np.asarray(a)/255.0)).astype("uint8"))
    glow=Image.new("RGBA",(CW,CH),(0,0,0,0)); glow.paste((255,250,240,255),(0,0),sheen.filter(ImageFilter.GaussianBlur(30)))
    base.alpha_composite(glow)
    # crop to content bbox + margin
    bb=base.split()[3].getbbox(); pad=24
    bb=(max(0,bb[0]-pad),max(0,bb[1]-pad),min(CW,bb[2]+pad),min(CH,bb[3]+pad))
    return base.crop(bb)

if __name__=="__main__":
    os.makedirs(OUT,exist_ok=True)
    for k in (sys.argv[1:] or ["apollo"]):
        im=make3d(k); im.save(f"{OUT}/{k}.png"); print("built",k,im.size)   # keep RGBA (alpha for shadow/depth)
    # preview the first one on a dark slide-like bg
    k=(sys.argv[1:] or ["apollo"])[0]; prev=Image.new("RGB",(1080,1350),(25,25,25))
    ob=Image.open(f"{OUT}/{k}.png").convert("RGBA"); s=min(900/ob.width,700/ob.height)
    ob=ob.resize((int(ob.width*s),int(ob.height*s)),Image.LANCZOS)
    prev.paste(ob,((1080-ob.width)//2,(1350-ob.height)//2),ob); prev.save("/home/user/tiberiu-claude/scratchpad/solo3d_prev.png")
