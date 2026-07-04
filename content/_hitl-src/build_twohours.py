#!/usr/bin/env python3
# ONE IDEA, TWO HOURS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/twohours"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Idea at 14:00.')],[co('Business live at 16:00.')]])
T2.CONTENT=[
 ('14:00', [[wo('One sentence.')],[co('The idea goes in.')]], 'A service for founders who hate bookkeeping. That was the entire input.', [co('No deck, no plan.')], f"{M}/input.png", 1.0),
 ('14:20', [[wo('The offer')],[co('stands up.')]], 'Positioning, price, guarantee: drafted against the niche, not a template.', [co('Offer before logo.')], f"{M}/offer.png", 1.0),
 ('14:50', [[wo('The page')],[co('goes live.')]], 'Crescendo assembles hero, pricing and FAQ from the pack, in brand tokens.', [co('Preview, tap, live.')], f"{M}/page.png", 1.0),
 ('15:10', [[wo('The content plan')],[co('lands.')]], '14 slots, three hooks per post, queued at 10:00 local.', [co('Distribution included.')], f"{M}/plan.png", 1.0),
 ('15:30', [[wo('The outreach')],[co('waits at the gate.')]], 'Twenty openers, one trigger each, parked for your tap.', [co('Nothing sent alone.')], f"{M}/outreach.png", 1.0),
 ('16:00', [[wo('You review.')],[co('It ships.')]], 'Offer, page, plan, script: two hours, one operator, zero meetings.', [co('Your tap, then live.')], f"{M}/review.png", 1.0),
 ('16:01', [[wo('The excuse')],[co('died here.')]], 'No team, no budget, no time: none of the three survived the afternoon.', [co('Excuses need effort now.')], f"{M}/excuse.png", 1.0),
 ('THE MOAT', [[wo('Speed is the moat.')],[co('The gate keeps it safe.')]], 'Idea to live while others plan. Feedback to fix within the hour.', [co('Move first, gated.')], f"{M}/moat.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this timeline',l2='and pick your idea.',q='What would you build in two hours?')
MARK2="claude"
