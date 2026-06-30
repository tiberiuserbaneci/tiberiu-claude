#!/usr/bin/env python3
# MONEY IN YOUR SLEEP - 9:16 3D, TikTok + IG. Real-app objects showing money/results overnight.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB   # premium fresh objects, no reuse
T2.COVER=dict(head=[[wo("I slept 8 hours.")],[co("It worked all 8.")]])
T2.CONTENT=[
 ("APOLLO",   [[wo("It sourced")],[co("200 leads.")]],           f"{M}/apollo.png",     0.95),
 ("GMAIL",    [[wo("It sent")],[co("every email.")]],            f"{M}/gmail_sent.png", 0.95),
 ("REPLIES",  [[wo("18 replies")],[co("by 6am.")]],              f"{M}/gmail.png",      0.95),
 ("CALENDLY", [[wo("6 calls")],[co("booked.")]],                 f"{M}/calendly.png",   0.95),
 ("HUBSPOT",  [[wo("2 deals")],[co("Closed Won.")]],             f"{M}/hubspot.png",    0.95),
 ("STRIPE",   [[wo("$8,400")],[co("collected.")]],               f"{M}/stripe.png",     0.95),
 ("THE GATE", [[wo("Nothing ran")],[co("without my yes.")]],     f"{M}/gate.png",       0.72),
 ("ULTRON",   [[wo("One operator.")],[co("The night shift.")]],  f"{M}/ultron.png",     0.92),
]
T2.CTA=("WAKE UP TO IT", [[wo("Wake up to it,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this for",l2="your first night off.",q="What would you run overnight?")
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/sleep_tt",overlay=False); b=T2.deck_close(f"{T2.OUTBASE}/sleep_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/sleep_tt","sleep_tt",a); T2.montage(f"{T2.OUTBASE}/sleep_ig","sleep_ig",b)
    print("tt",a,"ig",b)
