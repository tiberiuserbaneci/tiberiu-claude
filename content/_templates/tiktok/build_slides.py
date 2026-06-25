#!/usr/bin/env python3
# Hybrid slide builder: Vertex supplies the model-only 3D object (roll3/models/mN.png);
# THIS renders ALL chrome in PIL with LOCKED typography so every slide is identical in
# font/size/position. Bottom: swipe on slide 1, progress bar + page number on 2-8, URL footer on last.
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
MODELS=f"{TE}/roll3/models"; OUT=f"{TE}/roll3/operator2"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; MX=70
BG=(25,25,25); WHITE=(250,250,247); CORAL=(200,100,63); MUTED=(154,154,146); GHOST=(42,41,39); TRACK=(60,59,57)
def dm(w,px):
    f=ImageFont.truetype(f"{TE}/DMSans-VF.ttf",px)
    try: f.set_variation_by_axes([w])
    except: pass
    return f
def mono(px,med=True): return ImageFont.truetype(f"{TE}/DMMono-Medium.ttf" if med else f"{TE}/DMMono-Regular.ttf",px)

def ls_text(d,xy,s,font,fill,ls):
    x,y=xy
    for ch in s:
        d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+ls
    return x
def ls_width(d,s,font,ls): return sum(d.textlength(ch,font=font)+ls for ch in s)-ls if s else 0

def seg_line(d,x,y,segs,font):
    for txt,col in segs:
        d.text((x,y),txt,font=font,fill=col); x+=d.textlength(txt,font=font)
    return x

def wrap_runs(d,runs,font_reg,font_bold,maxw):
    # runs: list of (text,bold). Produce lines of [(word,bold)] fitting maxw.
    words=[]
    for txt,b in runs:
        for i,w in enumerate(txt.split(" ")):
            if w=="": continue
            words.append((w,b))
    lines=[[]]; cur=0
    sp=d.textlength(" ",font=font_reg)
    for w,b in words:
        ft=font_bold if b else font_reg
        ww=d.textlength(w,font=ft)
        if cur+ww>maxw and lines[-1]:
            lines.append([]); cur=0
        lines[-1].append((w,b)); cur+=ww+sp
    return lines

def draw_body(d,x,y,runs,maxw,lh=46):
    fr=dm(400,34); fb=dm(700,34)
    for line in wrap_runs(d,runs,fr,fb,maxw):
        cx=x
        for i,(w,b) in enumerate(line):
            ft=fb if b else fr; col=WHITE if b else MUTED
            d.text((cx,y),w,font=ft,fill=col); cx+=d.textlength(w,font=ft)+d.textlength(" ",font=fr)
        y+=lh
    return y

def ghost(base,num):
    f=dm(900,360)
    layer=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(layer)
    tw=dl.textlength(num,font=f)
    dl.text((W-tw-30,-70),num,font=f,fill=(56,55,52,255))
    layer=layer.filter(ImageFilter.GaussianBlur(5))
    base.alpha_composite(layer)

def progress(d,page,n):
    x0,x1=MX,W-MX; y=1295; h=6
    d.rounded_rectangle([x0,y,x1,y+h],radius=3,fill=TRACK)
    fillw=int((x1-x0)*page/n)
    d.rounded_rectangle([x0,y,x0+fillw,y+h],radius=3,fill=CORAL)
    f=mono(26); lbl=f"{page:02d} / {n:02d}"; lw=d.textlength(lbl,font=f)
    d.text((W-MX-lw,y-40),lbl,font=f,fill=MUTED)

def footer(d,page,n):
    f=mono(30); txt="51ultron.com"; w=d.textlength(txt,font=f)
    d.text(((W-w)/2,1288),txt,font=f,fill=CORAL)
    # full progress + number still
    x0,x1=MX,W-MX; y=1262; h=6
    d.rounded_rectangle([x0,y,x1,y+h],radius=3,fill=TRACK)
    d.rounded_rectangle([x0,y,x1,y+h],radius=3,fill=CORAL)
    f2=mono(24); lbl=f"{page:02d} / {n:02d}"; lw=d.textlength(lbl,font=f2)
    d.text((W-MX-lw,y-34),lbl,font=f2,fill=MUTED)

def swipe(base):
    bw,bh=250,72; bx=(W-bw)//2; by=1232
    sh=Image.new("RGBA",(bw+60,bh+60),(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle([30,34,30+bw,34+bh],radius=bh//2,fill=(200,100,63,150)); sh=sh.filter(ImageFilter.GaussianBlur(14))
    base.alpha_composite(sh,(bx-30,by-30))
    btn=Image.new("RGBA",(bw,bh),(0,0,0,0)); bd=ImageDraw.Draw(btn)
    bd.rounded_rectangle([0,0,bw-1,bh-1],radius=bh//2,fill=(200,100,63,255))
    base.alpha_composite(btn,(bx,by))
    d=ImageDraw.Draw(base); f=dm(800,34); lbl="Swipe"; lw=d.textlength(lbl,font=f); gap=16; aw=30
    tx=bx+(bw-(lw+gap+aw))/2; ty=by+(bh-40)/2
    d.text((tx,ty),lbl,font=f,fill=WHITE)
    ay=by+bh/2; ax0=tx+lw+gap; ax1=ax0+aw
    d.line([(ax0,ay),(ax1,ay)],fill=WHITE,width=5)
    d.line([(ax1-12,ay-10),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay+10),(ax1,ay)],fill=WHITE,width=5)

# ---- per-slide content ----
C="c"; Wt="w"
def co(s): return (s,CORAL)
def wo(s): return (s,WHITE)
SPECS={
1:dict(role="cover",num="01",eyebrow=None,
   head=[[wo("I gave Ultron")],[co("7 jobs.")],[wo("It runs the company.")]],
   sub="One operator. 71 skills, 92 tools, one $19 plan."),
2:dict(role="mid",num="02",eyebrow="WHY IT WORKS",
   head=[[wo("You don't need a team.")],[co("You need an operator.")]],
   body=[("A prompt asks for brilliance once and prays. An operator loads it ",0),("before every single run",1),(".",0)]),
3:dict(role="mid",num="03",eyebrow="THE ROSTER",
   head=[[co("7 agents.")],[wo("One per job.")]]),
4:dict(role="mid",num="04",eyebrow="AGENT 01 / RESEARCH",
   head=[[wo("Account research")],[co("runs itself.")]],
   body=[("It reads the web, the funding and the hiring, then ranks every account by buying signal.",0)]),
5:dict(role="mid",num="05",eyebrow="AGENT 02 / OUTBOUND",
   head=[[wo("Cold email that")],[co("sounds like you.")]],
   body=[("It drafts the whole sequence from your real wins, then ",0),("waits for your yes",1),(" before a single send.",0)]),
6:dict(role="mid",num="06",eyebrow="THE DEPTH",
   head=[[co("71 skills. 92 tools.")],[wo("Loaded before you type.")]]),
7:dict(role="mid",num="07",eyebrow="ROUTING + CONTROL",
   head=[[wo("3 model tiers.")],[co("1 human gate.")]],
   body=[("The router picks the cheapest model that can do the job. Nothing irreversible ships without your yes.",0)]),
8:dict(role="last",num="08",eyebrow="GET THE SETUP",
   head=[[wo("Comment "),co("OPERATOR")],[wo("I will send the setup.")]],
   body=[("The exact operator setup I run my company on: the agents, the skills and the gates. Follow for one AI system for founders every day.",0)]),
}
N=8
def build(n):
    s=SPECS[n]
    if s["role"]=="cover":
        base=Image.new("RGBA",(W,H),BG+(255,))
        mkp=f"{TE}/claude_logo_genuine.png"               # genuine Claude sunburst
        if os.path.exists(mkp):
            mk=Image.open(mkp).convert("RGBA"); mk.thumbnail((150,150),Image.LANCZOS)
            base.alpha_composite(mk,(MX,54))
    else:
        base=Image.open(f"{MODELS}/m{n}.png").convert("RGB").resize((W,H),Image.LANCZOS).convert("RGBA")
    ghost(base,s["num"])
    d=ImageDraw.Draw(base)
    if s.get("eyebrow"):
        ef=mono(28); ls_text(d,(MX,96),s["eyebrow"],ef,CORAL,4); y=156
    elif s["role"]=="cover":
        y=452
    else:
        y=120
    hsize=104 if s["role"]=="cover" else 78
    hf=dm(900,hsize); lh=hsize+(16 if s["role"]=="cover" else 10)
    for line in s["head"]:
        seg_line(d,MX,y,line,hf); y+=lh
    y+=14
    if s.get("sub"):
        sf=dm(500,34); d.text((MX,y),s["sub"],font=sf,fill=MUTED); y+=50
    if s.get("body"):
        draw_body(d,MX,y,s["body"],W-2*MX)
    # bottom chrome
    if s["role"]=="cover": swipe(base)
    elif s["role"]=="last": footer(d,n,N)
    else: progress(d,n,N)
    out=f"{OUT}/s{n}.png"; base.convert("RGB").save(out); return out

if __name__=="__main__":
    import sys
    only=[int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(1,N+1)
    for n in only: print("built",build(n))
    # montage
    ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1) if os.path.exists(f"{OUT}/s{i}.png")]
    if len(ims)==N:
        cols=4;rows=2;sc=330;sh=int(sc*H/W)
        st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
        for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
        st.save(f"{TE}/operator2_montage.png"); print("montage saved")
