#!/usr/bin/env python3
# Overlay the TikTok/IG vertical safe zones on a 1080x1920 slide to verify chrome is inside.
# §9 safe: top 300, bottom 330, right 130, left 70. Red wash = unsafe.
import sys
from PIL import Image, ImageDraw
src=sys.argv[1]; out=sys.argv[2]
im=Image.open(src).convert("RGB").resize((1080,1920),Image.LANCZOS).convert("RGBA")
ov=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(ov)
red=(255,40,40,70)
# CROSS-CHANNEL STANDARD (TikTok + Instagram intersection): top 300, bottom 470 (IG feed caption), left 90, right 150
d.rectangle([0,0,1080,300],fill=red)          # top
d.rectangle([0,1450,1080,1920],fill=red)       # bottom (IG feed caption block)
d.rectangle([0,0,90,1920],fill=red)            # left
d.rectangle([930,0,1080,1920],fill=red)        # right
im.alpha_composite(ov)
d2=ImageDraw.Draw(im); d2.rectangle([90,300,930,1450],outline=(80,255,80,255),width=3)
im.convert("RGB").save(out); print("safe overlay ->",out)
