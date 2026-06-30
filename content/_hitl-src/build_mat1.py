#!/usr/bin/env python3
# START YOUR COMPANY TONIGHT - NORMAL Vertex GTM dashboards (no phone), TikTok+IG (deck_poll)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
import numpy as np
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
# Fixed panel box: every dashboard at the SAME size + position (no per-slide jitter)
PBW,PBH,PX,PY=820,1044,130,486
def fixed_panel(objpath):
    im=Image.open(objpath).convert("RGB"); a=np.asarray(im).astype(int)
    diff=np.abs(a-np.array([25,25,25])).sum(2); ys,xs=np.where(diff>40)
    x0,y0,x1,y1=int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())
    pan=im.crop((x0,y0,x1,y1)); pw,ph=pan.size; tar=PBW/PBH
    if pw/ph>tar:  # too wide -> crop sides
        nw=int(ph*tar); pan=pan.crop(((pw-nw)//2,0,(pw-nw)//2+nw,ph))
    else:          # too tall -> crop top/bottom
        nh=int(pw/tar); pan=pan.crop((0,(ph-nh)//2,pw,(ph-nh)//2+nh))
    return pan.resize((PBW,PBH),Image.LANCZOS)
T2.COVER=dict(head=[[wo("Start your company")],[co("tonight.")]])
T2.CONTENT=[
  ("LEADS", [[wo("Find your")],[co("first buyers.")]], f"{D}/m1b_01.png", 1.0),
  ("OUTREACH", [[wo("Reach them")],[co("at scale.")]], f"{D}/m1b_02.png", 1.0),
  ("PIPELINE", [[wo("Track every")],[co("deal.")]], f"{D}/m1b_03.png", 1.0),
  ("CALLS", [[wo("Book the")],[co("calls.")]], f"{D}/m1b_04.png", 1.0),
  ("PROJECTS", [[wo("Run the whole")],[co("company.")]], f"{D}/m1b_05.png", 1.0),
  ("PAYMENTS", [[wo("Get")],[co("paid.")]], f"{D}/m1b_06.png", 1.0),
  ("STACK", [[wo("One chat")],[co("runs it all.")]], f"{D}/m1b_07.png", 1.0),
  ("ULTRON", [[wo("No team.")],[co("Just you and one chat.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this for",l2="the day you start.",q="Which tool are you wiring first?")
MX=T2.MX
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    if last:
        T2.ls_text(d,(MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
        s=T2.fit_hook(d,head,T2.W-2*MX,start=84,floor=58); hf=T2.dm(900,s); y=534
        for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (130,720,950,1245), fill=fill)
        _ft=(T2.save_foot() if getattr(T2,"_TT",False) else "Follow for one AI system for founders every day.")
        d.text((MX,1262),_ft,font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
        return
    T2.ls_text(d,(MX,300),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*MX,start=64,floor=44),56); hf=T2.dm(900,s); y=340
    for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    # dashboards: fixed box + fixed position (no jitter); other objects: place_in_zone
    if "models_dash" in objpath:
        base.alpha_composite(fixed_panel(objpath).convert("RGBA"),(PX,PY))
    else:
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (130,492,950,1560), fill=1.0)
    x0,x1=90,928; yb=1576; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat1_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat1_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat1_tt","mat1_tt",a); T2.montage(f"{T2.OUTBASE}/mat1_ig","mat1_ig",b)
    print("tt",a,"ig",b)
