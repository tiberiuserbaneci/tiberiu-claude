#!/usr/bin/env python3
# SIXTEEN TABS OR ONE SYSTEM - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src29"; LIB=T2.LIB
TITLE="SIXTEEN TABS OR ONE SYSTEM"
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You bolted 16 tools onto Claude.')],[co('Operators wired one system.')]])
T2.CONTENT=[
 ('STACK VS SYSTEM', [[wo('Sixteen tabs.')],[co('Still not a system.')]], 'MCP servers, repos, wrappers. Sixteen logins that never talk to each other.', [co('One replaces the pile.')], f"{M}/stack.png", 1.0),
 ('THE ROSTER', [[wo('Not one bot.')],[co('Seven specialists.')]], 'Research, outbound, deals, content, code, publishing, legal. Each owns its job.', [co('Seven hires, one login.')], f"{M}/agents.png", 1.0),
 ('THE ROUTER', [[wo('You never pick a model.')],[co('It budgets the thinking.')]], 'Reads each job, hires the right agent, picks the cheapest tier that can do it.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('THE BILL', [[wo('Their stack bills dollars.')],[co('Ours bills cents.')]], 'The 16-tool stack is a monthly invoice. Ultron charges cents per task, per token.', [co('Pay for work, not seats.')], f"{M}/cents.png", 1.0),
 ('HUMAN GATE', [[wo('Full power.')],[co('Parked on your tap.')]], 'Every email, deal move and deploy waits in a queue until you approve it.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('SHARED MEMORY', [[wo('Sixteen tools forget you.')],[co('One core never does.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same memory.', [co('Nothing repeats itself.')], f"{M}/memory.png", 1.0),
 ('SYSTEMS NOT PROMPTS', [[wo('Stop pasting prompts.')],[co('Save the system.')]], 'A sequence you run once and rerun forever. Steps chained, not copied by hand.', [co('Build once, reuse it.')], f"{M}/systems.png", 1.0),
 ('ONE LOGIN', [[wo('Close the 16 tabs.')],[co('Open one operator.')]], 'One chat routes to every agent, holds the memory, waits at the gate.', [co('The whole stack, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the operator playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='close the other 15 tabs.',q='How many tools are you paying for that never talk?')
MARK2="claude"
