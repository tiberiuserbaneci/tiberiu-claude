#!/usr/bin/env python3
# INBOXES THAT LAND - cold-email sending infrastructure / deliverability layer (adaptare IG s3src30)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src30"; LIB=T2.LIB
PREMIUM=1
TITLE="INBOXES THAT LAND"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your cold email')],[co('never reached a human.')]])
T2.CONTENT=[
 ('THE SPAM WALL', [[wo('One blast and')],[co('your domain is burned.')]], 'Send cold from your root and every deal reply and invoice lands in spam too.', [co('Never send from your root.')], f"{M}/spam.png", 1.0),
 ('STEP 01 - DOMAINS', [[wo('Spin up domains')],[co('built to be burned.')]], 'Separate sending domains absorb every filter hit so your primary stays clean.', [co('The brand stays untouched.')], f"{M}/burners.png", 1.0),
 ('STEP 02 - MAILBOXES', [[wo('Many inboxes,')],[co('light load on each.')]], 'Four sends per mailbox per day keeps every box under the filter radar.', [co('No inbox over-sends.')], f"{M}/fleet.png", 1.0),
 ('STEP 03 - WARMUP', [[wo('Reputation is earned')],[co('one day at a time.')]], 'Volume ramps slowly for weeks while providers learn to trust each new mailbox.', [co('Trust before volume.')], f"{M}/warmup.png", 1.0),
 ('STEP 04 - ROTATION', [[wo('Sends spread')],[co('across the fleet.')]], 'Every message picks the next box in line, so no single one ever spikes.', [co('Rotate, never spike.')], f"{M}/rotation.png", 1.0),
 ('STEP 05 - AUTH', [[wo('SPF, DKIM, DMARC')],[co('signed and verified.')]], 'The records that prove you are real, set once and checked on every domain.', [co('Proven, not spoofed.')], f"{M}/auth.png", 1.0),
 ('THE PROOF', [[wo('Landed in the inbox,')],[co('not the spam bin.')]], 'Warmed, rotated and signed: 985 of 1,000 sends reached a real inbox.', [co('Inbox, not spam.')], f"{M}/placement.png", 1.0),
 ('THE OPERATOR', [[wo('One agent runs')],[co('the whole sending layer.')]], 'Ultron spins the domains, warms the mailboxes and rotates every send, gated by you.', [co('You approve. It runs.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the setup?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='let the agent send.',q='Whose spam folder is your pipeline sitting in?')
MARK2="claude"
