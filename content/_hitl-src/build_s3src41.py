#!/usr/bin/env python3
# HAND IT THE KEYS - IG Scraped s3src41 ("10 skills / tools to build a $10M business", a list of
# self-hosted open-source AI agents that actually DO things) adapted to Ultron. The real subject:
# an AI that takes real actions is holding the keys to your business. Give them to one operator
# that picks the model, remembers only what is yours, costs cents, and parks every move for your tap.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src41"; LIB=T2.LIB
PREMIUM=1
TITLE="HAND IT THE KEYS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('An AI that acts')],[co('holds your keys.')]])
T2.CONTENT=[
 ('THE INBOX KEY', [[wo('It sends the sequence.')],[co('It does not suggest it.')]], 'One line becomes a five-touch follow-up, written and delivered for you.', [co('No copy-paste.')], f"{M}/sends.png", 1.0),
 ('THE CALENDAR KEY', [[wo('It books the call')],[co('into your week.')]], 'A yes lands and the meeting is on your calendar before you refresh.', [co('The slot, held.')], f"{M}/books.png", 1.0),
 ('THE STACK KEY', [[wo('It touches your tools.')],[co('All of them.')]], 'Email, CRM, docs, calendar and payments, driven from one plain sentence.', [co('It acts on tools.')], f"{M}/connects.png", 1.0),
 ('THE MODEL KEY', [[wo('It never overpays')],[co('for a thought.')]], 'The router reads each job and picks the cheapest tier that can finish it.', [co('Cents, not dollars.')], f"{M}/budget.png", 1.0),
 ('THE MEMORY KEY', [[wo('It remembers your')],[co('business, not the web.')]], 'ICP, pricing, brand voice and deals live in one private vault it reads first.', [co('Nothing forgets you.')], f"{M}/vault.png", 1.0),
 ('THE PRICE KEY', [[wo('The stack costs thousands.')],[co('This costs cents.')]], 'Ten self-hosted repos and a VPS you babysit, or one operator billed per token.', [co('Pay for work done.')], f"{M}/cents.png", 1.0),
 ('THE SIGNAL KEY', [[wo('It saw the round')],[co('before the press did.')]], 'Funding, hiring, stack and intent on your accounts, watched on triggers.', [co('First to know.')], f"{M}/watch.png", 1.0),
 ('THE LAST KEY', [[wo('It holds every send')],[co('for your tap.')]], 'It can touch anything, but nothing external ships until you approve it.', [co('You stay in control.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the keys?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this before you',l2='self-host a tenth repo.',q='How many keys are you still holding alone?')
MARK2="claude"
