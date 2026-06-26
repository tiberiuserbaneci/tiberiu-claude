#!/usr/bin/env python3
# TikTok 3D (Model B) - HUMAN GATE. Reuses build_3d916's 9:16 pager with HITL content + HITL models.
import os
from PIL import Image
import build_slides as B
import build_3d916 as T
co=lambda s:(s,B.CORAL); wo=lambda s:(s,B.WHITE)
HITL={
1:dict(role="cover",num="01",head=[[wo("Your AI can send,")],[wo("charge and delete.")],[co("Mine asks first.")]],sub="It runs the busywork. It stops before anything it cannot undo."),
2:dict(role="mid",num="02",eyebrow="THE GATE",head=[[wo("It stops before")],[co("it ships.")]],body=[("It drafts the work and runs it, then pauses at every step that leaves the building.",0)]),
3:dict(role="mid",num="03",eyebrow="WHAT NEEDS A YES",head=[[co("7 moves")],[wo("that need your yes.")]]),
4:dict(role="mid",num="04",eyebrow="THE DECISION",head=[[wo("Approve, decline,")],[co("or pick a path.")]]),
5:dict(role="mid",num="05",eyebrow="EDIT FIRST",head=[[wo("Change it before")],[co("it ships.")]],body=[("Edit the action on the card, then approve the version you actually want.",0)]),
6:dict(role="mid",num="06",eyebrow="THE RULE",head=[[wo("Before the action.")],[co("Never after.")]],body=[("An approval after the fact is theatre. The gate sits before the irreversible step.",0)]),
7:dict(role="mid",num="07",eyebrow="THE RECORD",head=[[wo("Every yes")],[co("is logged.")]]),
8:dict(role="last",num="08",eyebrow="GET THE SETUP",head=[[wo("Comment "),co("GATE")],[wo("I will send it.")]],body=[("The exact human-gate setup I run my company on. Follow for one AI system for founders every day.",0)]),
}
B.SPECS=HITL
MF=f"{T.TE}/roll3/models_hitl"; OUT=f"{T.TE}/roll3/hitl_3d_9"; os.makedirs(OUT,exist_ok=True)
for n in range(1,9): T.build(n,MF,OUT); print("built",n)
# Instagram variant: slide 1 = transparent overlay (hook + 3D logo only, no corner number, no swipe),
# laid over a short reel video; slides 2-8 identical to the TikTok 3D set.
import shutil
IGOUT=f"{T.TE}/roll3/hitl_ig_3d"; os.makedirs(IGOUT,exist_ok=True)
T.build(1,MF,IGOUT,transparent=True); print("built IG s1 (transparent overlay)")
for n in range(2,9): shutil.copy(f"{OUT}/s{n}.png", f"{IGOUT}/s{n}.png")
ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,9)]
cols=4;rows=2;sc=300;sh=int(sc*1920/1080)
st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
st.save(f"{T.TE}/hitl_3d_montage.png"); print("montage saved")
