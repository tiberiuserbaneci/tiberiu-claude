#!/usr/bin/env python3
# ONE OPERATOR OVER A TOOL ZOO - adaptare IG/TikTok in context Ultron (generat de adapt_build.py)
# Reframe: stop juggling ten AI tools; one Ultron operator, the ROUTER picks model/agent per job.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="ONE OPERATOR, NOT TEN TABS"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2aitoolsdifferent"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Ten AI tabs open.')],[co('Operators run one.')]])
T2.CONTENT=[
 ('THE ZOO', [[wo('One tab per job.')],[co('That is the trap.')]], 'ChatGPT here, Claude there, Gemini for the rest. Ten logins, ten bills, ten tabs.', [co('One login instead.')], f"{M}/toolzoo.png", 1.0),
 ('THE ROUTER', [[wo('One router reads')],[co('every job.')]], 'It hires the right agent and picks the model tier per turn, so you never pick a tool.', [co('You never pick a tool.')], f"{M}/router.png", 1.0),
 ('THE WATCH', [[wo('It runs every job')],[co('at once.')]], 'Research, outreach, deals, content, legal. One operator, not ten tabs you switch between.', [co('Nothing waits its turn.')], f"{M}/radar.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents.')],[co('One login.')]], 'CORTEX, SPECTER, STRIKER, PULSE and the rest, under one roof and one subscription.', [co('Not ten subscriptions.')], f"{M}/stack.png", 1.0),
 ('THE PRICE', [[wo('The whole zoo,')],[co('for cents.')]], 'Pay per token, cents per job. The ten-tool stack it replaces cost hundreds a month.', [co('Cents, not flat fees.')], f"{M}/gauge.png", 1.0),
 ('THE VOLUME', [[wo('Every job routed')],[co('from one thread.')]], 'A thousand small jobs a month, each sent to the cheapest tier that can actually do it.', [co('One place, all of it.')], f"{M}/field.png", 1.0),
 ('THE CORE', [[wo('One core.')],[co('Every agent.')]], 'Shared memory feeds all seven agents, and every external move waits for your tap.', [co('Gated, never loose.')], f"{M}/hub.png", 1.0),
 ('THE OPERATOR', [[wo('Close nine tabs.')],[co('Keep one operator.')]], 'Your whole day on one thread, instead of switching between ten different AI tools.', [co('One operator, one login.')], f"{M}/timeline.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Ready to consolidate?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='close the other nine tabs.',q='Which tab would you kill first?')
MARK2="claude"
