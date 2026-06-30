#!/usr/bin/env python3
# THE UNFAIR ADVANTAGE - 9:16 3D carousel, TikTok + IG. Same engine as build_team_3d (imported),
# only the cover/content/objects/pill differ. Objects = REAL competitor app windows (Vertex, real
# logos) shown dimmed + 'replaced', plus the stack grid and the monthly bill. One material system.
import importlib.util, os
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
R=f"{T2.OBJ}/models_rival"; V=f"{T2.OBJ}/models_team/v3"; LIB=T2.LIB

T2.COVER=dict(head=[[wo("My rival has 40 staff.")],[co("I have a chat.")]])   # no eyebrow (rule)
T2.CONTENT=[
 ("RESEARCH", [[wo("They pay for Apollo.")],[co("I just ask.")]],   f"{R}/research.png", 0.95),
 ("OUTREACH", [[wo("They run Outreach.")],[co("I just ask.")]],     f"{R}/outreach.png", 0.95),
 ("CRM",      [[wo("They run Salesforce.")],[co("I just ask.")]],   f"{R}/crm.png",      0.95),
 ("CONTENT",  [[wo("They run Canva.")],[co("I just ask.")]],        f"{R}/content.png",  0.95),
 ("SITE",     [[wo("They run Webflow.")],[co("I just ask.")]],      f"{R}/site.png",     0.95),
 ("THE STACK",[[wo("Twelve tools.")],[co("One chat.")]],            f"{R}/stack.png",    0.90),
 ("THE GATE", [[wo("And I approve")],[co("every move.")]],          f"{V}/gate.png",     0.62),
 ("THE BILL", [[wo("They pay for all this.")],[co("I pay for a chat.")]], f"{R}/cost.png", 0.93),
]
T2.CTA=("GET THE EDGE", [[wo("Replace your stack,")],[co("in your chat.")]], f"{LIB}/cta3d-founder.png", 0.92)

if __name__=="__main__":
    ntt=T2.deck_poll(f"{T2.OUTBASE}/rival_tt", overlay=False)
    nig=T2.deck_poll(f"{T2.OUTBASE}/rival_ig", overlay=True)
    T2.montage(f"{T2.OUTBASE}/rival_tt","rival_tt",ntt)
    T2.montage(f"{T2.OUTBASE}/rival_ig","rival_ig",nig)
    print("TikTok slides:",ntt," IG slides:",nig)
