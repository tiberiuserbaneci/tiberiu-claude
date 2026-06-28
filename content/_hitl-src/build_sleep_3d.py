#!/usr/bin/env python3
# MONEY IN YOUR SLEEP - 9:16 3D, TikTok + IG. Real-app objects showing money/results overnight.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money"; V=f"{T2.OBJ}/models_team/v3"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("I woke up to")],[co("$4,000 in Stripe.")]])
T2.CONTENT=[
 ("STRIPE",   [[wo("Stripe pinged")],[co("all night.")]],        f"{M}/stripe_phone.png", 0.90),
 ("PAYMENTS", [[wo("Cards charged")],[co("while I slept.")]],     f"{M}/stripe_dash.png",  0.95),
 ("CALENDAR", [[wo("My calendar")],[co("booked itself.")]],       f"{M}/calendly.png",     0.95),
 ("DEALS",    [[wo("Deals closed")],[co("on their own.")]],       f"{M}/hubspot.png",      0.95),
 ("INBOX",    [[wo("Replies stacked up")],[co("overnight.")]],    f"{M}/gmail.png",        0.95),
 ("THE GATE", [[wo("It still asks")],[co("before it acts.")]],    f"{V}/gate.png",         0.62),
 ("REVENUE",  [[wo("I just watched")],[co("it climb.")]],         f"{M}/revenue.png",      0.95),
 ("HOW",      [[wo("One chat")],[co("ran the night shift.")]],    f"{M}/ultron_chat.png",  0.92),
]
T2.CTA=("WAKE UP TO IT", [[wo("Wake up to it,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/sleep_tt",overlay=False); b=T2.deck(f"{T2.OUTBASE}/sleep_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/sleep_tt","sleep_tt",a); T2.montage(f"{T2.OUTBASE}/sleep_ig","sleep_ig",b)
    print("tt",a,"ig",b)
