#!/usr/bin/env python3
# START YOUR COMPANY TONIGHT - congruent framed Vertex dashboards (no phone), TikTok+IG (deck_close)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
D=f"{T2.OBJ}/models_dash"; UL=f"{T2.OBJ}/models_rival2/ultron_login.png"
T2.COVER=dict(head=[[wo("Start your company")],[co("tonight.")]])
# 6-tuple for the 1080x1350 editorial renderer: (eyebrow, hook, SUBHOOK, FOOT idea, object, fill)
T2.CONTENT=[
  ("LEADS",    [[wo("Find your")],[co("first buyers.")]],   "Describe your ICP and a ranked list comes back, live in the chat.",  [co("No list to buy.")],      f"{D}/m1b_01.png", 1.0),
  ("OUTREACH", [[wo("Reach them")],[co("at scale.")]],       "Personalised first-touch and follow-ups, sent from one message.",   [co("No SDR to hire.")],      f"{D}/m1b_02.png", 1.0),
  ("PIPELINE", [[wo("Track every")],[co("deal.")]],          "Deals move by asking, not by logging into a CRM all day.",          [co("No CRM seat.")],         f"{D}/m1b_03.png", 1.0),
  ("CALLS",    [[wo("Book the")],[co("calls.")]],            "It offers times and drops the call straight on your calendar.",      [co("No scheduler tool.")],   f"{D}/m1b_04.png", 1.0),
  ("PROJECTS", [[wo("Run the whole")],[co("company.")]],     "Every workstream in one place, updated as the work ships.",          [co("No project app.")],      f"{D}/m1b_05.png", 1.0),
  ("PAYMENTS", [[wo("Get")],[co("paid.")]],                  "Invoices raised and reconciled for you, cents on the fees.",         [co("Cents on fees.")],       f"{D}/m1b_06.png", 1.0),
  ("STACK",    [[wo("One chat")],[co("runs it all.")]],      "Every job above lives behind a single subscription.",               [mu("Twelve tools."),co("  One chat.")], f"{D}/m1b_07.png", 1.0),
  ("ULTRON",   [[wo("No team.")],[co("Just you.")]],         "You approve every move. The company runs on you, not a headcount.",  [co("You, plus Ultron.")],    UL, 0.98),
]
T2.CLOSE=dict(l1="Save this for",l2="the day you start.",q="Which tool are you wiring first?")
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{T2.LIB}/cta3d-operator.png", 0.92)
T2.body_slide=T2.dash_body
T2.SCREEN_CROP=True   # 1080x1350 editorial: crop dashboards to the app screen (no bezel), floating with edge fade
if __name__=="__main__":
    a=T2.deck_close(f"{T2.OUTBASE}/mat1_tt",False); b=T2.deck_close(f"{T2.OUTBASE}/mat1_ig",True)
    T2.montage(f"{T2.OUTBASE}/mat1_tt","mat1_tt",a); T2.montage(f"{T2.OUTBASE}/mat1_ig","mat1_ig",b)
    print("tt",a,"ig",b)
