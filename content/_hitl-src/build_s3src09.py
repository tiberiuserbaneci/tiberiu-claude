#!/usr/bin/env python3
# DROP THE REQUEST, GET THE FILE - adaptare IG Scraped (Obsidian vault as business OS) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src09"; LIB=T2.LIB
PREMIUM=1
TITLE="DROP THE REQUEST, GET THE FILE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop chatting with Claude.')],[co('Start filing with it.')]])
T2.CONTENT=[
 ('THE GAP', [[wo('A chat forgets')],[co('everything you said.')]], 'Close the tab and the context is gone. Nothing was ever written down.', [co('No vault, no memory.')], f"{M}/gap.png", 1.0),
 ('THE VAULT', [[wo('Your whole company')],[co('in plain text.')]], 'ICP, pricing, pipeline, offers, voice. Every fact in files an agent can read.', [co('One memory, not many.')], f"{M}/vault.png", 1.0),
 ('THE STRUCTURE', [[wo('Eight folders')],[co('run the business.')]], 'Clients, projects, operations, content, finances, research, queue, generated.', [co('A business, not a brain.')], f"{M}/folders.png", 1.0),
 ('THE QUEUE', [[wo('You drop a request')],[co('as a plain-text file.')]], 'Write what you need into Queue. That note is the whole interface, no dashboard.', [co('That is the only input.')], f"{M}/queue.png", 1.0),
 ('THE AGENTS', [[wo('Seven specialists')],[co('read one vault.')]], 'Cortex, Specter, Striker, Pulse, Sentinel, Amplify, Counsel all draw from it.', [co('Same files, every agent.')], f"{M}/agents.png", 1.0),
 ('THE ROUTER', [[wo('It prices the job')],[co('the tier it actually needs.')]], 'Lite for lookups, Smart for daily work, Deep for hard calls. Cents per run.', [co('Cents, not a seat fee.')], f"{M}/tier.png", 1.0),
 ('THE OUTPUT', [[wo('The finished file')],[co('lands in Generated.')]], 'Drafts, briefs, invoices, sequences. The system files the result back for you.', [co('Output becomes memory.')], f"{M}/generated.png", 1.0),
 ('THE GATE', [[wo('You seal it')],[co('before it ever ships.')]], 'Every external move parks for your tap, then compounds into the next run.', [co('Still your company.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the vault blueprint?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='file your business.',q='What is the first folder you would open?')
MARK2="claude"
