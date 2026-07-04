#!/usr/bin/env python3
# THE $10M OPERATOR STACK - adaptare IG/TikTok in context Ultron (structura din build_aibody.py)
# Source topic: "Everything you need to master in 2026 to build a $10M business."
# Reframe: you don't master 20 skills, you install one operator.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2everythingneedma"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('20 skills to master?')],[co('Install one operator.')]])
T2.CONTENT=[
 ('THE STACK', [[wo('Everyone lists 20 skills')],[co('to hit $10M.')]], 'You do not master twenty things. You install one operator that already holds them.', [co('One install, not twenty.')], f"{M}/stack.png", 1.0),
 ('THE ROADMAP', [[wo('The whole path to')],[co('$10M, one screen.')]], 'Signal, outreach, close, ship, publish. The same loop, run every single day.', [co('One loop, run daily.')], f"{M}/roadmap.png", 1.0),
 ('THE CURVE', [[wo('One operator, not')],[co('a hire per skill.')]], 'Headcount curves up with revenue. An operator stack stays flat, in cents.', [co('Flat cost, cents per run.')], f"{M}/curve.png", 1.0),
 ('THE ROLES', [[wo('Your whole org chart')],[co('reports to you.')]], 'Research, outbound, deals, content, code, legal. Seven agents, zero payroll.', [co('Seven agents, no payroll.')], f"{M}/org.png", 1.0),
 ('THE HANDOFFS', [[wo('Each agent hands off')],[co('to the next.')]], 'Research feeds outreach, outreach feeds deals, deals feed content. It composes.', [co('The work moves itself.')], f"{M}/graph.png", 1.0),
 ('THE MEASURE', [[wo('One founder, output')],[co('of a full team.')]], 'The stack does the work of a headcount of twelve for the cost of your coffee.', [co('12x output, cents in.')], f"{M}/gauge.png", 1.0),
 ('THE VOLUME', [[wo('Thousands of moves')],[co('while you sleep.')]], 'Accounts scored, emails drafted, PRs opened. A handful need your eyes today.', [co('It runs, you review.')], f"{M}/field.png", 1.0),
 ('THE OPERATOR', [[wo('Stop mastering skills.')],[co('Install the operator.')]], 'Agents, loops, memory and a gate wire into one system that reports to you.', [co('One system, one login.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='install the operator.',q='Which skill are you still trying to master by hand?')
MARK2="claude"
