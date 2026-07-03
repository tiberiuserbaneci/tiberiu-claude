#!/usr/bin/env python3
# SEED frame for Veo image-to-video, CLAUDE LIGHT palette (operator: no bright red, use Claude palette
# / the white from our presentations). Veo animates THIS (code populates, push-in). Logo stays faithful.
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SP=f"{ROOT}/scratchpad/covers"
W,H=1080,1920
CREAM=(245,243,238); CREAM2=(236,232,222); PAPER=(252,251,247); INK=(41,38,34); INK2=(90,84,76)
MUT=(150,140,128); CORAL=(217,119,87); KRAFT=(196,150,110); LINEC=(222,216,205)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
cx=W//2; tx0,ty0,tx1,ty1=150,700,930,1330

bg=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(bg,"RGBA")
glow=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(glow).ellipse([cx-560,520,cx+560,1420],fill=(217,119,87,26)); glow=glow.filter(ImageFilter.GaussianBlur(220))
bg=Image.alpha_composite(bg.convert("RGBA"),glow).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
# Claude sunburst (coral) + wordmark
sun=Image.open(f"{ROOT}/content/_hitl-src/claude_official.png").convert("RGBA"); bb=sun.split()[3].getbbox(); sun=sun.crop(bb) if bb else sun
sun.thumbnail((92,92),Image.LANCZOS); tint=Image.new("RGBA",sun.size,CORAL+(255,)); tint.putalpha(sun.split()[3])
bg.paste(tint,(cx-tint.width-10,452),tint); d.text((cx+2,466),"Claude",font=dm(700,44),fill=INK2)
def spaced(dr,s,f,y,fill,ls):
    tot=sum(dr.textlength(c,font=f)+ls for c in s)-ls; x=cx-tot/2
    for c in s: dr.text((x,y),c,font=f,fill=fill); x+=dr.textlength(c,font=f)+ls
spaced(d,"FABLE",dm(900,96),556,INK,16)
# light terminal + soft warm shadow
sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([tx0+4,ty0+16,tx1+4,ty1+16],radius=26,fill=(120,95,60,60))
bg=Image.alpha_composite(bg.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(26))).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=26,fill=PAPER,outline=LINEC,width=2)
d.rounded_rectangle([tx0,ty0,tx1,ty0+58],radius=26,fill=CREAM2); d.rectangle([tx0,ty0+40,tx1,ty0+58],fill=CREAM2)
d.line([tx0,ty0+58,tx1,ty0+58],fill=LINEC,width=1)
for i,c in enumerate([(217,119,87),(210,160,90),(180,170,150)]): d.ellipse([tx0+24+i*24,ty0+22,tx0+38+i*24,ty0+36],fill=c)
d.text((tx0+120,ty0+18),"fable.py — agent",font=mono(24),fill=MUT)
CODES=[("def build(brief):",None),("    plan = claude.think(brief)",None),("    ui = design(plan)","# self-assembling"),
       ("    for step in plan:",None),("        agent.run(step)","# writing..."),("    ship(ui)","# done")]
f=mono(27)
for i,(ln,cm) in enumerate(CODES):
    d.text((tx0+34,ty0+92+i*46),ln,font=f,fill=INK)
    if cm: d.text((tx0+34+d.textlength(ln+"   ",font=f),ty0+92+i*46),cm,font=f,fill=MUT)
base=ty0+92+6*46+8; d.text((tx0+34,base),"> shipped in 6.2s",font=f,fill=CORAL)
chx=tx0+34+d.textlength("> shipped in 6.2s  ",font=f); d.line([chx,base+16,chx+8,base+24],fill=(120,165,120),width=3); d.line([chx+8,base+24,chx+22,base+6],fill=(120,165,120),width=3)
# preview panel
px0,py0=tx0+470,ty1-210
d.rounded_rectangle([px0,py0,tx1-30,ty1-30],radius=14,fill=CREAM2,outline=LINEC,width=1)
d.text((px0+18,py0+16),"PREVIEW",font=mono(18),fill=MUT)
for j in range(3): d.rounded_rectangle([px0+18,py0+48+j*40,tx1-48,py0+76+j*40],radius=7,fill=(CORAL if j==0 else KRAFT))
d.text((cx- d.textlength("the agent designs itself",font=dm(700,30))/2,1372),"the agent designs itself",font=dm(700,30),fill=INK2)
bg.convert("RGB").save(f"{SP}/seed_fable.png"); print("saved seed_fable.png (Claude light palette)")
