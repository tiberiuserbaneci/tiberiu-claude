#!/usr/bin/env python3
# IT REFUSES TO INVENT - adaptare IG Scraped s3src20 (NotebookLM "skills factory" -> Ultron grounded
# expert, zero hallucination) in context Ultron. Angle: grounded on YOUR vault, citations enforced,
# HUMAN GATE. Generat pe standardul WIRE ITS EYES.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src20"; LIB=T2.LIB
PREMIUM=1
TITLE="IT REFUSES TO INVENT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your AI invents.')],[co('Mine cites its sources.')]])
T2.CONTENT=[
 ('THE PROBLEM', [[wo('It sounded certain.')],[co('It made it up.')]], 'Generic AI answers with total confidence and zero sources behind it.', [co('Confident is not correct.')], f"{M}/liar.png", 1.0),
 ('STEP ONE', [[wo('Feed it your real')],[co('sources, not the web.')]], 'PDFs, calls, docs and past replies land in one private vault.', [co('Your truth, not the internet.')], f"{M}/vault.png", 1.0),
 ('THE BUILD', [[wo('An expert built only')],[co('on what you gave it.')]], 'Every answer is drawn from your vault, nothing lives outside the ring.', [co('Grounded, not guessing.')], f"{M}/grounded.png", 1.0),
 ('THE PROOF', [[wo('Every claim carries')],[co('a source line.')]], 'Click any sentence and it shows the exact document it came from.', [co('Trace every word.')], f"{M}/cite.png", 1.0),
 ('THE GUARDRAIL', [[wo('No source?')],[co('It declines.')]], 'When the vault has no answer it says so, instead of inventing one.', [co('It would rather refuse.')], f"{M}/decline.png", 1.0),
 ('THE RESULT', [[wo('264 answers shipped.')],[co('Zero invented.')]], 'Every reply this week traced back to a real line in your vault.', [co('Zero hallucinations.')], f"{M}/field.png", 1.0),
 ('THE ROSTER', [[wo('One vault,')],[co('seven experts.')]], 'Research, outbound, deals, content and legal all read the same core.', [co('All grounded on you.')], f"{M}/experts.png", 1.0),
 ('HUMAN GATE', [[wo('Cited and ready.')],[co('Still your call.')]], 'Every external move parks in a queue for your tap before it sends.', [co('Approved, never auto.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='ground your AI.',q='What would your AI stop inventing first?')
MARK2="claude"
