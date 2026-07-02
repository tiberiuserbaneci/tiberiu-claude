#!/usr/bin/env python3
# EDITORIAL 4:5 (1080x1350) renderer - TikTok/IG photo-carousel top-performer format (S9).
# Kills the 9:16 empty bands: ~112px side padding (extra left breathing room), NO 300/330 safe
# insets, big dark-premium objects that fill the frame, plus a per-slide SUBHOOK (the why / one
# more fact). Reuses an imported material's COVER/CONTENT/CTA/CLOSE + engine helpers.
# CONTENT item: (eyebrow, hook, [subhook], object, fill)  - subhook optional (5-tuple).
# Usage: python3 build_ed45.py <build_module.py> <outprefix>
import importlib.util, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
def load(p):
    s=importlib.util.spec_from_file_location("MAT",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
MAT=load(sys.argv[1]); OUT=sys.argv[2]
T2=MAT.T2
COVER,CONTENT,CTA=T2.COVER,T2.CONTENT,T2.CTA
CLOSE=getattr(T2,"CLOSE",dict(l1="Save this",l2="for later",q="Which first?"))
dm,mono=T2.dm,T2.mono
WHITE,CORAL,MUTED,BG,TRACK,GHOST=T2.WHITE,T2.CORAL,T2.MUTED,T2.BG,T2.TRACK,T2.GHOST
INK=(206,206,199)   # sub-hook ink (brighter than MUTED)
ULOGO,CLAUDE_SUN=T2.ULOGO,T2.CLAUDE_SUN
crop_obj,fit_hook,seg_line,ls_text,seg_center=T2.crop_obj,T2.fit_hook,T2.seg_line,T2.ls_text,T2.seg_center
# ---- SAFE ZONES (1080x1350 TikTok/IG photo carousel) ----
# left  112  (extra breathing room, operator)   right 112 -> object x ~[112,968], clear of edge
# top   ~60  (status bar)                        bottom ~100 (caption band); progress sits above it
W,H,MX=1080,1350,112

def dots(base):
    d=ImageDraw.Draw(base)
    for y in range(0,H,30):
        for x in range(0,W,30): d.point((x,y),fill=(31,26,24))
def ghost(base,num):
    d=ImageDraw.Draw(base); f=dm(900,112)   # smaller + higher so it clears the sub-hook line
    d.text((W-MX-d.textlength(num,font=f),58),num,font=f,fill=GHOST)
def progress(d,page,n):
    # symmetric inset sized for the LARGER TikTok action-icon rail so ONE deck works on both TikTok + IG
    # (operator: TikTok icons are bigger; one standard, no per-channel slides). right end ~880.
    pm=200; x0,x1=pm,W-pm; yb=H-56; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=ACC)
def footer(base):
    d=ImageDraw.Draw(base); y=H-70
    lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((44,44),Image.LANCZOS); base.alpha_composite(lg,(MX,y-8))
    d.text((MX+58,y),"ULTRON",font=mono(26),fill=WHITE)
    u="51ultron.com"; f=dm(900,30); d.text((W-MX-d.textlength(u,font=f),y-4),u,font=f,fill=WHITE)
def wrap(d,text,font,maxw,maxlines=2):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines[:maxlines]

OBJ_CY=762; OBJ_H=660; OBJ_MAXW=940   # every object: WHOLE (uncut), FRONT-ON, full-width (operator: no tilt, no half-empty slides)
ACC=tuple(getattr(T2,"ACCENT",CORAL))  # per-material accent (book / book-dark / kraft) -> decks stop looking identical
def _tbox(d,thr=55,dens=80):
    # bbox of the WHOLE tablet (dense region), incl. its dark lower half; the diffuse drop-glow is
    # not dense enough to survive the column/row filter, so it is excluded from sizing.
    m=d>thr; cols=np.where(m.sum(0)>dens)[0]; rows=np.where(m.sum(1)>dens)[0]
    if len(cols) and len(rows): return int(cols.min()),int(rows.min()),int(cols.max()),int(rows.max())
    ys,xs=np.where(d>40); return int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())
def place_screen(base,objpath,fill=1.0):
    # NO-bezel path for light app dashboards: crop to the bright screen, round + fade edges, drop shadow,
    # fit the zone, centre at (W/2, OBJ_CY) -> every dashboard identical, no device frame.
    im=Image.open(objpath).convert("RGB"); a=np.asarray(im).astype(int); lum=a.sum(2)/3
    ys,xs=np.where(lum>170)
    if len(xs)==0: return _place_dark(base,objpath,fill)
    x0,y0,x1,y1=int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())
    p=int((x1-x0)*0.012); x0+=p;y0+=p;x1-=p;y1-=p
    crop=im.crop((x0,y0,x1,y1)).convert("RGBA")
    s=min(OBJ_MAXW/crop.width, OBJ_H/crop.height)*fill
    cw,ch=max(1,int(crop.width*s)),max(1,int(crop.height*s)); crop=crop.resize((cw,ch),Image.LANCZOS)
    r=int(cw*0.03); mask=Image.new("L",(cw,ch),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,cw-1,ch-1],radius=r,fill=255)
    crop.putalpha(mask.filter(ImageFilter.GaussianBlur(3)))
    px=(W-cw)//2; py=int(OBJ_CY-ch/2)
    sm=Image.new("L",(W,H),0); sd=Image.new("L",(cw,ch),0); ImageDraw.Draw(sd).rounded_rectangle([0,0,cw-1,ch-1],radius=r,fill=140)
    sm.paste(sd,(px,py+16)); sm=sm.filter(ImageFilter.GaussianBlur(30))
    base.alpha_composite(Image.merge("RGBA",(Image.new("L",(W,H),0),)*3+(sm,))); base.alpha_composite(crop,(px,py))
def _place_dark(base,objpath,fill=1.0):
    arr=np.asarray(Image.open(objpath).convert("RGB")).astype(int); H0,W0=arr.shape[:2]
    cs=np.concatenate([arr[:48,:48].reshape(-1,3),arr[:48,-48:].reshape(-1,3),arr[-48:,:48].reshape(-1,3),arr[-48:,-48:].reshape(-1,3)])
    bg=np.median(cs,0); d=np.abs(arr-bg).sum(2)
    tx0,ty0,tx1,ty1=_tbox(d, getattr(T2,"OBJ_THR",55))     # the whole panel (lower thr for dark 2.5D windows)
    pad=42; cx0,cy0=max(0,tx0-pad),max(0,ty0-pad); cx1,cy1=min(W0,tx1+pad),min(H0,ty1+pad)
    alpha=np.clip((d-16)*18,0,255).astype("uint8")         # near-opaque: dark lower half stays solid; far bg drops out
    el=Image.fromarray(np.dstack([arr.astype("uint8"),alpha]),"RGBA").crop((cx0,cy0,cx1,cy1))
    tw,th=tx1-tx0,ty1-ty0; r=min(OBJ_MAXW/tw, OBJ_H/th)*fill   # SIZE by the tablet -> equal across slides
    el=el.resize((max(1,int(el.width*r)),max(1,int(el.height*r))),Image.LANCZOS)
    tcx=((tx0+tx1)/2-cx0)*r; tcy=((ty0+ty1)/2-cy0)*r          # tablet centre inside the scaled crop
    base.alpha_composite(el,(int(W/2-tcx), int(OBJ_CY-tcy)))  # tablet centre -> identical X/Y every slide
def _place_alpha(base,objpath,fill=1.0):
    # coded-3D objects carry real alpha (panel+depth+shadow). Composite as-is, sized/centred by alpha bbox.
    el=Image.open(objpath).convert("RGBA"); bb=el.split()[3].getbbox()
    if bb: el=el.crop(bb)
    s=min(OBJ_MAXW/el.width, OBJ_H/el.height)*fill
    el=el.resize((max(1,int(el.width*s)),max(1,int(el.height*s))),Image.LANCZOS)
    base.alpha_composite(el,(int(W/2-el.width/2), int(OBJ_CY-el.height/2)))
def place_obj(base,objpath,fill=1.0):
    if getattr(T2,"ALPHA_OBJ",False): return _place_alpha(base,objpath,fill)
    im=Image.open(objpath)
    if im.mode=="RGBA" and im.getextrema()[3][0]<250: return _place_alpha(base,objpath,fill)  # per-file real alpha (real-app crops)
    (place_screen if getattr(T2,"SCREEN_CROP",False) else _place_dark)(base,objpath,fill)

# ---------- REF-STYLE FLOW CARDS (operator: the dark windows were "jalnic"; refs = icon-flow cards) ----------
CREAM=(246,241,231); CINK=(23,21,15); CMUT=(107,99,87); CPAPER=(240,233,218); CLINE=(216,205,184)
def _glyph(d,kind,cx,cy,r,col,w=6):
    # simple line glyphs, reference style
    if kind=="chat":
        d.rounded_rectangle([cx-r,cy-r*0.8,cx+r,cy+r*0.5],radius=10,outline=col,width=w)
        d.polygon([(cx-r*0.4,cy+r*0.5),(cx-r*0.05,cy+r*0.95),(cx+r*0.05,cy+r*0.5)],fill=col)
        d.line([cx-r*0.55,cy-r*0.3,cx+r*0.55,cy-r*0.3],fill=col,width=w); d.line([cx-r*0.55,cy,cx+r*0.15,cy],fill=col,width=w)
    elif kind=="mag":
        d.ellipse([cx-r,cy-r,cx+r*0.35,cy+r*0.35],outline=col,width=w)
        d.line([cx+r*0.25,cy+r*0.25,cx+r,cy+r],fill=col,width=w+2)
    elif kind=="rows":
        for i,yy in enumerate((-0.75,-0.15,0.45)):
            d.rounded_rectangle([cx-r,cy+yy*r,cx+r,cy+yy*r+r*0.42],radius=6,outline=col,width=w-2)
    elif kind=="send":
        d.polygon([(cx-r,cy+r*0.75),(cx+r,cy-r*0.75),(cx-r*0.25,cy+r*0.15),(cx-r*0.4,cy+r*0.8)],outline=col,width=w)
        d.line([cx+r,cy-r*0.75,cx-r*0.25,cy+r*0.15],fill=col,width=w)
        d.line([cx-r,cy+r*0.75,cx+r,cy-r*0.75],fill=col,width=w)
    elif kind=="check":
        d.line([cx-r*0.8,cy+r*0.05,cx-r*0.15,cy+r*0.7],fill=col,width=w+3)
        d.line([cx-r*0.15,cy+r*0.7,cx+r*0.9,cy-r*0.6],fill=col,width=w+3)
    elif kind=="cal":
        d.rounded_rectangle([cx-r,cy-r*0.75,cx+r,cy+r*0.85],radius=8,outline=col,width=w)
        d.line([cx-r,cy-r*0.25,cx+r,cy-r*0.25],fill=col,width=w-1)
        d.line([cx-r*0.5,cy-r*1.0,cx-r*0.5,cy-r*0.55],fill=col,width=w); d.line([cx+r*0.5,cy-r*1.0,cx+r*0.5,cy-r*0.55],fill=col,width=w)
    elif kind=="gear":
        d.ellipse([cx-r*0.45,cy-r*0.45,cx+r*0.45,cy+r*0.45],outline=col,width=w)
        import math
        for a in range(0,360,45):
            x1=cx+r*0.62*math.cos(math.radians(a)); y1=cy+r*0.62*math.sin(math.radians(a))
            x2=cx+r*0.95*math.cos(math.radians(a)); y2=cy+r*0.95*math.sin(math.radians(a))
            d.line([x1,y1,x2,y2],fill=col,width=w)
    elif kind=="coin":
        d.ellipse([cx-r*0.9,cy-r*0.9,cx+r*0.9,cy+r*0.9],outline=col,width=w)
        f=T2.dm(800,int(r*1.1)); d.text((cx-r*0.32,cy-r*0.62),"$",font=f,fill=col)
    elif kind=="chart":
        d.line([cx-r,cy+r*0.85,cx+r,cy+r*0.85],fill=col,width=w)
        for i,(hx,hh) in enumerate(((-0.62,0.5),(-0.05,0.95),(0.52,1.45))):
            d.rounded_rectangle([cx+hx*r,cy+r*0.75-hh*r,cx+hx*r+r*0.4,cy+r*0.75],radius=4,fill=col)
    elif kind=="shield":
        d.polygon([(cx,cy-r),(cx+r*0.85,cy-r*0.6),(cx+r*0.85,cy+r*0.15),(cx,cy+r),(cx-r*0.85,cy+r*0.15),(cx-r*0.85,cy-r*0.6)],outline=col,width=w)
        d.line([cx-r*0.35,cy-r*0.05,cx-r*0.05,cy+r*0.3],fill=col,width=w); d.line([cx-r*0.05,cy+r*0.3,cx+r*0.45,cy-r*0.35],fill=col,width=w)
    elif kind=="doc":
        d.rounded_rectangle([cx-r*0.75,cy-r,cx+r*0.75,cy+r],radius=8,outline=col,width=w)
        for yy in (-0.4,0.0,0.4): d.line([cx-r*0.4,cy+yy*r,cx+r*0.4,cy+yy*r],fill=col,width=w-2)
    elif kind=="person":
        d.ellipse([cx-r*0.4,cy-r,cx+r*0.4,cy-r*0.2],outline=col,width=w)
        d.arc([cx-r*0.85,cy-r*0.15,cx+r*0.85,cy+r*1.5],200,340,fill=col,width=w)
    elif kind=="bolt":
        d.polygon([(cx+r*0.2,cy-r),(cx-r*0.7,cy+r*0.2),(cx-r*0.05,cy+r*0.2),(cx-r*0.2,cy+r),(cx+r*0.7,cy-r*0.2),(cx+r*0.05,cy-r*0.2)],fill=col)
    elif kind=="loop":
        d.arc([cx-r,cy-r,cx+r,cy+r],300,200,fill=col,width=w)
        d.polygon([(cx-r*0.15,cy-r*1.15),(cx+r*0.35,cy-r*0.85),(cx-r*0.15,cy-r*0.55)],fill=col)
    elif kind=="orb":
        im=Image.open(ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
        ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
        sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
        m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq,sq],fill=255); s2.putalpha(m)
        s2=s2.resize((int(r*1.9),int(r*1.9)),Image.LANCZOS); return s2

# per-object flows: (mono command, [(glyph,label)x3-4])  - WHY stays the slide foot
FLOWS={
 "apollo":      ("> source my ICP matches",[("chat","one line"),("mag","CORTEX hunts"),("rows","1,284 found"),("check","200 out")]),
 "gmail_sent":  ("> run the sequence",[("doc","brief in"),("send","4-step draft"),("shield","gate holds"),("check","sent 10:00")]),
 "hubspot":     ("> update the pipeline",[("chat","reply lands"),("gear","auto-move"),("rows","stage right"),("check","no dragging")]),
 "calendly":    ("> book the yeses",[("send","reply"),("cal","slot found"),("check","confirmed")]),
 "stripe":      ("> invoice + collect",[("doc","invoice"),("send","auto-chase"),("coin","paid")]),
 "scheduler":   ("> queue this week",[("doc","one message"),("cal","42 queued"),("send","10:00 local")]),
 "warmup":      ("> keep me inboxing",[("send","ramp sends"),("chart","watch spam"),("check","99.2% inbox")]),
 "seowriter":   ("> write it ranked",[("chat","topic in"),("doc","draft 92"),("check","publish")]),
 "softwarebill":("> replace the stack",[("rows","5 subs"),("bolt","one chat"),("coin","cents")]),
 "bill":        ("> replace the payroll",[("person","5 roles"),("bolt","one chat"),("coin","cents")]),
 "designer":    ("> make it on-brand",[("chat","brief"),("doc","9 assets"),("check","approved")]),
 "developer":   ("> ship the page",[("chat","plain English"),("gear","build + test"),("check","live")]),
 "orgchart":    ("> run every role",[("person","5 seats"),("bolt","one chat"),("check","headcount 0")]),
 "workflows":   ("> set it once",[("gear","9 flows"),("cal","fire on triggers"),("check","runs daily")]),
 "leadscore":   ("> rank my pipe",[("rows","1,284 in"),("chart","scored"),("bolt","63 hot")]),
 "skills":      ("> install the desk",[("rows","12 skills"),("gear","one chat"),("check","runs daily")]),
 "revenue":     ("> show me the money",[("chart","$48k MRR"),("bolt","up 32%"),("person","one operator")]),
 "agents":      ("> run them in parallel",[("person","6 agents"),("bolt","one task each"),("check","you approve")]),
 "levels":      ("> climb a level",[("rows","7 levels"),("bolt","you: L5"),("check","L7: run it all")]),
 "content":     ("> plan the week",[("cal","14 slots"),("doc","drafted"),("send","queued")]),
 "gate":        ("> nothing sends alone",[("send","240 ready"),("shield","YOUR TAP"),("check","released")]),
}
def _flow_card(base,stem,page):
    cmd,steps=FLOWS[stem]
    cw,ch=OBJ_MAXW,600; x0=(W-cw)//2; y0=OBJ_CY-ch//2
    d=ImageDraw.Draw(base)
    # drop shadow + cream card (the pattern interrupt on slate)
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([x0+6,y0+22,x0+cw-6,y0+ch+22],radius=26,fill=(0,0,0,180))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    d.rounded_rectangle([x0,y0,x0+cw,y0+ch],radius=26,fill=CREAM)
    d.rounded_rectangle([x0,y0,x0+cw,y0+ch],radius=26,outline=(200,190,170),width=2)
    # header row: number badge + mono tag
    bx,by=x0+30,y0+26
    d.rounded_rectangle([bx,by,bx+56,by+56],radius=14,fill=ACC)
    f=dm(900,30); d.text((bx+16,by+9),f"{page-1}",font=f,fill=(255,255,255))
    T2.ls_text(d,(bx+74,by+16),"THE PLAY",mono(24),CMUT,3)
    tagf=mono(22); tag="ULTRON RUNS IT"
    d.text((x0+cw-30-d.textlength(tag,font=tagf),by+18),tag,font=tagf,fill=(165,97,63))
    # icon flow
    n=len(steps); fy=y0+150; tile=128
    span=cw-120; step_w=tile; gap=(span-n*tile)/(n-1) if n>1 else 0
    for i,(g,lb) in enumerate(steps):
        tx=x0+60+i*(tile+gap)
        hot=(i==n-2)
        d.rounded_rectangle([tx,fy,tx+tile,fy+tile],radius=22,fill=(ACC if hot else CPAPER))
        d.rounded_rectangle([tx,fy,tx+tile,fy+tile],radius=22,outline=(CLINE if not hot else ACC),width=3)
        col=(255,255,255) if hot else CINK
        gl=_glyph(d,g,tx+tile//2,fy+tile//2,int(tile*0.30),col,w=7)
        if gl is not None: base.alpha_composite(gl,(tx+tile//2-gl.width//2,fy+tile//2-gl.height//2))
        lf=dm(800,23); d.text((tx+tile//2-d.textlength(lb,font=lf)/2,fy+tile+14),lb,font=lf,fill=(CINK if hot else CMUT))
        if i<n-1:
            ax=tx+tile+gap*0.18; axe=tx+tile+gap*0.82; ay=fy+tile//2
            d.line([ax,ay,axe,ay],fill=(143,134,114),width=5)
            d.polygon([(axe,ay-9),(axe+13,ay),(axe,ay+9)],fill=(143,134,114))
    # command chip (dark, mono, send dot) - the paste-this element from the refs
    cy0=y0+ch-146
    d.rounded_rectangle([x0+30,cy0,x0+cw-30,cy0+64],radius=14,fill=(27,26,22))
    cf=mono(26); d.text((x0+52,cy0+17),cmd,font=cf,fill=(232,217,196))
    d.ellipse([x0+cw-30-48,cy0+14,x0+cw-30-12,cy0+50],fill=tuple(ACC))
    d.line([x0+cw-30-30,cy0+40,x0+cw-30-30,cy0+24],fill=(255,255,255),width=5)
    d.polygon([(x0+cw-30-38,cy0+28),(x0+cw-30-30,cy0+18),(x0+cw-30-22,cy0+28)],fill=(255,255,255))
    # thin base strip: brand
    bf=mono(20); d.text((x0+30,y0+ch-52),"ULTRON  ·  ONE CHAT, WHOLE COMPANY",font=bf,fill=CMUT)
    uf=dm(900,24); u="51ultron.com"; d.text((x0+cw-30-d.textlength(u,font=uf),y0+ch-56),u,font=uf,fill=(165,97,63))


# ---------- EDITORIAL v5 (operator refs: alternating light/dark, TIP pill, one elegant anchor) ----------
LIGHT_BG=(246,241,231); LIGHT_INK=(23,21,15); LIGHT_MUT=(87,80,63); LIGHT_CARD=(253,250,243); LIGHT_LINE=(216,205,184)
DARK_CARD=(31,31,30); DARK_LINE=(64,63,60)
def slide_base(light):
    base=Image.new("RGBA",(W,H),(LIGHT_BG if light else BG)+(255,))
    grid=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(grid)
    gc=(23,21,15,26) if light else (250,250,247,18)
    for gy in range(0,H,44): gd.line([(0,gy),(W,gy)],fill=gc,width=1)
    for gx in range(0,W,44): gd.line([(gx,0),(gx,H)],fill=gc,width=1)
    base.alpha_composite(grid)
    return base
def _card(base,d,x0,y0,x1,y1,light,r=24):
    sh=Image.new("RGBA",base.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([x0+5,y0+16,x1+5,y1+16],radius=r,fill=(0,0,0,110 if light else 170))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle([x0,y0,x1,y1],radius=r,fill=(LIGHT_CARD if light else DARK_CARD))
    d.rounded_rectangle([x0,y0,x1,y1],radius=r,outline=(LIGHT_INK if light else (96,94,90)),width=3)
def _ink(light): return LIGHT_INK if light else WHITE
def _mut(light): return LIGHT_MUT if light else (168,163,152)
def anchor(base,stem,light):
    # ONE elegant crescendo-model mini card, centered in the lower band
    d=ImageDraw.Draw(base)
    x0,y0,x1,y1=150,660,W-150,1218; cx=(x0+x1)//2
    ink=_ink(light); mut=_mut(light); ln=(LIGHT_LINE if light else DARK_LINE)
    _card(base,d,x0,y0,x1,y1,light)
    f8=dm(800,26); f5=dm(500,21); m5=mono(20)
    def hdr(t,tag):
        d.text((x0+34,y0+26),t,font=f8,fill=ink)
        d.text((x1-34-d.textlength(tag,font=m5),y0+30),tag,font=m5,fill=tuple(ACC))
    def meta(txt,rule=True,xr=None):
        if rule: d.line([x0+34,y1-76,(xr or x1)-34,y1-76],fill=ln,width=2)
        d.text((x0+34,y1-58),txt,font=mono(18),fill=mut)
    if stem in ("scheduler","content"):
        hdr("Content board","CRESCENDO · KANBAN")
        cols=["Queued","Drafted","Posted"]; cw=(x1-x0-68-40)//3
        for i,cn in enumerate(cols):
            bx=x0+34+i*(cw+20); d.text((bx+4,y0+84),cn,font=f5,fill=mut)
            for j in range(3):
                cy=y0+124+j*114
                d.rounded_rectangle([bx,cy,bx+cw,cy+98],radius=12,fill=((240,233,218) if light else (42,42,40)))
                d.rounded_rectangle([bx+14,cy+14,bx+cw-14,cy+50],radius=7,fill=tuple(ACC) if (i==2 and j==0) else ((214,203,182) if light else (58,58,55)))
                d.text((bx+14,cy+60),["Post","Reel","Carousel","Story","Launch","Newsletter","Thread","Teardown","Case study"][(i+j*3)%9],font=dm(700,17),fill=mut)
        meta("42 pieces queued · drafted in your voice · posts 10:00 local")
    elif stem in ("hubspot","leadscore"):
        hdr("Pipeline","CRESCENDO · CRM")
        st=[("Qualified","$25k"),("Proposal","$90k"),("Closed won","$120k")]; cw=(x1-x0-68-40)//3
        for i,(cn,v) in enumerate(st):
            bx=x0+34+i*(cw+20); won=i==2
            d.text((bx+4,y0+84),cn,font=f5,fill=mut)
            d.rounded_rectangle([bx,y0+120,bx+cw,y0+236],radius=12,fill=tuple(ACC) if won else ((240,233,218) if light else (42,42,40)))
            d.text((bx+18,y0+138),["Acme","Globex","Northwind"][i],font=dm(800,24),fill=(255,255,255) if won else ink)
            d.text((bx+18,y0+180),v,font=dm(900,30),fill=(255,240,230) if won else tuple(ACC))
            if i<2:
                ay=y0+178; d.line([bx+cw+2,ay,bx+cw+18,ay],fill=mut,width=4); d.polygon([(bx+cw+18,ay-7),(bx+cw+28,ay),(bx+cw+18,ay+7)],fill=mut)
        ny=y0+272
        d.rounded_rectangle([x0+34,ny,x1-34,ny+108],radius=12,fill=((240,233,218) if light else (42,42,40)))
        d.text((x0+58,ny+16),"Next: Globex proposal",font=dm(700,23),fill=ink)
        d.text((x0+58,ny+50),"drafted from the last call · parked on HOLD for your tap",font=dm(500,18),fill=mut)
        d.rounded_rectangle([x1-186,ny+30,x1-58,ny+78],radius=24,fill=tuple(ACC)); d.text((x1-166,ny+42),"Review",font=dm(700,20),fill=(255,255,255))
        meta("$235k open · every stage moved by a reply, not by dragging")
    elif stem in ("gmail_sent","warmup"):
        hdr("Outbox","CRESCENDO · MAIL")
        rows=[("Acme · partnership","Sent 10:00"),("Globex · pricing","Sent 10:00"),("Northwind · intro","Sent 10:01"),("Initech · follow-up 2","Sent 10:01")]
        for j,(a,b2) in enumerate(rows):
            ry=y0+92+j*84
            d.rounded_rectangle([x0+34,ry,x1-34,ry+70],radius=12,fill=((240,233,218) if light else (42,42,40)))
            d.ellipse([x0+52,ry+19,x0+84,ry+51],fill=tuple(ACC))
            d.text((x0+102,ry+11),a,font=dm(700,23),fill=ink); d.text((x0+102,ry+41),"one trigger · 62 words",font=dm(500,17),fill=mut)
            d.text((x1-54-d.textlength(b2,font=m5),ry+23),b2,font=m5,fill=tuple(ACC))
        meta("240 sends this week · every one gated on your tap first")
    elif stem in ("revenue","stripe"):
        hdr("Revenue","CRESCENDO · ANALYTICS")
        d.text((x0+34,y0+84),"$48,200",font=dm(900,84),fill=tuple(ACC))
        d.text((x0+40,y0+186),"MRR · up 32% · one operator",font=dm(700,22),fill=mut)
        for j,(a,b2) in enumerate([("New MRR","$6,4k"),("Churn","1.8%"),("Payroll","$0")]):
            ry=y0+240+j*74
            d.rounded_rectangle([x0+34,ry,x0+446,ry+60],radius=10,fill=((240,233,218) if light else (42,42,40)))
            d.text((x0+56,ry+16),a,font=dm(700,21),fill=mut)
            d.text((x0+446-24-d.textlength(b2,font=dm(800,24)),ry+14),b2,font=dm(800,24),fill=ink)
        bars=[0.3,0.42,0.5,0.62,0.74,0.9,1.0]; bw=56
        for i,hh in enumerate(bars):
            bx=x0+520+i*(bw+12); bh=int(300*hh)
            d.rounded_rectangle([bx,y1-100-bh,bx+bw,y1-100],radius=9,fill=tuple(ACC) if i==len(bars)-1 else ((214,203,182) if light else (58,58,55)))
            d.text((bx+10,y1-90),["J","F","M","A","M","J","J"][i],font=dm(700,17),fill=mut)
        meta("subscription + credits · the whole company on one bill",rule=False)
    elif stem in ("softwarebill","bill","orgchart"):
        hdr("The bill","CRESCENDO · PRICING")
        rows=[("Five tools / five seats","$202/mo"),("One operator + Ultron","cents")]
        for j,(a,b2) in enumerate(rows):
            ry=y0+100+j*150; onc=j==1
            d.rounded_rectangle([x0+34,ry,x1-34,ry+118],radius=14,fill=tuple(ACC) if onc else ((240,233,218) if light else (42,42,40)))
            d.text((x0+60,ry+22),a,font=dm(800,28),fill=(255,255,255) if onc else ink)
            d.text((x0+60,ry+66),"context lost · logins · renewals" if not onc else "one context · one bill · the gate",font=dm(500,19),fill=(255,235,225) if onc else mut)
            d.text((x1-60-d.textlength(b2,font=dm(900,42)),ry+34),b2,font=dm(900,42),fill=(255,255,255) if onc else tuple(ACC))
        for i,ch2 in enumerate(["writer","designer","researcher","SDR","ops"]):
            chf=dm(700,19); chw=int(d.textlength(ch2,font=chf))+36
            bx=x0+34+sum(int(d.textlength(c,font=chf))+36+14 for c in ["writer","designer","researcher","SDR","ops"][:i])
            d.rounded_rectangle([bx,y0+404,bx+chw,y0+452],radius=24,outline=ln,width=2)
            d.text((bx+18,y0+416),ch2,font=chf,fill=mut)
        meta("all five roles fold into the chat · you keep the approval tap")
    elif stem in ("developer",):
        hdr("Deploy","CRESCENDO · DEV KIT")
        d.rounded_rectangle([x0+34,y0+88,x1-34,y1-90],radius=14,fill=(20,20,19))
        for j,l in enumerate(["> build the launch funnel","> pulling: hero · pricing · FAQ · CTA","> wired to the 200-founder list","> tests: 42 passed · 0 failed","> live at /launch · $0 beyond the plan","> next: connect the calendar"]):
            d.text((x0+60,y0+116+j*52),l,font=mono(23),fill=(240,201,175) if j==0 else (168,163,152))
        d.ellipse([x1-108,y1-158,x1-64,y1-114],fill=(63,125,92)); d.line([x1-98,y1-136,x1-88,y1-126],fill=(255,255,255),width=5); d.line([x1-88,y1-126,x1-72,y1-146],fill=(255,255,255),width=5)
        meta("plain English in · tested page out · no builder to learn",rule=False)
    elif stem in ("apollo",):
        hdr("The list","CRESCENDO · DATA TABLE")
        for j,(nm,co,sc) in enumerate([("Sarah Lin","Northwind · hiring SDRs","94"),("Marco Diaz","Globex · raised $4M","88"),("Priya Rao","Initech · new CMO","81"),("Alex Chen","Vandelay · tech switch","79")]):
            ry=y0+92+j*84
            d.rounded_rectangle([x0+34,ry,x1-34,ry+70],radius=12,fill=((240,233,218) if light else (42,42,40)))
            d.text((x0+58,ry+11),nm,font=dm(700,23),fill=ink); d.text((x0+58,ry+41),co,font=dm(500,17),fill=mut)
            d.rounded_rectangle([x1-150,ry+15,x1-58,ry+55],radius=11,fill=tuple(ACC)); d.text((x1-136,ry+21),sc+" hot",font=dm(700,20),fill=(255,255,255))
        meta("1,284 scanned · 200 match your ICP · scored while you typed")
    elif stem in ("workflows","skills"):
        hdr("Systems","CRESCENDO · SETTINGS")
        for j,(nm,tg) in enumerate([("Inbound triage","every message"),("Follow-up cadence","daily 09:00"),("Churn watch","on usage drop"),("Weekly digest","Fri 17:00")]):
            ry=y0+92+j*84
            d.rounded_rectangle([x0+34,ry,x1-34,ry+70],radius=12,fill=((240,233,218) if light else (42,42,40)))
            d.text((x0+58,ry+11),nm,font=dm(700,23),fill=ink); d.text((x0+58,ry+41),tg,font=dm(500,17),fill=mut)
            tx=x1-128; d.rounded_rectangle([tx,ry+19,tx+72,ry+51],radius=16,fill=tuple(ACC)); d.ellipse([tx+42,ry+23,tx+68,ry+49],fill=(255,255,255))
        meta("set once · fires on triggers · no standing meetings")
    elif stem in ("calendly",):
        hdr("Booked","CRESCENDO · CALENDAR")
        days=["Mon","Tue","Wed","Thu","Fri"]; cw=(x1-x0-68-64)//5
        for i,dn in enumerate(days):
            bx=x0+34+i*(cw+16); d.text((bx+6,y0+88),dn,font=f5,fill=mut)
            for j in range(3):
                cy=y0+126+j*106; on=(i,j) in ((0,0),(2,0),(3,1),(1,1),(4,2),(1,2))
                d.rounded_rectangle([bx,cy,bx+cw,cy+92],radius=10,fill=tuple(ACC) if on else ((240,233,218) if light else (42,42,40)))
                if on: d.text((bx+12,cy+12),"Call",font=dm(700,19),fill=(255,255,255)); d.text((bx+12,cy+42),"30m",font=dm(500,16),fill=(255,230,220))
        meta("6 calls this week · found, confirmed and prepped from replies")
    elif stem in ("levels",):
        hdr("The climb","CRESCENDO · ONBOARDING")
        d.text((x0+34,y0+84),"L1 answers a question. L7 runs the company.",font=dm(700,22),fill=mut)
        for i in range(7):
            bw2=90; bx=x0+40+i*112; bh=56+i*44
            d.rounded_rectangle([bx,y1-96-bh,bx+bw2,y1-96],radius=9,fill=tuple(ACC) if i==6 else ((214,203,182) if light else (58,58,55)))
            d.text((bx+28,y1-96-bh+8),f"L{i+1}",font=dm(800,20),fill=(255,255,255) if i==6 else mut)
            d.text((bx+10,y1-84),["ask","draft","flow","desk","team","gate","run"][i],font=dm(500,16),fill=mut)
        meta("most founders sit at L2 · the stack above is one chat away",rule=False)
    elif stem in ("gate",):
        hdr("The gate","YOUR TAP")
        for j,(a,b2,hold) in enumerate([("Send 240 outreach emails","parked on HOLD · waiting for you",True),("Publish 3 posts + newsletter","drafted in your voice · queued",True),("Move Globex to Proposal","from this morning's reply",False)]):
            ry=y0+92+j*98
            d.rounded_rectangle([x0+34,ry,x1-34,ry+84],radius=14,fill=((240,233,218) if light else (42,42,40)))
            d.text((x0+60,ry+12),a,font=dm(800,25),fill=ink)
            d.text((x0+60,ry+50),b2,font=dm(500,18),fill=mut)
            tg="HOLD" if hold else "AUTO"; tgf=dm(800,18)
            d.rounded_rectangle([x1-166,ry+22,x1-58,ry+62],radius=20,fill=tuple(ACC) if hold else ((214,203,182) if light else (58,58,55)))
            d.text((x1-146,ry+32),tg,font=tgf,fill=(255,255,255) if hold else mut)
        d.rounded_rectangle([x0+34,y0+404,x0+366,y0+474],radius=35,fill=(46,125,84)); d.text((x0+96,y0+422),"Approve all",font=dm(800,26),fill=(255,255,255))
        d.rounded_rectangle([x0+392,y0+404,x0+620,y0+474],radius=35,outline=ink,width=3); d.text((x0+456,y0+422),"Hold",font=dm(800,26),fill=ink)
        meta("nothing reaches a customer without your tap · undo anytime")
    elif stem in ("designer","seowriter"):
        hdr("On brand","CRESCENDO · SECTIONS")
        pal=[tuple(ACC),(212,162,127),(168,132,108)]
        for i,c in enumerate(pal):
            bx=x0+34+i*((x1-x0-68-40)//3+20)
            d.rounded_rectangle([bx,y0+92,bx+(x1-x0-68-40)//3,y0+240],radius=12,fill=c)
            d.text((bx+16,y0+200),["primary","kraft","earth"][i],font=dm(700,18),fill=(255,255,255))
        d.text((x0+34,y0+266),"assembled from the pack, in your tokens:",font=dm(500,20),fill=mut)
        for i,ch2 in enumerate(["hero","pricing","FAQ","CTA","proof","footer"]):
            chf=dm(700,19); chw=int(d.textlength(ch2,font=chf))+36
            bx=x0+34+sum(int(d.textlength(c,font=chf))+36+14 for c in ["hero","pricing","FAQ","CTA","proof","footer"][:i])
            d.rounded_rectangle([bx,y0+310,bx+chw,y0+358],radius=24,outline=ln,width=2)
            d.text((bx+18,y0+322),ch2,font=chf,fill=ink)
        d.text((x0+34,y0+392),"9 assets out of one brief · same tokens on every asset",font=dm(500,20),fill=mut)
        meta("822 components in the pack · zero briefs to a designer")
    else:
        hdr("Ultron","ONE CHAT")
        for j,(a,b2) in enumerate([("Research","CORTEX briefs the account"),("Outbound","SPECTER drafts, the gate holds"),("Deals","STRIKER moves the pipeline"),("Content","PULSE writes in your voice")]):
            ry=y0+92+j*84
            d.rounded_rectangle([x0+34,ry,x1-34,ry+70],radius=12,fill=((240,233,218) if light else (42,42,40)))
            d.text((x0+58,ry+20),a,font=dm(800,23),fill=ink)
            d.text((x0+300,ry+22),b2,font=dm(500,20),fill=mut)
        meta("one chat · every role · you approve every send")

def place_prem(base,objpath,light):
    # PREMIUM Vertex panel, uniform frame on every slide (operator 2026-07-02): rounded charcoal
    # plate, FIXED width + FIXED top Y, same orthographic view -> the deck reads as one family.
    im0=Image.open(objpath)
    if im0.mode=="RGBA" and im0.getextrema()[3][0]<250:
        # coded clay3d panel with REAL alpha: composite as-is (it carries its own shadow),
        # centred on its solid body at the same fixed zone as every other slide
        T2.place_in_zone(base,im0,(90,664,W-90,1264),fill=1.0)
        return
    im=im0.convert("RGB")
    a=np.asarray(im).astype(int); h,w=a.shape[:2]; area=h*w
    cs=np.concatenate([a[:48,:48].reshape(-1,3),a[:48,-48:].reshape(-1,3),a[-48:,:48].reshape(-1,3),a[-48:,-48:].reshape(-1,3)])
    bgm=np.median(cs,0).astype(int); diff=np.abs(a-bgm).sum(2); bbox=None
    # bbox on the BRIGHT panel body only (thr floor 42), so faint glow/vignette under the
    # panel does not inflate the plate with empty charcoal (s4 dead-space bug)
    for thr in (120,100,80,65,52,42):
        ys,xs=np.where(diff>thr)
        if len(xs)==0: continue
        b=(int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max()))
        if (b[2]-b[0])*(b[3]-b[1])<=0.90*area: bbox=b
        else: break
    if bbox is None: bbox=(0,0,w,h)
    pad=42
    x0=max(0,bbox[0]-pad); y0=max(0,bbox[1]-pad); x1=min(w,bbox[2]+pad); y1=min(h,bbox[3]+pad)
    plate=im.crop((x0,y0,x1,y1))
    # refine: if the plate is mostly an empty under-board (panel floating high on a slab),
    # re-key against the plate's own border colour and cut to the real panel
    pa=np.asarray(plate).astype(int); ph2,pw2=pa.shape[:2]
    pcs=np.concatenate([pa[:36,:36].reshape(-1,3),pa[:36,-36:].reshape(-1,3),pa[-36:,:36].reshape(-1,3),pa[-36:,-36:].reshape(-1,3)])
    pbg=np.median(pcs,0).astype(int); pdiff=np.abs(pa-pbg).sum(2)
    ys2,xs2=np.where(pdiff>44)
    if len(xs2):
        rb=(int(xs2.min()),int(ys2.min()),int(xs2.max()),int(ys2.max()))
        if (rb[2]-rb[0])*(rb[3]-rb[1]) < 0.80*ph2*pw2:
            rp=52
            plate=plate.crop((max(0,rb[0]-rp),max(0,rb[1]-rp),min(pw2,rb[2]+rp),min(ph2,rb[3]+rp)))
    # fit WHOLE plate (never crop the object) in the fixed lower zone, centred at a fixed point
    ZW,ZH=900,600; CX,CY=W//2,970
    sc=min(ZW/plate.width, ZH/plate.height)
    plate=plate.resize((max(1,int(plate.width*sc)),max(1,int(plate.height*sc))),Image.LANCZOS)
    r=28
    m=Image.new("L",plate.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,plate.width,plate.height],radius=r,fill=255)
    px=CX-plate.width//2; py=CY-plate.height//2
    sh=Image.new("RGBA",base.size,(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle([px+6,py+18,px+plate.width+6,py+plate.height+18],radius=r,fill=(0,0,0,120 if light else 180))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
    base.paste(plate,(px,py),m)
    d=ImageDraw.Draw(base)
    d.rounded_rectangle([px,py,px+plate.width,py+plate.height],radius=r,outline=((23,21,15) if light else (84,82,78)),width=3)

def body(base,eyebrow,head,sub,foot,objpath,page,n,fill):
    stem=os.path.splitext(os.path.basename(objpath))[0]
    light=(page%2==0)   # alternating editorial slides
    nb=slide_base(light); base.paste(nb,(0,0))
    d=ImageDraw.Draw(base)
    ink=_ink(light); mut=_mut(light)
    # TIP pill + ghost page no
    pill=f"{eyebrow}"
    pf=mono(22); pw=int(d.textlength(pill,font=pf))+44
    d.rounded_rectangle([70,64,70+pw,112],radius=12,outline=tuple(ACC),width=3)
    d.text((92,76),pill,font=pf,fill=tuple(ACC))
    gf=dm(900,96); gn=f"{page:02d}"
    gh=Image.new("RGBA",(W,H),(0,0,0,0))
    ImageDraw.Draw(gh).text((W-90-d.textlength(gn,font=gf),52),gn,font=gf,fill=((23,21,15,52) if light else (250,250,247,44)))
    base.alpha_composite(gh)
    # hook
    s=min(fit_hook(d,head,W-160,start=66,floor=48),62); hf=dm(900,s); y=150
    for ln in head:
        seg_line(d,80,y,[(t,(ink if c==WHITE else c)) for t,c in ln],hf); y+=int(s*1.12)
    y+=26
    # body paragraphs (bold-lead editorial)
    sf=dm(500,30)
    if sub:
        for lnw in wrap(d,sub,sf,W-170,maxlines=3): d.text((80,y),lnw,font=sf,fill=mut); y+=42
    y+=14
    if foot:
        ff=dm(800,30)
        seg_line(d,80,y,[(t,(ink if c==WHITE else tuple(ACC))) for t,c in foot],ff); y+=46
    if stem in FLOWS:
        cmd=FLOWS[stem][0]; cf=mono(24); cw2=int(d.textlength(cmd,font=cf))+56
        cy=y+8
        d.rounded_rectangle([80,cy,80+cw2,cy+56],radius=12,fill=((27,26,22) if light else (12,12,11)))
        d.text((106,cy+14),cmd,font=cf,fill=(232,217,196))
        # trace strip: what happens after the command (fills the mid band with real steps)
        steps=[lb for _,lb in FLOWS[stem][1]]
        tf=dm(700,20); ty=cy+82; bx=80
        for i,lb in enumerate(steps):
            tw2=int(d.textlength(lb,font=tf))+34
            if bx+tw2>W-80: break
            last=(i==len(steps)-1)
            d.rounded_rectangle([bx,ty,bx+tw2,ty+46],radius=23,fill=(tuple(ACC) if last else None),outline=(None if last else (tuple(ACC) if False else ((199,187,164) if light else (74,73,70)))),width=2)
            d.text((bx+17,ty+11),lb,font=tf,fill=((255,255,255) if last else _mut(light)))
            bx+=tw2
            if not last:
                d.line([bx+8,ty+23,bx+24,ty+23],fill=_mut(light),width=3)
                d.polygon([(bx+24,ty+17),(bx+32,ty+23),(bx+24,ty+29)],fill=_mut(light))
                bx+=44
    if getattr(MAT,"PREMIUM",0):
        place_prem(base,objpath,light)
    elif stem=="ultron_real":
        _bloom(base,W//2,980,430,300,alpha=70); place_obj(base,objpath,fill)
    else:
        anchor(base,stem,light)
    d=ImageDraw.Draw(base)
    progress(d,page,n)


def _orb():
    im=Image.open(ULOGO).convert("RGB"); lum=np.asarray(im).astype(int).sum(2)
    ys,xs=np.where(lum>36); c=im.convert("RGBA").crop((int(xs.min()),int(ys.min()),int(xs.max())+1,int(ys.max())+1))
    sq=max(c.size); s2=Image.new("RGBA",(sq,sq),(0,0,0,0)); s2.alpha_composite(c,((sq-c.width)//2,(sq-c.height)//2))
    m=Image.new("L",(sq,sq),0); ImageDraw.Draw(m).ellipse([0,0,sq,sq],fill=255); s2.putalpha(m); return s2

def _keyed_cluster(zone_w,zone_h):
    # Vertex cover render -> FLOATING logo stack: charcoal bg keyed out, tiles + their glow survive.
    # This is what lets the IG overlay sit ON the video without blocking it (operator correction).
    p=getattr(T2,"COVER_OBJ",None)
    if not p or not os.path.exists(p): return None
    im=Image.open(p).convert("RGB"); arr=np.asarray(im).astype(int)
    cs=np.concatenate([arr[:32,:32].reshape(-1,3),arr[:32,-32:].reshape(-1,3),arr[-32:,:32].reshape(-1,3),arr[-32:,-32:].reshape(-1,3)])
    bg=np.median(cs,0); d=np.abs(arr-bg).sum(2)
    alpha=np.clip((d-26)*7,0,255).astype("uint8")          # soft key: tiles opaque, glow feathers out
    el=Image.fromarray(np.dstack([arr.astype("uint8"),alpha]),"RGBA")
    bb=Image.fromarray((alpha>90).astype("uint8")*255,"L").getbbox()
    if bb:
        px=36; el=el.crop((max(0,bb[0]-px),max(0,bb[1]-px),min(el.width,bb[2]+px),min(el.height,bb[3]+px)))
    s=min(zone_w/el.width, zone_h/el.height)
    return el.resize((max(1,int(el.width*s)),max(1,int(el.height*s))),Image.LANCZOS)

def _bloom(base,cx,cy,rw,rh,alpha=90):
    gl=Image.new("RGBA",base.size,(0,0,0,0))
    ImageDraw.Draw(gl).ellipse([cx-rw,cy-rh,cx+rw,cy+rh],fill=T2.BOOK+(alpha,))
    base.alpha_composite(gl.filter(ImageFilter.GaussianBlur(120)))

def cover_tt(base):
    # TikTok cover = CAROUSEL page (operator 2026-07-02): the hook + marks block sits
    # CENTRED in the middle of the canvas, not top-anchored (that is the IG overlay).
    ghost(base,"01"); d=ImageDraw.Draw(base)
    s=fit_hook(d,COVER["head"],W-2*MX,start=84,floor=58); hf=dm(900,s)
    hh=int(s*1.12)*len(COVER["head"])
    mk_h=132   # marks band height (strip or logo pair)
    block=hh+72+mk_h
    y=(H-block)//2-40
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=int(s*1.12)
    my=y+72
    mk2=getattr(MAT,"MARK2",getattr(T2,"MARK2","claude"))
    d=ImageDraw.Draw(base)
    if mk2=="strip":
        # replacement narrative (operator 2026-07-02): ONLY the tool icons, BIG, no shelf
        # shadow, NO plus, NO Ultron logo on slide 1 - Ultron replaces them, it does not sit next to them
        stk=Image.open("/home/user/tiberiu-claude/content/_hitl-src/covers/tabsrow_clean.png").convert("RGBA")
        tw2=min(W-260, stk.width)
        stk=stk.resize((tw2,int(stk.height*tw2/stk.width)),Image.LANCZOS)
        base.alpha_composite(stk,((W-stk.width)//2, my))
    else:
        logos=[Image.open(CLAUDE_SUN).convert("RGBA"), _orb()]
        L=120; SLOT=88
        for im in logos: im.thumbnail((L,L),Image.LANCZOS)
        tot=sum(im.width for im in logos)+SLOT*(len(logos)-1); x=(W-tot)//2
        for i,im in enumerate(logos):
            base.alpha_composite(im,(x, my+(L-im.height)//2))
            if i<len(logos)-1:
                px=x+im.width+SLOT//2; ph,pt=12,3
                d.rectangle([px-ph,my+L//2-pt,px+ph,my+L//2+pt],fill=T2.BOOK+(255,)); d.rectangle([px-pt,my+L//2-ph,px+pt,my+L//2+ph],fill=T2.BOOK+(255,))
            x+=im.width+SLOT
    txt="Swipe  "+chr(8594); f=dm(900,34); tw=int(d.textlength(txt,font=f)); pw=tw+84; ph=78; px=(W-pw)//2; py=H-184
    d.rounded_rectangle([px,py,px+pw,py+ph],radius=ph//2,fill=(250,250,247))
    d.text((px+42,py+ph//2-24),txt,font=f,fill=(20,14,10))

def cover_ig(out):
    # TRANSPARENT overlay, TOP-THIRD ONLY: hook + small logo band + brand marks. The middle and
    # bottom stay fully open - the movie runs there (operator spec).
    base=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(base)
    s=fit_hook(d,COVER["head"],W-2*MX,start=80,floor=54); hf=dm(900,s); y=112
    halo=Image.new("RGBA",(W,H),(0,0,0,0)); hd=ImageDraw.Draw(halo)
    hh=int(s*1.12)*len(COVER["head"])
    hd.rounded_rectangle([40,y-30,W-40,y+hh+56+112+34],radius=38,fill=(12,10,9,170))
    base.alpha_composite(halo.filter(ImageFilter.GaussianBlur(34)))
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=int(s*1.12)
    # NO 3D model (operator 2026-07-02): marks raised right under the hook, centre stays open for the movie
    my=y+56
    mk2=getattr(MAT,"MARK2",getattr(T2,"MARK2","claude"))
    if mk2=="strip":
        # ONLY the tool icons, big, clean - no shelf shadow, no plus, no Ultron logo on slide 1
        stk=Image.open("/home/user/tiberiu-claude/content/_hitl-src/covers/tabsrow_clean.png").convert("RGBA")
        tw2=min(W-280, stk.width)
        stk=stk.resize((tw2,int(stk.height*tw2/stk.width)),Image.LANCZOS)
        base.alpha_composite(stk,((W-stk.width)//2, my))
    else:
        logos=[Image.open(CLAUDE_SUN).convert("RGBA"), _orb()]
        L=112; SLOT=84
        for im in logos: im.thumbnail((L,L),Image.LANCZOS)
        tot=sum(im.width for im in logos)+SLOT*(len(logos)-1); x=(W-tot)//2
        for i,im in enumerate(logos):
            base.alpha_composite(im,(x, my+(L-im.height)//2))
            if i<len(logos)-1:
                px=x+im.width+SLOT//2; ph,pt=11,3
                d.rectangle([px-ph,my+L//2-pt,px+ph,my+L//2+pt],fill=T2.BOOK+(255,)); d.rectangle([px-pt,my+L//2-ph,px+pt,my+L//2+ph],fill=T2.BOOK+(255,))
            x+=im.width+SLOT
    base.save(out)


def closing(base,handle,page,n):
    ghost(base,f"{page:02d}"); d=ImageDraw.Draw(base)
    ls_text(d,(MX,356),"SAVE THIS",mono(28),ACC,4)
    hf=dm(900,76); y=424
    for ln in [CLOSE["l1"],CLOSE["l2"]]: d.text((MX,y),ln,font=hf,fill=WHITE); y+=int(76*1.1)
    d.text((MX,y+10),CLOSE["q"],font=dm(500,33),fill=MUTED)
    py=y+92; txt=f"{handle}   →"; f=dm(800,42); tw=int(d.textlength(txt,font=f)); pw=tw+80; ph=90
    d.rounded_rectangle([MX,py,MX+pw,py+ph],radius=ph//2,fill=ACC); d.text((MX+40,py+ph//2-28),txt,font=f,fill=(22,13,8))
    lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS); base.alpha_composite(lg,(MX,H-160))
    d.text((MX+64,H-150),handle,font=mono(30),fill=ACC)

def unpack(item):
    eb,head=item[0],item[1]
    sub=item[2] if len(item)>4 else None
    foot=item[3] if len(item)>5 else None
    return eb,head,sub,foot,item[-2],item[-1]

def deck(outdir, overlay):
    os.makedirs(outdir,exist_ok=True)
    for f in os.listdir(outdir):
        if f.startswith("s") and f.endswith(".png"): os.remove(os.path.join(outdir,f))
    slides=[("cover",)]+[("mid",c) for c in CONTENT]
    slides+=[("close","@tiberiu.ai"),("close","@51ultron")] if not overlay else [("last",CTA)]
    n=len(slides)
    for i,sl in enumerate(slides,1):
        if sl[0]=="cover":
            if overlay: cover_ig(f"{outdir}/s{i}.png"); continue
            base=slide_base(False); cover_tt(base); base.convert("RGB").save(f"{outdir}/s{i}.png"); continue
        # first AND last slides share the same grid texture as the body slides (operator 2026-07-02)
        base=slide_base(False)
        if sl[0]=="close": closing(base,sl[1],i,n)
        elif sl[0]=="last":
            eb,head,objp,fill=CTA[0],CTA[1],CTA[-2],CTA[-1]; ghost(base,f"{i:02d}"); d=ImageDraw.Draw(base)
            ls_text(d,(MX,356),eb,mono(28),ACC,4)
            s=fit_hook(d,head,W-2*MX,start=76,floor=54); hf=dm(900,s); y=424
            for ln in head: seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
            T2.place_in_zone(base, crop_obj(Image.open(objp)), (MX,690,W-MX,1120), fill=fill)
            d.text((MX,1150),"Follow for one AI system for founders every day.",font=dm(700,28),fill=WHITE); footer(base)
        else:
            eb,head,sub,foot,objp,fill=unpack(sl[1]); body(base,eb,head,sub,foot,objp,i,n,fill)
        base.convert("RGB").save(f"{outdir}/s{i}.png")
    return n

if __name__=="__main__":
    a=deck(f"{T2.OUTBASE}/{OUT}_tt",False); b=deck(f"{T2.OUTBASE}/{OUT}_ig",True)
    print("tt",a,"ig",b)
