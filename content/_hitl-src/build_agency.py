#!/usr/bin/env python3
# A FULL AGENCY, ONE CLAUDE - gleam of catalin's "10 skills. One Claude. A full agency team." reference.
# 1080x1350 3D. Each installed skill = an agency function, all under one chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(212,162,127); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/agency.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("A full agency.")],[co("One chat.")]])
T2.CONTENT=[
 ("THE SKILLS",   [[wo("The whole agency?")],[co("Ten skills.")]],"Ten skills installed, each one a function you used to outsource.", [co("10 installed.")],          f"{M}/skills.png",    1.0),
 ("THE RESEARCH", [[wo("Account research?")],[co("A skill.")]],  "Live briefs on people and companies, pulled the moment you ask.",  [co("No researcher to brief.")],f"{M}/apollo.png",    1.0),
 ("THE COPY",     [[wo("The copywriter?")],[co("A skill.")]],    "On-brand, ranked content written straight from the chat.",         [co("No writer to pay.")],     f"{M}/seowriter.png", 1.0),
 ("THE DESIGN",   [[wo("The designer?")],[co("A skill.")]],      "Posts, carousels and ad sets come out of the same chat, on brand.",[co("No designer to brief.")], f"{M}/designer.png",  1.0),
 ("THE CALENDAR", [[wo("The scheduler?")],[co("A skill.")]],     "A full week of content planned and queued across channels.",       [co("No coordinator.")],       f"{M}/content.png",   1.0),
 ("THE DEALS",    [[wo("The account exec?")],[co("A skill.")]],  "The pipeline updates itself as replies land and deals move.",      [co("No ops seat.")],          f"{M}/hubspot.png",   1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every asset.")]],  "Nothing publishes until you say go. You are the creative director.",[co("You approve every move.")],f"{M}/gate.png",     1.0),
 ("THE OPERATOR", [[wo("Ten hires.")],[co("One chat.")]],        "A full agency roster, for the price of a chat, not a retainer.",   [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("AGENCY", [[wo("Want the roster?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="your next retainer.",q="Which function would you install first?")
