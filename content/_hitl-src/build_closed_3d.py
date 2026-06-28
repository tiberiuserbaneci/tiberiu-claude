#!/usr/bin/env python3
# I CLOSED WITHOUT SELLING - 9:16 3D, TikTok + IG. Real-app objects: leads -> replies -> calls -> won -> paid.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money"; V=f"{T2.OBJ}/models_team/v3"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("I closed 4 deals.")],[co("I sent zero emails.")]])
T2.CONTENT=[
 ("LEADS",    [[wo("It found")],[co("the buyers.")]],         f"{M}/leads.png",      0.95),
 ("REPLIES",  [[wo("The replies")],[co("came back.")]],       f"{M}/gmail.png",      0.95),
 ("CALENDAR", [[wo("Calls booked")],[co("themselves.")]],     f"{M}/calendly.png",   0.95),
 ("PIPELINE", [[wo("Deals moved")],[co("to won.")]],          f"{M}/hubspot.png",    0.95),
 ("PAID",     [[wo("Then Stripe")],[co("lit up.")]],          f"{M}/stripe_dash.png",0.95),
 ("THE GATE", [[wo("I approved.")],[co("It sent.")]],         f"{V}/gate.png",       0.62),
 ("PROOF",    [[wo("Four closed.")],[co("Zero pitches.")]],   f"{M}/revenue.png",    0.95),
 ("HOW",      [[wo("All of it")],[co("from one chat.")]],     f"{M}/ultron_chat.png",0.92),
]
T2.CTA=("CLOSE ON AUTOPILOT", [[wo("Close on autopilot,")],[co("comment FOUNDER.")]], f"{LIB}/cta3d-founder.png", 0.92)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/closed_tt",overlay=False); b=T2.deck(f"{T2.OUTBASE}/closed_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/closed_tt","closed_tt",a); T2.montage(f"{T2.OUTBASE}/closed_ig","closed_ig",b)
    print("tt",a,"ig",b)
