#!/usr/bin/env python3
# LOCK SCREEN, ONE DAY - 9:16 (1080x1920) coded 2D carousel, TikTok + Instagram (Type 2, S31).
# A single iPhone lock screen that fills up with real Ultron outcome notifications across one day.
# One evolving scene (NOT a slide-per-section deck) - a different structure from the phone/object
# carousels. Cover + 8 notification beats + CTA pill. Ultron sphere as the app icon (S31), Claude
# mark on the TikTok cover, sphere in the footer. Cents value-prop respected (no scary prices).
import importlib.util, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
W,H,MX=T2.W,T2.H,T2.MX
WHITE,CORAL,MUTED,SLATE=T2.WHITE,T2.CORAL,T2.MUTED,(25,25,25)
wo=lambda s:(s,WHITE); co=lambda s:(s,CORAL)

T2.COVER=dict(head=[[wo("My company had")],[co("a full day.")]], sub="I barely touched my phone.")
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{T2.LIB}/cta3d-operator.png", 0.92)

# (clock, eyebrow context, title, subtitle) - newest stacks on top, time = newest's clock
NOTIFS=[
 ("6:50",  "06:50 · STILL ASLEEP",   "Standup ready",        "Read 47 PRs and 12 issues overnight."),
 ("8:12",  "08:12 · ON THE TRAIN",   "Reply drafted",        "A lead answered. Follow-up sent."),
 ("9:30",  "09:30 · FIRST COFFEE",   "Call booked",          "Tuesday 10:00 added to your calendar."),
 ("11:05", "11:05 · IN A MEETING",   "Research brief ready", "12 accounts ranked and scored."),
 ("13:20", "13:20 · LUNCH",          "Deal moved",           "Acme moved to Closed Won."),
 ("15:40", "15:40 · SCHOOL RUN",     "Post published",       "LinkedIn post, written in your voice."),
 ("17:15", "17:15 · AT THE GYM",     "Shipped to production","The new page is live."),
 ("21:00", "21:00 · HOME, FINALLY",  "Day wrapped",          "9 done. 1 waiting your approval."),
]
T2.CONTENT=[(NOTIFS[i][1],[[wo("x")]],"",1.0) for i in range(len(NOTIFS))]  # drives the deck loop

def _sphere_icon(px):
    # clean round orb, transparent around it (NO black square under the logo)
    im=Image.open(T2.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
    ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
    sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
    m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq-1,sq-1],fill=255)
    s2.putalpha(m)
    return s2.resize((px,px),Image.LANCZOS)

def _wallpaper():
    # slate base + soft warm glow (coded depth), subtle vignette
    base=np.zeros((H,W,3),float); base[:]= (22,22,22)
    yy,xx=np.mgrid[0:H,0:W]
    g=np.exp(-(((xx-W*0.5)/(W*0.95))**2 + ((yy-H*0.30)/(H*0.34))**2))
    for c,v in zip(range(3),(204,120,92)): base[...,c]+= g*v*0.16
    vg=1-0.20*(((xx-W/2)/(W/2))**2 + ((yy-H/2)/(H/2))**2); base*=np.clip(vg,0,1)[...,None]
    return Image.fromarray(np.clip(base,0,255).astype("uint8"),"RGB").convert("RGBA")

def _statusbar(d):
    d.text((MX,300),"",font=T2.mono(28),fill=MUTED)  # reserved
    # right side: battery / signal hint (minimal)
    d.text((W-MX-150,300),"100%",font=T2.mono(26),fill=(150,150,146))

ICON=_sphere_icon(88)

def _lock_body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    # paint wallpaper over the slate base, then the lock-screen scene
    base.alpha_composite(_wallpaper())
    d=ImageDraw.Draw(base)
    count=page-1                               # slide 2 -> 1 notif ... slide 9 -> 8
    clock=NOTIFS[count-1][0]
    # date + clock (top, inside safe zone)
    d.text((MX,322),"Monday, June 29",font=T2.dm(500,34),fill=(210,210,205))
    cf=T2.dm(900,184); tw=d.textlength(clock,font=cf); d.text(((W-tw)//2,360),clock,font=cf,fill=WHITE)
    _statusbar(d)
    # eyebrow (narrative voice)
    T2.ls_text(d,(MX,604),eyebrow,T2.mono(27),CORAL,4)
    # notification stack: newest on top, show newest 5, collapse older
    show=list(range(count-1, max(-1,count-1-5), -1))   # indices newest->older, up to 5
    x0,x1=70,1010; y=650; ch=150; gap=18
    for rank,idx in enumerate(show):
        tline,title,sub=NOTIFS[idx][0],NOTIFS[idx][2],NOTIFS[idx][3]
        newest=(rank==0)
        card=Image.new("RGBA",(W,H),(0,0,0,0)); cd=ImageDraw.Draw(card)
        fillc=(52,47,43,235) if newest else (42,42,44,220)
        cd.rounded_rectangle([x0,y,x1,y+ch],radius=38,fill=fillc)
        if newest: cd.rounded_rectangle([x0,y,x0+8,y+ch],radius=4,fill=CORAL+(255,))
        base.alpha_composite(card); d=ImageDraw.Draw(base)
        base.alpha_composite(ICON,(x0+30,y+(ch-88)//2))
        d.text((x0+148,y+34),title,font=T2.dm(700,42),fill=WHITE)
        d.text((x0+148,y+92),sub,font=T2.dm(500,33),fill=(196,196,190))
        d.text((x1-150,y+38),("now" if newest else tline),font=T2.mono(27),fill=(150,150,146))
        y+=ch+gap
    older=count-len(show)
    if older>0:
        d.text((x0+8,y+10),f"{older} more earlier today",font=T2.dm(500,31),fill=(150,150,146))
        y+=60
    # progress bar
    bx0,bx1=90,928; yb=1578; d.rounded_rectangle([bx0,yb,bx1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([bx0,yb,bx0+int((bx1-bx0)*page/n),yb+7],radius=4,fill=CORAL)

def _last_body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    base.alpha_composite(_wallpaper()); d=ImageDraw.Draw(base)
    T2.ls_text(d,(MX,470),"ONE CHAT. ONE OPERATOR.",T2.mono(28),CORAL,4)
    s=T2.fit_hook(d,T2.CTA[1],W-2*MX,start=84,floor=58); hf=T2.dm(900,s); y=534
    for ln in T2.CTA[1]: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
    T2.place_in_zone(base, T2.crop_obj(Image.open(T2.CTA[2])), (50,720,1030,1245), fill=0.92)
    d.text((MX,1262),"Follow for one AI system for founders every day.",font=T2.dm(700,29),fill=WHITE)
    T2.footer(base)

def body_slide(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    (_last_body if last else _lock_body)(base,eyebrow,head,objpath,page,n,last,fill)
T2.body_slide=body_slide

if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/lock_tt",False); b=T2.deck(f"{T2.OUTBASE}/lock_ig",True)
    T2.montage(f"{T2.OUTBASE}/lock_tt","lock_tt",a); T2.montage(f"{T2.OUTBASE}/lock_ig","lock_ig",b)
    print("tt",a,"ig",b)
