#!/usr/bin/env python3
# FROM 9 TO 5 TO FOUNDER - congruent framed Vertex dashboards (no phone), TikTok+IG (deck_close)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("From 9 to 5,")],[co("to founder.")]])
T2.CONTENT=[
  ("LIVE",     [[wo("It runs")],[co("while you clock in.")]],  f"{D}/mb_live.png", 1.0),   # Ultron activity
  ("OUTREACH", [[wo("Outreach goes out")],[co("on its own.")]],f"{D}/m1b_02.png", 1.0),    # Gmail
  ("PIPELINE", [[wo("Deals move")],[co("without you.")]],      f"{D}/m1b_03.png", 1.0),    # HubSpot
  ("PROJECTS", [[wo("Your side company,")],[co("organized.")]],f"{D}/m1b_05.png", 1.0),    # Notion
  ("UNITS",    [[wo("Seven units,")],[co("zero hires.")]],     f"{D}/mb_units.png", 1.0),  # Ultron agents
  ("MEMORY",   [[wo("It never")],[co("forgets.")]],            f"{D}/mb_memory.png", 1.0), # Ultron memory
  ("STACK",    [[wo("One bill,")],[co("your whole stack.")]],  f"{D}/m1b_07.png", 1.0),    # integrations
  ("ULTRON",   [[wo("Quit when")],[co("it pays you.")]],       UL, 0.98),
]
T2.CLOSE=dict(l1="Save this for",l2="the day you quit.",q="What would you automate first?")
T2.body_slide=T2.dash_body
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat3_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat3_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat3_tt","mat3_tt",a); T2.montage(f"{T2.OUTBASE}/mat3_ig","mat3_ig",b)
    print("tt",a,"ig",b)
