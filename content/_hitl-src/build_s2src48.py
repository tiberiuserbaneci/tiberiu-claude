#!/usr/bin/env python3
# NOTHING TO INSTALL - adaptare IG Scraped (Claude Code + Remotion skill install) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src48"; LIB=T2.LIB
PREMIUM=1
TITLE="NOTHING TO INSTALL"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You installed the skill.')],[co('Who runs the job?')]])
T2.CONTENT=[
 ('THE GAP', [[wo('You installed the skill.')],[co('You still ran the job.')]], 'A skill adds one trick to a chatbox. It does not source, write, qualify or ship.', [co('A trick is not an operator.')], f"{M}/install.png", 1.0),
 ('THE SETUP', [[wo('One command to install.')],[co('A week to wire.')]], 'Keys, configs, updates, glue between every tool. You quietly became devops.', [co('The setup is the second job.')], f"{M}/glue.png", 1.0),
 ('THE ROUTER', [[wo('Nothing to install.')],[co('You just talk.')]], 'Plain English in. It reads the job, hires the agent and picks the model tier per turn.', [co('No skills to manage.')], f"{M}/router.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents.')],[co('Already wired.')]], 'Research, outbound, deals, content, code, publishing, legal. Pre-built, not bolted on.', [co('A team, not a plugin.')], f"{M}/roster.png", 1.0),
 ('THE BILL', [[wo('The skill was free.')],[co('The stack was not.')]], 'A wall of subscriptions to run one funnel. Ultron runs the same job for cents.', [co('Cents per run, not seats.')], f"{M}/cents.png", 1.0),
 ('THE MEMORY', [[wo('A skill forgets you.')],[co('The system will not.')]], 'ICP, pipeline, pricing and docs live in one core every agent reads from.', [co('One core, every agent.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('It can send.')],[co('It waits for your tap.')]], 'Every external move parks at a human gate. Powerful, never unsupervised.', [co('Still your name on it.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop collecting skills.')],[co('Run a company.')]], 'One login wires research, outbound, deals and content into one operator.', [co('The whole job, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop installing tricks.',q='What are you still wiring by hand?')
MARK2="claude"
