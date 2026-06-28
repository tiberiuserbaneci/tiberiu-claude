#!/usr/bin/env python3
# FIRST DOLLARS FAST - 9:16 3D, TikTok + IG. Real-app objects: landing -> leads -> DMs -> calls -> first payment.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money"; V=f"{T2.OBJ}/models_team/v3"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("My first sale came")],[co("before the product.")]])
T2.CONTENT=[
 ("LANDING",  [[wo("It built")],[co("the page.")]],            f"{M}/landing.png",     0.95),
 ("LEADS",    [[wo("It found")],[co("the first buyers.")]],    f"{M}/leads.png",       0.95),
 ("INBOUND",  [[wo("The DMs")],[co("rolled in.")]],            f"{M}/dms.png",         0.90),
 ("CALENDAR", [[wo("Calls")],[co("on the books.")]],          f"{M}/calendly.png",    0.95),
 ("FIRST SALE",[[wo("First payment.")],[co("Day three.")]],   f"{M}/stripe_dash.png", 0.95),
 ("THE GATE", [[wo("I approved")],[co("each step.")]],         f"{V}/gate.png",        0.62),
 ("PROOF",    [[wo("Paying customers.")],[co("No product yet.")]], f"{M}/stripe_phone.png", 0.90),
 ("HOW",      [[wo("All of it")],[co("from one chat.")]],      f"{M}/ultron_chat.png", 0.92),
]
T2.CTA=("START TODAY", [[wo("Start today,")],[co("comment BUILDER.")]], f"{LIB}/cta3d-builder.png", 0.92)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/first_tt",overlay=False); b=T2.deck(f"{T2.OUTBASE}/first_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/first_tt","first_tt",a); T2.montage(f"{T2.OUTBASE}/first_ig","first_ig",b)
    print("tt",a,"ig",b)
