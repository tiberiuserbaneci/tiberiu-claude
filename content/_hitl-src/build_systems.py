#!/usr/bin/env python3
# SYSTEMS NOT EMPLOYEES - Dark Ultron gleam of catalin's "you don't need more employees, you need
# better AI systems" reference. 1080x1350 3D (own coded objects). Each hire -> a system that runs itself.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/systems"; LIB=T2.LIB
PREMIUM=1   # coded clay3d panels
T2.ACCENT=(200,70,35); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/systems.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("They told me to hire.")],[co("I built systems instead.")]])
T2.CONTENT=[
 ("THE ORG CHART", [[wo("My org chart")],[co("is one chat.")]],        "Every role on the chart collapses into one chat you already run.", [co("No seats to fill.")],          f"{M}/orgchart.png",  1.0),
 ("THE SYSTEMS",   [[wo("Set once.")],[co("Runs every day.")]],"Seven workflows fire on their own triggers, all day, no reminders.", [co("Set once, runs daily.")],   f"{M}/workflows.png", 1.0),
 ("THE PIPELINE",  [[wo("No ops hire.")],[co("The pipe runs itself.")]],"Deals move stage by stage as replies land. Nobody drags a card.", [co("No ops seat needed.")],     f"{M}/hubspot.png",   1.0),
 ("THE CADENCE",   [[wo("42 posts queued.")],[co("Zero coordinators.")]], "A week of content goes out on schedule from one message.",        [co("No coordinator to chase.")],f"{M}/scheduler.png", 1.0),
 ("THE LEADS",     [[wo("1,284 scanned.")],[co("63 worth calling.")]],      "Leads are found, enriched and scored before you open your laptop.",[co("No SDR to hire.")],         f"{M}/leadscore.png", 1.0),
 ("THE WORKERS",   [[wo("Six workers.")],[co("None on payroll.")]],        "Six agents work in parallel while you do one thing at a time.",    [co("No payroll to run.")],      f"{M}/agents.png",    1.0),
 ("THE GATE",      [[wo("Systems move fast.")],[co("I hold the brakes.")]],"Nothing ships until you say go. A system, not a free-for-all.",   [co("You stay in control.")],    f"{M}/gate.png",      1.0),
 ("THE OPERATOR",  [[wo("Employees: zero.")],[co("Output: a company.")]],"You do not manage people. You run systems from one chat.",       [co("Run it solo.")],            f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("SYSTEMS", [[wo("Want the systems?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="you hire again.",q="Which role would you systemize first?")


MARK2="orb"
