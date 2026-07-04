#!/usr/bin/env python3
# SYSTEMS NOT PROMPTS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="SYSTEMS, NOT PROMPTS"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src02"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop engineering prompts.')],[co('Ship the whole system.')]])
T2.CONTENT=[
 ('THE FRAME', [[wo('You are still')],[co('prompting.')]], 'Operators stopped writing prompts. They run pre-built systems that ship the work.', [co('Prompts do not scale.')], f"{M}/frame.png", 1.0),
 ('THE STACK', [[wo('Seven agents are')],[co('the whole stack.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL. Research to close, one roster.', [co('Not one more tool.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('One plain line')],[co('picks the agent.')]], 'Type what you need. The router hires the right agent and the cheapest model tier that can do it.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE EYES', [[wo('It saw the round')],[co('before my VC did.')]], 'Funding, hiring, stack changes, intent. CORTEX watches the live web, not last year data.', [co('Overnight, every night.')], f"{M}/signals.png", 1.0),
 ('THE GATE', [[wo('Every send waits')],[co('for your tap.')]], 'SPECTER drafts the full sequence. Nothing leaves the building until you approve it.', [co('Still your company.')], f"{M}/sequence.png", 1.0),
 ('THE PROOF', [[wo('Twelve hundred')],[co('accounts, watched.')]], 'It scans your whole market each morning and lights only the ones that moved today.', [co('Signal, not noise.')], f"{M}/proof.png", 1.0),
 ('THE PRICE', [[wo('The old stack')],[co('cost you thousands.')]], 'Ultron runs pay-per-token. A full research brief lands for cents, not a seat license.', [co('Cents, not dollars.')], f"{M}/cents.png", 1.0),
 ('THE OPERATOR', [[wo('Stop wiring prompts.')],[co('Run the system.')]], 'One login composes every agent, one shared memory, one gate. The whole operator, assembled.', [co('The full system, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the system map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the whole system.',q='Which prompt are you still writing by hand?')
MARK2="claude"
