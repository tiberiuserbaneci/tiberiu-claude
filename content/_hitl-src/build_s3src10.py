#!/usr/bin/env python3
# THE HOUSE RECIPE - adaptare IG Scraped (s3src10, NotebookLM->Claude "Skills Factory") in context Ultron.
# Narrow reframe: distill your best sources ONCE into a grounded recipe your whole agent roster reuses.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src10"; LIB=T2.LIB
PREMIUM=1
TITLE="THE HOUSE RECIPE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Distill it once.')],[co('Reuse it forever.')]])
T2.CONTENT=[
 ('THE SOURCES', [[wo('Your best thinking')],[co('is scattered.')]], 'Pull your real playbooks, docs and call notes into one place.', [co('Curated, not scraped.')], f"{M}/sources.png", 1.0),
 ('THE DISTILL', [[wo('Distill it into')],[co('one recipe.')]], 'Hours of sources become one page an agent can actually follow.', [co('One file. One skill.')], f"{M}/distill.png", 1.0),
 ('GROUNDED', [[wo('Every step traces')],[co('to a source.')]], 'Written only from what you fed it. No invented steps, no drift.', [co('Zero hallucination.')], f"{M}/grounded.png", 1.0),
 ('THE SHELF', [[wo('One recipe')],[co('per job.')]], 'Cold email, proposal, FAQ, contract clause. A shelf of grounded recipes.', [co('A skill for each job.')], f"{M}/shelf.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents,')],[co('one recipe.')]], 'CORTEX, SPECTER, STRIKER, PULSE and the rest cook from the same page.', [co('Same standard, every run.')], f"{M}/roster.png", 1.0),
 ('CONSISTENT', [[wo('Monday or Friday,')],[co('same output.')]], 'No more lottery. The recipe holds whoever runs it and whenever.', [co('Repeatable, not random.')], f"{M}/consistent.png", 1.0),
 ('VERSIONED', [[wo('Fix it once,')],[co('everyone upgrades.')]], 'Improve the recipe and every agent inherits the new version instantly.', [co('Versioned and yours.')], f"{M}/versions.png", 1.0),
 ('THE LOOP', [[wo('Add one recipe')],[co('per new job.')]], 'Each cycle your library grows and your operator only gets sharper.', [co('It compounds.')], f"{M}/loop.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Distill once,',l2='reuse forever.',q='Which job would you turn into a recipe first?')
MARK2="claude"
