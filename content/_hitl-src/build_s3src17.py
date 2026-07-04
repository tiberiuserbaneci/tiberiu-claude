#!/usr/bin/env python3
# STARRED, NOT SHIPPED - adaptare IG Scraped s3src17 ("10 GitHub repos worth starring") in context
# Ultron: un star e un bookmark, zece repo-uri sunt piese nelegate, iar munca reala e asamblarea -
# Ultron livreaza echipa deja cablata si pornita.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src17"; LIB=T2.LIB
PREMIUM=1
TITLE="STARRED, NOT SHIPPED"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You starred ten repos.')],[co('You shipped nothing.')]])
T2.CONTENT=[
 ('THE STAR', [[wo('A star is a save.')],[co('Not a system.')]], 'One click stars the repo. Nothing is deployed, wired or running.', [co('A bookmark, not a build.')], f"{M}/star.png", 1.0),
 ('THE PILE', [[wo('Ten repos.')],[co('Zero wired together.')]], 'Each project is a loose part with a dangling wire. Ten do not connect themselves.', [co('Assembly not included.')], f"{M}/pile.png", 1.0),
 ('THE GAP', [[wo('The gap is the work.')],[co('Not the star.')]], 'Clone, install, configure, wire, host, patch. Weeks of assembly stand between star and running.', [co('Free star, heavy build.')], f"{M}/gap.png", 1.0),
 ('THE ROUTER', [[wo('One line hires')],[co('the right agent.')]], 'Type the job in plain English. The router picks the agent and the cheapest model that can do it.', [co('You never wire a thing.')], f"{M}/router.png", 1.0),
 ('THE CREW', [[wo('Seven agents,')],[co('already talking.')]], 'Research, outbound, deals, content, code, publishing, legal. Wired to each other on day one.', [co('The crew comes assembled.')], f"{M}/team.png", 1.0),
 ('THE MEMORY', [[wo('Ten repos forget you.')],[co('One vault does not.')]], 'ICP, pipeline, pricing and docs in one core every agent reads from, every run.', [co('Nothing restarts from zero.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Full power.')],[co('Held on your tap.')]], 'Every send, deal and deploy parks for your approval before it moves.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('No clone. No install.')],[co('Already running.')]], 'You open one login and the operator is already researching, writing and shipping.', [co('Stars saved. This ships.')], f"{M}/running.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the assembly?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Stop collecting stars.',l2='Run the operator.',q='How many of your stars are running right now?')
MARK2="claude"
