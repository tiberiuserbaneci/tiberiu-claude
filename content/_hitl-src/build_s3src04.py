#!/usr/bin/env python3
# THE HANDOFF IS THE PRODUCT - adaptare IG Scraped in context Ultron (source: "build a Claude
# 4-agent team that ships"). Angle: you are the copy-paste glue between AI steps; the fix is a
# pipeline of specialists that hand off automatically from one command.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="THE HANDOFF IS THE PRODUCT"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src04"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You are the copy-paste')],[co('between your AI steps.')]])
T2.CONTENT=[
 ('THE BOTTLENECK', [[wo('Four AI steps.')],[co('You are the glue.')]], 'Plan, code, test, review. You copy-paste every baton between them by hand.', [co('You are the bottleneck.')], f"{M}/bottleneck.png", 1.0),
 ('THE PIPELINE', [[wo('The fix is a handoff,')],[co('not another chat.')]], 'Four specialist agents that hand off to each other automatically.', [co('The handoff is the product.')], f"{M}/pipeline.png", 1.0),
 ('THE TRIGGER', [[wo('One command')],[co('kicks it all off.')]], 'You describe the feature in plain English. The pipeline runs itself.', [co('One kick, four hands.')], f"{M}/command.png", 1.0),
 ('AGENT 1 - PLAN', [[wo('It reads the ask,')],[co('drafts the plan.')]], 'The first agent scopes the request and writes the ordered build plan.', [co('No blank page.')], f"{M}/plan.png", 1.0),
 ('AGENT 2 - CODE', [[wo('It writes the')],[co('working build.')]], 'SENTINEL turns the plan into clean, working software.', [co('Plain English in, product out.')], f"{M}/code.png", 1.0),
 ('AGENT 3 - TEST', [[wo('It tests every')],[co('path before you.')]], '48 checks pass, 0 fail. The agent breaks it so you never have to.', [co('Nothing ships untested.')], f"{M}/test.png", 1.0),
 ('AGENT 4 - REVIEW', [[wo('It reviews,')],[co('then waits for you.')]], 'The last agent polishes and approves, then parks for your tap.', [co('Augmented, never unsupervised.')], f"{M}/review.png", 1.0),
 ('DELIVERED', [[wo('You come back')],[co('to a shipped feature.')]], 'No babysitting, no copy-paste between agents, no manual work.', [co('The team ships without you.')], f"{M}/delivered.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the exact setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='let the team ship.',q='Which handoff are you still doing by hand?')
MARK2="claude"
