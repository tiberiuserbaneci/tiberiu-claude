#!/usr/bin/env python3
# FIFTY VS ONE (50 EMPLOYEES vs ME) - 9:16 3D, TikTok + IG. Logo-forward (UNFAIR ADVANTAGE winner
# direction) but framed by HEADCOUNT: each slide = a whole department the rival STAFFS, shown via a
# DIFFERENT real-brand app (ZoomInfo/Salesloft/Gong/Intercom/Notion/Figma/Google Ads). Fresh brand
# set, zero overlap with UNFAIR's tools. Ultron = sphere only (slide 8 + footer). Cents value-prop.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
R=f"{T2.OBJ}/models_rival2"; P=f"{T2.OBJ}/models_money/p"; LIB=T2.LIB

T2.COVER=dict(head=[[wo("My rival has 50 staff.")],[co("I have one chat.")]])
T2.CONTENT=[
 ("RESEARCH", [[wo("A research team of six.")],[co("Or one chat.")]], f"{R}/zoominfo.png",  0.95),
 ("OUTBOUND", [[wo("Eight SDRs on the floor.")],[co("Or one chat.")]],f"{R}/salesloft.png", 0.95),
 ("SALES",    [[wo("Five closers.")],[co("Or one chat.")]],           f"{R}/gong.png",      0.95),
 ("SUPPORT",  [[wo("A support desk of seven.")],[co("Or one chat.")]],f"{R}/intercom.png",  0.95),
 ("CONTENT",  [[wo("Four content writers.")],[co("Or one chat.")]],   f"{R}/notion.png",    0.95),
 ("DESIGN",   [[wo("Three designers.")],[co("Or one chat.")]],        f"{R}/figma.png",     0.95),
 ("GROWTH",   [[wo("A growth team of five.")],[co("Or one chat.")]],  f"{R}/googleads.png", 0.95),
 ("ULTRON",   [[wo("Fifty people.")],[co("Or one chat.")]],           f"{P}/ultron.png",    0.92),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)

if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/rival2_tt",False); b=T2.deck(f"{T2.OUTBASE}/rival2_ig",True)
    T2.montage(f"{T2.OUTBASE}/rival2_tt","rival2_tt",a); T2.montage(f"{T2.OUTBASE}/rival2_ig","rival2_ig",b)
    print("tt",a,"ig",b)
