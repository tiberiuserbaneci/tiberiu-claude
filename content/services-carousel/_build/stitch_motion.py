#!/usr/bin/env python3
# Crossfade the motion frames into a smooth loop; lock the headline (top) and footer (bottom)
# strips from the base slide so text never drifts. Only the mid-band (objects/apps) animates.
import os, sys, glob, subprocess
import numpy as np
from PIL import Image
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()
base=Image.open(sys.argv[1]).convert("RGB").resize((1080,1350),Image.LANCZOS)  # e.g. out/final-2.png
frames=[Image.open(p).convert("RGB").resize((1080,1350),Image.LANCZOS) for p in sorted(sys.argv[3:])]
out=sys.argv[2]
b=np.asarray(base).astype(np.float32)
# lock masks: top headline 0..H*0.24, bottom footer H*0.93..H ; feathered
H,W=1350,1080
mask=np.zeros((H,1),np.float32)
top=int(H*0.24); bot=int(H*0.93); fe=40
mask[:top,0]=1.0
for k in range(fe):
    if top+k<H: mask[top+k,0]=1-k/fe
mask[bot:,0]=1.0
for k in range(fe):
    if bot-k>=0: mask[bot-k,0]=1-k/fe
M=np.repeat(mask,W,axis=1)[:,:,None]
locked=[ (np.asarray(f).astype(np.float32)*(1-M)+b*M) for f in frames]
HOLD=3; XF=19; seq=[]   # less hold, longer crossfade -> more continuous, prominent motion
n=len(locked)
for i in range(n):
    a=locked[i]; nx=locked[(i+1)%n]
    for _ in range(HOLD): seq.append(a)
    for k in range(1,XF+1): t=k/(XF+1); seq.append(a*(1-t)+nx*t)
td="mtmp"; os.makedirs(td,exist_ok=True)
for f in glob.glob(td+"/*.png"): os.remove(f)
for j,fr in enumerate(seq): Image.fromarray(np.clip(fr,0,255).astype('uint8')).save(f"{td}/{j:04d}.png")
subprocess.run([FF,"-y","-framerate","30","-i",f"{td}/%04d.png","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-movflags","+faststart",out],capture_output=True)
print("loop:",len(seq),"frames",round(len(seq)/30,2),"s ->",out,os.path.getsize(out))
