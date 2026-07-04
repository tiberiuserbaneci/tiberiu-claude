#!/usr/bin/env python3
# THE 60-SECOND BRIEF - adaptare IG Scraped in context Ultron (CORTEX account research).
# Reframe: a GEO "paste a URL -> 5 agents in parallel -> full report in 60s" carousel becomes Ultron's
# CORTEX turning one URL into a ranked, sourced account brief for cents, gated by the operator.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src44"; LIB=T2.LIB
PREMIUM=1
TITLE="THE 60-SECOND BRIEF"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You paste one URL.')],[co('It reads the whole web.')]])
T2.CONTENT=[
 ('THE OLD WAY', [[wo('Two hours per account.')],[co('Then you do it again.')]], 'Twelve tabs, one prospect. An agency charges 10K a month to do it for you.', [co('Hours you do not have.')], f"{M}/manual.png", 1.0),
 ('ONE COMMAND', [[wo('You just paste a URL.')],[co('No brief, no intake.')]], 'One slash command in Ultron. No form, no research VA, no agency call.', [co('Type it, hit send.')], f"{M}/paste.png", 1.0),
 ('FIVE AGENTS', [[wo('One command splits')],[co('into five agents.')]], 'The router reads the job and runs five research agents in parallel.', [co('At once, not in line.')], f"{M}/fanout.png", 1.0),
 ('THE SOURCES', [[wo('The whole web,')],[co('read for you.')]], 'Funding, hiring, stack, reviews, intent - pulled and cross-checked.', [co('Nothing scraped twice.')], f"{M}/sources.png", 1.0),
 ('THE BRIEF', [[wo('A ranked brief,')],[co('not a link dump.')]], 'Top accounts first, each with the one reason they are ready to buy now.', [co('Ranked by fit.')], f"{M}/brief.png", 1.0),
 ('THE RECEIPTS', [[wo('Every line')],[co('carries its source.')]], 'Sourced and dated. Your rep never quotes a hallucination.', [co('Cited, not guessed.')], f"{M}/receipts.png", 1.0),
 ('THE PRICE', [[wo('A full brief')],[co('costs cents.')]], 'Pay per token. Cents per prospect, not a five-figure retainer.', [co('Cents, not thousands.')], f"{M}/cents.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Read the brief, tap approve, then SPECTER writes the opener.', [co('Your call, always.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the brief prompt?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='brief your next account.',q='How long does one account take you today?')
MARK2="claude"
