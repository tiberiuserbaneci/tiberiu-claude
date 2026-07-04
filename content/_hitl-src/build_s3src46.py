#!/usr/bin/env python3
# THE UNBUILT WEDGES - adaptare IG Scraped (s3src46, "10 AI startups that don't exist yet") in context Ultron.
# Fresh angle: concrete under-built AI-agent companies + the wedge to win each, all buildable solo on Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src46"; LIB=T2.LIB
PREMIUM=1
TITLE="THE UNBUILT WEDGES"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Companies nobody built yet.')],[co('And the wedge to win each.')]])
T2.CONTENT=[
 ('THE SURFACE', [[wo('The boring jobs')],[co('are unclaimed.')]], 'Every dull, repeated workflow is a company nobody has bothered to ship.', [co('Pick one and build it.')], f"{M}/surface.png", 1.0),
 ('THE TAX FILER', [[wo('Taxes that')],[co('file themselves.')]], 'It pulls your documents, finds every deduction and files the return end to end.', [co('Done, not help.')], f"{M}/taxfiler.png", 1.0),
 ('THE RISK POOL', [[wo('Insurance for')],[co('when AI slips.')]], 'A wrong refund, a rogue email, a bad payment. This is the policy that covers it.', [co('Every AI company, a customer.')], f"{M}/riskpool.png", 1.0),
 ('THE COLLECTOR', [[wo('Collections that')],[co('actually collect.')]], 'It chases 412 overdue invoices on a schedule and recovers the cash owed.', [co('Paid on what it recovers.')], f"{M}/collector.png", 1.0),
 ('THE SOURCER', [[wo('Sourced, screened,')],[co('and booked.')]], 'It finds the candidates, scores the match and puts the call on your calendar.', [co('Kill the recruiter retainer.')], f"{M}/sourcer.png", 1.0),
 ('THE NEGOTIATOR', [[wo('It renews your')],[co('software cheaper.')]], 'It reads every contract and trims the bill, saving 890 dollars a month.', [co('Pays for itself, renewal one.')], f"{M}/negotiator.png", 1.0),
 ('THE FRONT DESK', [[wo('It answers the')],[co('call you miss.')]], 'The receptionist for every trade that still sends after-hours calls to voicemail.', [co('Always on, never a missed lead.')], f"{M}/frontdesk.png", 1.0),
 ('THE ECONOMICS', [[wo('Any of these')],[co('runs on cents.')]], 'Pay per token, price on the outcome. The whole company runs for the price of a coffee.', [co('The spread is the business.')], f"{M}/economics.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build map?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Stop reading the list.',l2='Build the boring one.',q='Which wedge would you ship first?')
MARK2="claude"
