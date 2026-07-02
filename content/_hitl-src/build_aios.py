#!/usr/bin/env python3
# THE AI OPERATING SYSTEM - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/aios"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Nine tools forgot who I was.')],[co('I quit all nine.')]])
T2.CONTENT=[
 ('THE BOTTLENECK', [[wo('My AI asked who I was.')],[co('For the 40th time.')]], 'Every chat starts from zero. That is the real bottleneck, not the model.', [co('The tab is not a system.')], f"{M}/amnesia.png", 1.0),
 ('THE BRAIN', [[wo('It knows my no-list')],[co('better than my cofounder.')]], 'Your ICP, voice, pricing and pipeline live in one memory, loaded in every run.', [co('Set once. Never re-briefed.')], f"{M}/brain.png", 1.0),
 ('THE DASHBOARD', [[wo('Nine tabs died.')],[co('One screen survived.')]], 'Every agent, flow and approval in one place, built on your own data.', [co('No tab zoo.')], f"{M}/command.png", 1.0),
 ('THE HOURS', [[wo('3am. It closed a task.')],[co('I found out at 7.')]], 'Flows fire on triggers around the clock, even with the laptop shut.', [co('Overnight is work time now.')], f"{M}/always.png", 1.0),
 ('THE MEMORY', [[wo('I say things once.')],[co('That is the whole trick.')]], 'Say no discounts once and the gate blocks them forever.', [co('It compounds monthly.')], f"{M}/rules.png", 1.0),
 ('THE PROOF', [[wo('1,284 companies read.')],[co('My coffee was still hot.')]], 'The OS briefed 200 accounts before the first coffee. One typed sentence.', [co('While you slept.')], f"{M}/proof.png", 1.0),
 ('THE GATE', [[wo('It can do anything.')],[co('It may do nothing alone.')]], 'Nothing external fires alone. You read, you tap, it moves.', [co('Power, gated.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Renters restart daily.')],[co('Owners compound.')]], 'One subscription, one memory, one command center behind a chat.', [co('Build yours today.')], f"{M}/own.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save this to',l2='own your OS.',q='Rented tools or your own command center?')
MARK2="claude"
