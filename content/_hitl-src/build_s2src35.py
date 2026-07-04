#!/usr/bin/env python3
# THE COMPOUND MEMORY - adaptare IG Scraped in context Ultron (slug s2src35, generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src35"; LIB=T2.LIB
PREMIUM=1
TITLE="THE COMPOUND MEMORY"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Most AI forgets you')],[co('by the next message.')]])
T2.CONTENT=[
 ('THE AMNESIA', [[wo('You re-explain your')],[co('business every time.')]], 'Generic AI starts blank. No client history, no deal context, no memory.', [co('Groundhog Day, daily.')], f"{M}/amnesia.png", 1.0),
 ('THE LOOP', [[wo('Every call and deal')],[co('feeds one core.')]], 'Calls, inboxes, deals and docs land in one memory. Nothing gets dropped.', [co('Captured, not lost.')], f"{M}/capture.png", 1.0),
 ('WEEK ONE', [[wo('It learns who')],[co('you are.')]], 'Who you sell to, what you charge, how you win. The basics, locked in.', [co('The seed is set.')], f"{M}/week1.png", 1.0),
 ('WEEK FOUR', [[wo('It knows your')],[co('clients cold.')]], 'Every account, every thread, every promise made on a call, remembered.', [co('Your whole book, recalled.')], f"{M}/week4.png", 1.0),
 ('WEEK EIGHT', [[wo('It catches what')],[co('you missed.')]], 'Overdue follow-ups, forgotten commitments, dots joined across your pipeline.', [co('It flags before you slip.')], f"{M}/week8.png", 1.0),
 ('THE CURVE', [[wo('It compounds while')],[co('tools reset.')]], 'Every interaction deepens the core. Week over week it gets sharper.', [co('Memory is the moat.')], f"{M}/curve.png", 1.0),
 ('THE AGENTS', [[wo('Seven agents,')],[co('one memory.')]], 'CORTEX, SPECTER, STRIKER and the rest all draw from the same brain.', [co('One core, seven hands.')], f"{M}/agents.png", 1.0),
 ('THE MATH', [[wo('A second brain')],[co('for cents.')]], 'Replaces the CRM, the notetaker and the enrichment tools you stitch together.', [co('Cents per update.')], f"{M}/cents.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the memory')],[co('playbook? comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and let it',l2='remember for you.',q='What would your AI know by week eight?')
MARK2="claude"
