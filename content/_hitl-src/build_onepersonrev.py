#!/usr/bin/env python3
# THE 1-PERSON REVENUE STACK - gleam of catalin's "$0K 1-person business stack" reference.
# 1080x1350 3D. One operator, real revenue, the whole money engine behind one chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(212,162,127); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/onepersonrev.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("One operator.")],[co("Real revenue.")]])
T2.CONTENT=[
 ("THE NUMBER",   [[wo("The result?")],[co("$48k MRR.")]],       "One person, up 32% this month, no team on the payroll.",           [co("Solo, not small.")],      f"{M}/revenue.png",   1.0),
 ("THE PAYMENTS", [[wo("Getting paid?")],[co("Automatic.")]],    "Invoices, subscriptions and receipts run without a finance seat.", [co("No bookkeeper.")],        f"{M}/stripe.png",    1.0),
 ("THE LEADS",    [[wo("Filling the pipe?")],[co("A system.")]], "Leads sourced, enriched and scored before you open your laptop.",  [co("471 scored, 63 hot.")],   f"{M}/leadscore.png", 1.0),
 ("THE DEALS",    [[wo("Closing?")],[co("Self-updating.")]],     "The pipeline moves as replies land. Nobody drags a card.",         [co("No ops seat.")],          f"{M}/hubspot.png",   1.0),
 ("THE CALLS",    [[wo("Booking?")],[co("Handled.")]],           "Replies become calls on your calendar, no back and forth.",        [co("63 booked.")],            f"{M}/calendly.png",  1.0),
 ("THE CADENCE",  [[wo("Marketing?")],[co("Queued.")]],          "A week of content posts on schedule from one message.",            [co("No coordinator.")],       f"{M}/scheduler.png", 1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every move.")]],   "The money engine runs, but nothing ships until you say go.",       [co("You stay in control.")],  f"{M}/gate.png",      1.0),
 ("THE OPERATOR", [[wo("No headcount.")],[co("Just cents.")]],   "The whole revenue stack runs behind one subscription, for cents.", [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("STACK", [[wo("Want the stack?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this to",l2="run lean.",q="What is your one-person MRR goal?")

MARK2="strip"
