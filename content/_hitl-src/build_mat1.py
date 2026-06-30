#!/usr/bin/env python3
# START YOUR COMPANY TONIGHT - NORMAL Vertex GTM dashboards (no phone), TikTok+IG (deck_poll)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Start your company")],[co("tonight.")]])
T2.CONTENT=[
  ("LIVE", [[wo("A whole company,")],[co("running tonight.")]], f"{D}/m1_01.png", 1.0),
  ("LEADS", [[wo("It finds your")],[co("first buyers.")]], f"{D}/m1_02.png", 1.0),
  ("OUTREACH", [[wo("It writes")],[co("every message.")]], f"{D}/m1_03.png", 1.0),
  ("UNITS", [[wo("Seven units,")],[co("one operator.")]], f"{D}/m1_04.png", 1.0),
  ("PROJECTS", [[wo("Every workstream,")],[co("one place.")]], f"{D}/m1_05.png", 1.0),
  ("MEMORY", [[wo("It remembers")],[co("everything.")]], f"{D}/m1_06.png", 1.0),
  ("STACK", [[wo("Your whole stack,")],[co("connected.")]], f"{D}/m1_07.png", 1.0),
  ("ULTRON", [[wo("No team.")],[co("Just you and one chat.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
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
    # NORMAL dashboard: native aspect, uniform scale (no distortion, sphere stays circular)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (130,492,950,1560), fill=1.0)
    x0,x1=90,928; yb=1576; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck_poll(f"{T2.OUTBASE}/mat1_tt",False); b=T2.deck_poll(f"{T2.OUTBASE}/mat1_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat1_tt","mat1_tt",a); T2.montage(f"{T2.OUTBASE}/mat1_ig","mat1_ig",b)
    print("tt",a,"ig",b)
