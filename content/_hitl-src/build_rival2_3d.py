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

T2.COVER=dict(head=[[wo("38 staff, 9 to 5.")],[co("vs me. One chat.")]])
T2.CONTENT=[
 ("RESEARCH", [[wo("A research team of six.")],[co("Or one chat.")]], f"{R}/zoominfo.png",  0.95),
 ("OUTBOUND", [[wo("Eight SDRs on the floor.")],[co("Or one chat.")]],f"{R}/salesloft.png", 0.95),
 ("SALES",    [[wo("Five closers.")],[co("Or one chat.")]],           f"{R}/gong.png",      0.95),
 ("SUPPORT",  [[wo("A support desk of seven.")],[co("Or one chat.")]],f"{R}/intercom.png",  0.95),
 ("CONTENT",  [[wo("Four content writers.")],[co("Or one chat.")]],   f"{R}/notion.png",    0.95),
 ("DESIGN",   [[wo("Three designers.")],[co("Or one chat.")]],        f"{R}/figma.png",     0.95),
 ("GROWTH",   [[wo("A growth team of five.")],[co("Or one chat.")]],  f"{R}/googleads.png", 0.95),
 ("ULTRON",   [[wo("38 people.")],[co("Or one chat.")]],           f"{R}/ultron_login.png", 0.98),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)

# --- uniform hook size across content slides (no per-slide drift); cover keeps its own sizing ---
from PIL import Image as _I
from PIL import ImageDraw as _ID
def _uniform_size():
    d=_ID.Draw(_I.new("RGB",(10,10)))
    heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]
    s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_uniform_size(); _origfit=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:( _origfit(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ )

if __name__=="__main__":
    a=T2.deck_poll(f"{T2.OUTBASE}/rival2_tt",False); b=T2.deck_poll(f"{T2.OUTBASE}/rival2_ig",True)
    T2.montage(f"{T2.OUTBASE}/rival2_tt","rival2_tt",a); T2.montage(f"{T2.OUTBASE}/rival2_ig","rival2_ig",b)
    print("tt",a,"ig",b)
