#!/usr/bin/env python3
# YOUR FIRST PAYING CUSTOMER - NORMAL Vertex GTM dashboards (no phone), TikTok+IG (deck_poll)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Your first")],[co("paying customer.")]])
T2.CONTENT=[
  ("LEADS", [[wo("It builds")],[co("the list.")]], f"{D}/m2_01.png", 1.0),
  ("OUTREACH", [[wo("It writes")],[co("every message.")]], f"{D}/m2_02.png", 1.0),
  ("FOLLOW-UP", [[wo("It follows up")],[co("until they reply.")]], f"{D}/m2_03.png", 1.0),
  ("PIPELINE", [[wo("Every deal,")],[co("one view.")]], f"{D}/m2_04.png", 1.0),
  ("BOOKED", [[wo("It books")],[co("the call.")]], f"{D}/m2_05.png", 1.0),
  ("UNITS", [[wo("A sales team")],[co("of one.")]], f"{D}/m2_06.png", 1.0),
  ("STACK", [[wo("Wired to")],[co("your tools.")]], f"{D}/m2_07.png", 1.0),
  ("ULTRON", [[wo("Your first customer,")],[co("closed.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
MX=T2.MX
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    if last:
        T2.ls_text(d,(MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
        s=T2.fit_hook(d,head,T2.W-2*MX,start=84,floor=58); hf=T2.dm(900,s); y=534
        for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.14)
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (50,720,1030,1245), fill=fill)
        _ft=(T2.save_foot() if getattr(T2,"_TT",False) else "Follow for one AI system for founders every day.")
        d.text((MX,1262),_ft,font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
        return
    T2.ls_text(d,(MX,300),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*MX,start=64,floor=44),56); hf=T2.dm(900,s); y=340
    for ln in head: T2.seg_line(d,MX,y,ln,hf); y+=int(s*1.12)
    # NORMAL dashboard: native aspect, uniform scale (no distortion, sphere stays circular)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (40,492,1040,1560), fill=1.0)
    x0,x1=90,928; yb=1576; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck_poll(f"{T2.OUTBASE}/mat2_tt",False); b=T2.deck_poll(f"{T2.OUTBASE}/mat2_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat2_tt",f"mat2_tt",a); T2.montage(f"{T2.OUTBASE}/mat2_ig",f"mat2_ig",b)
    print("tt",a,"ig",b)
