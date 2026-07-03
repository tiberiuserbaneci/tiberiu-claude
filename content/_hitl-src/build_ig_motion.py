#!/usr/bin/env python3
# Build the 9:16 IG reel intro: burn hook + marks overlay onto the Veo eye motion.
import os, subprocess, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT="/home/user/tiberiu-claude"; SP=f"{ROOT}/scratchpad/covers"; A=f"{ROOT}/content/assets"
W,H=1080,1920; ACC=(212,162,127); WHITE=(250,250,247)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)
def mono(s): return ImageFont.truetype(f"{A}/DMMono-500.ttf",s)

ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
# hook ONLY (operator: no eyebrow chip, no logos), 2 lines, centered on the middle of the frame
l1="Your AI is blind by default."; l2="Wire its eyes."
def fit(line,start,floor):
    s=start
    while s>floor and d.textlength(line,font=dm(900,s))>W-120: s-=2
    return s
s1=fit(l1,78,46); f1=dm(900,s1); f2=dm(900,s1)
lh=int(s1*1.16); total=lh*2; y0=H//2-total//2
# soft scrim behind the block for legibility over the moving eye
mw=max(d.textlength(l1,font=f1),d.textlength(l2,font=f2))
scrim=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(scrim)
sd.rounded_rectangle([(W-mw)/2-70,y0-50,(W+mw)/2+70,y0+total+40],radius=60,fill=(10,9,8,160))
scrim=scrim.filter(ImageFilter.GaussianBlur(34)); ov.alpha_composite(scrim)
d=ImageDraw.Draw(ov)
y=y0
for line,font,col in [(l1,f1,WHITE),(l2,f2,ACC)]:
    w=d.textlength(line,font=font); d.text(((W-w)/2,y),line,font=font,fill=col); y+=lh
ov.save(f"{SP}/overlay_ig_9x16.png"); print("overlay built s1=",s1)

# --- burn overlay onto the (upscaled) video, keep audio ---
ff=imageio_ffmpeg.get_ffmpeg_exe()
cmd=[ff,"-y","-i",f"{SP}/eye_motion_v3.mp4","-i",f"{SP}/overlay_ig_9x16.png",
     "-filter_complex","[0:v]scale=1080:1920:flags=lanczos[bg];[bg][1:v]overlay=0:0:format=auto",
     "-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-preset","medium","-c:a","copy",
     f"{SP}/ig_reel_intro.mp4"]
r=subprocess.run(cmd,capture_output=True,text=True)
print("ffmpeg rc",r.returncode)
if r.returncode!=0: print(r.stderr[-1200:])
else: print("saved ig_reel_intro.mp4", os.path.getsize(f"{SP}/ig_reel_intro.mp4"),"bytes")
