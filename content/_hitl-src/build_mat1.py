#!/usr/bin/env python3
# START YOUR COMPANY TONIGHT - congruent framed Vertex dashboards (no phone), TikTok+IG (deck_close)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Start your company")],[co("tonight.")]])
T2.CONTENT=[
  ("LEADS",    [[wo("Find your")],[co("first buyers.")]],   f"{D}/m1b_01.png", 1.0),
  ("OUTREACH", [[wo("Reach them")],[co("at scale.")]],       f"{D}/m1b_02.png", 1.0),
  ("PIPELINE", [[wo("Track every")],[co("deal.")]],          f"{D}/m1b_03.png", 1.0),
  ("CALLS",    [[wo("Book the")],[co("calls.")]],            f"{D}/m1b_04.png", 1.0),
  ("PROJECTS", [[wo("Run the whole")],[co("company.")]],     f"{D}/m1b_05.png", 1.0),
  ("PAYMENTS", [[wo("Get")],[co("paid.")]],                  f"{D}/m1b_06.png", 1.0),
  ("STACK",    [[wo("One chat")],[co("runs it all.")]],      f"{D}/m1b_07.png", 1.0),
  ("ULTRON",   [[wo("No team.")],[co("Just you and one chat.")]], UL, 0.98),
]
T2.CLOSE=dict(l1="Save this for",l2="the day you start.",q="Which tool are you wiring first?")
T2.body_slide=T2.dash_body
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat1_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat1_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat1_tt","mat1_tt",a); T2.montage(f"{T2.OUTBASE}/mat1_ig","mat1_ig",b)
    print("tt",a,"ig",b)
