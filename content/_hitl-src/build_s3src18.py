#!/usr/bin/env python3
# KEYWORD TO RANK - adaptare IG Scraped (s3src18) in context Ultron. SEO publishing pipeline (PULSE):
# keyword -> brief -> draft -> cluster -> index -> rank -> loop. Narrower than the existing
# "be the citation" material - this is the ranking mechanics, not the citation framing.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src18"; LIB=T2.LIB
PREMIUM=1
TITLE="KEYWORD TO RANK"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Keyword to ranked,')],[co('on autopilot.')]])
T2.CONTENT=[
 ('THE CADENCE', [[wo('One blog a month')],[co('by hand is dead.')]], 'A fresh article every working day, published and indexed the same night.', [co('Daily, forever.')], f"{M}/cadence.png", 1.0),
 ('THE KEYWORDS', [[wo('It mines what')],[co('your buyers search.')]], 'Ranked by search volume and how hard each keyword is to win, not guesswork.', [co('You confirm, it runs.')], f"{M}/keywords.png", 1.0),
 ('THE BRIEF', [[wo('Every article built')],[co('to rank, not ramble.')]], 'Title tag, meta, headings, links and schema, structured before a word is written.', [co('Structured to win.')], f"{M}/brief.png", 1.0),
 ('THE DRAFT', [[wo('Drafted in your voice,')],[co('not a robot tone.')]], 'Sampled from your real pages so every post reads exactly like your brand.', [co('Sounds like you.')], f"{M}/draft.png", 1.0),
 ('THE CLUSTER', [[wo('It weaves the')],[co('internal web for you.')]], 'Each new post links into a topic cluster, so authority compounds across the site.', [co('Authority compounds.')], f"{M}/links.png", 1.0),
 ('THE INDEX', [[wo('Indexed by night,')],[co('climbing by week.')]], 'Submitted to search the same day, then tracked as it moves up the results.', [co('Live, then rising.')], f"{M}/serp.png", 1.0),
 ('THE CLIMB', [[wo('Position 47')],[co('to 3 in ten weeks.')]], 'Real tracking on every target term, so you watch rank move, not vanity traffic.', [co('Rank, not vanity.')], f"{M}/rank.png", 1.0),
 ('THE FLYWHEEL', [[wo('Set it once.')],[co('It compounds forever.')]], 'Research, write, publish, learn: PULSE runs the loop while you run the company.', [co('One setup, endless posts.')], f"{M}/loop.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the pipeline?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and', l2='publish on autopilot.', q='What would daily SEO do for your pipeline?')
MARK2="claude"
