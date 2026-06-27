#!/usr/bin/env python3
# Code-injected EMBOSSED text/numbers for the reusable-shell pipeline. The Vertex shell supplies the 3D
# container; this renders the dynamic content so it reads as raised/engraved on the surface (no Vertex text,
# no drift). emboss_text = soft drop-shadow (raised off the surface) + a faint top-left bevel highlight.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import build_slides as B
WHITE=B.WHITE; CORAL=B.CORAL; MUTED=(150,148,140)

def emboss_text(base, xy, text, font, fill, anchor="la", strength=1.0):
    x,y=xy
    sh=Image.new("RGBA",base.size,(0,0,0,0)); ImageDraw.Draw(sh).text((x+2,y+3),text,font=font,fill=(0,0,0,int(165*strength)),anchor=anchor)
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(1.7)))
    d=ImageDraw.Draw(base)
    d.text((x-1,y-2),text,font=font,fill=(255,238,222,int(52*strength)),anchor=anchor)   # bevel highlight (top-left)
    d.text((x,y),text,font=font,fill=fill,anchor=anchor)                                  # face

def fit_font(d,text,maxw,wght,px,minpx=20):
    while px>minpx:
        f=B.dm(wght,px)
        if d.textlength(text,font=f)<=maxw: return f
        px-=2
    return B.dm(wght,minpx)

if __name__=="__main__":
    # validation swatch: embossed headline, label, big number, a kv-row, on a charcoal panel-tone
    W,H=900,1100; base=Image.new("RGBA",(W,H),(38,37,35,255)); d=ImageDraw.Draw(base)
    emboss_text(base,(60,70),"Model tier",B.dm(700,46),WHITE)
    emboss_text(base,(60,170),"Lite",B.dm(800,40),MUTED); emboss_text(base,(260,170),"Smart",B.dm(800,40),MUTED); emboss_text(base,(520,170),"Deep",B.dm(800,40),CORAL)
    emboss_text(base,(60,320),"$48k",B.dm(900,150),CORAL)            # big embossed number
    emboss_text(base,(60,520),"MRR",B.mono(34),MUTED)
    for i,(k,v) in enumerate([("Northwind Labs","92"),("Belmont Freight","88"),("Carver Studios","81")]):
        yy=640+i*90; emboss_text(base,(60,yy),k,B.dm(600,36),WHITE); emboss_text(base,(W-60,yy),v,B.dm(800,36),CORAL,anchor="ra")
    emboss_text(base,(60,960),"71%",B.dm(900,90),WHITE)
    base.convert("RGB").save("/tmp/emboss_test.png"); print("emboss swatch saved")
