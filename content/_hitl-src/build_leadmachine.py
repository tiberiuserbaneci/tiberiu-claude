#!/usr/bin/env python3
# THE LEAD MACHINE - gleam of catalin's "build a B2B lead machine with Ultron" reference.
# 1080x1350 3D. One chat = sourcing + enrichment + scoring + sending + booking.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/leadmachine"; LIB=T2.LIB
PREMIUM=1   # coded clay3d panels
T2.ACCENT=(204,120,92); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/leadmachine.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("My SDR desk runs")],[co("while I sleep.")]])
T2.CONTENT=[
 ("THE SOURCE",   [[wo("1,284 leads in.")],[co("One sentence typed.")]],   "Live company and contact data pulled the moment you ask.",        [co("1,284 sourced.")],       f"{M}/apollo.png",     1.0),
 ("THE SCORING",  [[wo("471 pass my ICP.")],[co("63 are hot.")]],     "Every lead enriched and scored, so you only touch the hot ones.",  [co("471 scored, 63 hot.")], f"{M}/leadscore.png",  1.0),
 ("THE SEND",     [[wo("240 sends queued.")],[co("No copy-paste.")]],"The whole sequence goes out from one message, personalised.",     [co("No SDR to hire.")],      f"{M}/gmail_sent.png", 1.0),
 ("THE INBOXING", [[wo("99.2% hit the inbox.")],[co("Domains stay warm.")]],  "Domains warm, spam avoided, mail lands where it should.",          [co("99.2% inboxed.")],       f"{M}/warmup.png",     1.0),
 ("THE BOOKING",  [[wo("Replies become calls.")],[co("On their own.")]],       "Replies turn into calls on your calendar without a second tool.",  [co("63 booked.")],           f"{M}/calendly.png",   1.0),
 ("THE PIPELINE", [[wo("Touch 2 books 58%.")],[co("Mine never dies.")]],"Deals move as replies land. The pipeline keeps itself current.",  [co("No ops seat.")],         f"{M}/hubspot.png",    1.0),
 ("THE GATE",     [[wo("It writes. It waits.")],[co("I release.")]],   "Nothing goes out until you say go. You stay in control.",          [co("You approve every send.")],f"{M}/gate.png",     1.0),
 ("THE OPERATOR", [[wo("A whole SDR desk.")],[co("One subscription.")]], "Sourcing to booked calls, run behind a single subscription.",     [co("Run it solo.")],         f"{M}/ultron_real.png",     1.0),
]
T2.CTA=("LEADS", [[wo("Want the machine?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="fill your pipe.",q="Where does your pipeline break today?")


MARK2="claude"
