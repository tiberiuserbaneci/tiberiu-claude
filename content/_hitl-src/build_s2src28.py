#!/usr/bin/env python3
# THE STACK IS NOT A SYSTEM - adaptare IG Scraped ("Top 22 Claude Skills & GitHub Repos") in
# context Ultron (generat pe modelul build_aibody.py). Reframe founder-GTM: nu 22 de repo-uri, un
# singur sistem cablat (7 agenti, ROUTER, cents, HUMAN GATE, memorie).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src28"; LIB=T2.LIB
PREMIUM=1
TITLE="The stack is not a system"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You saved 22 repos.')],[co('Founders ship one system.')]])
T2.CONTENT=[
 ('THE STACK TAX', [[wo('22 repos. Zero revenue.')],[co('You are the glue.')]], 'Every skill, repo and prompt is one more thing you wire, patch and babysit.', [co('The stack is the tax.')], f"{M}/stack.png", 1.0),
 ('THE ROUTER', [[wo('You keep picking models.')],[co('It picks for you.')]], 'It reads each job, hires the right agent, sets the model tier per turn.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('THE SEVEN', [[wo('Not 22 skills.')],[co('Seven agents, wired.')]], 'Research, outbound, deals, content, code, publishing, legal - one roster.', [co('One roster, one login.')], f"{M}/roster.png", 1.0),
 ('CENTS PRICING', [[wo('The stack bills monthly.')],[co('This bills in cents.')]], 'Pay per token. A run that costs a stack ninety dollars costs you a few cents.', [co('Cents per thousand rows.')], f"{M}/cents.png", 1.0),
 ('SYSTEMS, NOT PROMPTS', [[wo('You wrote a prompt.')],[co('It ran a system.')]], 'Plain English in, a composed pipeline of agents out, handing work to each other.', [co('English in, system out.')], f"{M}/system.png", 1.0),
 ('HUMAN GATE', [[wo('Full power.')],[co('Your one tap.')]], 'Every external send parks for your approval. Augmented, never unsupervised.', [co('Nothing sends alone.')], f"{M}/gate.png", 1.0),
 ('SHARED MEMORY', [[wo('22 tools forget you.')],[co('One core remembers.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same memory.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE OPERATOR', [[wo('Stop assembling repos.')],[co('Run the system.')]], 'One chat wires seven agents, router, memory and gate into one operator.', [co('The whole system, one login.')], f"{M}/assemble.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run one system.',q='Still gluing 22 repos together?')
MARK2="claude"
