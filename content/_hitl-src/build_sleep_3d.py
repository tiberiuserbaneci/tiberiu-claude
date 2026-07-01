#!/usr/bin/env python3
# MONEY IN YOUR SLEEP - 9:16 3D, TikTok + IG. Real-app objects showing money/results overnight.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB   # premium fresh objects, no reuse
T2.COVER=dict(head=[[wo("I slept 8 hours.")],[co("It worked all 8.")]])
# 6-tuple for the 1080x1350 editorial renderer: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
 ("APOLLO",   [[wo("It sourced")],[co("200 leads.")]],           "Your ICP pulled and ranked while you were offline.",       [co("No list bought.")],   f"{M}/apollo.png",     0.95),
 ("GMAIL",    [[wo("It sent")],[co("every email.")]],            "Personalised first-touch, out the door by 2am.",           [co("No SDR awake.")],     f"{M}/gmail_sent.png", 0.95),
 ("REPLIES",  [[wo("18 replies")],[co("by 6am.")]],              "It drafted the follow-ups, so you wake to warm threads.",   [co("Warm, not cold.")],   f"{M}/gmail.png",      0.95),
 ("CALENDLY", [[wo("6 calls")],[co("booked.")]],                 "It offered times and dropped each call on your calendar.",  [co("Diary filled.")],     f"{M}/calendly.png",   0.95),
 ("HUBSPOT",  [[wo("2 deals")],[co("Closed Won.")]],             "It moved the pipeline overnight, with no CRM login.",       [co("Pipeline moved.")],   f"{M}/hubspot.png",    0.95),
 ("STRIPE",   [[wo("$8,400")],[co("collected.")]],               "Invoices raised and reconciled, cents on the fees.",         [co("Cents on fees.")],    f"{M}/stripe.png",     0.95),
 ("THE GATE", [[wo("Nothing ran")],[co("without my yes.")]],     "Every send waited on your approval. You stay in control.",  [co("You approve.")],      f"{M}/gate.png",       0.72),
 ("ULTRON",   [[wo("One operator.")],[co("The night shift.")]],  "One chat ran the whole company while you were asleep.",     [co("The night shift.")],  f"{M}/ultron.png",     0.92),
]
T2.CTA=("WAKE UP TO IT", [[wo("Wake up to it,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this for",l2="your first night off.",q="What would you run overnight?")
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/sleep_tt",overlay=False); b=T2.deck_close(f"{T2.OUTBASE}/sleep_ig",overlay=True)
    T2.montage(f"{T2.OUTBASE}/sleep_tt","sleep_tt",a); T2.montage(f"{T2.OUTBASE}/sleep_ig","sleep_ig",b)
    print("tt",a,"ig",b)
