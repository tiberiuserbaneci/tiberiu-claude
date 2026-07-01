#!/usr/bin/env python3
# WHILE I SLEPT - phone-DEVICE lock screen carousel (1080x1920), TikTok + IG.
# One fixed iPhone device: same frame, wallpaper, clock position EVERY slide (no phone transition).
# Only the NOTIFICATIONS flow in (accumulate), and the clock advances + battery charges + date rolls
# across the night. Cover = the same phone with the hook where the notifications will land, so slide 1
# already IS the phone (operator: "notificarile sa curga pe acelasi telefon fara tranzitia telefonului").
import importlib.util, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
W,H=1080,1920
WHITE,CORAL,MUTED=T2.WHITE,T2.CORAL,T2.MUTED
dm,mono=T2.dm,T2.mono

# device geometry (FIXED every slide)
DW,DH=872,1792; DX=(W-DW)//2; DY=(H-DH)//2; DR=104          # device body
SI=17; SX,SY,SW,SH=DX+SI,DY+SI,DW-2*SI,DH-2*SI; SR=DR-SI    # screen
HOOK=[("While I slept,",WHITE),("my company worked.",CORAL)]

# (clock, battery%, date, eyebrow, title, sub) - one entry per notification beat, oldest first
DATE0="Tuesday, June 30"; DATE1="Wednesday, July 1"
NOTIFS=[
 ("23:10", 12, DATE0, "LIGHTS OUT",      "Outbound queued",   "240 emails scheduled for the morning."),
 ("00:42", 26, DATE1, "MIDNIGHT",        "Leads sourced",     "300 founders found and ranked."),
 ("01:55", 39, DATE1, "DEEP SLEEP",      "Sequences written", "3-touch, in your voice, ready to send."),
 ("03:20", 55, DATE1, "STILL ASLEEP",    "Deal advanced",     "NorthPeak moved to Closed Won."),
 ("04:38", 71, DATE1, "PRE-DAWN",        "Invoice raised",    "Stripe invoice sent, cents on fees."),
 ("05:49", 88, DATE1, "ALMOST MORNING",  "Standup ready",     "Read 47 PRs and 12 issues overnight."),
 ("06:50",100, DATE1, "YOU WAKE UP",     "Day is waiting",    "8 done. 1 needs your approval."),
]
def _sphere(px):
    im=Image.open(T2.ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
    ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
    sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
    m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq-1,sq-1],fill=255); s2.putalpha(m)
    return s2.resize((px,px),Image.LANCZOS)
ICON=_sphere(76)
def _fit(d,lines,maxw,start,floor):
    s=start
    while s>floor:
        if max(d.textlength(t,font=dm(900,s)) for t,_ in lines)<=maxw: break
        s-=2
    return s

def _surface():
    # dark surface behind the phone + a soft warm glow (depth)
    base=np.zeros((H,W,3),float); base[:]=(16,16,16)
    yy,xx=np.mgrid[0:H,0:W]
    g=np.exp(-(((xx-W*0.5)/(W*0.72))**2+((yy-H*0.34)/(H*0.40))**2))
    for c,v in zip(range(3),(204,120,92)): base[...,c]+=g*v*0.14
    return Image.fromarray(np.clip(base,0,255).astype("uint8"),"RGB").convert("RGBA")

def _wallpaper():
    # lock-screen wallpaper (only inside the screen): warm-dark radial, subtle vignette
    ov=np.zeros((SH,SW,3),float); ov[:]=(20,19,18)
    yy,xx=np.mgrid[0:SH,0:SW]
    g=np.exp(-(((xx-SW*0.5)/(SW*0.9))**2+((yy-SH*0.26)/(SH*0.32))**2))
    for c,v in zip(range(3),(204,120,92)): ov[...,c]+=g*v*0.18
    vg=1-0.16*(((xx-SW/2)/(SW/2))**2+((yy-SH/2)/(SH/2))**2); ov*=np.clip(vg,0,1)[...,None]
    im=Image.new("RGBA",(SW,SH),(0,0,0,0)); im.paste(Image.fromarray(np.clip(ov,0,255).astype("uint8"),"RGB"),(0,0))
    m=Image.new("L",(SW,SH),0); ImageDraw.Draw(m).rounded_rectangle([0,0,SW-1,SH-1],radius=SR,fill=255); im.putalpha(m)
    return im

WALL=_wallpaper()
def _device(base):
    # soft drop shadow
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([DX,DY+16,DX+DW,DY+DH+16],radius=DR,fill=(0,0,0,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(34)))
    d=ImageDraw.Draw(base)
    d.rounded_rectangle([DX-3,DY-3,DX+DW+3,DY+DH+3],radius=DR+3,fill=(60,58,55))     # rim highlight
    d.rounded_rectangle([DX,DY,DX+DW,DY+DH],radius=DR,fill=(9,9,10))                 # body
    base.alpha_composite(WALL,(SX,SY))                                               # screen wallpaper
    # dynamic island
    iw,ih=126,37; ix=(W-iw)//2; iy=SY+30
    d.rounded_rectangle([ix,iy,ix+iw,iy+ih],radius=ih//2,fill=(0,0,0))

def _signal(d,x,y,col):
    for i,h in enumerate((8,13,18,23)): d.rounded_rectangle([x+i*9,y+ (23-h),x+i*9+6,y+23],radius=2,fill=col)
def _wifi(d,cx,cyb,col):
    for r in (20,13,6): d.arc([cx-r,cyb-r,cx+r,cyb+r],221,319,fill=col,width=5)
    d.ellipse([cx-3,cyb-3,cx+3,cyb+3],fill=col)
def _battery(d,x,y,pct,col,charging):
    d.rounded_rectangle([x,y,x+50,y+25],radius=7,outline=col,width=3)
    d.rounded_rectangle([x+50+3,y+8,x+50+6,y+17],radius=2,fill=col)
    w=int((50-8)*max(0.06,pct/100)); fc=(94,168,132) if charging else col
    d.rounded_rectangle([x+4,y+4,x+4+w,y+21],radius=3,fill=fc)
    if charging:
        bx,by=x+22,y+12
        d.polygon([(bx+3,by-8),(bx-3,by+2),(bx+1,by+2),(bx-2,by+9),(bx+5,by-2),(bx,by-2)],fill=(20,20,18))

def _statusbar(d,batt,charging):
    y=SY+64; col=(232,232,227)
    _signal(d,SX+40,y,col); _wifi(d,SX+128,y+23,col)
    bx=SX+SW-40-50; _battery(d,bx,y,batt,col,charging)
    pf=mono(27); pt=f"{batt}%"; d.text((bx-16-d.textlength(pt,font=pf),y-1),pt,font=pf,fill=col)

def _clockdate(d,clock,date):
    df=dm(500,36); d.text(((W-d.textlength(date,font=df))//2,SY+188),date,font=df,fill=(214,214,208))
    cf=dm(700,232); d.text(((W-d.textlength(clock,font=cf))//2,SY+232),clock,font=cf,fill=WHITE)

def _notif_card(base,x0,x1,y,title,sub,tstamp,newest):
    ch=150
    card=Image.new("RGBA",(W,H),(0,0,0,0)); cd=ImageDraw.Draw(card)
    cd.rounded_rectangle([x0,y,x1,y+ch],radius=34,fill=(56,51,47,236) if newest else (40,40,42,214))
    if newest: cd.rounded_rectangle([x0,y,x0+7,y+ch],radius=4,fill=CORAL+(255,))
    base.alpha_composite(card); d=ImageDraw.Draw(base)
    base.alpha_composite(ICON,(x0+28,y+(ch-76)//2))
    d.text((x0+130,y+32),title,font=dm(700,40),fill=WHITE)
    d.text((x0+130,y+88),sub,font=dm(500,31),fill=(198,198,192))
    d.text((x1-40-d.textlength(tstamp,font=mono(26)),y+34),tstamp,font=mono(26),fill=(150,150,146))
    return y+ch+16

def scene(count):
    # count = how many notifications are shown (0 = cover with hook)
    base=_surface(); _device(base); d=ImageDraw.Draw(base)
    idx=max(0,count-1)
    clock,batt,date=NOTIFS[idx][0],NOTIFS[idx][1],NOTIFS[idx][2]
    if count==0: clock,batt,date=NOTIFS[0][0],NOTIFS[0][1],NOTIFS[0][2]
    _statusbar(d,batt,charging=(batt<100))
    _clockdate(d,clock,date)
    x0,x1=SX+30,SX+SW-30; ytop=SY+560
    if count==0:
        # HOOK where the notifications will land (phone already present)
        T2.ls_text(d,(x0+4,ytop),"LOCKED  22:00",mono(27),CORAL,4)
        s=_fit(d,HOOK,SW-60,82,60); hf=dm(900,s); y=ytop+56
        for ln in HOOK: d.text((x0+4,y),ln[0],font=hf,fill=ln[1]); y+=int(s*1.12)
        # swipe pill
        pt="Swipe  >"; pf=dm(800,38); pw=d.textlength(pt,font=pf)+72; ph=82; px=(W-pw)//2; py=SY+SH-150
        d.rounded_rectangle([px,py,px+pw,py+ph],radius=ph//2,fill=CORAL); d.text((px+36,py+ph//2-27),pt,font=pf,fill=(24,14,9))
    else:
        eb=NOTIFS[idx][3]
        T2.ls_text(d,(x0+4,ytop),f"{clock}  {eb}",mono(27),CORAL,4)
        y=ytop+52
        show=list(range(idx,max(-1,idx-5),-1))       # newest -> older, up to 5
        for rank,i in enumerate(show):
            y=_notif_card(base,x0,x1,y,NOTIFS[i][4],NOTIFS[i][5],"now" if rank==0 else NOTIFS[i][0],rank==0)
        older=count-len(show)
        if older>0: ImageDraw.Draw(base).text((x0+8,y+8),f"{older} more overnight",font=dm(500,30),fill=(150,150,146))
    return base

def cta_slide():
    base=_surface(); _device(base); d=ImageDraw.Draw(base)
    T2.ls_text(d,(SX+60,SY+430),"ONE CHAT. ONE OPERATOR.",mono(28),CORAL,4)
    hd=[("Run on one,",WHITE),("comment OPERATOR.",CORAL)]
    s=_fit(d,hd,SW-90,76,54); hf=dm(900,s); y=SY+496
    for ln in hd: d.text((SX+60,y),ln[0],font=hf,fill=ln[1]); y+=int(s*1.14)
    T2.place_in_zone(base,T2.crop_obj(Image.open(f"{T2.LIB}/cta3d-operator.png")),(SX+40,SY+740,SX+SW-40,SY+1250),fill=0.9)
    d.text((SX+60,SY+1280),"Follow for one AI system for founders every day.",font=dm(700,29),fill=WHITE)
    lg=_sphere(46); base.alpha_composite(lg,(SX+60,SY+1360)); d.text((SX+118,SY+1372),"51ultron.com",font=mono(28),fill=(214,214,208))
    return base

def progressbar(base,page,n):
    d=ImageDraw.Draw(base); x0,x1=SX+180,SX+SW-180; yb=SY+SH-70
    d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=CORAL)

def deck(outdir):
    os.makedirs(outdir,exist_ok=True)
    for f in os.listdir(outdir):
        if f.startswith("s") and f.endswith(".png"): os.remove(os.path.join(outdir,f))
    slides=[("cover",)]+[("notif",k) for k in range(1,len(NOTIFS)+1)]+[("cta",)]
    n=len(slides)
    for i,sl in enumerate(slides,1):
        if sl[0]=="cover": base=scene(0)
        elif sl[0]=="cta": base=cta_slide()
        else: base=scene(sl[1])
        if sl[0]!="cta": progressbar(base,i,n)
        base.convert("RGB").save(f"{outdir}/s{i}.png")
    return n

if __name__=="__main__":
    n=deck(f"{T2.OUTBASE}/nightphone_tt")
    print("slides",n)
