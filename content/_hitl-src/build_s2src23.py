#!/usr/bin/env python3
# ONE SYSTEM, NOT TEN SKILLS - adaptare IG Scraped (s2src23) in context Ultron (shape build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="ONE SYSTEM, NOT TEN SKILLS"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src23"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You are learning ten AI tools.')],[co('Your company needs one system.')]])
T2.CONTENT=[
 ('THE STACK TAX', [[wo('Ten tabs open.')],[co('None of them talk.')]], 'Every tool is its own login, its own memory, its own bill. Context dies between them.', [co('One system replaces the stack.')], f"{M}/stack.png", 1.0),
 ('THE ROSTER', [[wo('Not ten skills to learn.')],[co('Seven agents that work.')]], 'Research to legal in one roster. Call one by name, or type plain English and it routes.', [co('The whole company, one chat.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('You never pick a model.')],[co('The router does.')]], 'It reads each job and hires the cheapest tier that can do it, Lite Smart or Deep, per turn.', [co('Cents per job, not a flat seat.')], f"{M}/router.png", 1.0),
 ('THE BILL', [[wo('The old stack: hundreds a seat.')],[co('This one bills in cents.')]], 'Pay per token, per job. The scary monthly invoice belongs to the tools you are replacing.', [co('Cents per thousand rows.')], f"{M}/cents.png", 1.0),
 ('THE MEMORY', [[wo('Ten tools forget you.')],[co('One core never does.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same memory, every single turn.', [co('Tell it once. It stays told.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('It drafts everything.')],[co('It sends nothing alone.')]], 'Every email and every external move parks for your tap. Automated, never unsupervised.', [co('Still your name on the send.')], f"{M}/gate.png", 1.0),
 ('THE SYSTEM', [[wo('A prompt gives a reply.')],[co('A system runs the job.')]], 'Research to draft to follow-up to close, chained and repeatable. Not one clever message.', [co('Workflows, not one-off prompts.')], f"{M}/system.png", 1.0),
 ('ONE OPERATOR', [[wo('Stop stacking tools.')],[co('Run one operator.')]], 'Seven agents, one router, one memory, one gate. Plain English in, founder GTM out.', [co('One login runs the company.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the map?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='kill the stack.',q='Which of the ten tools dies first?')
MARK2="claude"
