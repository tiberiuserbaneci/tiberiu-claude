#!/usr/bin/env python3
# Detect the dark console card bbox in a Vertex render, plus prompt/rows/gate bands by proportion.
# Normalises the render to 1080x1350 (4:5) first. Writes a debug overlay to eyeball alignment.
import sys, json
import numpy as np
from PIL import Image, ImageDraw

def norm(path):
    im=Image.open(path).convert("RGB")
    w,h=im.size
    # fit to height 1350, center-crop width to 1080
    nh=1350; nw=round(w*nh/h)
    im=im.resize((nw,nh),Image.LANCZOS)
    if nw>=1080:
        x=(nw-1080)//2; im=im.crop((x,0,x+1080,1350))
    else:
        bg=Image.new("RGB",(1080,1350),(243,235,223)); bg.paste(im,((1080-nw)//2,0)); im=bg
    return im

def detect_console(im):
    a=np.asarray(im).astype(np.float32)
    lum=0.299*a[:,:,0]+0.587*a[:,:,1]+0.114*a[:,:,2]
    dark=lum<95
    H,W=dark.shape
    # vertical extent: rows whose dark-density (in central 60% width) exceeds threshold
    cx0,cx1=int(W*0.18),int(W*0.82)
    rowden=dark[:,cx0:cx1].mean(axis=1)
    rows=np.where(rowden>0.45)[0]
    if len(rows)<10: rows=np.where(rowden>0.35)[0]
    y0,y1=int(rows.min()),int(rows.max())
    # horizontal extent within that band
    colden=dark[y0:y1,:].mean(axis=0)
    cols=np.where(colden>0.55)[0]
    if len(cols)<10: cols=np.where(colden>0.4)[0]
    x0,x1=int(cols.min()),int(cols.max())
    return x0,y0,x1,y1

if __name__=="__main__":
    src=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else "detect_debug.png"
    im=norm(src)
    x0,y0,x1,y1=detect_console(im)
    W=x1-x0; Hc=y1-y0
    # bands by proportion of console interior
    pad=int(W*0.045)
    ix0,ix1=x0+pad,x1-pad
    prompt=(ix0, y0+int(Hc*0.10), ix1, y0+int(Hc*0.205))
    rows_top=y0+int(Hc*0.255); rows_bot=y0+int(Hc*0.80)
    gate=(ix0, y0+int(Hc*0.805), ix1, y0+int(Hc*0.905))
    nrows=5
    rowys=[rows_top+int((rows_bot-rows_top)*(i+0.5)/nrows) for i in range(nrows)]
    info=dict(console=[x0,y0,x1,y1],prompt=list(prompt),gate=list(gate),
              rows_top=rows_top,rows_bot=rows_bot,rowys=rowys,
              check_x=x1-int(W*0.055))
    print(json.dumps(info))
    d=ImageDraw.Draw(im)
    d.rectangle([x0,y0,x1,y1],outline=(255,0,0),width=4)
    d.rectangle(prompt,outline=(0,200,255),width=3)
    d.rectangle(gate,outline=(255,150,0),width=3)
    for ry in rowys:
        d.line([ix0,ry,ix1,ry],fill=(0,255,0),width=2)
        d.ellipse([info["check_x"]-10,ry-10,info["check_x"]+10,ry+10],outline=(255,0,255),width=3)
    im.save(out)
    print("debug ->",out)
