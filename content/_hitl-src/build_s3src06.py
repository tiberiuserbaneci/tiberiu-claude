#!/usr/bin/env python3
# A SECOND BRAIN THAT CLOSES - adapts the "Obsidian workflow plugins / connected second brain" IG
# carousel into Ultron: scattered notes vs a connected memory graph that seven agents actually act on.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src06"; LIB=T2.LIB
PREMIUM=1
TITLE="A SECOND BRAIN THAT CLOSES"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your notes just sit there.')],[co('A second brain that closes.')]])
T2.CONTENT=[
 ('THE PILE', [[wo('Notes that never')],[co('connect.')]], 'Docs, tabs and CRM fields. Linear, disconnected, nothing ever acts on them.', [co('It just sits there.')], f"{M}/pile.png", 1.0),
 ('THE GRAPH', [[wo('Everything wired')],[co('to one core.')]], 'Briefs, contacts, deals and docs, linked into one living memory graph.', [co('Connected, not scattered.')], f"{M}/graph.png", 1.0),
 ('THE MEMORY', [[wo('It never forgets')],[co('a single thing.')]], 'Every session writes back to the same vault. Your context compounds daily.', [co('Nothing resets to zero.')], f"{M}/memory.png", 1.0),
 ('THE ROSTER', [[wo('Seven hands')],[co('on your notes.')]], 'Research, outbound, deals, content, code, publishing and legal, all reading one graph.', [co('A team, not a tab.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('Plain English in.')],[co('The right agent out.')]], 'One line of intent. The router hires the agent and the cheapest tier that works.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('THE WASTE', [[wo('You use a fraction')],[co('of what you hold.')]], 'A knowledge base full of power. Almost none of it is ever wired to act.', [co('Latent, until now.')], f"{M}/waste.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Sequences, posts and emails queue for approval. You stay the operator.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE PAYOFF', [[wo('It ships work,')],[co('not just notes.')]], 'A brief, a sequence, a proposal. Out the door while you run the day.', [co('Knowledge that acts.')], f"{M}/payoff.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the wiring?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='wire your knowledge.',q='What is your knowledge actually doing for you?')
MARK2="claude"
