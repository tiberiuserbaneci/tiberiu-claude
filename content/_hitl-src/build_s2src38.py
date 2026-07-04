#!/usr/bin/env python3
# THE COLD-START PLAYBOOK - adaptare IG Scraped ("Ultimate Claude Starter Pack Playbook") in
# context Ultron: o singura campanie de outbound rulata cap-coada de un founder solo, 8 plays.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src38"; LIB=T2.LIB
PREMIUM=1
TITLE="THE COLD-START PLAYBOOK"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('My first sales week,')],[co('run on one login.')]])
T2.CONTENT=[
 ('PLAY 1 / SOURCE', [[wo('847 accounts,')],[co('ranked by fit.')]], 'One brief and it sourced and scored every account that matches your ICP.', [co('Overnight, not weeks.')], f"{M}/sourced.png", 1.0),
 ('PLAY 2 / TIME IT', [[wo('It waits for the')],[co('right trigger.')]], 'Funding, hiring, new tools. It reaches out the day the signal fires.', [co('Timed, not sprayed.')], f"{M}/signal.png", 1.0),
 ('PLAY 3 / WRITE', [[wo('58 words,')],[co('your cadence.')]], 'One specific trigger, a question not a pitch, written in your real voice.', [co('Never a template.')], f"{M}/written.png", 1.0),
 ('PLAY 4 / APPROVE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every message queues for approval. You skim, edit, release the batch.', [co('Augmented, not autopilot.')], f"{M}/gate.png", 1.0),
 ('PLAY 5 / SEND', [[wo('Sent at each')],[co('local 9am.')]], 'Staggered by timezone so every prospect gets it at their own morning.', [co('Right inbox, right hour.')], f"{M}/sent.png", 1.0),
 ('PLAY 6 / FOLLOW UP', [[wo('It chases the')],[co('silent ones.')]], 'A spaced three-step cadence on every no-reply, across the whole week.', [co('You forget. It does not.')], f"{M}/followup.png", 1.0),
 ('PLAY 7 / BOOK', [[wo('7 replies.')],[co('3 calls booked.')]], 'Replies qualified and slotted straight onto your calendar for you.', [co('You just show up.')], f"{M}/booked.png", 1.0),
 ('PLAY 8 / THE BILL', [[wo('The whole week')],[co('cost cents.')]], 'The old stack billed hundreds a month. This ran on pay-per-token cents.', [co('Cents, not seats.')], f"{M}/cents.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run your first week.',q='Which play would you run first?')
MARK2="claude"
