#!/usr/bin/env python3
# OPERATORS NOT STUDENTS - "stop studying AI, start operating it" - IG/TikTok adaptation in Ultron
# context (consumed by adapt_build.py). Panels rendered by s2wantacenext_t3.py into models_clay/s2wantacenext.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2wantacenext"; LIB=T2.LIB
PREMIUM=1
TITLE="OPERATORS NOT STUDENTS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop studying AI.')],[co('Start operating it.')]])
T2.CONTENT=[
 ('THE SPLIT', [[wo('You studied.')],[co('They shipped.')]], 'Most founders read about AI agents. Operators wire them and ship the same week.', [co('Notes ship nothing.')], f"{M}/split.png", 1.0),
 ('THE CLOCK', [[wo('Four hundred hours,')],[co('zero shipped.')]], 'You can study the agent for a year, or run it before lunch. One of those pays.', [co('One day to live.')], f"{M}/clock.png", 1.0),
 ('THE ROSTER', [[wo('Seven hires.')],[co('No onboarding.')]], 'Research, outbound, deals, content, code, legal. A full team, live on day one.', [co('No theory needed.')], f"{M}/roster.png", 1.0),
 ('THE OUTPUT', [[wo('Working systems,')],[co('not notes.')]], 'Each agent ships a real output while you would still be watching the tutorial.', [co('Proof, not certificates.')], f"{M}/stack.png", 1.0),
 ('THE PRICE', [[wo('A course costs $600.')],[co('This costs cents.')]], 'Pay per token. 240 emails drafted for the price of a coffee, no seat fee.', [co('Cents, not courses.')], f"{M}/gauge.png", 1.0),
 ('THE EYES', [[wo('It watches the market')],[co('while you sleep.')]], 'Funding, hiring, rivals, intent. Signals no syllabus will ever teach you.', [co('Overnight, every night.')], f"{M}/radar.png", 1.0),
 ('THE TRUTH', [[wo('Reading is not')],[co('shipping.')]], 'Ten thousand tutorials read. Eight systems live. Only the live ones sent an email.', [co('Close the tab. Ship.')], f"{M}/field.png", 1.0),
 ('THE GATE', [[wo('Seven agents run it.')],[co('You hold the reins.')]], 'The agents do the work. Every external move still parks for your tap.', [co('Augmented, not unsupervised.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the operator kit?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='ship, do not study.',q='What have you studied but never shipped?')
MARK2="claude"
