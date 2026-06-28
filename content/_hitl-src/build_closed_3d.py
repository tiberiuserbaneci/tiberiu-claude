#!/usr/bin/env python3
# I CLOSED WITHOUT SELLING - 9:16 3D, TikTok + IG. Real-app objects: leads -> replies -> calls -> won -> paid.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money/closed"; P=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("I closed 4 deals.")],[co("I sent zero emails.")]])
T2.CONTENT=[
 ("APOLLO",   [[wo("It found")],[co("the buyers.")]],         f"{M}/apollo.png",   0.95),
 ("OUTREACH", [[wo("It wrote")],[co("the emails.")]],         f"{M}/outreach.png", 0.95),
 ("GMAIL",    [[wo("The replies")],[co("came in.")]],         f"{M}/gmail.png",    0.95),
 ("CALENDLY", [[wo("Calls booked")],[co("themselves.")]],     f"{M}/calendly.png", 0.95),
 ("HUBSPOT",  [[wo("Deals moved")],[co("to Won.")]],          f"{M}/hubspot.png",  0.95),
 ("STRIPE",   [[wo("Then Stripe")],[co("lit up.")]],          f"{M}/stripe.png",   0.95),
 ("THE GATE", [[wo("I approved.")],[co("It sent.")]],         f"{M}/gate.png",     0.72),
 ("ULTRON",   [[wo("Four closed.")],[co("One chat.")]],       f"{P}/ultron.png",   0.92),
]
T2.CTA=("CLOSE ON AUTOPILOT", [[wo("Close on autopilot,")],[co("comment FOUNDER.")]], f"{LIB}/cta3d-founder.png", 0.92)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/closed_tt",overlay=False); b=T2.deck(f"{T2.OUTBASE}/closed_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/closed_tt","closed_tt",a); T2.montage(f"{T2.OUTBASE}/closed_ig","closed_ig",b)
    print("tt",a,"ig",b)
