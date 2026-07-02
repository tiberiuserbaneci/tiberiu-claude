#!/usr/bin/env python3
# SEVEN LEVELS OF ULTRON - gleam of catalin's "7 Levels of Ultron" reference.
# 1080x1350 3D. Most founders stop at level 2; the operators reach level 7.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/levels"; LIB=T2.LIB
PREMIUM=1   # coded clay3d panels
T2.ACCENT=(204,120,92); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/levels.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("Most stop")],[co("at level 2.")]])
T2.CONTENT=[
 ("THE LADDER",   [[wo("Seven levels.")],[co("You: level 5.")]], "Ask, chain, run an agent, wire them, automate, approve, then run it all.",[co("Climb one a week.")],  f"{M}/levels.png",    1.0),
 ("LEVEL 3",      [[wo("Level 3?")],[co("Run an agent.")]],      "Hand a whole job to one named agent instead of typing every step.",[co("It goes and finds it.")], f"{M}/apollo.png",    1.0),
 ("LEVEL 4",      [[wo("Level 4?")],[co("Wire them.")]],         "Agents hand off to each other, six working at once, in parallel.", [co("A team of agents.")],     f"{M}/agents.png",    1.0),
 ("LEVEL 5",      [[wo("Level 5?")],[co("Automate.")]],          "Workflows fire on triggers all day, no prompt, no reminder.",      [co("Set once, runs daily.")], f"{M}/workflows.png", 1.0),
 ("LEVEL 6",      [[wo("Level 6?")],[co("Approve, do not do.")]],"Your systems update the pipeline; you only say yes or no.",         [co("You stop doing.")],       f"{M}/hubspot.png",   1.0),
 ("LEVEL 7",      [[wo("Level 7?")],[co("Run the company.")]],   "The whole business runs behind a chat, and the numbers climb.",    [co("$48k MRR, one operator.")],f"{M}/revenue.png",  1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every move.")]],   "At every level, nothing ships until you say go.",                  [co("You stay in control.")],  f"{M}/gate.png",      1.0),
 ("THE OPERATOR", [[wo("Level 7.")],[co("One operator.")]],      "The top level is one person running the whole thing from one chat.",[co("Run it solo.")],         f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("LEVELS", [[wo("Want the map?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this and",l2="climb a level.",q="What level are you stuck on?")


MARK2="orb"
