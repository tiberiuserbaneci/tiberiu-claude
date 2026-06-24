#!/usr/bin/env python3
# Exact rows: anchor on two reliable signals, then even-split the regular 5-row grid.
#  - GATE: the only orange-highlighted row -> detect by orange pixel density (bottom anchor).
#  - PROMPT: the bright command pill near the top -> brightness band (top anchor).
# The 5 service rows are evenly spaced between prompt-bottom and gate-top.
import sys, os
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detect import norm, detect_console

def detect_rows(im):
    x0,y0,x1,y1=detect_console(im)
    W=x1-x0; H=y1-y0
    ix0,ix1=x0+int(W*0.045),x1-int(W*0.045)
    rgb=np.asarray(im).astype(np.float32)
    R,G,B=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    lum=0.299*R+0.587*G+0.114*B
    hsv=np.asarray(im.convert("HSV")).astype(np.float32)
    Hh,S,V=hsv[:,:,0],hsv[:,:,1]/255.0,hsv[:,:,2]/255.0
    # ORANGE gate row (the only orange row) -> reliable bottom anchor. Inclusive threshold
    # so we catch the whole gate band (border+glow+lock), then take its TOP edge.
    orange=((Hh>=6)&(Hh<=34)&(S>0.34)&(V>0.40)).astype(np.float32)
    ocol=orange[:, ix0:ix1].mean(axis=1)
    lo=y0+int(H*0.52); hi=y1-int(H*0.02)
    oseg=ocol[lo:hi]
    othr=max(oseg.max()*0.35, 0.03)
    omask=oseg>othr
    gband=None; i=0;n=len(omask)
    while i<n:
        if omask[i]:
            j=i
            while j<n and omask[j]: j+=1
            if gband is None or (j-i)>(gband[1]-gband[0]): gband=[i,j]
            i=j
        else: i+=1
    gate=[lo+gband[0], lo+gband[1]] if gband else [y0+int(H*0.80),y0+int(H*0.90)]
    # PROMPT bottom: bright command pill in the upper console -> reliable top anchor
    pl=y0+int(H*0.07); ph=y0+int(H*0.27)
    plum=lum[pl:ph, ix0:ix1].mean(axis=1); pthr=plum.mean()+0.3*plum.std()
    pidx=np.where(plum>pthr)[0]
    prompt_bot=(pl+int(pidx.max())) if len(pidx) else y0+int(H*0.23)
    # 5 service rows evenly between prompt-bottom and gate-top (regular grid)
    rt=prompt_bot+int(H*0.018); rb=gate[0]-int(H*0.012); step=(rb-rt)/5
    centers=[int(rt+step*(i+0.5)) for i in range(5)]
    rh=int(step*0.90)
    rects=[[ix0,c-rh//2,ix1,c+rh//2] for c in centers]
    return dict(console=[x0,y0,x1,y1], interior=[ix0,ix1], prompt_bot=prompt_bot,
                centers=centers, row_h=rh, rects=rects, gate=[ix0,gate[0],ix1,gate[1]])

if __name__=="__main__":
    src=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else "rows_debug.png"
    im=norm(src); r=detect_rows(im)
    x0,y0,x1,y1=r["console"]; ix0,ix1=r["interior"]
    d=ImageDraw.Draw(im); d.rectangle([x0,y0,x1,y1],outline=(255,0,0),width=2)
    d.line([ix0,r["prompt_bot"],ix1,r["prompt_bot"]],fill=(0,200,255),width=3)
    for rc in r["rects"]: d.rectangle(rc,outline=(0,220,80),width=3)
    d.rectangle(r["gate"],outline=(255,150,0),width=3)
    im.save(out); print(f"prompt_bot={r['prompt_bot']} centers={r['centers']} rh={r['row_h']} gate={r['gate'][1:4:2]} -> {out}")
