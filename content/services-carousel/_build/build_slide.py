#!/usr/bin/env python3
# Composite ADDITIVE motion on top of a Vertex render (no hiding, no rebuild).
# First frame = the clean Vertex design (all overlays transparent). When the animation
# starts, each row LIGHTS UP in sequence (orange glow fire), a scan line rides down,
# check pings pop, the gate pulses, the prompt shimmers, swipe arrow nudges, captions sync.
# Usage: build_slide.py <png> <out.mp4> <dur_s> <mode static|motion> <swipe 0|1> <caption.json>
import sys, json, base64, os, glob, subprocess
import numpy as np
from PIL import Image
import imageio_ffmpeg
from playwright.sync_api import sync_playwright
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from detect import norm, detect_console

TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
HERE=os.path.dirname(os.path.abspath(__file__))
sans=base64.b64encode(open(f"{TE}/DMSans-VF.ttf","rb").read()).decode()
mono=base64.b64encode(open(f"{TE}/DMMono-Medium.ttf","rb").read()).decode()

def build(png,out,dur,mode,swipe,caps):
    im=norm(png)
    x0,y0,x1,y1=detect_console(im)
    W=x1-x0; Hc=y1-y0; pad=int(W*0.045); ix0,ix1=x0+pad,x1-pad
    rows_top=y0+int(Hc*0.255); gate_top=y0+int(Hc*0.805)
    gate=[ix0,gate_top,ix1,y0+int(Hc*0.905)]
    prompt=[ix0,y0+int(Hc*0.10),ix1,y0+int(Hc*0.205)]
    n=5; seg=(gate_top-rows_top)/n
    img64=base64.b64encode(open(_resave(im),"rb").read()).decode()

    # LEAD = blank-paint buffer that gets trimmed off the front so the reel starts on the
    # fully-painted clean Vertex design. All animation delays + caption times are shifted by LEAD.
    LEAD=0.8
    # motion timing (seconds). Brief clean hold, then prompt shimmer, then rows fire in sequence.
    t_prompt=LEAD+0.35
    t_rows0=t_prompt+0.55
    t_rows_span=max(1.8,dur-(t_rows0-LEAD)-1.7)
    rowdelay=lambda i:t_rows0+i*(t_rows_span/n)
    t_gate=rowdelay(n-1)+0.45
    caps=[{"t":c["t"],"s":c["s"]+LEAD,"e":c["e"]+LEAD} for c in caps]

    # ADDITIVE row-fire: each row is always visible; an orange highlight pulses over it in turn.
    fires="".join(
      f'<div class="rfire" style="left:{ix0}px;top:{rows_top+i*seg:.0f}px;width:{ix1-ix0}px;height:{seg-6:.0f}px;'
      f'animation:rfire .75s ease forwards;animation-delay:{rowdelay(i):.2f}s"></div>'
      for i in range(n)) if mode=="motion" else ""
    pings="".join(
      f'<div class="ping" style="left:{x1-int(W*0.05)}px;top:{rows_top+(i+0.5)*seg:.0f}px;'
      f'animation:ping .6s ease-out forwards;animation-delay:{rowdelay(i)+0.12:.2f}s"></div>'
      for i in range(n)) if mode=="motion" else ""
    scan=(f'<div class="scan" style="left:{ix0}px;width:{ix1-ix0}px;'
          f'animation:scan {t_rows_span:.2f}s linear forwards;animation-delay:{t_rows0:.2f}s;'
          f'--y0:{rows_top}px;--y1:{gate_top}px"></div>') if mode=="motion" else ""
    promptfx=(f'<div class="shim" style="left:{prompt[0]}px;top:{prompt[1]}px;width:{prompt[2]-prompt[0]}px;height:{prompt[3]-prompt[1]}px;'
              f'animation:shim .7s ease-out forwards {t_prompt:.2f}s"></div>') if mode=="motion" else ""
    gatefx=(f'<div class="gate" style="left:{gate[0]}px;top:{gate[1]}px;width:{gate[2]-gate[0]}px;height:{gate[3]-gate[1]}px;'
            f'animation:gate 1.7s ease-in-out infinite;animation-delay:{t_gate:.2f}s"></div>') if mode=="motion" else ""
    swipefx=('<div class="swipe"><div class="slbl">SWIPE</div><div class="sbtn">&#8594;</div></div>') if swipe else ""

    capdivs=""
    for c in caps:
        txt=c["t"].replace("[",'<em>').replace("]",'</em>')
        capdivs+=(f'<div class="cap" style="animation:capin .4s ease forwards {c["s"]:.2f}s,capout .3s ease forwards {c["e"]:.2f}s">'
                  f'<span>{txt}</span></div>')

    HTML=f"""<!doctype html><html><head><meta charset=utf8><style>
@font-face{{font-family:S;src:url(data:font/ttf;base64,{sans}) format('truetype');font-weight:100 1000}}
@font-face{{font-family:M;src:url(data:font/ttf;base64,{mono}) format('truetype')}}
*{{margin:0;padding:0;box-sizing:border-box}}
.cv{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#f3ebdf}}
.bg{{position:absolute;inset:0;width:1080px;height:1350px}}
.rfire{{position:absolute;z-index:3;border-radius:14px;opacity:0;
   background:linear-gradient(90deg,rgba(255,122,69,.12),rgba(255,122,69,.03));
   box-shadow:inset 0 0 0 2px rgba(255,122,69,.6),0 0 26px 2px rgba(255,122,69,.28)}}
.ping{{position:absolute;z-index:4;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;
   border:3px solid #34c759;opacity:0}}
.scan{{position:absolute;z-index:4;height:3px;top:var(--y0);
   background:linear-gradient(90deg,transparent,#ff7a45,transparent);
   box-shadow:0 0 16px 3px rgba(255,122,69,.7);opacity:0}}
.shim{{position:absolute;z-index:4;border-radius:14px;opacity:0;
   background:linear-gradient(110deg,transparent 30%,rgba(255,255,255,.24) 50%,transparent 70%)}}
.gate{{position:absolute;z-index:2;border-radius:12px;pointer-events:none}}
.swipe{{position:absolute;z-index:6;right:24px;top:50%;transform:translateY(-50%);text-align:center}}
.slbl{{font-family:M;font-size:15px;letter-spacing:.26em;color:#7a6f60;margin-bottom:10px}}
.sbtn{{width:74px;height:74px;border-radius:50%;background:linear-gradient(160deg,#f0613a,#d8401f);
   display:flex;align-items:center;justify-content:center;color:#fff;font-family:S;font-size:36px;font-weight:900;
   box-shadow:0 12px 28px rgba(216,64,31,.5),inset 0 2px 0 rgba(255,255,255,.3);animation:nudge 1.4s ease-in-out infinite}}
.cap{{position:absolute;z-index:7;left:50%;bottom:54px;transform:translateX(-50%);opacity:0;
   max-width:940px;padding:18px 30px;border-radius:18px;background:rgba(20,16,12,.82);
   backdrop-filter:blur(4px);box-shadow:0 10px 30px rgba(0,0,0,.3)}}
.cap span{{font-family:S;font-weight:800;font-size:38px;line-height:1.22;color:#fff;letter-spacing:-.3px;
   display:block;text-align:center;white-space:nowrap}}
.cap em{{color:#ff7a45;font-style:normal}}
@keyframes rfire{{0%{{opacity:0}}28%{{opacity:1}}62%{{opacity:1}}100%{{opacity:0}}}}
@keyframes ping{{0%{{opacity:.9;transform:scale(.4)}}100%{{opacity:0;transform:scale(2.6)}}}}
@keyframes scan{{0%{{opacity:1;top:var(--y0)}}92%{{opacity:1}}100%{{opacity:0;top:var(--y1)}}}}
@keyframes shim{{0%{{opacity:0;transform:translateX(-30%)}}30%{{opacity:1}}100%{{opacity:0;transform:translateX(30%)}}}}
@keyframes gate{{0%,100%{{box-shadow:0 0 0 0 rgba(255,122,69,0)}}50%{{box-shadow:0 0 40px 6px rgba(255,122,69,.5)}}}}
@keyframes nudge{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(10px)}}}}
@keyframes capin{{from{{opacity:0;transform:translate(-50%,12px)}}to{{opacity:1;transform:translate(-50%,0)}}}}
@keyframes capout{{to{{opacity:0}}}}
</style></head><body>
<div class="cv"><img class="bg" src="data:image/png;base64,{img64}">
{fires}{scan}{pings}{promptfx}{gatefx}{swipefx}{capdivs}</div></body></html>"""
    hp=f"{HERE}/_slide.html"; open(hp,"w").write(HTML)
    vid=f"{HERE}/_vid"; os.makedirs(vid,exist_ok=True)
    for f in glob.glob(vid+"/*.webm"): os.remove(f)
    with sync_playwright() as p:
        br=p.chromium.launch(args=["--force-color-profile=srgb"])
        ctx=br.new_context(viewport={"width":1080,"height":1350},record_video_dir=vid,
                           record_video_size={"width":1080,"height":1350})
        pg=ctx.new_page(); pg.goto(f"file://{hp}",wait_until="load")
        pg.wait_for_function("()=>{const i=document.querySelector('.bg');return i&&i.complete&&i.naturalWidth>0;}",timeout=6000)
        pg.wait_for_timeout(int((dur+LEAD)*1000)+300)
        ctx.close(); br.close()
    webm=glob.glob(vid+"/*.webm")[0]
    FF=imageio_ffmpeg.get_ffmpeg_exe()
    # trim the LEAD blank-paint buffer off the front; keep exactly dur seconds of painted content
    subprocess.run([FF,"-y","-i",webm,"-ss",f"{LEAD:.2f}","-t",f"{dur:.2f}",
                    "-vf","scale=1080:1350:flags=lanczos,fps=30",
                    "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-movflags","+faststart",out],
                   capture_output=True)
    return out

def _resave(im):
    p=f"{HERE}/_bg.png"; im.save(p); return p

if __name__=="__main__":
    png,out,dur,mode,swipe,capf=sys.argv[1:7]
    caps=json.load(open(capf)) if capf!="-" else []
    r=build(png,out,float(dur),mode,swipe=="1",caps)
    print("built",r,os.path.getsize(r) if os.path.exists(r) else "FAIL")
