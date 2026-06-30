#!/usr/bin/env python3
# LOOK LIKE A FUNDED STARTUP - congruent framed Vertex dashboards (no phone), TikTok+IG (deck_close)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
D=f"{T2.OBJ}/models_dash"; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Look like a")],[co("funded startup.")]])
T2.CONTENT=[
  ("RESEARCH",  [[wo("Briefs like")],[co("a research team.")]],  f"{D}/mb_research.png", 1.0),# Clay
  ("OUTREACH",  [[wo("Outreach like")],[co("a full floor.")]],   f"{D}/m1b_02.png", 1.0),     # Gmail
  ("PIPELINE",  [[wo("A pipeline")],[co("that looks staffed.")]],f"{D}/m1b_03.png", 1.0),     # HubSpot
  ("PROJECTS",  [[wo("Client work,")],[co("all organized.")]],   f"{D}/m1b_05.png", 1.0),     # Notion
  ("UNITS",     [[wo("Seven units,")],[co("one operator.")]],    f"{D}/mb_units.png", 1.0),   # Ultron agents
  ("PROPOSALS", [[wo("Proposals that")],[co("look funded.")]],   f"{D}/mb_proposal.png", 1.0),# PandaDoc
  ("STACK",     [[wo("The stack of")],[co("a funded team.")]],   f"{D}/m1b_07.png", 1.0),     # integrations
  ("ULTRON",    [[wo("Solo.")],[co("Looks like thirty.")]],      UL, 0.98),
]
T2.CLOSE=dict(l1="Save this to",l2="look funded solo.",q="Which one sells you short today?")
T2.body_slide=T2.dash_body
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat5_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat5_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat5_tt","mat5_tt",a); T2.montage(f"{T2.OUTBASE}/mat5_ig","mat5_ig",b)
    print("tt",a,"ig",b)
