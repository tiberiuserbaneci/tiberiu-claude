#!/usr/bin/env python3
# FROM MY PHONE v1
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{T2.OBJ}/models_phone"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("My company runs")],[co("from my phone.")]])
T2.CONTENT=[
  ("LIVE", [[wo("A whole team's work,")],[co("running live.")]], f"{PH}/p2_jobs.png", 1.0),
  ("DEALS", [[wo("Agents work")],[co("the deals.")]], f"{PH}/p2_deals.png", 1.0),
  ("PIPELINE", [[wo("Every deal,")],[co("one pipeline.")]], f"{PH}/p2_pipeline.png", 1.0),
  ("PROJECTS", [[wo("Every project,")],[co("one place.")]], f"{PH}/p2_projects.png", 1.0),
  ("STACK", [[wo("One subscription.")],[co("My whole stack.")]], f"{PH}/p2_stack.png", 1.0),
  ("PLAYBOOKS", [[wo("Proven playbooks,")],[co("built in.")]], f"{PH}/p2_playbooks.png", 1.0),
  ("PRIMITIVES", [[wo("Drop-in workflows,")],[co("ready.")]], f"{PH}/p2_primitives.png", 1.0),
  ("ULTRON", [[wo("One chat.")],[co("In my pocket.")]], UL, 0.98),
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
    a=T2.deck(f"{T2.OUTBASE}/phone_tt",False); b=T2.deck(f"{T2.OUTBASE}/phone_ig",True)
    T2.montage(f"{T2.OUTBASE}/phone_tt","phone_tt",a); T2.montage(f"{T2.OUTBASE}/phone_ig","phone_ig",b)
    print("tt",a,"ig",b)
