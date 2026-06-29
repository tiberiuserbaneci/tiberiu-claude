#!/usr/bin/env python3
# I RUN IT FROM MY PHONE - 9:16 3D, TikTok + IG. Freedom/mobility founder fantasy (platform-safe).
# Objects = REAL Ultron mobile app (app.51ultron.com, captured live) in a coded phone frame +
# real-style notification banners (deal/reply/ship/meeting/standup/gate). Real reference, no Vertex.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL)
PH=f"{T2.OBJ}/models_phone"; LIB=T2.LIB
T2.COVER=dict(head=[[wo("My company runs")],[co("from my phone.")]])
T2.CONTENT=[
 ("LIVE",    [[wo("A whole team's work,")],[co("running live.")]], f"{PH}/jobs.png",    1.0),
 ("REPLIES", [[wo("It answered")],[co("the lead.")]],             f"{PH}/n_reply.png",  1.0),
 ("CALLS",   [[wo("It booked")],[co("the call.")]],               f"{PH}/n_meeting.png",1.0),
 ("DEALS",   [[wo("It moved")],[co("the deal.")]],                f"{PH}/n_deal.png",   1.0),
 ("SHIP",    [[wo("It shipped")],[co("the update.")]],            f"{PH}/n_ship.png",   1.0),
 ("BRIEF",   [[wo("It wrote")],[co("the standup.")]],             f"{PH}/n_standup.png",1.0),
 ("THE GATE",[[wo("I just tap")],[co("approve.")]],               f"{PH}/n_gate.png",   1.0),
 ("ULTRON",  [[wo("One chat.")],[co("In my pocket.")]],           f"{PH}/home.png",     1.0),
]
T2.CTA=("RUN ON ONE", [[wo("Run on one,")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
from PIL import Image as _I
from PIL import ImageDraw as _ID
def _u():
    d=_ID.Draw(_I.new("RGB",(10,10))); heads=[h for _,h,_,_ in T2.CONTENT]+[T2.CTA[1]]; s=84
    while s>50:
        hf=T2.dm(900,s)
        if all(max(d.textlength("".join(t for t,_ in ln),font=hf) for ln in head)<=T2.W-2*T2.MX for head in heads): break
        s-=2
    return s
_USZ=_u(); _of=T2.fit_hook
T2.fit_hook=lambda d,head,maxw,start=84,floor=58:(_of(d,head,maxw,start=start,floor=floor) if head is T2.COVER["head"] else _USZ)
if __name__=="__main__":
    a=T2.deck(f"{T2.OUTBASE}/phone_tt",False); b=T2.deck(f"{T2.OUTBASE}/phone_ig",True)
    T2.montage(f"{T2.OUTBASE}/phone_tt","phone_tt",a); T2.montage(f"{T2.OUTBASE}/phone_ig","phone_ig",b)
    print("tt",a,"ig",b)
