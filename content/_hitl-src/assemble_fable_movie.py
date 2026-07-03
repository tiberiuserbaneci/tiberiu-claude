#!/usr/bin/env python3
# Cut the 3 Veo clips into ONE "Claude Fable 5 in action" movie: logo -> code -> DONE.
# Hard cuts on beat, NO LOOP, >=12.8s of UNIQUE footage. Uses only the CLEAN early part of each clip
# (Veo drifts text after ~4s, so B is trimmed short). Upscaled to 1080x1920 for the reel.
import subprocess, imageio_ffmpeg, os
SP="/home/user/tiberiu-claude/scratchpad/covers"; FF=imageio_ffmpeg.get_ffmpeg_exe()
# (clip, start, dur) -- CLEAN windows only (Veo drifts text late; stable push-in B/C hold ~4s).
# total = 5.0+4.0+4.0 = 13.0s (>=12.8, no loop). Narrative: logo hero -> code writing -> DONE.
SEG=[("veoA.mp4",0.0,5.0),("veoB.mp4",0.0,4.0),("veoC.mp4",0.0,4.0)]
parts=[]
for i,(clip,ss,dur) in enumerate(SEG):
    o=f"{SP}/_seg{i}.mp4"
    subprocess.run([FF,"-y","-ss",str(ss),"-i",f"{SP}/{clip}","-t",str(dur),
        "-vf","scale=1080:1920:flags=lanczos:force_original_aspect_ratio=increase,crop=1080:1920,fps=30",
        "-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","17",o],capture_output=True)
    parts.append(o)
lst=f"{SP}/_concat.txt"; open(lst,"w").write("".join(f"file '{p}'\n" for p in parts))
out=f"{SP}/fable_movie.mp4"
subprocess.run([FF,"-y","-f","concat","-safe","0","-i",lst,"-c:v","libx264","-pix_fmt","yuv420p",
    "-crf","17","-map_metadata","-1",out],capture_output=True)
# report duration
import json
pr=subprocess.run([FF,"-i",out],capture_output=True,text=True)
print("built fable_movie.mp4"); print([l for l in pr.stderr.splitlines() if "Duration" in l])
