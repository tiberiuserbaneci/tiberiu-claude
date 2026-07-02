#!/usr/bin/env python3
# AN AGENT, NOT A CHATBOT - gleam of catalin's "Ultron: an agent, not a chatbot" reference.
# 1080x1350 3D. A chatbot answers; an agent does the work and remembers.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(200,70,35); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/agentchatbot.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("Yours answers.")],[co("Mine works.")]])
T2.CONTENT=[
 ("THE RUNS",     [[wo("A chatbot talks.")],[co("This runs.")]], "Six agents work in parallel while you do one thing at a time.",    [co("Live, not a reply box.")],f"{M}/agents.png",    1.0),
 ("THE SYSTEMS",  [[wo("It keeps going")],[co("without you.")]], "Workflows fire on their own triggers all day, no prompt needed.",  [co("Set once, runs daily.")], f"{M}/workflows.png", 1.0),
 ("THE RESEARCH", [[wo("It goes")],[co("and finds it.")]],       "It pulls live account data instead of guessing from memory.",      [co("Real data, not vibes.")], f"{M}/apollo.png",    1.0),
 ("THE PIPELINE", [[wo("It updates")],[co("your systems.")]],    "Deals move in your CRM as replies land. A chatbot cannot do that.",[co("It acts on tools.")],     f"{M}/hubspot.png",   1.0),
 ("THE OUTPUT",   [[wo("It ships")],[co("real revenue.")]],      "The work turns into booked calls and closed deals, not just text.",[co("$48k MRR, one operator.")],f"{M}/revenue.png",  1.0),
 ("THE OUTREACH", [[wo("It sends,")],[co("not suggests.")]],     "The whole sequence is written and sent, not pasted for you to send.",[co("No copy-paste.")],      f"{M}/gmail_sent.png",1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every move.")]],   "It acts, but nothing ships until you say go. You stay in control.",[co("You approve every send.")],f"{M}/gate.png",    1.0),
 ("THE OPERATOR", [[wo("Not a chatbot.")],[co("An operator.")]], "It runs the company behind a single subscription, all day.",       [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("OPERATOR", [[wo("Want the agent?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this if you",l2="still just chat.",q="Chatbot or operator, which do you run?")

MARK2="strip"
