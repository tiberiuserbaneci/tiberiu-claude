#!/usr/bin/env python3
# SEED for Veo image-to-video (operator: inject the assets, Veo ONLY animates).
# Injects: Vertex 3D Claude logo + Vertex 'Fable 5' 3D logo (keyed off cream) + REAL code + REAL output.
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SP=f"{ROOT}/scratchpad/covers"
W,H=1080,1920
CREAM=(245,243,238); CREAM2=(236,232,222); PAPER=(252,251,247); INK=(41,38,34); INK2=(90,84,76)
MUT=(150,140,128); CORAL=(217,119,87); KRAFT=(196,150,110); LINEC=(222,216,205)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
cx=W//2
def key_logo(path,tol=30):
    im=Image.open(path).convert("RGB"); a=np.asarray(im).astype(int)
    corner=np.concatenate([a[6:40,6:40].reshape(-1,3),a[6:40,-40:-6].reshape(-1,3)]).mean(0)
    dist=np.abs(a-corner).sum(2); alpha=np.clip((dist-tol)*5,0,255).astype("uint8")
    out=Image.fromarray(np.dstack([np.asarray(im),alpha]),"RGBA"); bb=out.split()[3].getbbox()
    return out.crop(bb) if bb else out

bg=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(bg,"RGBA")
glow=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(glow).ellipse([cx-560,120,cx+560,900],fill=(217,119,87,22)); glow=glow.filter(ImageFilter.GaussianBlur(220))
bg=Image.alpha_composite(bg.convert("RGBA"),glow).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")

# --- inject Vertex 3D Claude logo (top) ---
cl=key_logo(f"{SP}/claude3d.png"); cl.thumbnail((300,300),Image.LANCZOS)
bg.paste(cl,(cx-cl.width//2,150),cl)
# --- inject Vertex Fable 5 3D wordmark ---
fb=key_logo(f"{SP}/fable5.png"); fb.thumbnail((620,260),Image.LANCZOS)
bg.paste(fb,(cx-fb.width//2,150+cl.height+8),fb)

# --- inject REAL code (light editor) ---
tx0,ty0,tx1,ty1=132,760,948,1240
sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([tx0+4,ty0+16,tx1+4,ty1+16],radius=24,fill=(120,95,60,55))
bg=Image.alpha_composite(bg.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(24))).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=24,fill=PAPER,outline=LINEC,width=2)
d.rounded_rectangle([tx0,ty0,tx1,ty0+52],radius=24,fill=CREAM2); d.rectangle([tx0,ty0+34,tx1,ty0+52],fill=CREAM2)
d.line([tx0,ty0+52,tx1,ty0+52],fill=LINEC,width=1)
for i,c in enumerate([(217,119,87),(210,160,90),(180,170,150)]): d.ellipse([tx0+22+i*22,ty0+19,tx0+34+i*22,ty0+31],fill=c)
d.text((tx0+110,ty0+15),"fable.py",font=mono(22),fill=MUT)
f=mono(26)
CODE=[("def build(brief):",None),("    plan = claude.plan(brief)",None),("    ui = fable.design(plan)","# self-designs"),
      ("    for step in plan:",None),("        agent.run(step)","# ships it"),("    return ui",None)]
for i,(ln,cm) in enumerate(CODE):
    d.text((tx0+30,ty0+80+i*44),ln,font=f,fill=INK)
    if cm: d.text((tx0+30+d.textlength(ln+"  ",font=f),ty0+80+i*44),cm,font=f,fill=MUT)

# --- inject REAL output (a shipped mini interface, NOT a preview) ---
ox0,oy0,ox1,oy1=132,1300,948,1720
sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([ox0+4,oy0+16,ox1+4,oy1+16],radius=24,fill=(120,95,60,55))
bg=Image.alpha_composite(bg.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(24))).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
d.rounded_rectangle([ox0,oy0,ox1,oy1],radius=24,fill=PAPER,outline=LINEC,width=2)
d.text((ox0+30,oy0+22),"OUTPUT",font=mono(20),fill=CORAL); d.text((ox0+30+d.textlength("OUTPUT   ",font=mono(20)),oy0+22),"landing.app · shipped",font=mono(18),fill=MUT)
# a finished landing hero built by the agent
d.text((ox0+30,oy0+70),"Your services, on autopilot.",font=dm(900,42),fill=INK)
d.text((ox0+30,oy0+128),"One operator. Every agent. Cents per run.",font=dm(500,24),fill=INK2)
d.rounded_rectangle([ox0+30,oy0+184,ox0+250,oy0+238],radius=27,fill=CORAL); d.text((ox0+66,oy0+198),"Get started",font=dm(800,24),fill=(255,252,248))
d.rounded_rectangle([ox0+270,oy0+184,ox0+430,oy0+238],radius=27,outline=LINEC,width=2); d.text((ox0+300,oy0+198),"See how",font=dm(700,24),fill=INK2)
for j in range(3):
    bx=ox0+30+j*300; d.rounded_rectangle([bx,oy0+270,bx+270,oy0+360],radius=14,fill=CREAM2,outline=LINEC,width=1)
    d.rounded_rectangle([bx+18,oy0+288,bx+90,oy0+306],radius=6,fill=(CORAL if j==0 else KRAFT))
    d.rounded_rectangle([bx+18,oy0+320,bx+240,oy0+334],radius=5,fill=LINEC); d.rounded_rectangle([bx+18,oy0+342,bx+180,oy0+356],radius=5,fill=LINEC)

bg.convert("RGB").save(f"{SP}/seed_fable.png"); print("saved seed_fable.png (injected Vertex logos + real code + real output)")
