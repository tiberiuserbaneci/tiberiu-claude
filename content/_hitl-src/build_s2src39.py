#!/usr/bin/env python3
# THE ASSEMBLY LINE (s2src39) - adaptare IG Scraped ("Claude Code + NotebookLM" pipeline cheatsheet)
# in context Ultron: one plain-English ask travels the founder-GTM production line to a sourced,
# gated deliverable, priced in cents. Generat in stilul build_aibody.py.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src39"; LIB=T2.LIB
PREMIUM=1
TITLE="THE ASSEMBLY LINE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You typed one sentence.')],[co('It shipped a sourced brief.')]])
T2.CONTENT=[
 ('THE ASK', [[wo('One line in.')],[co('Not a prompt.')]], 'Plain English, once. No prompt engineering, no picking a model, no copy-paste.', [co('Type it. Walk away.')], f"{M}/ask.png", 1.0),
 ('THE ROUTER', [[wo('It hires the crew')],[co('for you.')]], 'Reads the job, hands each step to the right agent, picks the tier per turn.', [co('You pick nothing.')], f"{M}/route.png", 1.0),
 ('THE RESEARCH', [[wo('The web, ranked')],[co('into one page.')]], 'CORTEX reads competitors, funding, hiring and filings, then ranks the fits.', [co('No tabs. No reading.')], f"{M}/research.png", 1.0),
 ('THE SYSTEM', [[wo('A saved pipeline.')],[co('Not a throwaway prompt.')]], 'The whole run is stored. Next week the same ask reruns itself in one click.', [co('Systems, not prompts.')], f"{M}/workflow.png", 1.0),
 ('THE DRAFT', [[wo('It writes')],[co('in your voice.')]], 'PULSE samples your real posts and enforces your banned words on every line.', [co('96% you. Zero hedging.')], f"{M}/draft.png", 1.0),
 ('THE MEMORY', [[wo('One core')],[co('feeds every stage.')]], 'ICP, pipeline, pricing and docs. It never re-asks who you sell to.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Finished.')],[co('Then it stops.')]], 'Twenty emails ready, parked. Nothing sends until you tap approve.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('THE PRICE', [[wo('The stack it kills')],[co('cost thousands.')]], 'Clay, Apollo, an SDR agency, a RevOps hire. This whole run costs cents.', [co('Twenty-four cents. One run.')], f"{M}/cost.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the pipeline?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the line once.',q='What would you ask it to build first?')
MARK2="claude"
