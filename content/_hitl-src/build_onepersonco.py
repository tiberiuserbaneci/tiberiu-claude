#!/usr/bin/env python3
# THE ONE-PERSON COMPANY - gleam of catalin's "I built a personal AI agent / one-person business" refs.
# 1080x1350 3D. One person, every department, run from a single chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(204,120,92); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/onepersonco.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("One person.")],[co("Every department.")]])
T2.CONTENT=[
 ("THE CHART",    [[wo("The whole company?")],[co("One chat.")]],"Every department on the org chart runs from one place.",           [co("Headcount zero.")],       f"{M}/orgchart.png",  1.0),
 ("SALES",        [[wo("Sales?")],[co("A system.")]],            "Leads found, enriched and briefed before you open your laptop.",   [co("No SDR to hire.")],       f"{M}/apollo.png",    1.0),
 ("OPERATIONS",   [[wo("Operations?")],[co("Automated.")]],      "Workflows fire on triggers all day, no reminders, no missed steps.",[co("Set once, runs daily.")], f"{M}/workflows.png", 1.0),
 ("PRODUCT",      [[wo("Product?")],[co("Shipped from chat.")]], "Pages and updates go live straight from the chat, no builder.",     [co("No dev to wait on.")],    f"{M}/developer.png", 1.0),
 ("MARKETING",    [[wo("Marketing?")],[co("Queued.")]],          "A week of content planned and posted across channels.",             [co("14 scheduled.")],         f"{M}/content.png",   1.0),
 ("FINANCE",      [[wo("Finance?")],[co("It adds up.")]],        "One operator, $48k MRR, up 32%, no team on payroll.",               [co("Solo, not small.")],      f"{M}/revenue.png",   1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every move.")]],   "Every department runs, but nothing ships until you say go.",        [co("You stay in control.")],  f"{M}/gate.png",      1.0),
 ("THE OPERATOR", [[wo("Every department.")],[co("One operator.")]],"The whole company runs behind a single subscription.",           [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("COMPANY", [[wo("Want the build?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="run it solo.",q="Which department would you automate first?")

MARK2="strip"
