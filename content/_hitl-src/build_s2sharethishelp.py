#!/usr/bin/env python3
# ZERO TO FIRST DOLLAR - adaptare IG/TikTok in context Ultron (structura copiata din build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2sharethishelp"; LIB=T2.LIB
PREMIUM=1
TITLE="YOUR FIRST DOLLAR"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your first dollar online,')],[co('without a team.')]])
T2.CONTENT=[
 ('THE PATH', [[wo('You do not need')],[co('a big audience.')]], 'Zero to first dollar is a path, not a pile of tips. Six steps, one system.', [co('Start at step zero.')], f"{M}/start.png", 1.0),
 ('THE FUNNEL', [[wo('200 cold leads.')],[co('One first client.')]], 'Leads narrow to replies, replies to calls, calls to your first paid deal.', [co('Every stage, tracked.')], f"{M}/funnel.png", 1.0),
 ('THE LEADS', [[wo('CORTEX finds who')],[co('will actually buy.')]], 'It ranks companies by fit and buying signals, so you skip the tire-kickers.', [co('Ranked, not random.')], f"{M}/leads.png", 1.0),
 ('THE OUTREACH', [[wo('SPECTER writes')],[co('every first message.')]], 'Cold emails and follow-ups in your voice, personalised per lead, sent in sequence.', [co('You just approve.')], f"{M}/outreach.png", 1.0),
 ('THE COST', [[wo('Your whole outreach')],[co('costs cents.')]], 'Pay per token, not per seat. A hundred personalised emails for a few cents.', [co('Cents, not a salary.')], f"{M}/price.png", 1.0),
 ('THE REPLIES', [[wo('Watch the replies')],[co('land overnight.')]], 'Hundreds sent, a handful reply today. Those are your first real conversations.', [co('Warm, while you sleep.')], f"{M}/replies.png", 1.0),
 ('THE SYSTEM', [[wo('One operator wires')],[co('the whole engine.')]], 'CORTEX finds, SPECTER writes, STRIKER books. One memory, one gate: your tap.', [co('No team to hire.')], f"{M}/system.png", 1.0),
 ('THE PAYOFF', [[wo('Day one to')],[co('first dollar.')]], 'A booked call becomes a signed client. The revenue is real, the team is one.', [co('Then you repeat it.')], f"{M}/firstdollar.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the first-dollar path?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='earn your first dollar.',q='What would your first paid client be?')
MARK2="claude"
