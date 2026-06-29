#!/usr/bin/env python3
# I RUN IT FROM MY PHONE - v2 (TikTok second account). Same theme, structurally DIFFERENT from v1:
# full-bleed real app section (no phone frame) with hook overlay. Reuses the real captures (cheap).
import importlib.util, os
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw, ImageFilter
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
SRC="/home/user/tiberiu-claude/scratchpad"
# (eyebrow, [line1,line2], section_capture, crop_top)
COVER=[[wo("One chat.")],[co("It runs the company.")]]
SECT=[
 ("CHAT",     [[wo("It starts with one line.")]],     "mob_home", 0),
 ("LIVE",     [[wo("A whole team, running live.")]],   "mob_jobs", 0),
 ("DEALS",    [[wo("Agents work the deals.")]],        "h_deals", 150),
 ("SKILLS",   [[wo("Seven units. One operator.")]],    "h_skills", 150),
 ("MEMORY",   [[wo("It remembers everything.")]],      "h_brain", 150),
 ("PROJECTS", [[wo("Every project, one place.")]],     "h_projects", 150),
 ("STACK",    [[wo("One subscription. Whole stack.")]],"h_stack", 150),
 ("ULTRON",   [[wo("One operator. In your pocket.")]], None, 0),
]
CTA=("RUN ON ONE",[[wo("Run on one,")],[co("comment OPERATOR.")]], f"{T2.LIB}/cta3d-operator.png")
W,H,MX=T2.W,T2.H,T2.MX

def bleed(base, eyebrow, head, cap, crop_top, page, n):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    # full-bleed section screenshot in the visible band
    bx0,by0,bx1,by1=70,560,1010,1330
    img=Image.open(f"{SRC}/{cap}.png").convert("RGB")
    if crop_top: img=img.crop((0,crop_top,img.width,img.height))
    tw=bx1-bx0; th=by1-by0
    r=max(tw/img.width, th/img.height)*0.0+tw/img.width  # fit width
    img=img.resize((tw,int(img.height*tw/img.width)),Image.LANCZOS)
    img=img.crop((0,0,tw,min(th,img.height)))
    rad=40; m=Image.new("L",img.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,img.width-1,img.height-1],radius=rad,fill=255)
    # shadow
    sh=Image.new("RGBA",base.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle([bx0,by0+10,bx0+img.width,by0+img.height+10],radius=rad,fill=(0,0,0,150))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(28)))
    base.paste(img,(bx0,by0),m)
    ImageDraw.Draw(base).rounded_rectangle([bx0,by0,bx0+img.width-1,by0+img.height-1],radius=rad,outline=(70,70,66),width=2)
    # eyebrow + hook ABOVE the screenshot
    T2.ls_text(d,(MX,360),eyebrow,T2.mono(28),T2.CORAL,4)
    s=T2.fit_hook(d,head,W-2*MX,start=70,floor=46); hf=T2.dm(900,s); y=420
    for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    T2.progress(d,page,n)

def deck(outdir, overlay):
    os.makedirs(outdir,exist_ok=True)
    T2.COVER=dict(head=COVER)
    n=len(SECT)+2
    # cover
    if overlay: T2.cover_ig(f"{outdir}/s1.png")
    else:
        base=Image.new("RGBA",(W,H),T2.BG+(255,)); T2.cover_tt(base,n); base.convert("RGB").save(f"{outdir}/s1.png")
    # content
    for i,(eb,head,cap,ct) in enumerate(SECT,2):
        base=Image.new("RGBA",(W,H),T2.BG+(255,))
        if cap is None:
            T2.body_slide(base, eb, head, f"{T2.OBJ}/models_rival2/ultron_login.png", i, n, fill=0.98)
        else:
            bleed(base, eb, head, cap, ct, i, n)
        base.convert("RGB").save(f"{outdir}/s{i}.png")
    # CTA
    base=Image.new("RGBA",(W,H),T2.BG+(255,)); T2.body_slide(base, CTA[0], CTA[1], CTA[2], n, n, last=True, fill=0.92)
    base.convert("RGB").save(f"{outdir}/s{n}.png")
    return n

if __name__=="__main__":
    a=deck(f"{T2.OUTBASE}/phv2_tt",False); b=deck(f"{T2.OUTBASE}/phv2_ig",True)
    T2.montage(f"{T2.OUTBASE}/phv2_tt","phv2_tt",a); T2.montage(f"{T2.OUTBASE}/phv2_ig","phv2_ig",b)
    print("tt",a,"ig",b)
