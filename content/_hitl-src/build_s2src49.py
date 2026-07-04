#!/usr/bin/env python3
# YOU ARE NOT AN AI ENGINEER (s2src49) - adaptare IG Scraped in context Ultron (generat manual).
# Sursa: o lista "Top 60 Claude repos / skills / frameworks". Reframe: acele framework-uri sunt
# schele pentru ingineri - le dai star si nu livrezi nimic; Ultron livreaza cei 7 agenti deja
# cablati, rutati, gated, in vocea ta, la centi.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src49"; LIB=T2.LIB
PREMIUM=1
TITLE="YOU ARE NOT AN AI ENGINEER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.TITLE=TITLE
T2.COVER=dict(head=[[wo('You are not')],[co('an AI engineer.')]])
T2.CONTENT=[
 ('THE GRAVEYARD', [[wo('60 starred repos.')],[co('Zero shipped.')]], 'LangGraph, AutoGPT, CrewAI. Frameworks built for engineers, not founders.', [co('Stars are not sales.')], f"{M}/graveyard.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents,')],[co('already wired.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL. No install.', [co('You wire nothing.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('No orchestration')],[co('to write.')]], 'It reads each job, hires the right agent, picks the model tier per turn.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE PRICE', [[wo('Free to star.')],[co('Brutal to run.')]], 'The DIY stack needs infra and an engineer. Ultron runs on cents per token.', [co('Cents, not salaries.')], f"{M}/cents.png", 1.0),
 ('THE GATE', [[wo('Strong body.')],[co('Your reins.')]], 'Every external move parks for your tap. The human gate is already built in.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE MEMORY', [[wo('Persistent state')],[co('you never configure.')]], 'ICP, pipeline, pricing, docs. One core every agent reads from.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE VOICE', [[wo('It writes')],[co('in your voice.')]], 'Sampled from your real posts. Banned words enforced on every draft.', [co('Your voice, multiplied.')], f"{M}/voice.png", 1.0),
 ('THE OPERATOR', [[wo('Close the tabs.')],[co('Open one login.')]], 'Seven agents, one router, one gate, one memory. One place to run it.', [co('One login, whole system.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the stack?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Stop collecting repos.',l2='Run the system.',q='Which agent would you turn on first?')
MARK2="claude"
