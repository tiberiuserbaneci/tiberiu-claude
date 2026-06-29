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
  ("THE TEAM", [[wo("This looks like")],[co("a whole team.")]], f"{PH}/p_jobs.png", 1.0),
  ("DEALS", [[wo("Three agents,")],[co("one deal.")]], f"{PH}/p_pipeline.png", 1.0),
  ("UNITS", [[wo("Seven units.")],[co("One person.")]], f"{PH}/p_skills.png", 1.0),
  ("MEMORY", [[wo("One shared")],[co("memory.")]], f"{PH}/p_brain.png", 1.0),
  ("PROJECTS", [[wo("Every project.")],[co("One owner. Me.")]], f"{PH}/p_projects.png", 1.0),
  ("PLAYBOOKS", [[wo("My playbooks,")],[co("on tap.")]], f"{PH}/p_playbooks.png", 1.0),
  ("STACK", [[wo("One bill,")],[co("not ten salaries.")]], f"{PH}/p_stack.png", 1.0),
  ("ULTRON", [[wo("No team.")],[co("Just me.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
# bigger phone zone -> fills the visible band (kills bottom dead space); progress moved lower
def _body(base, eyebrow, head, objpath, page, n, last=False, fill=1.0):
    d=ImageDraw.Draw(base); T2.ghost(base,f"{page:02d}")
    T2.ls_text(d,(T2.MX,470),eyebrow,T2.mono(28),T2.CORAL,4)
    s=T2.fit_hook(d,head,T2.W-2*T2.MX,start=84,floor=58); hf=T2.dm(900,s); lh=int(s*1.14); y=534
    for ln in head: T2.seg_line(d,T2.MX,y,ln,hf); y+=lh
    z=(50,720,1030,1250) if last else (50,720,1030,1520)
    T2.place_in_zone(base, T2.crop_obj(Image.open(objpath)), z, fill=fill)
    if last:
        d.text((T2.MX,1262),"Follow for one AI system for founders every day.",font=T2.dm(700,29),fill=T2.WHITE); T2.footer(base)
    else:
        x0,x1=90,928; yb=1556; d.rounded_rectangle([x0,yb,x1,yb+7],radius=4,fill=T2.TRACK)
        d.rounded_rectangle([x0,yb,x0+int((x1-x0)*page/n),yb+7],radius=4,fill=T2.CORAL)
T2.body_slide=_body
# uniform hook size across content slides
def _u():
    dd=ImageDraw.Draw(Image.new("RGB",(10,10))); heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]; s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(dd.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_u(); _of=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:(_of(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/justme_tt",False); b=T2.deck(f"{T2.OUTBASE}/justme_ig",True)
    T2.montage(f"{T2.OUTBASE}/justme_tt","justme_tt",a); T2.montage(f"{T2.OUTBASE}/justme_ig","justme_ig",b)
    print("tt",a,"ig",b)
