#!/usr/bin/env python3
# Full services carousel reel: Vertex slides + additive motion + Studio-Q voice + captions, stitched.
import os, json, base64, subprocess, re
import requests, imageio_ffmpeg
from build_slide import build

FF=imageio_ffmpeg.get_ffmpeg_exe()
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
ANIM="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/anim"
TOK=open(f"{TE}/gcp_token.txt").read().strip(); PROJ="project-c28b1276-8b53-430a-a7a"; CA="/root/.ccr/ca-bundle.crt"
VOICE="en-US-Studio-Q"
os.makedirs(f"{TE}/voice",exist_ok=True)

SLIDES=[
  dict(png="serviceinfo-45-1.png", mode="static", swipe=1,
       vo="You run every service in your business by hand. Ultron runs them for you.",
       caps=[]),
  dict(png="serviceinfo-45-2.png", mode="motion", swipe=1,
       vo="Chasing overdue invoices used to eat my week. Now Ultron pulls the aging report, drafts a reminder for every client, and waits before it ever charges a late fee.",
       caps=[("Overdue invoices ate my week",0.03,0.33),("Ultron [chases every one]",0.36,0.65),("It [waits] before the late fee",0.68,0.99)]),
  dict(png="serviceinfo-45-3.png", mode="motion", swipe=1,
       vo="After every call I used to rebuild the proposal from scratch. Now Ultron pulls the notes, drafts the scope, builds the quote, and holds it until I say send.",
       caps=[("Rebuilding proposals by hand",0.03,0.31),("Ultron [writes the proposal]",0.35,0.63),("It [holds] until you say send",0.67,0.99)]),
  dict(png="serviceinfo-45-4.png", mode="motion", swipe=1,
       vo="The support inbox never emptied on its own. Ultron reads every open ticket, drafts each reply, pulls the order status, and stops before it issues a single refund.",
       caps=[("The inbox never emptied",0.03,0.30),("Ultron [clears every ticket]",0.34,0.62),("It [stops] before any refund",0.66,0.99)]),
  dict(png="serviceinfo-45-5.png", mode="static", swipe=0,
       vo="One ask, and every service runs. Comment SERVICES, and I will send you the playbook.",
       caps=[("One ask. [Every service runs]",0.04,0.5),("Comment [SERVICES]",0.54,0.97)]),
]

def synth(text,out):
    H={"Authorization":f"Bearer {TOK}","Content-Type":"application/json","x-goog-user-project":PROJ}
    body={"input":{"text":text},"voice":{"languageCode":"en-US","name":VOICE},
          "audioConfig":{"audioEncoding":"MP3","speakingRate":1.02,"pitch":-1.0}}
    r=requests.post("https://texttospeech.googleapis.com/v1/text:synthesize",headers=H,data=json.dumps(body),verify=CA,timeout=90)
    if r.status_code!=200: raise SystemExit(f"TTS {r.status_code}: {r.text[:200]}")
    open(out,"wb").write(base64.b64decode(r.json()["audioContent"])); return os.path.getsize(out)

def dur_of(p):
    o=subprocess.run([FF,"-i",p],capture_output=True,text=True).stderr
    m=re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)",o); h,mi,s=m.groups()
    return int(h)*3600+int(mi)*60+float(s)

# PHASE 1: synth all VO (one token pass), measure durations
print("== PHASE 1: voice ==")
for i,s in enumerate(SLIDES):
    s["vofile"]=f"{TE}/voice/v{i+1}.mp3"
    print(f"  synth {i+1}:", synth(s["vo"],s["vofile"]),"bytes")
    s["dvo"]=dur_of(s["vofile"]); print(f"    dur {s['dvo']:.2f}s")

# PHASE 2: build clips (no token needed)
print("== PHASE 2: clips ==")
clips=[]
for i,s in enumerate(SLIDES):
    tail=0.75 if s["mode"]=="motion" else 0.55
    vdur=round(s["dvo"]+tail,2)
    caps=[{"t":t,"s":round(a*s["dvo"],2),"e":round(b*s["dvo"],2)} for (t,a,b) in s["caps"]]
    mp4=f"{ANIM}/clip{i+1}.mp4"
    build(f"{TE}/out/{s['png']}",mp4,vdur,s["mode"],bool(s["swipe"]),caps)
    apad=f"{ANIM}/a{i+1}.m4a"
    subprocess.run([FF,"-y","-i",s["vofile"],"-af","apad","-t",f"{vdur:.2f}","-c:a","aac","-b:a","160k",apad],capture_output=True)
    voiced=f"{ANIM}/v{i+1}.mp4"
    subprocess.run([FF,"-y","-i",mp4,"-i",apad,"-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-shortest",voiced],capture_output=True)
    clips.append(voiced); print(f"  clip {i+1}: vdur {vdur}s  size {os.path.getsize(voiced)}")

# PHASE 3: concat (re-encode for safe timestamps) + strip metadata
print("== PHASE 3: stitch ==")
lst=f"{ANIM}/concat.txt"; open(lst,"w").write("".join(f"file '{c}'\n" for c in clips))
final=f"{ANIM}/services-carousel-45.mp4"
subprocess.run([FF,"-y","-f","concat","-safe","0","-i",lst,
                "-fflags","+bitexact","-flags:v","+bitexact","-flags:a","+bitexact",
                "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-r","30",
                "-c:a","aac","-b:a","160k","-map_metadata","-1","-movflags","+faststart",final],capture_output=True)
print("FINAL",final,f"{dur_of(final):.2f}s",os.path.getsize(final),"bytes")
