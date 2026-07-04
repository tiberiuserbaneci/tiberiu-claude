#!/usr/bin/env python3
# YOU ARE THE BOARD NOW - adaptare IG Scraped in context Ultron (org-chart of agents / accountability)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src46"; LIB=T2.LIB
PREMIUM=1
TITLE="You are the board now"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do every job yourself.')],[co('Promote yourself to the board.')]])
T2.CONTENT=[
 ('THE MESS', [[wo('Twenty tabs.')],[co('Zero accountability.')]], 'A dozen disconnected AI tabs, each forgetting the last, none reporting to you.', [co('Nobody is in charge.')], f"{M}/chaos.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents.')],[co('One founder.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL. A named team, not a chat box.', [co('Each one a slash away.')], f"{M}/orgchart.png", 1.0),
 ('THE CHAIR', [[wo('One chair reads the job')],[co('and assigns it.')]], 'The ROUTER hands each task to the right agent and the cheapest model tier that can do it.', [co('Cents per turn, not dollars.')], f"{M}/router.png", 1.0),
 ('THE BOOKS', [[wo('Every move')],[co('costs cents.')]], 'Spend tracked down to the token. The old stack billed you nine hundred a month for the same work.', [co('Priced by the token.')], f"{M}/ledger.png", 1.0),
 ('THE RECORD', [[wo('Nobody forgets')],[co('the last meeting.')]], 'ICP, pipeline, pricing and docs live in one core every agent reads before it acts.', [co('One memory, seven hands.')], f"{M}/memory.png", 1.0),
 ('THE APPROVAL', [[wo('Nothing ships')],[co('without your sign-off.')]], 'Every external send parks at the HUMAN GATE and waits for one tap from you.', [co('You still run the company.')], f"{M}/gate.png", 1.0),
 ('THE PLAYBOOK', [[wo('You save systems,')],[co('not prompts.')]], 'Wire a sequence once and it reruns on every account. A chat you retype dies at the tab.', [co('Built once, runs forever.')], f"{M}/systems.png", 1.0),
 ('THE BOARD', [[wo('A company of agents,')],[co('one login.')]], 'You set the goals and approve the work. The team researches, writes, closes and ships.', [co('You are the board now.')], f"{M}/board.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='take the board seat.',q='Which agent would you hire first?')
MARK2="claude"
