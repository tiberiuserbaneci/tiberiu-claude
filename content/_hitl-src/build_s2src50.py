#!/usr/bin/env python3
# THE ASSEMBLY LINE - adaptare IG scraped ("Claude Code into a content machine") in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src50"; LIB=T2.LIB
PREMIUM=1
TITLE="THE CONTENT FACTORY"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One brief in.')],[co('A week of work ships.')]])
T2.CONTENT=[
 ('THE INTAKE', [[wo('You brief it once.')],[co('It runs the line.')]], 'Most founders hand-build every asset. Feed the line one order and the floor runs it.', [co('One order in.')], f"{M}/intake.png", 1.0),
 ('THE ROUTER', [[wo('The line picks')],[co('its own tools.')]], 'It reads each order, assigns the right agent, picks the model tier per job.', [co('Cents per job.')], f"{M}/router.png", 1.0),
 ('SEVEN STATIONS', [[wo('Seven workers.')],[co('One conveyor.')]], 'Research, outbound, deals, content, code, publishing, legal. Each does one thing.', [co('Seven, in sync.')], f"{M}/stations.png", 1.0),
 ('OFF THE BELT', [[wo('One input.')],[co('Every format ships.')]], 'Emails, proposals, posts, briefs, sequences. Finished work, not chat replies.', [co('Assets, not answers.')], f"{M}/output.png", 1.0),
 ('COST PER UNIT', [[wo('A finished asset')],[co('costs you cents.')]], 'Pay per token, per unit. The old stack billed hundreds a seat for the same shift.', [co('Cents, not seats.')], f"{M}/throughput.png", 1.0),
 ('SHARED CORE', [[wo('Every station')],[co('pulls one memory.')]], 'ICP, pipeline, pricing, docs. One warehouse every worker draws from.', [co('Nothing forgets you.')], f"{M}/warehouse.png", 1.0),
 ('SHIPPING BAY', [[wo('Nothing leaves')],[co('without your stamp.')]], 'Every external move parks at the bay for your tap. Augmented, never loose.', [co('Still your company.')], f"{M}/qc.png", 1.0),
 ('ONE FLOOR', [[wo('Stop crafting')],[co('one asset at a time.')]], 'One chat runs intake, routing, stations and shipping as a single floor.', [co('The whole plant, one login.')], f"{M}/factory.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the floor plan?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the whole line.',q='Which asset are you still building by hand?')
MARK2="claude"
