#!/usr/bin/env python3
# CLIMB PAST THE CHAT BOX - adaptare IG Scraped in context Ultron (generat de adapt_build.py).
# Sursa: "5 Claude tools to learn in 2026" (Chat / Projects / Cowork / Skills / Code) - retold ca
# Ultron: cei mai multi stau in chat, operatorii urca toate cele cinci suprafete.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src01"; LIB=T2.LIB
PREMIUM=1
TITLE="CLIMB PAST THE CHAT BOX"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You use one Claude surface.')],[co('There are five.')]])
T2.CONTENT=[
 ('THE FLOOR', [[wo('Everyone lives in one box.')],[co('Four stay locked.')]], 'Most people only ever open the chat window. Claude has five surfaces above it.', [co('One of five, unlocked.')], f"{M}/floor.png", 1.0),
 ('SURFACE 01', [[wo('Type a question.')],[co('Get an answer.')]], 'Chat is the ground floor. Fast, stateless, forgets you the second you close it.', [co('High speed, low ceiling.')], f"{M}/chat.png", 1.0),
 ('SURFACE 02', [[wo('A chat box that')],[co('remembers you.')]], 'Projects add memory. Your docs, ICP and voice pinned once, then reused on every reply.', [co('Memory changes it all.')], f"{M}/projects.png", 1.0),
 ('SURFACE 03', [[wo('An agent that works')],[co('your real files.')]], 'Cowork runs on your actual workspace. Seven named agents, each one owning a job.', [co('It does, not just talks.')], f"{M}/cowork.png", 1.0),
 ('SURFACE 04', [[wo('Teach your process')],[co('once.')]], 'Skills onboard Claude to how you work, then reuse it on every task without re-explaining.', [co('Taught once, used daily.')], f"{M}/skills.png", 1.0),
 ('SURFACE 05', [[wo('Describe the software.')],[co('Claude builds it.')]], 'Code turns plain English into shipped pages, dashboards and fixes. Tested before it goes live.', [co('Words in, product out.')], f"{M}/code.png", 1.0),
 ('WHEN TO USE EACH', [[wo('One job walks in.')],[co('The right surface answers.')]], 'You should not guess the mode. The router reads the job and opens the surface that fits.', [co('Never pick it yourself.')], f"{M}/router.png", 1.0),
 ('ALL FIVE', [[wo('Most use one.')],[co('Operators climb all five.')]], 'Chat to Projects to Cowork to Skills to Code. Each rung compounds the one below it.', [co('One operator, five surfaces.')], f"{M}/climb.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the surface map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='climb past chat.',q='Which surface are you still stuck on?')
MARK2="claude"
