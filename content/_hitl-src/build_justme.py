#!/usr/bin/env python3
# IT'S JUST ME
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
from PIL import Image, ImageDraw
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{T2.OBJ}/models_phone"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("It's just me.")],[co("And one chat.")]], sub="Everyone thinks I have a team of thirty.")
T2.CONTENT=[
  ("THE TEAM", [[wo("This looks like")],[co("a whole team.")]], f"{PH}/p2_jobs.png", 1.0),
  ("DEALS", [[wo("Three agents,")],[co("one deal.")]], f"{PH}/p2_deals.png", 1.0),
  ("UNITS", [[wo("Seven units.")],[co("One person.")]], f"{PH}/p2_skills.png", 1.0),
  ("MEMORY", [[wo("One shared")],[co("memory.")]], f"{PH}/p2_brain.png", 1.0),
  ("PROJECTS", [[wo("Every project.")],[co("One owner. Me.")]], f"{PH}/p2_projects.png", 1.0),
  ("STACK", [[wo("One bill,")],[co("not ten salaries.")]], f"{PH}/p2_stack.png", 1.0),
  ("EVERYTHING", [[wo("Everything,")],[co("already built.")]], f"{PH}/p2_everything.png", 1.0),
  ("ULTRON", [[wo("No team.")],[co("Just me.")]], UL, 0.98),
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
    T2.ls_text(d,(T2.MX,318),eyebrow,T2.mono(26),T2.CORAL,4)
    s=min(T2.fit_hook(d,head,T2.W-2*T2.MX,start=64,floor=44),58); hf=T2.dm(900,s); y=360
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=int(s*1.12)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), (40,478,1040,1548), fill=fill)
    x0,x1=90,928; yb=1566; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
    d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/justme_tt",False); b=T2.deck(f"{T2.OUTBASE}/justme_ig",True)
    T2.montage(f"{T2.OUTBASE}/justme_tt","justme_tt",a); T2.montage(f"{T2.OUTBASE}/justme_ig","justme_ig",b)
    print("tt",a,"ig",b)
