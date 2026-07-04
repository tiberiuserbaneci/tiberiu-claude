#!/usr/bin/env python3
# THE WEEKEND INSTALL - adaptare IG Scraped ("10 free courses on Claude, this weekend") in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="THE WEEKEND INSTALL"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src30"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Ten tabs of AI courses.')],[co('Zero systems shipped.')]])
T2.CONTENT=[
 ('THE STACK', [[wo('Ten courses, a weekend gone.')],[co('One system, a weekend live.')]], 'Skip the syllabus. Wire the seven agents, the router and the gate once.', [co('A stack, not a playlist.')], f"{M}/install.png", 1.0),
 ('THE ROUTER', [[wo('A brain that budgets')],[co('its own thinking.')]], 'It reads each job, hires the right agent, picks the model tier per turn.', [co('Cents per run, not dollars.')], f"{M}/router.png", 1.0),
 ('CORTEX', [[wo('It ranked 400 accounts')],[co('while I slept.')]], 'CORTEX profiles people, companies and markets into one scored brief.', [co('Research, already sorted.')], f"{M}/cortex.png", 1.0),
 ('SPECTER', [[wo('Two hundred cold emails.')],[co('One sequence, my voice.')]], 'SPECTER drafts the opener, the follow-ups and the whole multi-step chase.', [co('Outbound that runs itself.')], f"{M}/specter.png", 1.0),
 ('STRIKER', [[wo('Every deal knows')],[co('its own next move.')]], 'STRIKER qualifies, handles objections and builds the close plan per deal.', [co('Pipeline that thinks.')], f"{M}/striker.png", 1.0),
 ('PULSE', [[wo('It stole my writing style.')],[co('I approved.')]], 'PULSE samples your real posts and drafts in your voice, banned words enforced.', [co('Your voice, multiplied.')], f"{M}/pulse.png", 1.0),
 ('THE GATE', [[wo('Strong body.')],[co('My reins.')]], 'Every external move parks for your tap. Memory holds ICP, pipeline, pricing.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop collecting courses.')],[co('Assemble the operator.')]], 'One chat wires research, outbound, deals, content and code into one system.', [co('The whole stack, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the install list?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='install it this weekend.',q='Which module do you wire first?')
MARK2="claude"
