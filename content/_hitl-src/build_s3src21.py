#!/usr/bin/env python3
# PROMOTE YOUR CODER - SENTINEL seniority ladder (junior-vague -> senior spec/test/review/ship).
# IG Scraped s3src21 adapted into Ultron context. Panels rendered by s3src21_t3.py.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src21"; LIB=T2.LIB
PREMIUM=1
TITLE="PROMOTE YOUR CODER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('A junior guesses.')],[co('A senior ships.')]])
T2.CONTENT=[
 ('RUNG 01 · THE LADDER', [[wo('Same agent.')],[co('Four levels.')]], 'Junior fires off code from a one-liner. Senior specs, tests and ships. You pick which shows up.', [co('Level it up.')], f"{M}/ladder.png", 1.0),
 ('RUNG 02 · THE SPEC', [[wo('Never code from')],[co('a vague ask.')]], 'Make it write the spec first: acceptance criteria, edge cases, done means done.', [co('Spec, then build.')], f"{M}/spec.png", 1.0),
 ('RUNG 03 · PLAN FIRST', [[wo('It maps the code')],[co('before it moves.')]], 'Plan mode reads your dependencies and proposes the full change. No code written yet.', [co('No rabbit holes.')], f"{M}/plan.png", 1.0),
 ('RUNG 04 · PROJECT MEMORY', [[wo('It never re-learns')],[co('your codebase.')]], 'One rules file, your stack and conventions, loaded every session. It stops guessing your style.', [co('Loaded every time.')], f"{M}/memory.png", 1.0),
 ('RUNG 05 · TESTS', [[wo('It ships green,')],[co('not hopeful.')]], 'It writes the tests, runs them, and hands you zero failing before you ever look.', [co('Zero red first.')], f"{M}/tests.png", 1.0),
 ('RUNG 06 · SELF-REVIEW', [[wo('It reviews itself')],[co('before you do.')]], 'It catches its own edge cases, silent failures and untested paths, then fixes them.', [co('Caught by itself.')], f"{M}/review.png", 1.0),
 ('RUNG 07 · SHIP THE PR', [[wo('Plain English in,')],[co('merged PR out.')]], 'Branch, tests, description, pull request. A senior loop from one line while you are out.', [co('It opens the PR.')], f"{M}/ship.png", 1.0),
 ('RUNG 08 · THE OPERATOR', [[wo('Stop prompting.')],[co('Start speccing.')]], 'SENTINEL is the code agent inside Ultron: spec, plan, test, review, ship, gated by you.', [co('Junior no more.')], f"{M}/versus.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the senior setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and', l2='promote your coder.', q='Which rung is your agent stuck on?')
MARK2="claude"
