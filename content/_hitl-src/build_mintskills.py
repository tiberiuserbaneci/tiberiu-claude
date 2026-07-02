#!/usr/bin/env python3
# MINT YOUR OWN SKILLS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/mintskills"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop downloading skills.')],[co('Start minting your own.')]])
T2.CONTENT=[
 ('THE ADMISSION', [[wo('Building agents')],[co('was the wrong move.')]], 'Even Anthropic says it now: the unit of leverage is the skill, not the mega-agent.', [co('Smaller is the fix.')], f"{M}/admission.png", 1.0),
 ('THE STACK', [[wo('Five folders.')],[co('One SKILL file.')]], 'That is the entire anatomy of a skill. No graphs, no framework, no PhD.', [co('Small enough to own.')], f"{M}/folders.png", 1.0),
 ('THE ORE', [[wo('Your best workflow')],[co('is the raw material.')]], 'The proposal you always write the same way. The audit you repeat monthly.', [co('You already have it.')], f"{M}/ore.png", 1.0),
 ('THE MINT', [[wo('Discover. Scaffold.')],[co('Distill. Audit.')]], 'Four passes and the workflow becomes a command anyone on your desk can run.', [co('Ten minutes flat.')], f"{M}/mint.png", 1.0),
 ('THE VOICE', [[wo('A downloaded skill')],[co('writes like everyone.')]], 'A minted one carries your rules, your no-list, your phrasing. Unfair by design.', [co('Yours cannot be copied.')], f"{M}/voice.png", 1.0),
 ('THE SHELF', [[wo('Six skills minted')],[co('from my own desk.')]], 'Proposal, audit, brief, pricing, follow-up, report: each one born from a repeated job.', [co('My playbook, executable.')], f"{M}/shelf.png", 1.0),
 ('THE COMPOUND', [[wo('Every correction')],[co('hardens the skill.')]], 'Fix it once, the skill remembers forever. Month three runs sharper than month one.', [co('Assets, not chores.')], f"{M}/compound.png", 1.0),
 ('THE SHIFT', [[wo('Downloaders collect.')],[co('Minters compound.')]], 'The library you make beats the library you save.', [co('Cast the first one tonight.')], f"{M}/shift.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the minting steps',l2='and cast your first one.',q='Which workflow would you mint?')
MARK2="claude"
