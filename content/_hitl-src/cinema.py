#!/usr/bin/env python3
# CINEMA - motor de beats cinematic (operator 2026-07-02: "cinematic, miscarea si tranzitiile
# studiate, blocurile au ele insele viata"). Limbaj preluat din referintele aprobate
# (claude-mem/prompt-key bookcloth): tipografie cinetica cuvant-cu-cuvant, un obiect viu per
# beat (float + respiratie + spotlight care creste), camera cu drift continuu, iesiri variate.
# Un singur HTML cu master-timeline CSS; cadre deterministe (Web Animations API seek) -> ffmpeg.
# Usage: python3 cinema.py <slug> <r,g,b> [out.mp4]
import sys, os, glob, subprocess, shutil, importlib.util, html as H
from PIL import Image
from playwright.sync_api import sync_playwright
import imageio_ffmpeg

ROOT="/home/user/tiberiu-claude"
W,Hh=1080,1920; FPS=30; BEAT=3.2
SAFE_T,SAFE_B,SAFE_L,SAFE_R=300,330,70,130
ASSETS=f"{ROOT}/content/assets"; ULOGO=f"{ROOT}/content/ultron-logo.png"

def load(p):
    s=importlib.util.spec_from_file_location("MAT",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def beats_from(slug):
    M=load(f"{ROOT}/content/_hitl-src/build_{slug}.py"); T2=M.T2
    beats=[]
    cov=T2.COVER["head"]
    beats.append(dict(kind="title",
        w1="".join(t for t,_ in cov[0]), w2="".join(t for t,_ in cov[1]), obj=None))
    for (eb,hook,sub,foot,objp,fill) in T2.CONTENT:
        beats.append(dict(kind="beat", eb=eb,
            w1="".join(t for t,_ in hook[0]), w2="".join(t for t,_ in hook[1]),
            sub=sub, obj=objp))
    c=T2.CLOSE
    beats.append(dict(kind="cta", w1=c["l1"], w2=c["l2"], sub=c["q"], obj=None))
    return beats

def words_html(text,cls,base_delay,step=0.09,beat_t0=0.0,total=0.0):
    # fiecare cuvant intra separat: slam + settle (keyframes procentuale pe master timeline)
    out=""
    for i,w in enumerate(text.split()):
        d=beat_t0+base_delay+i*step
        out+=f'<span class="wd {cls}" style="--d:{d/total*100:.3f}%">{H.escape(w)}</span> '
    return out

def build_html(slug,acc,beats):
    n=len(beats); total=n*BEAT
    orb="file://"+ULOGO
    css_beats=""; body=""
    for bi,b in enumerate(beats):
        t0=bi*BEAT; p0=t0/total*100; p1=(t0+BEAT)/total*100
        pin=p0+0.35/total*100      # scene in
        pout=p1-0.32/total*100      # scene exit start
        # fereastra scenei: intra rapid, iese cu push-up + blur (variat: beats impare ies cu drop)
        exit_tf = "translateY(-90px)" if bi%2==0 else "translateY(120px) rotate(1.6deg)"
        css_beats+=(f"@keyframes sc{bi}{{0%,{p0:.3f}%{{opacity:0}}{pin:.3f}%,{pout:.3f}%{{opacity:1}}"
                    f"{p1:.3f}%,100%{{opacity:0;transform:{exit_tf};filter:blur(6px)}}}}"
                    f".sc{bi}{{animation:sc{bi} {total}s linear infinite}}\n")
        inner=""
        if b["kind"]=="title":
            inner+=f'<div class="big">{words_html(b["w1"],"iv",0.25,0.11,t0,total)}</div>'
            inner+=f'<div class="big acc">{words_html(b["w2"],"bk",0.75,0.11,t0,total)}</div>'
            inner+=f'<img class="orb obj-live" src="{orb}" style="--d:{(t0+1.3)/total*100:.3f}%">'
        elif b["kind"]=="cta":
            inner+=f'<div class="big">{words_html(b["w1"],"iv",0.25,0.1,t0,total)}</div>'
            inner+=f'<div class="big acc">{words_html(b["w2"],"bk",0.7,0.1,t0,total)}</div>'
            inner+=f'<div class="sub ty" style="--d:{(t0+1.35)/total*100:.3f}%">{H.escape(b.get("sub",""))}</div>'
        else:
            inner+=f'<div class="eb ty" style="--d:{(t0+0.18)/total*100:.3f}%">{H.escape(b["eb"])}</div>'
            inner+=f'<div class="mid">{words_html(b["w1"],"iv",0.4,0.09,t0,total)}</div>'
            inner+=f'<div class="mid acc">{words_html(b["w2"],"bk",0.85,0.09,t0,total)}</div>'
            if b.get("sub"):
                inner+=f'<div class="sub ty" style="--d:{(t0+1.15)/total*100:.3f}%">{H.escape(b["sub"])}</div>'
            if b.get("obj") and os.path.exists(b["obj"]):
                cp=f"{ROOT}/scratchpad/_cinobj_{os.path.basename(os.path.dirname(b['obj']))}_{os.path.basename(b['obj'])}"
                if not os.path.exists(cp):
                    im=Image.open(b["obj"]).convert("RGBA"); bb=im.split()[3].getbbox()
                    if bb: im=im.crop(bb)
                    im.save(cp)
                d=(t0+1.45)/total*100
                inner+=(f'<div class="objwrap"><div class="spot" style="--d:{d:.3f}%"></div>'
                        f'<img class="panel obj-live" src="file://{cp}" style="--d:{d:.3f}%"></div>')
        body+=f'<section class="sc sc{bi}">{inner}</section>'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-900.ttf');font-weight:900}}
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-700.ttf');font-weight:700}}
@font-face{{font-family:'DM Sans';src:url('file://{ASSETS}/DMSans-500.ttf');font-weight:500}}
@font-face{{font-family:'DM Mono';src:url('file://{ASSETS}/DMMono-500.ttf');font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{Hh}px;overflow:hidden;background:#191919;font-family:'DM Sans',sans-serif}}
.film{{position:absolute;inset:0;animation:cam {BEAT*len(beats)}s ease-in-out infinite alternate;transform-origin:50% 44%}}
@keyframes cam{{0%{{transform:scale(1.012) translateX(-6px)}}25%{{transform:scale(1.05) translateY(-10px)}}50%{{transform:scale(1.02) translateX(8px)}}75%{{transform:scale(1.055) translateY(6px)}}100%{{transform:scale(1.015)}}}}
.film::before{{content:'';position:absolute;inset:0;
  background-image:linear-gradient(rgba(250,250,247,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(250,250,247,.05) 1px,transparent 1px);
  background-size:72px 72px}}
.atm{{position:absolute;inset:0;background:radial-gradient(ellipse 70% 34% at 82% 4%,rgba({acc},.16),transparent 62%),
  radial-gradient(ellipse 52% 26% at 8% 98%,rgba({acc},.09),transparent 60%)}}
.sc{{position:absolute;top:{SAFE_T+70}px;bottom:{SAFE_B+90}px;left:{SAFE_L}px;right:{SAFE_R}px;
  display:flex;flex-direction:column;justify-content:center;gap:30px;opacity:0}}
.wd{{display:inline-block;opacity:0;transform:translateY(90px) scale(1.4);filter:blur(10px);
  animation:wdin {BEAT*len(beats)}s linear infinite;animation-delay:0s}}
@keyframes wdin{{0%{{opacity:0;transform:translateY(90px) scale(1.4);filter:blur(10px)}}100%{{opacity:0}}}}
.big{{font-weight:900;font-size:132px;line-height:.95;letter-spacing:-5px;color:#FAFAF7}}
.mid{{font-weight:900;font-size:118px;line-height:.95;letter-spacing:-4.5px;color:#FAFAF7}}
.acc .wd,.acc{{color:rgb({acc})}}
.eb{{font-family:'DM Mono',monospace;font-size:26px;letter-spacing:.22em;color:rgba({acc},.95)}}
.sub{{font-weight:500;font-size:33px;line-height:1.3;color:rgba(250,250,247,.68);max-width:820px}}
.ty{{opacity:0}}
.objwrap{{position:relative;align-self:center;margin-top:8px}}
.spot{{position:absolute;left:50%;top:50%;width:760px;height:760px;border-radius:50%;transform:translate(-50%,-50%) scale(0);
  background:radial-gradient(circle, rgba({acc},.2) 0%, rgba({acc},.07) 52%, transparent 72%);opacity:0}}
.panel{{position:relative;display:block;max-width:900px;max-height:660px;opacity:0}}
.orb{{width:190px;align-self:center;border-radius:50%;opacity:0;box-shadow:0 30px 80px rgba(0,0,0,.5)}}
.brand{{position:absolute;bottom:{SAFE_B}px;left:{SAFE_L}px;right:{SAFE_R}px;display:flex;align-items:center;
  justify-content:space-between;border-top:1px solid rgba(250,250,247,.1);padding-top:18px;z-index:9}}
.brand .l{{display:flex;align-items:center;gap:13px;font-family:'DM Mono',monospace;font-size:19px;
  letter-spacing:.1em;color:rgba(250,250,247,.72)}}
.brand img{{width:44px;height:44px;border-radius:50%}}
.brand .r{{font-weight:900;font-size:25px;color:#FAFAF7}}
.brand .r em{{color:rgb({acc});font-style:normal}}
{css_beats}
</style></head><body>
<div class="film"><div class="atm"></div>{body}
<div class="brand"><span class="l"><img src="{orb}"> follow @tiberiu.ai</span><span class="r">51ultron<em>.</em>com</span></div>
</div>
<script>
const TOTAL={BEAT*len(beats)};
// cuvinte: slam + settle la momentul --d (procent din timeline)
document.querySelectorAll('.wd').forEach(el=>{{
  const d=parseFloat(el.style.getPropertyValue('--d'))/100*TOTAL;
  el.animate([
    {{opacity:0,transform:'translateY(90px) scale(1.42)',filter:'blur(12px)',offset:0}},
    {{opacity:0,transform:'translateY(90px) scale(1.42)',filter:'blur(12px)',offset:Math.max(0,d/TOTAL)}},
    {{opacity:1,transform:'translateY(-6px) scale(.985)',filter:'blur(0px)',offset:Math.min(1,(d+0.22)/TOTAL)}},
    {{opacity:1,transform:'none',filter:'blur(0px)',offset:Math.min(1,(d+0.34)/TOTAL)}},
    {{opacity:1,transform:'none',offset:1}}
  ],{{duration:TOTAL*1000,iterations:Infinity}});
}});
// eyebrow/sub: typing-fade
document.querySelectorAll('.ty').forEach(el=>{{
  const d=parseFloat(el.style.getPropertyValue('--d'))/100*TOTAL;
  el.animate([
    {{opacity:0,transform:'translateY(26px)',offset:0}},
    {{opacity:0,transform:'translateY(26px)',offset:Math.max(0,d/TOTAL)}},
    {{opacity:1,transform:'none',offset:Math.min(1,(d+0.3)/TOTAL)}},
    {{opacity:1,offset:1}}
  ],{{duration:TOTAL*1000,iterations:Infinity}});
}});
// obiectele TRAIESC: intrare cu gravitatie + bounce, apoi float continuu + micro-rotatie
document.querySelectorAll('.obj-live').forEach(el=>{{
  const d=parseFloat(el.style.getPropertyValue('--d'))/100*TOTAL;
  el.animate([
    {{opacity:0,transform:'translateY(-340px) rotate(-5deg) scale(.86)',offset:0}},
    {{opacity:0,transform:'translateY(-340px) rotate(-5deg) scale(.86)',offset:Math.max(0,d/TOTAL)}},
    {{opacity:1,transform:'translateY(24px) rotate(1.6deg) scale(1.01)',offset:Math.min(1,(d+0.34)/TOTAL)}},
    {{opacity:1,transform:'translateY(-10px) rotate(-.7deg)',offset:Math.min(1,(d+0.52)/TOTAL)}},
    {{opacity:1,transform:'none',offset:Math.min(1,(d+0.68)/TOTAL)}},
    {{opacity:1,transform:'translateY(-9px) rotate(.5deg)',offset:Math.min(1,(d+1.6)/TOTAL)}},
    {{opacity:1,transform:'translateY(0px) rotate(0deg)',offset:Math.min(1,(d+2.6)/TOTAL)}},
    {{opacity:1,offset:1}}
  ],{{duration:TOTAL*1000,iterations:Infinity}});
}});
// spotlight creste in spatele obiectului
document.querySelectorAll('.spot').forEach(el=>{{
  const d=parseFloat(el.style.getPropertyValue('--d'))/100*TOTAL;
  el.animate([
    {{opacity:0,transform:'translate(-50%,-50%) scale(0)',offset:0}},
    {{opacity:0,transform:'translate(-50%,-50%) scale(0)',offset:Math.max(0,d/TOTAL)}},
    {{opacity:1,transform:'translate(-50%,-50%) scale(1)',offset:Math.min(1,(d+0.55)/TOTAL)}},
    {{opacity:1,transform:'translate(-50%,-50%) scale(1.06)',offset:Math.min(1,(d+1.8)/TOTAL)}},
    {{opacity:1,transform:'translate(-50%,-50%) scale(1)',offset:1}}
  ],{{duration:TOTAL*1000,iterations:Infinity}});
}});
</script></body></html>"""

def render(slug,acc,out):
    beats=beats_from(slug)
    htmlp=f"{ROOT}/scratchpad/cinema_{slug}.html"
    open(htmlp,"w").write(build_html(slug,acc,beats))
    total=BEAT*len(beats); frames=int(total*FPS)
    fdir=f"{ROOT}/scratchpad/cin_{slug}"; shutil.rmtree(fdir,ignore_errors=True); os.makedirs(fdir)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":W,"height":Hh})
        pg.goto("file://"+htmlp); pg.wait_for_timeout(600)
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for f in range(frames):
            t=(f/FPS)*1000
            pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t})")
            pg.screenshot(path=f"{fdir}/f{f:05d}.png")
            if f%150==0: print(f"frame {f}/{frames}")
        b.close()
    ff=imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff,"-y","-framerate",str(FPS),"-i",f"{fdir}/f%05d.png",
                    "-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p",
                    "-movflags","+faststart",out],check=True,capture_output=True)
    shutil.rmtree(fdir,ignore_errors=True)
    print("OUT",out,os.path.getsize(out)//1024,"KB",f"({total:.0f}s)")

if __name__=="__main__":
    slug=sys.argv[1]; acc=sys.argv[2]
    out=sys.argv[3] if len(sys.argv)>3 else f"{ROOT}/scratchpad/{slug}_cinema.mp4"
    render(slug,acc,out)
