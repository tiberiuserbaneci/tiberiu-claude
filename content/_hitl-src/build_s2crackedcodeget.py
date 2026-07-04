#!/usr/bin/env python3
# BE THE CITATION - adaptare topic Catalin "cracked the code to get recommended by the AIs" in
# context Ultron (generat de adapt_build.py). Get cited by ChatGPT/Claude/Gemini/Google.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="BE THE CITATION"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2crackedcodeget"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You still chase Google.')],[co('800M people ask the AI.')]])
T2.CONTENT=[
 ('THE SHIFT', [[wo('They stopped searching.')],[co('They just ask the AI.')]], '800M people ask ChatGPT, Claude and Gemini instead of scrolling. Be the answer they get.', [co('Be the citation.')], f"{M}/answer.png", 1.0),
 ('EVERY MODEL', [[wo('Cited once.')],[co('Recommended everywhere.')]], 'ChatGPT, Claude, Gemini and Google pull from the same sourced web. Win it one time.', [co('One answer, every model.')], f"{M}/constellation.png", 1.0),
 ('THE RADAR', [[wo('It hears your name')],[co('across every model.')]], 'Every mention, every model, tracked. You see where the AI already recommends you.', [co('Mentions, watched nightly.')], f"{M}/radar.png", 1.0),
 ('THE RESEARCH', [[wo('CORTEX maps')],[co('why the AI picks you.')]], 'Category, proof, reviews and docs, wired into one entity the models can quote.', [co('Structured to be cited.')], f"{M}/graph.png", 1.0),
 ('THE CONTENT', [[wo('PULSE writes it')],[co('sourced and quotable.')]], 'Every claim carries a real source and date, written to be lifted straight into an answer.', [co('Built to be quoted.')], f"{M}/stack.png", 1.0),
 ('THE SHARE', [[wo('From invisible')],[co('to the answer.')]], 'Your share of the AI answer, tracked and grown. Cents per brief, not agency retainers.', [co('Cents, not retainers.')], f"{M}/gauge.png", 1.0),
 ('THE REACH', [[wo('One asset,')],[co('every surface.')]], 'AMPLIFY ships the sourced version to every place the models crawl and cite.', [co('Everywhere it gets read.')], f"{M}/field.png", 1.0),
 ('THE OPERATOR', [[wo('Be the answer')],[co('the AI recommends.')]], 'CORTEX, PULSE and AMPLIFY on one memory, every publish held at your gate.', [co('One login, gated, yours.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='become the answer.',q='Which model recommends you first?')
MARK2="claude"
