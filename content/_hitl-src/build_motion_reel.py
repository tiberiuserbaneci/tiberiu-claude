#!/usr/bin/env python3
# MOTION REEL proof (operator concept 2026-07-03): per material, 9:16, beat-synced.
#   hook 2.9s  ->  transition 1.1s  ->  work phase (Claude video BOTTOM + elements scroll TOP,
#   one element per 1.1s beat)  ->  caption 2.5s.  Transitions land on 1.1s beats for music sync.
# Usage: python3 build_motion_reel.py <slug> <bottom_video.mp4> <out.mp4>
import importlib.util, os, sys, math, subprocess, shutil, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H,FPS=1080,1920,30
HOOK,TRANS,ELEM,CAP=2.9,1.1,1.1,2.5
ACC=(212,162,127); WHITE=(250,250,247); MUT=(150,150,140)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
def ease(t): return 1-(1-t)**3   # ease-out cubic

slug,bottomv,out=sys.argv[1],sys.argv[2],sys.argv[3]
S=importlib.util.spec_from_file_location("AS",f"{ROOT}/content/_hitl-src/adapt_specs.py"); AS=importlib.util.module_from_spec(S); S.loader.exec_module(AS)
mat=[x for x in AS.ALL if x["slug"]==slug][0]
stems=[sl[4] for sl in mat["slides"]]
ehooks=[(sl[1][0],sl[1][1]) for sl in mat["slides"]]
cover=mat["cover"]; close=mat["close"]; ACCm=tuple(mat["accent"]); ACC=ACCm

# load element PNGs, cropped to alpha bbox
elems=[]
for st in stems:
    im=Image.open(f"{ROOT}/content/_hitl-src/models_clay/{slug}/{st}.png").convert("RGBA")
    bb=im.split()[3].getbbox()
    elems.append(im.crop(bb) if bb else im)

# extract bottom video frames -> band 1080x690 (cover-crop)
TMPB=f"{ROOT}/scratchpad/_reelb"; shutil.rmtree(TMPB,ignore_errors=True); os.makedirs(TMPB)
BOT_Y0,BOT_Y1=1092,1782; BOT_H=BOT_Y1-BOT_Y0
subprocess.run([FF,"-y","-i",bottomv,"-vf",f"fps={FPS},scale={W}:{BOT_H}:force_original_aspect_ratio=increase,crop={W}:{BOT_H}",f"{TMPB}/b%04d.png"],capture_output=True)
bframes=[Image.open(f"{TMPB}/{f}").convert("RGB") for f in sorted(os.listdir(TMPB))] or [Image.new("RGB",(W,BOT_H),(20,18,16))]

# static grid bg
BG=(25,25,25)
def grid_bg():
    c=Image.new("RGB",(W,H),BG); g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    for gy in range(0,H,44): gd.line([(0,gy),(W,gy)],fill=(250,250,247,16),width=1)
    for gx in range(0,W,44): gd.line([(gx,0),(gx,H)],fill=(250,250,247,16),width=1)
    c=c.convert("RGBA"); c.alpha_composite(g); return c.convert("RGB")
BASE=grid_bg()

def center_text(d,cx,y,lines_fonts):
    for txt,f,col in lines_fonts:
        w=d.textlength(txt,font=f); d.text((cx-w/2,y),txt,font=f,fill=col); y+=int(f.size*1.12)
    return y

def place_elem(canvas,el,cx,cy,maxw,maxh,alpha=255):
    s=min(maxw/el.width,maxh/el.height); w,h=int(el.width*s),int(el.height*s)
    r=el.resize((w,h),Image.LANCZOS)
    if alpha<255:
        a=r.split()[3].point(lambda p:int(p*alpha/255)); r.putalpha(a)
    canvas.alpha_composite(r,(int(cx-w/2),int(cy-h/2)))

TOP_CY=560; TOP_MAXW=980; TOP_MAXH=820
work=len(elems)*ELEM; total=HOOK+work+CAP; N=int(total*FPS)
TMPF=f"{ROOT}/scratchpad/_reelf"; shutil.rmtree(TMPF,ignore_errors=True); os.makedirs(TMPF)
hf=dm(900,84); sf=dm(900,60); ebf=mono(26); capf=dm(900,74); csf=dm(500,34)

for fr in range(N):
    t=fr/FPS; cv=BASE.copy().convert("RGBA"); d=ImageDraw.Draw(cv)
    if t<HOOK:
        # HOOK phase, fade out last 0.4s
        fade=1.0 if t<HOOK-0.4 else max(0.0,(HOOK-t)/0.4)
        col=(*WHITE,int(255*fade)); acol=(*ACC,int(255*fade))
        y=760
        w=d.textlength(cover[0],font=hf); d.text((W/2-w/2,y),cover[0],font=hf,fill=col); y+=int(84*1.12)
        w=d.textlength(cover[1],font=sf); d.text((W/2-w/2,y+6),cover[1],font=sf,fill=acol)
    elif t<HOOK+work:
        tw=t-HOOK; idx=min(len(elems)-1,int(tw/ELEM)); local=(tw-idx*ELEM)/ELEM
        # BOTTOM: Claude video band
        bf=bframes[int(tw*FPS)%len(bframes)]
        cv.paste(bf,(0,BOT_Y0))
        # soft top edge on the band
        sh=Image.new("RGBA",(W,60),(0,0,0,0)); sd=ImageDraw.Draw(sh)
        for i in range(60): sd.line([(0,i),(W,i)],fill=(25,25,25,int(255*(1-i/60))))
        cv.alpha_composite(sh,(0,BOT_Y0))
        # bottom label
        d.text((70,BOT_Y1+18),"CLAUDE, WORKING",font=mono(22),fill=(*ACC,220))
        # TOP: element carousel, slide-in on beat
        slide=ease(min(1.0,local/0.32)); dy=int((1-slide)*70); al=int(255*slide+0)
        place_elem(cv,elems[idx],W/2,TOP_CY+dy,TOP_MAXW,TOP_MAXH,alpha=min(255,al+40))
        # eyebrow + progress dots
        eb=f"{mat['title']}"
        d.text((70,120),eb,font=ebf,fill=(*ACC,230))
        dots_x=70
        for k in range(len(elems)):
            on=k==idx; r=6 if on else 4
            d.ellipse([dots_x,168,dots_x+r*2,168+r*2],fill=(*ACC,255) if on else (120,118,110,255)); dots_x+=22
    else:
        # CAPTION phase, bottom video fading under
        tw=t-HOOK-work; fin=ease(min(1.0,tw/0.5))
        bf=bframes[int((work)*FPS-1)%len(bframes)]
        dim=Image.eval(bf,lambda p:int(p*0.4)); cv.paste(dim,(0,BOT_Y0))
        y=760
        for ln,f,col in [(close[0],capf,WHITE),(close[1],capf,ACC)]:
            w=d.textlength(ln,font=f); d.text((W/2-w/2,y),ln,font=f,fill=(*col,int(255*fin))); y+=int(74*1.12)
        w=d.textlength(close[2],font=csf); d.text((W/2-w/2,y+16),close[2],font=csf,fill=(*MUT,int(255*fin)))
    cv.convert("RGB").save(f"{TMPF}/f{fr:05d}.png")

subprocess.run([FF,"-y","-framerate",str(FPS),"-i",f"{TMPF}/f%05d.png","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",out],capture_output=True)
print("saved",out,"frames",N,"dur",round(total,1),"s")
