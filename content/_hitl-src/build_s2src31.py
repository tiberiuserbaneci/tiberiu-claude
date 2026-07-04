#!/usr/bin/env python3
# THE 5AM SHIFT - adaptare IG Scraped (Claude Code Templates / Agent Teams) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="THE 5AM SHIFT"
T2.TITLE=TITLE
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src31"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You slept.')],[co('Your pipeline did not.')]])
T2.CONTENT=[
 ('THE SCHEDULE', [[wo('One line schedules')],[co('the whole team.')]], 'Set it once. At 5AM your seven agents wake, run, and report before coffee.', [co('Set once. Runs nightly.')], f"{M}/clock.png", 1.0),
 ('THE BRIEF', [[wo('It read 900 accounts')],[co('while you slept.')]], 'CORTEX scans funding, hiring and stack changes, then ranks the ones that moved.', [co('Nine movers by 6AM.')], f"{M}/brief.png", 1.0),
 ('THE OUTBOUND', [[wo('Cold emails, drafted')],[co('and sequenced.')]], 'SPECTER writes the opener and two follow-ups for every account CORTEX flagged.', [co('Waiting in drafts.')], f"{M}/reach.png", 1.0),
 ('THE DEALS', [[wo('It qualified the')],[co('inbound overnight.')]], 'STRIKER scores each lead, writes discovery notes, and drafts the objection replies.', [co('Only the real ones.')], f"{M}/deals.png", 1.0),
 ('THE CONTENT', [[wo('One idea became')],[co('a week of posts.')]], 'PULSE writes in your voice, then AMPLIFY formats each post for its channel.', [co('Your voice, multiplied.')], f"{M}/draft.png", 1.0),
 ('THE SHIP', [[wo('Built, tested,')],[co('PR opened.')]], 'SENTINEL turns plain English into a landing page, tests it, and opens the pull request.', [co('Shipped before dawn.')], f"{M}/ship.png", 1.0),
 ('THE COST', [[wo('The whole night')],[co('cost you cents.')]], 'Pay per token. The router picks the cheapest tier that can actually do each job.', [co('Cents, not seats.')], f"{M}/cents.png", 1.0),
 ('THE WAKE', [[wo('You wake to a')],[co('queue, not a mess.')]], 'Nothing sent, nothing shipped. Every move parks at the gate for one tap from you.', [co('Your tap sends it.')], f"{M}/wake.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the schedule?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='let it run tonight.',q='What would your team finish by 5AM?')
MARK2="claude"
