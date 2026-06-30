#!/usr/bin/env python3
# FIRST DOLLARS FAST - 9:16 3D, TikTok + IG. Real-app objects: landing -> leads -> DMs -> calls -> first payment.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money/first"; P=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("My first sale came")],[co("before the product.")]])
T2.CONTENT=[
 ("ULTRON",    [[wo("I described it")],[co("in one chat.")]],     f"{P}/ultron.png",            0.92),
 ("WEBSITE",   [[wo("It shipped")],[co("the site.")]],            f"{M}/landing.png",           0.95),
 ("APOLLO",    [[wo("It found")],[co("first buyers.")]],          f"{M}/apollo.png",            0.95),
 ("LINKEDIN",  [[wo("The DMs")],[co("rolled in.")]],              f"{M}/dms.png",               0.90),
 ("CALENDLY",  [[wo("Calls")],[co("on the books.")]],             f"{M}/calendly.png",          0.95),
 ("STRIPE",    [[wo("Day 3:")],[co("first payment.")]],           f"{M}/stripe.png",            0.95),
 ("THE GATE",  [[wo("I approved")],[co("each step.")]],           f"{M}/gate.png",              0.72),
 ("PROOF",     [[wo("9 customers.")],[co("No product yet.")]],    f"{M}/stripe_customers.png",  0.95),
]
T2.CTA=("START TODAY", [[wo("Start today,")],[co("comment BUILDER.")]], f"{LIB}/cta3d-builder.png", 0.92)
if __name__=="__main__":
    a=T2.deck_poll(f"{T2.OUTBASE}/first_tt",overlay=False); b=T2.deck_poll(f"{T2.OUTBASE}/first_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/first_tt","first_tt",a); T2.montage(f"{T2.OUTBASE}/first_ig","first_ig",b)
    print("tt",a,"ig",b)
