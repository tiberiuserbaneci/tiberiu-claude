#!/usr/bin/env python3
# THE VAULT THAT READS ITSELF - adaptare IG Scraped (Obsidian second brain) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src15"; LIB=T2.LIB
PREMIUM=1
TITLE="THE VAULT THAT READS ITSELF"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('A second brain that')],[co('reads itself.')]])
T2.CONTENT=[
 ('THE GRAVEYARD', [[wo('You saved 2,700 notes.')],[co('You reopened none.')]], 'A note app stores everything and hands nothing back. The library just grows.', [co('Storage is not memory.')], f"{M}/graveyard.png", 1.0),
 ('THE WEB', [[wo('Every note links to')],[co('every other note.')]], 'Obsidian ties your notes into a web. Nice to look at. Nobody ever walks it.', [co('Links you never follow.')], f"{M}/web.png", 1.0),
 ('THE PILE', [[wo('You do not need')],[co('30 plug-ins.')]], 'Bolting add-ons onto notes is not a brain. The Ultron vault ships wired.', [co('Assembled, not bolted.')], f"{M}/thirty.png", 1.0),
 ('ONE CORE', [[wo('One memory.')],[co('Seven agents read it.')]], 'ICP, pipeline, pricing, docs, past wins. Every agent draws from the same core.', [co('Shared, not siloed.')], f"{M}/sharedcore.png", 1.0),
 ('AUTO-CONTEXT', [[wo('It reads the vault')],[co('before it acts.')]], 'A job comes in and the right context loads itself. No copy-paste, no re-brief.', [co('Context, auto-loaded.')], f"{M}/readjob.png", 1.0),
 ('THE VAULT', [[wo('Not a pile of notes.')],[co('Working memory.')]], 'Your ICP, live pipeline, pricing, product docs and every closed deal, kept current.', [co('Everything it needs.')], f"{M}/vault.png", 1.0),
 ('THE TAX', [[wo('Stop re-explaining')],[co('yourself every task.')]], 'Most tools start from zero, so you paste your business back in each time. Not here.', [co('Re-brief tax: zero.')], f"{M}/tax.png", 1.0),
 ('YOURS', [[wo('One vault.')],[co('Your key.')]], 'Your data, one login, gated by you. Every draw from the vault waits for your tap.', [co('Still your company.')], f"{M}/yours.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the setup?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and give',l2='your agents one memory.',q='What does your second brain actually read back?')
MARK2="claude"
