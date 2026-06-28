#!/usr/bin/env python3
# 9:16 (1080x1920) page for the 3D-Vertex carousels. Reuses the EXISTING 3D model images
# (no Vertex regen) - crops + alpha-keys + grounds them in a fixed zone, with 1920 chrome.
# Usage: python3 build_3d916.py <model_dir_name> <out_dir_name>   e.g. models operator2_9
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import build_slides as B
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
W,H,MX=1080,1920,90   # left text margin: 90 aligns the text column with the progress bar / 3D zone (was 72, which sat ~16px left of everything else and touched the margin). Propagates to all build_*_3d.py via T.MX.
BG=B.BG; WHITE=B.WHITE; CORAL=B.CORAL; MUTED=B.MUTED; N=B.N
ULOGO="/home/user/tiberiu-claude/content/ultron-logo.png"; GEN=f"{TE}/claude_official.png"
ZONE=(90,888,928,1290)   # legacy default; build() now uses an adaptive zone that fills the band
LOGO3D="/home/user/tiberiu-claude/content/_templates/tiktok/lib/claude-logo-3d-glossy.png"  # cover hero (3D Claude)
CENTER_COVER=False   # new-batch spec: cover title centered in the middle (per-material builder sets True)

def seg_center(d,y,segs,font):   # horizontally-centered segmented line (for centered covers)
    tw=sum(d.textlength(t,font=font) for t,_ in segs); x=(W-tw)//2
    for t,c in segs: d.text((x,y),t,font=font,fill=c); x+=d.textlength(t,font=font)
    return x

def crop_obj(im):
    # FRAME THE WHOLE PANEL (never trim). The Vertex objects are generated complete; the container must show
    # the whole panel. Bound it by its DIFFERENCE FROM ITS OWN CORNER BACKGROUND, taking the most-inclusive
    # bbox that is still the panel (stop before the soft full-frame vignette explodes the box to the frame).
    # The earlier edge/bright crops trimmed soft right/bottom panel edges -> objects looked cut. place_in_zone
    # then scales this WHOLE captured panel to fit the zone, so the element is ALWAYS fully visible.
    a=np.asarray(im.convert("RGB")).astype(int); H,W=a.shape[:2]; area=H*W
    cs=np.concatenate([a[:48,:48].reshape(-1,3),a[:48,-48:].reshape(-1,3),a[-48:,:48].reshape(-1,3),a[-48:,-48:].reshape(-1,3)])
    bg=np.median(cs,0).astype(int); diff=np.abs(a-bg).sum(2); bbox=None
    for thr in (120,100,80,65,52,42,34,28,22):           # high->low: keep the largest bbox that is still panel-sized
        ys,xs=np.where(diff>thr)
        if len(xs)==0: continue
        b=(int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max()))
        if (b[2]-b[0])*(b[3]-b[1])<=0.93*area: bbox=b
        else: break                                      # this threshold caught the vignette -> stop, keep the panel bbox
    if bbox is None: return im.convert("RGBA")
    pad=18; x0=max(0,bbox[0]-pad); y0=max(0,bbox[1]-pad); x1=min(W,bbox[2]+pad); y1=min(H,bbox[3]+pad)
    crop=im.convert("RGB").crop((x0,y0,x1,y1)); c=np.asarray(crop).astype(int); d2=np.abs(c-bg).sum(2)
    alpha=np.clip((d2-16)*18,0,255).astype("uint8")      # key the panel's own bg out -> grounding shadow follows the panel
    return Image.fromarray(np.dstack([np.asarray(crop).astype("uint8"),alpha]),"RGBA")

def place_in_zone(base,el,zone):
    # Center the SOLID PANEL (not the crop, whose shadow margins are uneven) at the canvas X-centre and the
    # zone's Y-centre, identically on every slide -> all 3D elements line up; none sit higher/lower. Scale by
    # the panel bbox so the panel (not its margins) fills the zone.
    zx0,zy0,zx1,zy1=zone; pad=6; zw,zh=zx1-zx0-2*pad, zy1-zy0-2*pad
    solid=el.split()[3].point(lambda v:255 if v>140 else 0); pb=solid.getbbox() or (0,0,el.width,el.height)
    pw,ph=max(1,pb[2]-pb[0]),max(1,pb[3]-pb[1]); r=min(zw/pw, zh/ph)
    nw,nh=max(1,int(el.width*r)),max(1,int(el.height*r)); el=el.resize((nw,nh),Image.LANCZOS)
    solid=el.split()[3].point(lambda v:255 if v>140 else 0); pb=solid.getbbox() or (0,0,nw,nh)
    pcx=(pb[0]+pb[2])/2; pcy=(pb[1]+pb[3])/2
    cx=W//2; cy=(zy0+zy1)//2                       # canvas X-centre, zone Y-centre: same for every slide
    ox=int(round(cx-pcx)); oy=int(round(cy-pcy))
    al=el.split()[3]; shmask=Image.new("L",base.size,0); shmask.paste(al,(ox,oy+30))
    shmask=shmask.filter(ImageFilter.GaussianBlur(42)).point(lambda v:int(v*0.5))
    base.alpha_composite(Image.merge("RGBA",(Image.new("L",base.size,0),)*3+(shmask,)))
    base.alpha_composite(el,(ox,oy))

def ghost(base,num):                                  # SMALL top-right corner watermark; sits ABOVE the headline so titles never touch it
    f=B.dm(900,150); layer=Image.new("RGBA",(W,H),(0,0,0,0)); dl=ImageDraw.Draw(layer)
    tw=dl.textlength(num,font=f); dl.text((922-tw,298),num,font=f,fill=(54,53,50,255))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(4)))

def progress(d,page,n):
    x0,x1=90,928; y=1352; h=7                          # inside the cross-channel band (y<1450, x<930)
    d.rounded_rectangle([x0,y,x1,y+h],radius=4,fill=B.TRACK)
    d.rounded_rectangle([x0,y,x0+int((x1-x0)*page/n),y+h],radius=4,fill=CORAL)
    # page-number label removed (the corner watermark already shows it) - bar only

def footer(base,page,n):
    d=ImageDraw.Draw(base); lg=Image.open(ULOGO).convert("RGBA"); lg.thumbnail((50,50),Image.LANCZOS)
    base.alpha_composite(lg,(90,1330)); f=B.mono(30); d.text((154,1340),"51ultron.com",font=f,fill=CORAL)

def swipe(base):
    bw,bh=252,78; bx=(W-bw)//2; by=1360                # lower so it clears the cover logo (still inside the band)
    sh=Image.new("RGBA",(bw+60,bh+60),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([30,34,30+bw,34+bh],radius=bh//2,fill=(200,100,63,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(15)),(bx-30,by-30))
    btn=Image.new("RGBA",(bw,bh),(0,0,0,0)); ImageDraw.Draw(btn).rounded_rectangle([0,0,bw-1,bh-1],radius=bh//2,fill=(200,100,63,255))
    base.alpha_composite(btn,(bx,by)); d=ImageDraw.Draw(base); f=B.dm(800,37)
    lbl="Swipe"; lw=d.textlength(lbl,font=f); gap=16; aw=32; tx=bx+(bw-(lw+gap+aw))/2; ty=by+(bh-44)/2
    d.text((tx,ty),lbl,font=f,fill=WHITE); ay=by+bh/2; ax0=tx+lw+gap; ax1=ax0+aw
    d.line([(ax0,ay),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay-11),(ax1,ay)],fill=WHITE,width=5); d.line([(ax1-12,ay+11),(ax1,ay)],fill=WHITE,width=5)

def cover_logo(base):
    mk=Image.open(GEN).convert("RGBA"); mk.thumbnail((150,150),Image.LANCZOS); base.alpha_composite(mk,(MX,340))

def build(n,MF,OUT,transparent=False):
    s=B.SPECS[n]; base=Image.new("RGBA",(W,H),(0,0,0,0) if transparent else BG+(255,)); d=ImageDraw.Draw(base)
    cover=s["role"]=="cover"; last=s["role"]=="last"
    if not transparent: ghost(base,s["num"])              # corner watermark (skipped for the IG overlay cover)
    if cover and CENTER_COVER and not transparent:        # normal (opaque) TikTok cover: hook centered on top, 3D Claude mark BELOW it, no eyebrow/sub
        y=700; hf=B.dm(900,84); lh=96
        for line in s["head"]: seg_center(d,y,line,hf); y+=lh   # hook centered, no eyebrow / no sub-hook
        place_in_zone(base,crop_obj(Image.open(LOGO3D)),(380,910,700,1250))   # logos BELOW the hook
        swipe(base)
        o=f"{OUT}/s{n}.png"; base.convert("RGB").save(o); return o
    # --- text block at the top of the safe band (clears the watermark) ---
    # FIXED positions on EVERY slide so the 0.5s reel-flip has no visual jump:
    # eyebrow at 476, headline at 540 (size 84, 2 lines), 3D element zone top at 758.
    if s.get("eyebrow"): B.ls_text(d,(MX,476),s["eyebrow"],B.mono(28),CORAL,4)
    y=540; hf=B.dm(900,84); lh=96
    for line in s["head"]: B.seg_line(d,MX,y,line,hf); y+=lh
    elt_bottom=1238 if last else 1326   # only the thin progress bar sits below now
    src=LOGO3D if cover else f"{MF}/m{n}.png"
    place_in_zone(base,crop_obj(Image.open(src)),(88,758,942,elt_bottom))  # wider band -> bigger element
    # --- chrome ---
    if cover:
        if not transparent: swipe(base)                   # IG overlay cover: no swipe (sits over a video)
    elif last:
        d.text((MX,1258),"Follow for one AI system for founders every day.",font=B.dm(700,29),fill=WHITE)
        footer(base,n,N)
    else: progress(d,n,N)
    o=f"{OUT}/s{n}.png"; (base if transparent else base.convert("RGB")).save(o); return o

if __name__=="__main__":
    md=sys.argv[1]; od=sys.argv[2]; MF=f"{TE}/roll3/{md}"; OUT=f"{TE}/roll3/{od}"; os.makedirs(OUT,exist_ok=True)
    for n in range(1,N+1): build(n,MF,OUT); print("built",n)
    ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
    cols=4;rows=2;sc=300;sh=int(sc*H/W)
    st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
    for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
    st.save(f"{TE}/{od}_montage.png"); print("montage",od)
