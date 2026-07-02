#!/usr/bin/env python3
# THE CONTENT TEAM - gleam of catalin's "I replaced my 70K creative team with skills" reference.
# 1080x1350 3D. Writer, designer, scheduler, deliverability - one chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M=f"{T2.OBJ}/models_25d"; LIB=T2.LIB
T2.ACCENT=(200,70,35); T2.CORAL=T2.ACCENT   # per-material accent (anti-sameness)
T2.COVER_OBJ="/home/user/tiberiu-claude/content/_hitl-src/covers/contentteam.png"  # Vertex real-logo cover visual
T2.OBJ_THR=30   # front-on 2.5D windows: whole window+shadow bbox

T2.COVER=dict(head=[[wo("I replaced my")],[co("content team.")]])
T2.CONTENT=[
 ("THE CALENDAR", [[wo("The whole plan?")],[co("One chat.")]],   "A week of posts, carousels and reels planned across channels.",    [co("14 scheduled.")],         f"{M}/content.png",   1.0),
 ("THE DESIGNER", [[wo("The designer?")],[co("One chat.")]],     "On-brand posts, carousels and covers out of the same chat.",        [co("No designer to brief.")], f"{M}/designer.png",  1.0),
 ("THE WRITER",   [[wo("The copywriter?")],[co("One chat.")]],   "Ranked, on-voice copy written straight from the chat.",             [co("No writer to pay.")],     f"{M}/seowriter.png", 1.0),
 ("THE DRAFTS",   [[wo("The whole team?")],[co("Agents.")]],       "Several drafts written in parallel while you approve the best.",     [co("No coordinator.")],       f"{M}/agents.png",    1.0),
 ("THE INBOXING", [[wo("Newsletters?")],[co("They land.")]],     "Domains warm and mail lands in the inbox, not spam.",               [co("99.2% inboxed.")],        f"{M}/warmup.png",    1.0),
 ("THE SKILLS",   [[wo("The whole desk?")],[co("Ten skills.")]], "Every content function installed as a skill under one chat.",       [co("10 installed.")],         f"{M}/skills.png",    1.0),
 ("THE GATE",     [[wo("And I approve")],[co("every post.")]],   "Nothing publishes until you say go. You are the editor.",           [co("You approve every post.")],f"{M}/gate.png",     1.0),
 ("THE OPERATOR", [[wo("A creative team.")],[co("One chat.")]],  "A full content team, for the price of a chat, not a payroll.",      [co("Run it solo.")],          f"{M}/ultron_real.png",    1.0),
]
T2.CTA=("CONTENT", [[wo("Want the desk?")],[co("comment OPERATOR.")]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1="Save this before",l2="you hire a team.",q="Which content role eats your week?")

MARK2="claude"
