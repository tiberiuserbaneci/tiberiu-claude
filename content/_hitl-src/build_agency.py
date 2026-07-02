#!/usr/bin/env python3
# A FULL AGENCY, ONE CLAUDE - gleam of catalin's "10 skills. One Claude. A full agency team." reference.
# 1080x1350 3D. Each installed skill = an agency function, all under one chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/agency"; LIB=T2.LIB
PREMIUM=1   # coded clay3d panels
T2.ACCENT=(212,162,127); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/agency.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("I cancelled the agency.")],[co("Kept the output.")]])
T2.CONTENT=[
 ("THE SKILLS",   [[wo("Ten skills installed.")],[co("Zero contracts signed.")]],"Ten skills installed, each one a function you used to outsource.", [co("10 installed.")],          f"{M}/skills.png",    1.0),
 ("THE RESEARCH", [[wo("Account briefs, one page.")],[co("Fresh every morning.")]],  "Live briefs on people and companies, pulled the moment you ask.",  [co("No researcher to brief.")],f"{M}/apollo.png",    1.0),
 ("THE COPY",     [[wo("Copy ranked 92/100.")],[co("Straight from chat.")]],    "On-brand, ranked content written straight from the chat.",         [co("No writer to pay.")],     f"{M}/seowriter.png", 1.0),
 ("THE DESIGN",   [[wo("On-brand, first try.")],[co("No revision loop.")]],      "Posts, carousels and ad sets come out of the same chat, on brand.",[co("No designer to brief.")], f"{M}/designer.png",  1.0),
 ("THE CALENDAR", [[wo("14 slots planned.")],[co("One line in.")]],     "A full week of content planned and queued across channels.",       [co("No coordinator.")],       f"{M}/content.png",   1.0),
 ("THE DEALS",    [[wo("The account exec")],[co("answers in seconds.")]],  "The pipeline updates itself as replies land and deals move.",      [co("No ops seat.")],          f"{M}/hubspot.png",   1.0),
 ("THE GATE",     [[wo("Agency speed.")],[co("My signature.")]],  "Nothing publishes until you say go. You are the creative director.",[co("You approve every move.")],f"{M}/gate.png",     1.0),
 ("THE OPERATOR", [[wo("Ten hires replaced.")],[co("No retainer.")]],        "A full agency roster, for the price of a chat, not a retainer.",   [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("AGENCY", [[wo("Want the roster?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="your next retainer.",q="Which function would you install first?")


MARK2="strip"
STRIP="/home/user/tiberiu-claude/content/_hitl-src/covers/agency_strip.png"
