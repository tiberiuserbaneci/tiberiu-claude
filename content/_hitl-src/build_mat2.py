#!/usr/bin/env python3
# YOUR FIRST PAYING CUSTOMER - congruent framed Vertex dashboards (no phone), TikTok+IG (deck_close)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Your first")],[co("paying customer.")]])
T2.CONTENT=[
  ("LEADS",     [[wo("It builds")],[co("the list.")]],            f"{D}/m1b_01.png", 1.0),   # Apollo
  ("OUTREACH",  [[wo("It writes")],[co("every message.")]],       f"{D}/m1b_02.png", 1.0),   # Gmail
  ("FOLLOW-UP", [[wo("It follows up")],[co("until they reply.")]], f"{D}/mb_follow.png", 1.0),# Instantly
  ("PIPELINE",  [[wo("Every deal,")],[co("one view.")]],          f"{D}/m1b_03.png", 1.0),   # HubSpot
  ("BOOKED",    [[wo("It books")],[co("the call.")]],             f"{D}/m1b_04.png", 1.0),   # Calendly
  ("UNITS",     [[wo("A sales team")],[co("of one.")]],           f"{D}/mb_units.png", 1.0), # Ultron agents
  ("STACK",     [[wo("Wired to")],[co("your tools.")]],           f"{D}/m1b_07.png", 1.0),   # integrations
  ("ULTRON",    [[wo("Your first customer,")],[co("closed.")]],   UL, 0.98),
]
T2.CLOSE=dict(l1="Save this for",l2="customer number one.",q="Which step are you missing?")
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment FOUNDER.")]], f"{T2.LIB}/cta3d-founder.png", 0.92)
T2.body_slide=T2.dash_body
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat2_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat2_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat2_tt","mat2_tt",a); T2.montage(f"{T2.OUTBASE}/mat2_ig","mat2_ig",b)
    print("tt",a,"ig",b)
