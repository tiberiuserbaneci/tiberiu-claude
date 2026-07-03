#!/usr/bin/env python3
# Convert approved 4:5 (1080x1350) editorial slides to 9:16 (1080x1920) WITHOUT re-tuning the layout:
# place the card centered in the 9:16 band and continue the 44px grid, phased so the seam is invisible.
# Covers handled separately (Veo 9:16 eye frame + centered hook).
import sys, os, subprocess, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter, ImageFont
ROOT="/home/user/tiberiu-claude"; A=f"{ROOT}/content/assets"; SPC=f"{ROOT}/scratchpad/covers"
W,H=1080,1920; CARD_H=1350; OY=(H-CARD_H)//2   # 285: symmetric, content in the safe band
BG=(25,25,25); LIGHT_BG=(246,241,231); ACC=(212,162,127); WHITE=(250,250,247)
def dm(w,s): return ImageFont.truetype(f"{A}/DMSans-{w}.ttf",s)

def grid_canvas(light):
    bg=LIGHT_BG if light else BG
    c=Image.new("RGBA",(W,H),bg+(255,))
    g=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
    col=(23,21,15,26) if light else (250,250,247,18)
    ph=OY%44
    for gy in range(ph,H,44): gd.line([(0,gy),(W,gy)],fill=col,width=1)
    for gx in range(0,W,44): gd.line([(gx,0),(gx,H)],fill=col,width=1)
    c.alpha_composite(g); return c

def convert_slide(path):
    card=Image.open(path).convert("RGBA")
    if card.size!=(W,CARD_H): return False
    px=card.getpixel((6,6)); light=(sum(px[:3])/3)>128
    canvas=grid_canvas(light)
    canvas.alpha_composite(card,(0,OY))
    canvas.convert("RGB").save(path); return True

def veo_frame():
    ff=imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run([ff,"-y","-ss","4","-i",f"{SPC}/eye_motion_v3.mp4","-frames:v","1",
        "-vf","scale=1080:1920:flags=lanczos",f"{SPC}/veo_frame_916.png"],capture_output=True)
    return f"{SPC}/veo_frame_916.png"

def tt_cover(out):
    # opaque 9:16 TikTok cover: Veo eye frame + the centered 2-line hook overlay (same as the IG reel)
    base=Image.open(veo_frame()).convert("RGBA")
    ov=Image.open(f"{SPC}/overlay_ig_9x16.png").convert("RGBA")
    base.alpha_composite(ov); base.convert("RGB").save(out); print("tt 9:16 cover built")

if __name__=="__main__":
    tt=f"{ROOT}/scratchpad/eyes_tt"; ig=f"{ROOT}/scratchpad/eyes_ig"
    # content + close slides -> 9:16 (skip cover s1 in both)
    for d in (tt,ig):
        for f in sorted(os.listdir(d)):
            if not (f.startswith("s") and f.endswith(".png")): continue
            if f=="s1.png": continue
            ok=convert_slide(os.path.join(d,f)); print(d.split('/')[-1],f,"->",ok)
    tt_cover(f"{tt}/s1.png")     # TikTok cover = opaque 9:16 eye+hook
    # IG s1 stays the reel video (handled by put_ig_reel); the s1.png here is unused for the vault
    print("done")
