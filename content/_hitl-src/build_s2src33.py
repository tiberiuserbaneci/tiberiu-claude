#!/usr/bin/env python3
# COLD LIST, WARM REPLY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
# Source: "Top 100 Claude Code Tips" (Lead Gen & Outbound). Reframed: one outbound sequence,
# traced end to end, run by SPECTER at cents, gated by you.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src33"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
TITLE="COLD LIST, WARM REPLY"
T2.COVER=dict(head=[[wo('I gave it a cold list.')],[co('It handed back meetings.')]])
T2.CONTENT=[
 ('THE LIST', [[wo('2,000 names.')],[co('Most are dead weight.')]], 'It reads the whole list and keeps only the few worth a first line.', [co('Noise in, targets out.')], f"{M}/leadlist.png", 1.0),
 ('THE BRIEF', [[wo('One name,')],[co('fully known.')]], 'Funding, hiring, stack, intent. A raw name becomes a ranked brief.', [co('It does the homework.')], f"{M}/dossier.png", 1.0),
 ('THE DRAFT', [[wo('Written for one human,')],[co('not a template blast.')]], 'Every email opens on a real trigger the prospect actually cares about.', [co('Personal at scale.')], f"{M}/draft.png", 1.0),
 ('THE SEQUENCE', [[wo('One send is')],[co('a coin flip.')]], 'A four-touch cadence over twelve days. The replies live in the follow-ups.', [co('It never forgets to nudge.')], f"{M}/cadence.png", 1.0),
 ('THE COST', [[wo('The old stack')],[co('cost a salary.')]], 'Sending tools billed monthly. This bills in cents, per lead, per token.', [co('Cents, not subscriptions.')], f"{M}/cents.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Forty-two drafts sit ready and parked. One approval and the batch goes.', [co('Still your reputation.')], f"{M}/gate.png", 1.0),
 ('THE REPLIES', [[wo('You wake')],[co('to replies.')]], 'Sent while you slept, answered before your coffee. Booked, replied, passed.', [co('Overnight, every night.')], f"{M}/replies.png", 1.0),
 ('THE CALENDAR', [[wo('Cold Monday.')],[co('Full Friday.')]], 'A cold list turned into seven calls on the calendar, run overnight.', [co('The whole motion, one agent.')], f"{M}/calendar.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the outbound play?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and turn',l2='your list into calls.',q='How many names are dead weight in your list right now?')
MARK2="claude"
