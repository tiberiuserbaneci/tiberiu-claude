#!/usr/bin/env python3
# FROM ZERO TO COMPANY (phone, build-arc)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{T2.OBJ}/models_phone"; LIB=T2.LIB; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("From zero to a company.")],[co("One command.")]])
T2.CONTENT=[
  ("WORKSPACE", [[wo("It opens")],[co("the workspace.")]], f"{PH}/p_projects.png", 1.0),
  ("UNITS", [[wo("It staffs")],[co("every unit.")]], f"{PH}/p_skills.png", 1.0),
  ("PLAYBOOKS", [[wo("It loads")],[co("the playbooks.")]], f"{PH}/p_playbooks.png", 1.0),
  ("OUTBOUND", [[wo("It runs")],[co("the outbound.")]], f"{PH}/p_jobs.png", 1.0),
  ("DEALS", [[wo("It works")],[co("the deals.")]], f"{PH}/p_deals.png", 1.0),
  ("MEMORY", [[wo("It builds")],[co("the memory.")]], f"{PH}/p_brain.png", 1.0),
  ("STACK", [[wo("It connects")],[co("your tools.")]], f"{PH}/p_stack.png", 1.0),
  ("ULTRON", [[wo("From zero to a company.")],[co("One chat.")]], UL, 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
from PIL import Image as _I
from PIL import ImageDraw as _ID
def _u():
    d=_ID.Draw(_I.new("RGB",(10,10))); heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]; s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_u(); _of=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:(_of(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/zero_tt",False); b=T2.deck(f"{T2.OUTBASE}/zero_ig",True)
    T2.montage(f"{T2.OUTBASE}/zero_tt","zero_tt",a); T2.montage(f"{T2.OUTBASE}/zero_ig","zero_ig",b)
    print("tt",a,"ig",b)
