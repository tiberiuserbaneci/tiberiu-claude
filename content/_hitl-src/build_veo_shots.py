#!/usr/bin/env python3
# 3 CLEAN full-frame shot-seeds for the multi-shot Veo cut (operator: multiple angles + varied lighting).
# Each is its own 9:16 composition + distinct lighting. Veo image-to-video animates each; cut on beat.
# A: logo hero (rim light, dolly-in)  B: code editor (side light, pan)  C: output (soft top light, crane-down)
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SP=f"{ROOT}/scratchpad/covers"
W,H=1080,1920
CREAM=(245,243,238); CREAM2=(236,232,222); PAPER=(252,251,247); INK=(41,38,34); INK2=(90,84,76)
MUT=(150,140,128); CORAL=(217,119,87); KRAFT=(196,150,110); LINEC=(222,216,205)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
cx=W//2
def key_logo(path,tol):
    im=Image.open(path).convert("RGB"); a=np.asarray(im).astype(int)
    corner=np.concatenate([a[6:40,6:40].reshape(-1,3),a[6:40,-40:-6].reshape(-1,3)]).mean(0)
    dist=np.abs(a-corner).sum(2); alpha=np.clip((dist-tol)*5,0,255).astype("uint8")
    out=Image.fromarray(np.dstack([np.asarray(im),alpha]),"RGBA"); bb=out.split()[3].getbbox()
    return out.crop(bb) if bb else out
def cream_bg():
    return Image.new("RGB",(W,H),CREAM).convert("RGBA")

# ---- Shot A: logo hero, warm rim light ----
def shotA():
    bg=cream_bg()
    rim=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(rim).ellipse([cx-560,-320,cx+560,720],fill=(217,119,87,70)); rim=rim.filter(ImageFilter.GaussianBlur(170)); bg.alpha_composite(rim)
    cl=key_logo(f"{ROOT}/content/_templates/tiktok/lib/claude-logo-3d-matte.png",40); cl.thumbnail((560,560),Image.LANCZOS)
    bg.alpha_composite(cl,(cx-cl.width//2,470))
    fb=key_logo(f"{SP}/fable5.png",30); fb.thumbnail((720,300),Image.LANCZOS)
    bg.alpha_composite(fb,(cx-fb.width//2,470+cl.height+20))
    v=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(v).rectangle([0,H-560,W,H],fill=(30,18,10,70)); v=v.filter(ImageFilter.GaussianBlur(160)); bg.alpha_composite(v)
    return bg.convert("RGB")

# ---- Shot B: code editor, side (window) light ----
def shotB():
    bg=cream_bg(); d=ImageDraw.Draw(bg,"RGBA")
    tx0,ty0,tx1,ty1=110,470,970,1450
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([tx0+6,ty0+20,tx1+6,ty1+20],radius=28,fill=(120,95,60,60)); bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(28))); d=ImageDraw.Draw(bg,"RGBA")
    d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=28,fill=PAPER,outline=LINEC,width=2)
    d.rounded_rectangle([tx0,ty0,tx1,ty0+56],radius=28,fill=CREAM2); d.rectangle([tx0,ty0+38,tx1,ty0+56],fill=CREAM2); d.line([tx0,ty0+56,tx1,ty0+56],fill=LINEC,width=1)
    for i,c in enumerate([(217,119,87),(210,160,90),(180,170,150)]): d.ellipse([tx0+24+i*24,ty0+20,tx0+38+i*24,ty0+34],fill=c)
    d.text((tx0+120,ty0+16),"fable.py — agent",font=mono(26),fill=MUT)
    f=mono(32)
    CODE=[("def build(brief):",None),("    plan = claude.plan(brief)",None),("    ui = fable.design(plan)","# self-designs"),
          ("    for step in plan:",None),("        agent.run(step)","# ships it"),("    return ui",None)]
    for i,(ln,cm) in enumerate(CODE):
        d.text((tx0+34,ty0+92+i*58),ln,font=f,fill=INK)
        if cm: d.text((tx0+34+d.textlength(ln+"  ",font=f),ty0+92+i*58),cm,font=f,fill=MUT)
    # side window light gradient (left brighter)
    g=Image.new("L",(W,H),0)
    for x in range(W): ImageDraw.Draw(g).line([(x,0),(x,H)],fill=int(70*max(0,1-x/(W*0.7))))
    side=Image.merge("RGBA",(Image.new("L",(W,H),255),Image.new("L",(W,H),244),Image.new("L",(W,H),230),g)); bg.alpha_composite(side)
    return bg.convert("RGB")

# ---- Shot C: shipped output, soft top light ----
def shotC():
    bg=cream_bg(); d=ImageDraw.Draw(bg,"RGBA")
    top=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(top).ellipse([-200,-560,W+200,560],fill=(255,250,240,80)); top=top.filter(ImageFilter.GaussianBlur(180)); bg.alpha_composite(top); d=ImageDraw.Draw(bg,"RGBA")
    ox0,oy0,ox1,oy1=110,560,970,1360
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([ox0+6,oy0+20,ox1+6,oy1+20],radius=28,fill=(120,95,60,60)); bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(28))); d=ImageDraw.Draw(bg,"RGBA")
    d.rounded_rectangle([ox0,oy0,ox1,oy1],radius=28,fill=PAPER,outline=LINEC,width=2)
    d.text((ox0+34,oy0+28),"OUTPUT",font=mono(22),fill=CORAL); d.text((ox0+34+d.textlength("OUTPUT   ",font=mono(22)),oy0+28),"landing.app · shipped",font=mono(20),fill=MUT)
    d.text((ox0+34,oy0+84),"Your services,",font=dm(900,58),fill=INK); d.text((ox0+34,oy0+150),"on autopilot.",font=dm(900,58),fill=INK)
    d.text((ox0+34,oy0+228),"One operator. Every agent. Cents per run.",font=dm(500,28),fill=INK2)
    d.rounded_rectangle([ox0+34,oy0+292,ox0+290,oy0+356],radius=32,fill=CORAL); d.text((ox0+78,oy0+308),"Get started",font=dm(800,28),fill=(255,252,248))
    d.rounded_rectangle([ox0+312,oy0+292,ox0+512,oy0+356],radius=32,outline=LINEC,width=2); d.text((ox0+348,oy0+308),"See how",font=dm(700,28),fill=INK2)
    for j in range(3):
        bx=ox0+34+j*272; d.rounded_rectangle([bx,oy0+400,bx+250,oy0+520],radius=16,fill=CREAM2,outline=LINEC,width=1)
        d.rounded_rectangle([bx+20,oy0+420,bx+110,oy0+442],radius=7,fill=(CORAL if j==0 else KRAFT))
        d.rounded_rectangle([bx+20,oy0+460,bx+220,oy0+476],radius=6,fill=LINEC); d.rounded_rectangle([bx+20,oy0+486,bx+170,oy0+502],radius=6,fill=LINEC)
    return bg.convert("RGB")

if __name__=="__main__":
    shotA().save(f"{SP}/shotA.png"); shotB().save(f"{SP}/shotB.png"); shotC().save(f"{SP}/shotC.png")
    strip=Image.new("RGB",(3*370+40,660),(28,26,24))
    for i,p in enumerate(["shotA","shotB","shotC"]):
        t=Image.open(f"{SP}/{p}.png"); t.thumbnail((360,640)); strip.paste(t,(i*375+10,10))
    strip.save(f"{SP}/shots_strip.png"); print("shots built")
