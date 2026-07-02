#!/usr/bin/env python3
# SYSTEMS NOT EMPLOYEES - Dark Ultron gleam of catalin's "you don't need more employees, you need
# better AI systems" reference. 1080x1350 3D (own coded objects). Each hire -> a system that runs itself.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(200,70,35); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/systems.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("You don't need")],[co("more employees.")]])
T2.CONTENT=[
 ("THE ORG CHART", [[wo("Headcount?")],[co("Zero.")]],        "Every role on the chart collapses into one chat you already run.", [co("No seats to fill.")],          f"{M}/orgchart.png",  1.0),
 ("THE SYSTEMS",   [[wo("The work?")],[co("It runs itself.")]],"Seven workflows fire on their own triggers, all day, no reminders.", [co("Set once, runs daily.")],   f"{M}/workflows.png", 1.0),
 ("THE PIPELINE",  [[wo("The pipeline?")],[co("Self-updating.")]],"Deals move stage by stage as replies land. Nobody drags a card.", [co("No ops seat needed.")],     f"{M}/hubspot.png",   1.0),
 ("THE CADENCE",   [[wo("Posting?")],[co("Queued for you.")]], "A week of content goes out on schedule from one message.",        [co("No coordinator to chase.")],f"{M}/scheduler.png", 1.0),
 ("THE LEADS",     [[wo("Sourcing?")],[co("A system.")]],      "Leads are found, enriched and scored before you open your laptop.",[co("No SDR to hire.")],         f"{M}/leadscore.png", 1.0),
 ("THE WORKERS",   [[wo("The team?")],[co("Agents.")]],        "Six agents work in parallel while you do one thing at a time.",    [co("No payroll to run.")],      f"{M}/agents.png",    1.0),
 ("THE GATE",      [[wo("And I approve")],[co("every move.")]],"Nothing ships until you say go. A system, not a free-for-all.",   [co("You stay in control.")],    f"{M}/gate.png",      1.0),
 ("THE OPERATOR",  [[wo("One operator.")],[co("No headcount.")]],"You do not manage people. You run systems from one chat.",       [co("Run it solo.")],            f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("SYSTEMS", [[wo("Want the systems?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="you hire again.",q="Which role would you systemize first?")
