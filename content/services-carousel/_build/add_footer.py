#!/usr/bin/env python3
# Composite a discreet-but-visible orange "51ultron.com" footer, bottom-center, on every slide.
import os
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
SRC={1:"out/fix-1.png",2:"out/apps-2.png",3:"out/fix-3.png",4:"out/fix-4.png",5:"out/fix-5.png"}
ORANGE=(232,84,43)   # #e8542b
TEXT="51ultron.com"
def load_font(px):
    try:
        f=ImageFont.truetype(f"{HERE}/DMSans-VF.ttf",px)
        try: f.set_variation_by_axes([800])
        except Exception:
            try: f.set_variation_by_name("Bold")
            except Exception: pass
        return f
    except Exception:
        return ImageFont.load_default()
def add(src,out):
    im=Image.open(src).convert("RGB"); W,H=im.size
    d=ImageDraw.Draw(im)
    px=int(W*0.026)                      # ~48px on a 1856-wide master
    f=load_font(px)
    # letter-spaced draw, centered, near the bottom
    ls=int(px*0.04)
    widths=[d.textlength(c,font=f) for c in TEXT]
    total=sum(widths)+ls*(len(TEXT)-1)
    x=(W-total)/2; y=H-int(H*0.045)
    for c,w in zip(TEXT,widths):
        d.text((x,y),c,font=f,fill=ORANGE)
        x+=w+ls
    im.save(out)
for n,s in SRC.items():
    o=f"out/final-{n}.png"
    if os.path.exists(s): add(s,o); print("footer ->",o)
    else: print("MISSING",s)
print("DONE")
