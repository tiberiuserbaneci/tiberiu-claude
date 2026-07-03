#!/usr/bin/env python3
# "Claude Fable in action" - CODED animation on the CLAUDE LIGHT palette (operator: no bright red,
# use the Claude palette / the white from our presentations). Terminal types real code line by line,
# preview/output fills as it runs, cursor blinks, slow push-in. 13s, no loop.
import os, subprocess, shutil, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SP=f"{ROOT}/scratchpad/covers"; FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H,FPS,DUR=1080,1920,30,13.0
# ---- Claude palette (light) ----
CREAM=(245,243,238); CREAM2=(236,232,222); PAPER=(252,251,247); INK=(41,38,34); INK2=(90,84,76)
MUT=(150,140,128); CORAL=(217,119,87); KRAFT=(196,150,110); LINEC=(222,216,205)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)
cx=W//2; tx0,ty0,tx1,ty1=150,700,930,1330

def base_frame():
    bg=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(bg,"RGBA")
    # soft cream radial + faint coral warmth
    glow=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(glow).ellipse([cx-560,520,cx+560,1420],fill=(217,119,87,26)); glow=glow.filter(ImageFilter.GaussianBlur(220))
    bg=Image.alpha_composite(bg.convert("RGBA"),glow).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
    # Claude sunburst (coral) + Claude wordmark
    sun=Image.open(f"{ROOT}/content/_hitl-src/claude_official.png").convert("RGBA"); bb=sun.split()[3].getbbox(); sun=sun.crop(bb) if bb else sun
    sun.thumbnail((92,92),Image.LANCZOS); tint=Image.new("RGBA",sun.size,CORAL+(255,)); tint.putalpha(sun.split()[3])
    bg.paste(tint,(cx-tint.width-10,452),tint); d.text((cx+2,466),"Claude",font=dm(700,44),fill=INK2)
    # FABLE - big, ink with coral, letter-spaced
    def spaced(dr,s,f,y,fill,ls):
        tot=sum(dr.textlength(c,font=f)+ls for c in s)-ls; x=cx-tot/2
        for c in s: dr.text((x,y),c,font=f,fill=fill); x+=dr.textlength(c,font=f)+ls
    spaced(d,"FABLE",dm(900,96),556,INK,16)
    # terminal (light IDE) + soft shadow
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([tx0+4,ty0+16,tx1+4,ty1+16],radius=26,fill=(120,95,60,60))
    bg=Image.alpha_composite(bg.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(26))).convert("RGB"); d=ImageDraw.Draw(bg,"RGBA")
    d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=26,fill=PAPER,outline=LINEC,width=2)
    d.rounded_rectangle([tx0,ty0,tx1,ty0+58],radius=26,fill=CREAM2)
    d.rectangle([tx0,ty0+40,tx1,ty0+58],fill=CREAM2)
    d.line([tx0,ty0+58,tx1,ty0+58],fill=LINEC,width=1)
    for i,c in enumerate([(217,119,87),(210,160,90),(180,170,150)]): d.ellipse([tx0+24+i*24,ty0+22,tx0+38+i*24,ty0+36],fill=c)
    d.text((tx0+120,ty0+18),"fable.py — agent",font=mono(24),fill=MUT)
    d.text((cx- d.textlength("the agent designs itself",font=dm(700,30))/2,1372),"the agent designs itself",font=dm(700,30),fill=INK2)
    return bg
BASE=base_frame()

CODES=["def build(brief):","    plan = claude.think(brief)","    ui = design(plan)","    for step in plan:","        agent.run(step)","    ship(ui)"]
COMMENT={2:"# self-assembling",4:"# writing...",5:"# done"}
LINE_T=[(0.4,0.5),(1.0,0.9),(2.1,1.0),(3.3,0.7),(4.2,0.9),(5.4,0.6)]
PREVIEW_T=[6.6,7.2,7.8]; OUTPUT_T=8.6

def draw_dynamic(img,t):
    d=ImageDraw.Draw(img,"RGBA"); f=mono(27)
    shown=0
    for i,ln in enumerate(CODES):
        st,du=LINE_T[i]
        if t<st: break
        frac=min(1.0,(t-st)/du); nch=int(len(ln)*frac); shown=i
        d.text((tx0+34,ty0+92+i*46),ln[:nch],font=f,fill=INK)
        if frac>=1.0 and i in COMMENT:
            d.text((tx0+34+d.textlength(ln+"   ",font=f),ty0+92+i*46),COMMENT[i],font=f,fill=MUT)
    # blinking cursor at the current line end
    if int(t*2)%2==0 and t<OUTPUT_T:
        st,du=LINE_T[shown]; frac=min(1.0,(t-st)/du); nch=int(len(CODES[shown])*frac)
        cxp=tx0+34+d.textlength(CODES[shown][:nch],font=f); cyp=ty0+92+shown*46
        d.rectangle([cxp+4,cyp+4,cxp+17,cyp+34],fill=CORAL)
    # preview cards fill
    px0,py0=tx0+470,ty1-210
    d.rounded_rectangle([px0,py0,tx1-30,ty1-30],radius=14,fill=CREAM2,outline=LINEC,width=1)
    d.text((px0+18,py0+16),"PREVIEW",font=mono(18),fill=MUT)
    for j,pt in enumerate(PREVIEW_T):
        if t>=pt:
            gp=min(1.0,(t-pt)/0.4); wfull=(tx1-48)-(px0+18)
            d.rounded_rectangle([px0+18,py0+48+j*40,px0+18+int(wfull*gp),py0+76+j*40],radius=7,fill=(CORAL if j==0 else KRAFT))
    # output line
    if t>=OUTPUT_T:
        g=min(1.0,(t-OUTPUT_T)/0.5); base=ty0+92+6*46+8
        d.text((tx0+34,base),"> shipped in 6.2s",font=f,fill=(int(217*g+ (1-g)*245),int(119*g+(1-g)*243),int(87*g+(1-g)*238)))
        chx=tx0+34+d.textlength("> shipped in 6.2s  ",font=f)
        d.line([chx,base+16,chx+8,base+24],fill=(int(90+ (147)*g),int(150+ (30)*g),int(110)),width=3)
        d.line([chx+8,base+24,chx+22,base+6],fill=(int(90+147*g),int(150+30*g),110),width=3)
    return img

TMPF=f"{ROOT}/scratchpad/_fanim"; shutil.rmtree(TMPF,ignore_errors=True); os.makedirs(TMPF)
NF=int(DUR*FPS)
for fr in range(NF):
    t=fr/FPS; img=BASE.copy(); draw_dynamic(img,t)
    z=1.0+0.05*(t/DUR); cwp,chp=int(W/z),int(H/z); x0=(W-cwp)//2; y0=int((H-chp)*0.42)
    img=img.crop((x0,y0,x0+cwp,y0+chp)).resize((W,H),Image.LANCZOS)
    img.save(f"{TMPF}/f{fr:05d}.png")
subprocess.run([FF,"-y","-framerate",str(FPS),"-i",f"{TMPF}/f%05d.png","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",f"{SP}/fable_anim.mp4"],capture_output=True)
print("saved fable_anim.mp4 dur",DUR,"frames",NF)
