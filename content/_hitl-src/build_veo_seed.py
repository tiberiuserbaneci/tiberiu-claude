#!/usr/bin/env python3
# Duotone SEED frame for Veo image-to-video: agentic Claude from the terminal (self-designing),
# real Claude sunburst + CLAUDE + FABLE, tight/contained composition. charcoal + copper duotone.
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SP=f"{ROOT}/scratchpad/covers"
W,H=1080,1920
COP=(200,110,70); COP2=(230,150,100); INK=(240,225,215); MUT=(150,110,95)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)

# duotone background: charcoal -> deep maroon radial, copper glow, vignette (contained)
bg=Image.new("RGB",(W,H),(18,13,11)); d=ImageDraw.Draw(bg,"RGBA")
glow=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
gd.ellipse([W//2-520,560,W//2+520,1400],fill=(120,55,30,150)); glow=glow.filter(ImageFilter.GaussianBlur(200))
bg=Image.alpha_composite(bg.convert("RGBA"),glow).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")

# --- top: Claude sunburst (real) tinted copper + CLAUDE wordmark ---
sun=Image.open(f"{ROOT}/content/_hitl-src/claude_official.png").convert("RGBA")
bb=sun.split()[3].getbbox();  sun=sun.crop(bb) if bb else sun
sun.thumbnail((120,120),Image.LANCZOS)
# tint to copper (duotone): recolor via alpha mask
tint=Image.new("RGBA",sun.size,COP+(255,)); tint.putalpha(sun.split()[3])
cx=W//2
bg.paste(tint,(cx-tint.width-14,470),tint)
d.text((cx+2,486),"Claude",font=dm(900,58),fill=INK)
# FABLE label
ff=mono(30); fw=d.textlength("F A B L E",font=ff); d.text((cx-fw/2,572),"F A B L E",font=ff,fill=COP2)

# --- center: terminal / editor window (the hero), tight ---
tx0,ty0,tx1,ty1=150,680,930,1330
sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([tx0+6,ty0+18,tx1+6,ty1+18],radius=26,fill=(0,0,0,150))
bg=Image.alpha_composite(bg.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(22))).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=26,fill=(26,18,15),outline=(200,110,70,90),width=2)
# title bar
d.line([tx0,ty0+58,tx1,ty0+58],fill=(200,110,70,50),width=1)
for i,c in enumerate([(210,90,60),(210,150,70),(150,150,120)]): d.ellipse([tx0+24+i*24,ty0+22,tx0+38+i*24,ty0+36],fill=c)
d.text((tx0+120,ty0+18),"fable.py — agent",font=mono(24),fill=MUT)
# code lines (copper duotone)
codes=[("def build(brief):",1.0),("    plan = claude.think(brief)",0.9),("    ui = design(plan)   # self-assembling",0.9),
       ("    for step in plan:",0.85),("        agent.run(step)   # writing...",0.85),("    ship(ui)  # done",0.8)]
yy=ty0+92
for i,(ln,op) in enumerate(codes):
    col=(int(200*op+40),int(110*op+30),int(70*op+25))
    d.text((tx0+34,yy),ln,font=mono(27),fill=col); yy+=46
# cursor + prompt
d.text((tx0+34,yy+6),"> ",font=mono(27),fill=COP2); d.rectangle([tx0+70,yy+8,tx0+86,yy+40],fill=COP2)
# a small assembling UI panel (right/bottom of terminal) - "designs itself"
px0,py0=tx0+470,ty1-210
d.rounded_rectangle([px0,py0,tx1-30,ty1-30],radius=14,fill=(34,22,18),outline=(200,110,70,70),width=1)
d.text((px0+18,py0+16),"PREVIEW",font=mono(18),fill=MUT)
for j in range(3):
    d.rounded_rectangle([px0+18,py0+48+j*40,tx1-48,py0+76+j*40],radius=7,fill=(200,110,70,int(120-j*30)))

# --- caption line under (contained) ---
d.text((cx- d.textlength("the agent designs itself",font=dm(700,30))/2,1380),"the agent designs itself",font=dm(700,30),fill=INK)

# vignette (keeps it contained, not sprawling)
vig=Image.new("L",(W,H),0); ImageDraw.Draw(vig).ellipse([-260,-260,W+260,H+260],fill=255); vig=vig.filter(ImageFilter.GaussianBlur(300))
dark=Image.new("RGB",(W,H),(8,5,4)); bg=Image.composite(bg,dark,vig)
# subtle grain
import random
bg.convert("RGB").save(f"{SP}/seed_fable.png"); print("saved seed_fable.png")
