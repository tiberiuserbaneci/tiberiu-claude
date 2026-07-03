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
    f=mono(30)
    # code FILLS the window (operator: codul umple fereastra)
    CODE=[("def build(brief):",None),("    plan = claude.plan(brief)","# deep model"),
          ("    ui   = fable.design(plan)","# self-designs"),("",None),
          ("    for step in plan:",None),("        code = agent.write(step)",None),
          ("        test(code)","# grades itself"),("        agent.run(step)",None),("",None),
          ("    review = human.gate(ui)","# your tap"),("    if review.ok:",None),
          ("        ship(ui)","# done"),("    return ui",None),("",None),("build(brief)","# shipped")]
    y=ty0+92; lh=(ty1-30-y)//len(CODE)
    for i,(ln,cm) in enumerate(CODE):
        d.text((tx0+34,y+i*lh),ln,font=f,fill=INK)
        if cm: d.text((tx0+34+d.textlength(ln+"  ",font=f),y+i*lh),cm,font=f,fill=MUT)
    # side window light gradient (left brighter)
    g=Image.new("L",(W,H),0)
    for x in range(W): ImageDraw.Draw(g).line([(x,0),(x,H)],fill=int(70*max(0,1-x/(W*0.7))))
    side=Image.merge("RGBA",(Image.new("L",(W,H),255),Image.new("L",(W,H),244),Image.new("L",(W,H),230),g)); bg.alpha_composite(side)
    return bg.convert("RGB")

# ---- Shot C: clean DONE status (operator: output not generic; if no reference use a READY/DONE message) ----
def shotC():
    bg=cream_bg(); d=ImageDraw.Draw(bg,"RGBA")
    top=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(top).ellipse([-200,-560,W+200,600],fill=(255,250,240,85)); top=top.filter(ImageFilter.GaussianBlur(180)); bg.alpha_composite(top); d=ImageDraw.Draw(bg,"RGBA")
    # big coral ring + check
    ccx,ccy,r=cx,830,150
    glow=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(glow).ellipse([ccx-r-60,ccy-r-60,ccx+r+60,ccy+r+60],fill=(217,119,87,70)); glow=glow.filter(ImageFilter.GaussianBlur(70)); bg.alpha_composite(glow); d=ImageDraw.Draw(bg,"RGBA")
    d.ellipse([ccx-r,ccy-r,ccx+r,ccy+r],fill=CORAL)
    d.line([ccx-64,ccy+6,ccx-14,ccy+56],fill=(255,252,248),width=20,joint="curve"); d.line([ccx-14,ccy+56,ccx+70,ccy-52],fill=(255,252,248),width=20,joint="curve")
    # DONE
    t="DONE"; f=dm(900,120); w=d.textlength(t,font=f); d.text((cx-w/2,ccy+r+70),t,font=f,fill=INK)
    s="shipped in 6.2s"; fs=mono(34); ws=d.textlength(s,font=fs); d.text((cx-ws/2,ccy+r+210),s,font=fs,fill=INK2)
    # a slim status line
    d.rounded_rectangle([cx-210,ccy+r+280,cx+210,ccy+r+332],radius=26,outline=CORAL,width=2)
    st="READY TO PUBLISH"; fst=mono(24); wst=d.textlength(st,font=fst); d.text((cx-wst/2,ccy+r+293),st,font=fst,fill=CORAL)
    return bg.convert("RGB")

if __name__=="__main__":
    shotA().save(f"{SP}/shotA.png"); shotB().save(f"{SP}/shotB.png"); shotC().save(f"{SP}/shotC.png")
    strip=Image.new("RGB",(3*370+40,660),(28,26,24))
    for i,p in enumerate(["shotA","shotB","shotC"]):
        t=Image.open(f"{SP}/{p}.png"); t.thumbnail((360,640)); strip.paste(t,(i*375+10,10))
    strip.save(f"{SP}/shots_strip.png"); print("shots built")
