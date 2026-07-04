#!/usr/bin/env python3
# Minimal build to preview the dense MODEL panel on a full slide (hook + sub + progress bar).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/_model"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204,120,92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo("It saw the funding round")],[co("before my VC did.")]])
T2.CONTENT=[
 ("THE EYES", [[wo("It saw the funding round")],[co("before my VC did.")]],
  "Funding, hiring, stack, intent. Signals you would never spot by hand.",
  [co("Overnight, every night.")], f"{M}/model.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo("Want the signal list?")],[co("comment EYES.")]],
  "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1="Save this to",l2="see it first.",q="Founder or spectator?")
MARK2="claude"
