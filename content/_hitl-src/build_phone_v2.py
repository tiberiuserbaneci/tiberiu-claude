#!/usr/bin/env python3
# FROM MY PHONE v2
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{T2.OBJ}/models_phone"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("One chat.")],[co("One operator.")]])
T2.CONTENT=[
  ("MEMORY", [[wo("It never")],[co("forgets.")]], f"{PH}/p2_brain.png", 1.0),
  ("COMPUTER", [[wo("It runs")],[co("its own computer.")]], f"{PH}/p2_computer.png", 1.0),
  ("EVERYTHING", [[wo("Everything,")],[co("already built.")]], f"{PH}/p2_everything.png", 1.0),
  ("UNITS", [[wo("A team of seven,")],[co("on tap.")]], f"{PH}/p2_skills.png", 1.0),
  ("STACK", [[wo("Ten tools,")],[co("one bill.")]], f"{PH}/p2_stack.png", 1.0),
  ("DEALS", [[wo("It works")],[co("every deal.")]], f"{PH}/p2_deals.png", 1.0),
  ("PIPELINE", [[wo("The whole")],[co("pipeline.")]], f"{PH}/p2_pipeline.png", 1.0),
  ("ULTRON", [[wo("Always on.")],[co("In your pocket.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
# BIG phone (fills the visible band, screen continuous) + compact hook on top
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    if last:
        T2.ls_text(d,(T2.MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
        s=T2.fit_hook(d,head,T2.W-2*T2.MX,start=84,floor=58); hf=T2.dm(900,s); y=534
        for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=int(s*1.14)
        T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (50,720,1030,1245), fill=fill)
        d.text((T2.MX,1262),"Follow for one AI system for founders every day.",font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
        return
    T2.ls_text(d,(T2.MX,300),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*T2.MX,start=64,floor=44),56); hf=T2.dm(900,s); y=340
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=int(s*1.12)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (32,452,1048,1562), fill=1.0)
    x0,x1=90,928; yb=1578; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/phv2_tt",False); b=T2.deck(f"{T2.OUTBASE}/phv2_ig",True)
    T2.montage(f"{T2.OUTBASE}/phv2_tt","phv2_tt",a); T2.montage(f"{T2.OUTBASE}/phv2_ig","phv2_ig",b)
    print("tt",a,"ig",b)
