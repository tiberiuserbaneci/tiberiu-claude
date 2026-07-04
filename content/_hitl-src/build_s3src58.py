#!/usr/bin/env python3
# THE 10X SETUP - adaptare IG Scraped s3src58 in context Ultron ("5 moves decide whether Claude Code
# 10x's your output"). Angle: the 5 CONFIG DECISIONS you make at setup, each its own move/panel.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src58"; LIB=T2.LIB
PREMIUM=1
TITLE="THE 10X SETUP"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('5 moves decide')],[co('if Claude Code 10x you.')]])
T2.CONTENT=[
 ('THE DIFFERENCE', [[wo('Same Claude.')],[co('10x gap.')]], 'You are not bad at this. Most people drive it like a chatbot, one vague line at a time.', [co('It is a setup problem.')], f"{M}/split.png", 1.0),
 ('MOVE 1', [[wo('Write a brief,')],[co('not a one-liner.')]], 'Give it scope, the files, what NOT to touch, and what done looks like. A vague line gets a vague guess.', [co('Scope in, guess out.')], f"{M}/brief.png", 1.0),
 ('MOVE 2', [[wo('Give it a memory')],[co('so it stops guessing.')]], 'One rules file holds your stack, style, hard NOs and your bar for done. Loaded once, every session.', [co('Never re-explain yourself.')], f"{M}/memory.png", 1.0),
 ('MOVE 3', [[wo('Let it use')],[co('real tools.')]], 'Wire it to your repo, your tests and a browser. It runs and checks, it does not guess from memory.', [co('Hands, not just talk.')], f"{M}/tools.png", 1.0),
 ('MOVE 4', [[wo('Install guards')],[co('that block bad work.')]], 'Hooks that fail off-spec output at the door: wrong dimensions, wrong palette, dead space.', [co('Nothing bad reaches you.')], f"{M}/guards.png", 1.0),
 ('MOVE 5', [[wo('Approve the plan,')],[co('not every keystroke.')]], 'Read one plan, tap once, let it run all the steps. Stop babysitting every single line.', [co('Gate the plan, walk away.')], f"{M}/plan.png", 1.0),
 ('THE PAYOFF', [[wo('Five moves,')],[co('ten times out.')]], 'Refactors, dashboards and bug batches ship clean the first pass. Same day, same model.', [co('The setup is the multiplier.')], f"{M}/payoff.png", 1.0),
 ('THE OPERATOR', [[wo('Or ship all five')],[co('at once.')]], 'Brief, memory, tools, guards and a gate, wired in: seven agents, a router and your approval.', [co('One operator, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the 5-move setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the five moves.',q='Which move are you skipping right now?')
MARK2="claude"
