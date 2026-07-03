#!/usr/bin/env python3
# MOTION REEL v3 (IG only). operator-approved:
#   - IG safe zones enforced everywhere (top 240 / bottom 340 / left 60 / right 150)
#   - hook auto-fit + wrap (never touches edges)
#   - flow: video centered@t0 + hook top -> (1.1s) video descends & fills bottom half ->
#           elements scroll TOP one per 1.1s beat (transition A: reel-scroll spring + motion blur),
#           each element carries eyebrow + hook -> CTA slide overlay on the video background
# Usage: python3 build_motion_reel.py <slug> <bottom_video.mp4> <out.mp4>
import importlib.util, os, sys, math, subprocess, shutil, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H,FPS=1080,1920,30
SAFE_T,SAFE_B,SAFE_L,SAFE_R=240,340,60,150
CX=(SAFE_L+(W-SAFE_R))//2                 # content centre (avoids right rail)
SAFEW=(W-SAFE_R)-SAFE_L                    # safe content width = 870
SPLIT=1000                                 # top zone / bottom video divider (work phase)
TOP_Y0,TOP_Y1=SAFE_T,SPLIT                 # element strip band
TXT_B=H-SAFE_B                             # text must stay above this (1580)
HOOK,TRANS,ELEM,CAP=2.9,1.1,1.1,2.5
BG=(25,25,25)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
def spring(t):  # ease-out-back (slight overshoot)
    c1,c3=1.70158,2.70158; t=t-1; return 1+c3*t*t*t+c1*t*t

slug,bottomv,out=sys.argv[1],sys.argv[2],sys.argv[3]
S=importlib.util.spec_from_file_location("AS",f"{ROOT}/content/_hitl-src/adapt_specs.py"); AS=importlib.util.module_from_spec(S); S.loader.exec_module(AS)
mat=[x for x in AS.ALL if x["slug"]==slug][0]
slides=mat["slides"]; cover=mat["cover"]; close=mat["close"]; ACC=tuple(mat["accent"])
N_EL=len(slides)

def wrap_fit(draw,text,maxw,start,floor,weight=800):
    """shrink font until wrapped text fits maxw in <=3 lines; return (font, lines)."""
    for sz in range(start,floor-1,-2):
        f=dm(weight,sz); words=text.split(); lines=[]; cur=""
        for w in words:
            t=(cur+" "+w).strip()
            if draw.textlength(t,font=f)<=maxw: cur=t
            else: lines.append(cur); cur=w
        if cur: lines.append(cur)
        if len(lines)<=3 and all(draw.textlength(l,font=f)<=maxw for l in lines): return f,lines
    return dm(weight,floor),[text]

_scratch=Image.new("RGBA",(10,10)); _d=ImageDraw.Draw(_scratch)

# ---- build one element CARD (eyebrow + hook + element), fit into the TOP band ----
CARD_H=TOP_Y1-TOP_Y0            # 760
def build_card(sl):
    eb=sl[0]; hook=(sl[1][0]+" "+sl[1][1]).strip()
    el=Image.open(f"{ROOT}/content/_hitl-src/models_clay/{slug}/{sl[4]}.png").convert("RGBA")
    bb=el.split()[3].getbbox();  el=el.crop(bb) if bb else el
    card=Image.new("RGBA",(W,CARD_H),(0,0,0,0)); d=ImageDraw.Draw(card)
    y=6
    # eyebrow (slide title)
    ef=mono(24); ew=d.textlength(eb,font=ef); d.text((CX-ew/2,y),eb,font=ef,fill=(*ACC,255)); y+=40
    # hook (auto-fit, wrap, centred)
    hf,lines=wrap_fit(d,hook,SAFEW,46,32,weight=800)
    for ln in lines:
        w=d.textlength(ln,font=hf); d.text((CX-w/2,y),ln,font=hf,fill=(250,250,247,255)); y+=int(hf.size*1.1)
    y+=18
    # element: fit remaining height and safe width
    availh=CARD_H-y-10; s=min(SAFEW/el.width, availh/el.height)
    ew2,eh2=int(el.width*s),int(el.height*s); el=el.resize((ew2,eh2),Image.LANCZOS)
    card.alpha_composite(el,(int(CX-ew2/2),int(y)))
    return card
cards=[build_card(sl) for sl in slides]

# ---- bottom video frames (full width, cover-crop tall enough for both center-band and bottom-fill) ----
TMPB=f"{ROOT}/scratchpad/_reelb"; shutil.rmtree(TMPB,ignore_errors=True); os.makedirs(TMPB)
subprocess.run([FF,"-y","-i",bottomv,"-vf",f"fps={FPS},scale={W}:-2,crop={W}:{H}:0:0" if False else f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}",f"{TMPB}/b%04d.png"],capture_output=True)
bframes=[Image.open(f"{TMPB}/{f}").convert("RGB") for f in sorted(os.listdir(TMPB))] or [Image.new("RGB",(W,H),(20,18,16))]
# NO LOOP (operator): the video plays ONCE across the video phase [0, VIDEO_END] and freezes at CTA.
# placeholder (8s) is time-stretched to fill VIDEO_END; a real Veo of >=12.8s plays ~1:1.
VIDEO_END=HOOK+TRANS+N_EL*ELEM   # 12.8s for 8 elements
def bframe(t):
    tt=min(max(0.0,t),VIDEO_END)
    i=int((tt/VIDEO_END)*(len(bframes)-1)) if VIDEO_END>0 else 0
    return bframes[max(0,min(len(bframes)-1,i))]

# static grid bg
def grid_bg():
    c=Image.new("RGBA",(W,H),BG+(255,)); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    for gy in range(0,H,44): gd.line([(0,gy),(W,gy)],fill=(250,250,247,15),width=1)
    for gx in range(0,W,44): gd.line([(gx,0),(gx,H)],fill=(250,250,247,15),width=1)
    c.alpha_composite(g); return c
BASE=grid_bg()

def paste_video_band(cv,t,y0,y1):
    band=bframe(t).crop((0, max(0,(H-(y1-y0))//2), W, max(0,(H-(y1-y0))//2)+(y1-y0)))
    cv.paste(band,(0,y0))
    # feather top edge into the dark
    sh=Image.new("RGBA",(W,70),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for i in range(70): sd.line([(0,i),(W,i)],fill=(25,25,25,int(255*(1-i/70))))
    cv.alpha_composite(sh,(0,y0))

work=N_EL*ELEM; total=HOOK+TRANS+work+CAP; NF=int(total*FPS)
TMPF=f"{ROOT}/scratchpad/_reelf"; shutil.rmtree(TMPF,ignore_errors=True); os.makedirs(TMPF)
hookf_start=88

for fr in range(NF):
    t=fr/FPS; cv=BASE.copy(); d=ImageDraw.Draw(cv)
    if t<HOOK+TRANS:
        # intro (video centred) -> descent (video to bottom). hook top, fades during descent.
        if t<HOOK: p=0.0
        else: p=(t-HOOK)/TRANS
        pe=spring(min(1.0,p)) if p>0 else 0.0
        y0=int(560+(SPLIT-560)*min(1.0,max(0.0,p*1.3))); y1=H
        paste_video_band(cv,t,y0,y1)
        # hook top (auto-fit), fade out during descent
        d=ImageDraw.Draw(cv)
        f,lines=wrap_fit(d,cover[0],SAFEW,hookf_start,60,weight=900)
        sub=cover[1]; a=int(255*(1.0-min(1.0,p*1.4)))
        yy=300
        for ln in lines:
            w=d.textlength(ln,font=f); d.text((CX-w/2,yy),ln,font=f,fill=(250,250,247,a)); yy+=int(f.size*1.08)
        sf=dm(900,58); w=d.textlength(sub,font=sf); d.text((CX-w/2,yy+6),sub,font=sf,fill=(*ACC,a))
    elif t<HOOK+TRANS+work:
        tw=t-HOOK-TRANS; idx=min(N_EL-1,int(tw/ELEM)); local=(tw-idx*ELEM)/ELEM
        # bottom video fills bottom half
        paste_video_band(cv,t,SPLIT,H)
        d=ImageDraw.Draw(cv); d.text((SAFE_L,SPLIT+14),"CLAUDE, WORKING",font=mono(22),fill=(*ACC,220))
        # transition A: reel-scroll strip (card idx centred in TOP band), spring + motion blur
        mv=min(1.0, local/0.42); se=spring(mv) if idx>0 else 1.0
        # scroll offset: card idx center should land at TOP band center; during move come from below
        from_off = CARD_H*(1-se) if idx>0 else 0     # incoming rises from below
        # build a layer with current card (and a hint of outgoing sliding up)
        layer=Image.new("RGBA",(W,H),(0,0,0,0))
        layer.alpha_composite(cards[idx],(0,int(TOP_Y0+from_off)))
        if idx>0 and mv<1.0:
            layer.alpha_composite(cards[idx-1],(0,int(TOP_Y0-CARD_H*se)))
        # vertical motion blur while moving fast
        vel=(1-mv)
        if idx>0 and vel>0.12:
            blur=layer.copy(); k=int(6+vel*22)
            acc=Image.new("RGBA",(W,H),(0,0,0,0))
            for o in range(-k,k+1,max(1,k//3)):
                sh=Image.new("RGBA",(W,H),(0,0,0,0)); sh.alpha_composite(blur,(0,o))
                acc=Image.blend(acc,sh,0.5)
            layer=acc
        # clip strip to TOP band
        clip=Image.new("RGBA",(W,H),(0,0,0,0)); clip.paste(layer.crop((0,TOP_Y0,W,TOP_Y1)),(0,TOP_Y0))
        cv.alpha_composite(clip)
    else:
        # CTA: video becomes full background (dimmed), element gone, CTA slide overlay in safe box
        tw=t-HOOK-TRANS-work; fin=spring(min(1.0,tw/0.5))
        full=bframe(t); dim=Image.eval(full,lambda p:int(p*0.34)); cv.paste(dim,(0,0))
        cv2=Image.new("RGBA",(W,H),(0,0,0,0)); cv.alpha_composite(cv2)
        d=ImageDraw.Draw(cv)
        a=int(255*fin)
        ls=mono(28); w=d.textlength("SAVE THIS",font=ls);
        # letter-spaced eyebrow
        x=CX- (w+8*len("SAVE THIS"))/2
        d.text((SAFE_L,560),"SAVE THIS",font=ls,fill=(*ACC,a))
        f,lines=wrap_fit(d,close[0]+" "+close[1],SAFEW,76,54,weight=900); yy=610
        # split close into its two given lines instead of rewrap
        for ln,col in [(close[0],(250,250,247,a)),(close[1],(*ACC,a))]:
            fw=dm(900,74); w=d.textlength(ln,font=fw); d.text((SAFE_L,yy),ln,font=fw,fill=col); yy+=int(74*1.12)
        d.text((SAFE_L,yy+10),close[2],font=dm(500,32),fill=(150,150,140,a))
        # coded CTA pill
        pill=Image.open(f"{ROOT}/content/_hitl-src/_templates/cta/cta-{mat['pill']}.png").convert("RGBA")
        pb=pill.split()[3].getbbox(); pill=pill.crop(pb) if pb else pill
        s=min(560/pill.width, 200/pill.height); pill=pill.resize((int(pill.width*s),int(pill.height*s)),Image.LANCZOS)
        pill.putalpha(pill.split()[3].point(lambda p:int(p*fin)))
        cv.alpha_composite(pill,(SAFE_L,yy+90))
    cv.convert("RGB").save(f"{TMPF}/f{fr:05d}.png")

subprocess.run([FF,"-y","-framerate",str(FPS),"-i",f"{TMPF}/f%05d.png","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",out],capture_output=True)
print("saved",out,"| frames",NF,"| dur",round(total,1),"s | elems",N_EL)
