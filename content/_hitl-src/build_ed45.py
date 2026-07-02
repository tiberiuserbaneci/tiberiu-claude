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

def body(base,eyebrow,head,sub,foot,objpath,page,n,fill):
    ghost(base,f"{page:02d}"); d=ImageDraw.Draw(base)
    ls_text(d,(MX,66),eyebrow,mono(27),ACC,4)
    s=min(fit_hook(d,head,W-2*MX,start=64,floor=46),60); hf=dm(900,s); y=108
    for ln in head: seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    y+=32   # clear gap between hook and sub-hook
    if sub:
        sf=dm(500,31)
        for ln in wrap(d,sub,sf,W-2*MX): d.text((MX,y),ln,font=sf,fill=INK); y+=41
    stem=os.path.splitext(os.path.basename(objpath))[0]
    if stem in FLOWS:
        _bloom(base,W//2,OBJ_CY,470,330,alpha=64)
        _flow_card(base,stem,page)
    else:
        _bloom(base,W//2,OBJ_CY,470,330,alpha=54)
        place_obj(base,objpath,fill)
    if foot:   # the idea line under the object (fills the lower space)
        ff=dm(800,34); fw=int(d.textlength("".join(t for t,_ in foot),font=ff))
        seg_line(d,(W-fw)//2,H-176,foot,ff)
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
    ghost(base,"01"); d=ImageDraw.Draw(base)
    s=fit_hook(d,COVER["head"],W-2*MX,start=84,floor=58); hf=dm(900,s); y=118
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=int(s*1.12)
    # small logo band right under the hook - top third only, the rest of the canvas stays open
    el=_keyed_cluster(W-300, 442)
    if el is not None:
        _bloom(base,W//2,y+44+el.height//2,360,210,alpha=64)
        base.alpha_composite(el,((W-el.width)//2, y+44))
        my=y+44+el.height+34
    else: my=y+60
    logos=[Image.open(CLAUDE_SUN).convert("RGBA"), _orb()]
    L=84; SLOT=72
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    d=ImageDraw.Draw(base)
    nn=len(logos); x=(W-(L*nn+SLOT*(nn-1)))//2
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, my+(L-im.height)//2))
        if i<nn-1:
            px=x+L+SLOT//2; ph,pt=12,3
            d.rectangle([px-ph,my+L//2-pt,px+ph,my+L//2+pt],fill=T2.BOOK+(255,)); d.rectangle([px-pt,my+L//2-ph,px+pt,my+L//2+ph],fill=T2.BOOK+(255,))
        x+=L+SLOT
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
    hd.rounded_rectangle([40,y-30,W-40,y+hh+20],radius=38,fill=(12,10,9,170))
    base.alpha_composite(halo.filter(ImageFilter.GaussianBlur(34)))
    for ln in COVER["head"]: seg_center(d,y,ln,hf); y+=int(s*1.12)
    el=_keyed_cluster(W-320, 408)
    if el is not None:
        base.alpha_composite(el,((W-el.width)//2, y+38)); my=y+38+el.height+30
    else: my=y+54
    logos=[Image.open(CLAUDE_SUN).convert("RGBA"), _orb()]
    L=80; SLOT=68
    for im in logos: im.thumbnail((L,L),Image.LANCZOS)
    d=ImageDraw.Draw(base)
    nn=len(logos); x=(W-(L*nn+SLOT*(nn-1)))//2
    for i,im in enumerate(logos):
        base.alpha_composite(im,(x+(L-im.width)//2, my+(L-im.height)//2))
        if i<nn-1:
            px=x+L+SLOT//2; ph,pt=11,3
            d.rectangle([px-ph,my+L//2-pt,px+ph,my+L//2+pt],fill=T2.BOOK+(255,)); d.rectangle([px-pt,my+L//2-ph,px+pt,my+L//2+ph],fill=T2.BOOK+(255,))
        x+=L+SLOT
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
            base=Image.new("RGBA",(W,H),BG+(255,)); dots(base); cover_tt(base); base.convert("RGB").save(f"{outdir}/s{i}.png"); continue
        base=Image.new("RGBA",(W,H),BG+(255,)); dots(base)
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
