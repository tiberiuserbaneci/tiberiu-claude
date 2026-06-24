#!/usr/bin/env python3
# Assemble the 4:5 full-bleed Instagram movie: cover+CTA static, service slides animated (loops),
# Andrew Dragon voice + karaoke captions. No 9:16, no swipe. Run after mf2/mf3/mf4 frames exist.
import os, sys, base64, glob, subprocess, json, re
import numpy as np
from PIL import Image
import imageio_ffmpeg, requests
from playwright.sync_api import sync_playwright
FF=imageio_ffmpeg.get_ffmpeg_exe()
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
CA="/root/.ccr/ca-bundle.crt"; sans=base64.b64encode(open(f"{TE}/DMSans-VF.ttf","rb").read()).decode()
CW,CH=1080,1350; LEAD=0.6; CAP_BOTTOM=150; VOICE="en-US-Andrew:DragonHDLatestNeural"
SLIDES=[
 (1,"static","You run every service in your business by hand. Ultron runs them for you."),
 (2,"anim","Chasing overdue invoices used to eat my week. Now Ultron pulls the aging report, drafts a reminder for every client, and waits before it ever charges a late fee."),
 (3,"anim","After every call I used to rebuild the proposal from scratch. Now Ultron pulls the notes, drafts the scope, builds the quote, and holds it until I say send."),
 (4,"anim","The support inbox never emptied on its own. Ultron reads every open ticket, drafts each reply, pulls the order status, and stops before it issues a single refund."),
 (5,"static","One ask, and every service runs. Comment SERVICES, and I will send you the playbook."),
]
def synth(t,out):
    r=requests.post("https://edits.51ultron.com/api/tts",headers={"Content-Type":"application/json"},
        data=json.dumps({"text":t,"voice":VOICE,"rate":1.0}),verify=CA,timeout=90)
    if r.status_code!=200: raise SystemExit(f"TTS {r.status_code} {r.text[:160]}")
    open(out,"wb").write(r.content)
def dur_of(p):
    o=subprocess.run([FF,"-i",p],capture_output=True,text=True).stderr
    m=re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)",o); h,mi,s=m.groups(); return int(h)*3600+int(mi)*60+float(s)
def loop_for(n):
    base=f"{TE}/out/final-{n}.png"
    frames=sorted(glob.glob(f"{TE}/mf{n}b/f*.png")) or sorted(glob.glob(f"{TE}/mf{n}/f*.png"))
    out=f"{TE}/loop45-{n}.mp4"
    subprocess.run(["python3",f"{TE}/stitch_motion.py",base,out]+frames,capture_output=True)
    return out
def word_times(vo,dur,onset=0.12):
    raw=vo.split()
    def wt(w):
        b=len(w.strip(".,!?;:"))+1.0
        return b+(2.6 if w.endswith(('.','!','?')) else 1.3 if w.endswith((',',';',':')) else 0)
    ws=[wt(w) for w in raw]; tot=sum(ws); sp=max(.1,dur-onset-.15); t=onset; st=[]
    for w in ws: st.append(t); t+=(w/tot)*sp
    return raw,st
def chunks(raw,st):
    out=[];cur=[]
    for i,w in enumerate(raw):
        cur.append((w,st[i]))
        if w.endswith(('.','!','?',',',';',':')) or len(cur)>=4: out.append(cur);cur=[]
    if cur:out.append(cur)
    return out
def segment(design,isv,vo,dur,out):
    raw,st=word_times(vo,dur); chs=chunks(raw,st); cap=""
    for idx,ch in enumerate(chs):
        cs=ch[0][1]-0.10; ce=(chs[idx+1][0][1]-0.12) if idx+1<len(chs) else dur-0.05
        sp="".join(f'<span class="kw" style="animation-delay:{t+LEAD:.2f}s">{w}</span> ' for w,t in ch)
        cap+=f'<div class="cap" style="animation:capin .22s ease forwards {cs+LEAD:.2f}s,capout .22s ease forwards {ce+LEAD:.2f}s">{sp}</div>'
    media=(f'<video class="bg" src="file://{design}" autoplay loop muted playsinline></video>' if isv
           else f'<img class="bg" src="data:image/png;base64,{base64.b64encode(open(design,"rb").read()).decode()}">')
    HTML=f"""<!doctype html><html><head><meta charset=utf8><style>
@font-face{{font-family:S;src:url(data:font/ttf;base64,{sans}) format('truetype');font-weight:100 1000}}
*{{margin:0;padding:0;box-sizing:border-box}}
.cv{{width:{CW}px;height:{CH}px;position:relative;overflow:hidden;background:#f3ebdf}}
.bg{{position:absolute;inset:0;width:{CW}px;height:{CH}px;object-fit:cover}}
.cap{{position:absolute;z-index:7;left:50%;bottom:{CAP_BOTTOM}px;transform:translateX(-50%);opacity:0;
   max-width:{CW-120}px;padding:14px 26px;border-radius:14px;background:rgba(20,16,12,.80);text-align:center;white-space:nowrap}}
.kw{{font-family:S;font-weight:800;font-size:36px;line-height:1.2;color:#fff;opacity:.42;margin:0 .14em}}
.cap .kw{{animation:kw .45s ease forwards}}
@keyframes kw{{0%{{opacity:.42;color:#fff}}40%{{opacity:1;color:#ff7a45}}100%{{opacity:1;color:#fff}}}}
@keyframes capin{{from{{opacity:0;transform:translate(-50%,12px)}}to{{opacity:1;transform:translate(-50%,0)}}}}
@keyframes capout{{to{{opacity:0}}}}
</style></head><body><div class="cv">{media}{cap}</div></body></html>"""
    hp=f"{TE}/_seg45.html"; open(hp,"w").write(HTML); vid=f"{TE}/_segv"; os.makedirs(vid,exist_ok=True)
    for f in glob.glob(vid+"/*.webm"): os.remove(f)
    with sync_playwright() as p:
        br=p.chromium.launch(args=["--force-color-profile=srgb","--autoplay-policy=no-user-gesture-required"])
        ctx=br.new_context(viewport={"width":CW,"height":CH},record_video_dir=vid,record_video_size={"width":CW,"height":CH})
        pg=ctx.new_page(); pg.goto(f"file://{hp}",wait_until="load")
        try: pg.eval_on_selector("video","v=>{v.muted=true;v.play()}")
        except: pass
        pg.wait_for_timeout(int((dur+LEAD)*1000)+300); ctx.close(); br.close()
    webm=glob.glob(vid+"/*.webm")[0]
    subprocess.run([FF,"-y","-i",webm,"-ss",f"{LEAD:.2f}","-t",f"{dur:.2f}","-vf",f"scale={CW}:{CH}:flags=lanczos,fps=30",
                    "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-movflags","+faststart",out],capture_output=True)
if __name__=="__main__":
    only=int(sys.argv[1]) if len(sys.argv)>1 else 0
    clips=[]
    for n,mode,vo in SLIDES:
        if only and n!=only: continue
        vof=f"{TE}/voice/and{n}.mp3"; synth(vo,vof); dvo=dur_of(vof); dur=round(dvo+(0.6 if mode=="anim" else 0.45),2)
        design=loop_for(n) if mode=="anim" else f"{TE}/out/final-{n}.png"
        seg=f"{TE}/seg45-{n}.mp4"; segment(design,mode=="anim",vo,dur,seg)
        ap=f"{TE}/a45-{n}.m4a"; subprocess.run([FF,"-y","-i",vof,"-af","apad","-t",f"{dur:.2f}","-c:a","aac","-b:a","160k",ap],capture_output=True)
        vd=f"{TE}/v45-{n}.mp4"; subprocess.run([FF,"-y","-i",seg,"-i",ap,"-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-shortest",vd],capture_output=True)
        clips.append(vd); print(f"slide {n} dur {dur}")
    if not only:
        lst=f"{TE}/m45.txt"; open(lst,"w").write("".join(f"file '{c}'\n" for c in clips))
        out=f"{TE}/services-movie-45.mp4"
        subprocess.run([FF,"-y","-f","concat","-safe","0","-i",lst,"-fflags","+bitexact","-flags:v","+bitexact","-flags:a","+bitexact",
                        "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-r","30","-c:a","aac","-b:a","160k",
                        "-map_metadata","-1","-movflags","+faststart",out],capture_output=True)
        print("MOVIE",out,f"{dur_of(out):.2f}s",os.path.getsize(out))
