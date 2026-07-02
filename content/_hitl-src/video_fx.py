#!/usr/bin/env python3
# VIDEO FX - slideshow dinamic din cod (operator 2026-07-02: "fiecare slide sa se genereze
# in cele 3 secunde, cu explozie, cu culoare"). Fiecare slide e spart in straturi (header /
# panou / progress) si animat cu CSS keyframes in Chromium; cadrele se extrag deterministic
# cu Web Animations API (pause + currentTime), apoi ffmpeg le coase la 30fps.
# Usage: python3 video_fx.py <slug> <accent_r,g,b> [out.mp4]
import sys, os, glob, base64, subprocess, shutil
from PIL import Image
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

ROOT="/home/user/tiberiu-claude"
FPS=30; DUR=3.0          # sec per slide
W,H=1080,1350
HDR_Y=612                 # header zone ends ~612 (pill+hook+sub+chip+trace)
PNL_Y1,PNL_Y2=600,1272    # panel zone
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()

HTML="""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0}
body{width:1080px;height:1350px;overflow:hidden;background:#000}
.stage{position:relative;width:1080px;height:1350px}
img{position:absolute;left:0;display:block}
/* fundalul: slide-ul intreg, intra din intuneric cu zoom-out */
.bg{top:0;width:1080px;filter:brightness(.16) saturate(.5) blur(5px);transform:scale(1.06);
  animation:bgin .5s 1.12s cubic-bezier(.2,.7,.3,1) forwards}
@keyframes bgin{to{filter:brightness(1) saturate(1) blur(0px);transform:scale(1)}}
/* headerul cade cu overshoot */
.hdr{top:0;width:1080px;clip-path:inset(0 0 CLIPHDRpx 0);opacity:0;transform:translateY(-46px);
  animation:hdrin .5s .18s cubic-bezier(.34,1.45,.5,1) forwards}
@keyframes hdrin{to{opacity:1;transform:translateY(0)}}
/* panoul EXPLODEAZA: pop cu overshoot + rotatie care se aseaza */
.pnl{top:PNLTOPpx;width:1080px;clip-path:inset(PNLC1px 0 PNLC2px 0);opacity:0;
  transform:scale(.62) rotate(-4deg);transform-origin:50% 60%;
  animation:pnlin .62s .62s cubic-bezier(.3,1.6,.4,1) forwards}
@keyframes pnlin{60%{opacity:1;transform:scale(1.07) rotate(1.2deg)}to{opacity:1;transform:scale(1) rotate(0)}}
/* flash radial in culoarea deck-ului la impact */
.flash{position:absolute;inset:0;pointer-events:none;opacity:0;
  background:radial-gradient(circle at 50% 66%, rgba(ACC,.85) 0%, rgba(ACC,.25) 34%, transparent 62%);
  animation:fl .5s .66s ease-out forwards}
@keyframes fl{12%{opacity:.95}to{opacity:0}}
/* particule care zboara din centrul panoului */
.p{position:absolute;left:540px;top:900px;width:16px;height:16px;border-radius:50%;
  background:rgb(ACC);opacity:0;box-shadow:0 0 18px rgba(ACC,.8)}
PARTS
/* zoom lent dupa asamblare, tine cadrul viu */
.kb{position:absolute;inset:0;animation:kb 2.1s .9s linear forwards;transform-origin:50% 44%}
@keyframes kb{to{transform:scale(1.035)}}
/* shimmer pe progress */
.sh{position:absolute;left:200px;top:1288px;width:120px;height:14px;border-radius:7px;opacity:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);
  animation:sh 1.2s 1.4s ease-in-out forwards}
@keyframes sh{15%{opacity:1}to{opacity:0;transform:translateX(560px)}}
</style></head><body>
<div class="stage"><div class="kb">
<img class="bg" src="data:image/png;base64,B64FULL">
<img class="hdr" src="data:image/png;base64,B64FULL">
<img class="pnl" src="data:image/png;base64,B64FULL">
</div>
<div class="flash"></div>
PDIVS
<div class="sh"></div>
</div></body></html>"""

def slide_html(png,acc):
    full="file://"+png
    import math, random
    pk=""; pd=""
    for i in range(14):
        ang=i*(360/14); dist=330+ (i%3)*90
        dx=int(dist*math.cos(math.radians(ang))); dy=int(dist*0.72*math.sin(math.radians(ang)))
        sz=8+(i%4)*5
        pk+=(f".p{i}{{width:{sz}px;height:{sz}px;animation:pp{i} .75s {0.64+ (i%5)*0.03}s cubic-bezier(.2,.8,.4,1) forwards}}"
             f"@keyframes pp{i}{{8%{{opacity:1}}to{{opacity:0;transform:translate({dx}px,{dy}px) scale(.2)}}}}\n")
        pd+=f'<div class="p p{i}"></div>'
    h=HTML.replace("data:image/png;base64,B64FULL",full).replace("ACC",acc)
    h=h.replace("CLIPHDR",str(H-HDR_Y)).replace("PNLTOP","0").replace("PNLC1",str(PNL_Y1)).replace("PNLC2",str(H-PNL_Y2))
    h=h.replace("PARTS",pk).replace("PDIVS",pd)
    return h

def render(slug,acc,out):
    slides=sorted(glob.glob(f"{ROOT}/scratchpad/{slug}_tt/s*.png"),
                  key=lambda f:int(''.join(c for c in os.path.basename(f) if c.isdigit())))
    fdir=f"{ROOT}/scratchpad/fx_{slug}"; shutil.rmtree(fdir,ignore_errors=True); os.makedirs(fdir)
    n=0
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":W,"height":H})
        total=int(FPS*DUR)
        for si,png in enumerate(slides):
            hp=f"{fdir}/_slide.html"; open(hp,"w").write(slide_html(png,acc))
            pg.goto("file://"+hp); pg.wait_for_timeout(300)
            pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
            for f in range(total):
                t=f*1000.0/FPS
                pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t})")
                pg.screenshot(path=f"{fdir}/f{n:05d}.png"); n+=1
            print("slide",si+1,"/",len(slides),"ok")
        b.close()
    ff=imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff,"-y","-framerate",str(FPS),"-i",f"{fdir}/f%05d.png",
                    "-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p",
                    "-movflags","+faststart",out],check=True,capture_output=True)
    shutil.rmtree(fdir,ignore_errors=True)
    print("OUT",out,os.path.getsize(out)//1024,"KB")

if __name__=="__main__":
    slug=sys.argv[1]; acc=sys.argv[2]
    out=sys.argv[3] if len(sys.argv)>3 else f"{ROOT}/scratchpad/{slug}_fx.mp4"
    render(slug,acc,out)
