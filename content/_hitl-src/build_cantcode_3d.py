#!/usr/bin/env python3
# I CAN'T CODE - 9:16 3D, TikTok + IG. Founder competence fantasy. Real-app objects, no raw code (S30 ICP).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
M=f"{T2.OBJ}/models_code"; P=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("I've never written a line of code.")],[co("My app has 5,000+ users.")]])
T2.CONTENT=[
 ("CLAUDE CODE",[[wo("I asked")],[co("in plain English.")]],   f"{M}/claudecode.png", 1.0),
 ("BUILD",     [[wo("It built")],[co("the whole app.")]],      f"{M}/build.png",      0.88),
 ("DEPLOY",    [[wo("It shipped")],[co("to production.")]],     f"{M}/vercel.png",     0.95),
 ("LIVE",      [[wo("This is")],[co("the live app.")]],         f"{M}/liveapp.png",    0.95),
 ("FIXES",     [[wo("It fixes")],[co("its own bugs.")]],        f"{M}/fixes.png",      0.90),
 ("USERS",     [[wo("5,000+")],[co("signed up.")]],             f"{M}/analytics.png",  0.95),
 ("THE GATE",  [[wo("I approve")],[co("every ship.")]],         f"{M}/gate.png",       0.72),
 ("ULTRON",    [[wo("I can't code.")],[co("It can.")]],         f"{P}/ultron.png",     0.92),
]
T2.CTA=("BUILD YOURS", [[wo("Build yours,")],[co("comment BUILDER.")]], f"{LIB}/cta3d-builder.png", 0.92)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/code_tt",False); b=T2.deck(f"{T2.OUTBASE}/code_ig",True)
    T2.montage(f"{T2.OUTBASE}/code_tt","code_tt",a); T2.montage(f"{T2.OUTBASE}/code_ig","code_ig",b)
    print("tt",a,"ig",b)
