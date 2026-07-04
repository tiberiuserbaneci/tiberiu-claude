#!/usr/bin/env python3
# WHERE DEALS ACTUALLY DIE - the closing half of the funnel (STRIKER deal desk: qualify -> discovery
# -> objections -> proposal -> close plan, human gate at every send). IG Scraped adaptation, Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src50"; LIB=T2.LIB
PREMIUM=1
TITLE="WHERE DEALS ACTUALLY DIE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Booking the meeting')],[co('was the easy part.')]])
T2.CONTENT=[
 ('THE DEAL DESK', [[wo('The pipeline you can')],[co('actually see.')]], 'Every open deal on one board, qualify to close, always live.', [co('One desk, five stages.')], f"{M}/pipeline.png", 1.0),
 ('STAGE 1 QUALIFY', [[wo('It scores the deal')],[co('before you do.')]], 'Budget, authority, need and timeline, ranked so you work the live ones.', [co('No time on dead deals.')], f"{M}/qualify.png", 1.0),
 ('STAGE 2 DISCOVERY', [[wo('It listens on the call')],[co('and structures it.')]], 'The demo becomes ranked pains, an owner each, and the next step.', [co('No lost notes.')], f"{M}/discovery.png", 1.0),
 ('STAGE 3 OBJECTIONS', [[wo('Every no already')],[co('has your yes.')]], 'The objection each deal raises, matched to your best proven answer.', [co('Never caught flat.')], f"{M}/objection.png", 1.0),
 ('STAGE 4 PROPOSAL', [[wo('The proposal')],[co('writes itself.')]], 'Scope, metrics, timeline and terms, pulled straight from discovery.', [co('Minutes, cents to run.')], f"{M}/proposal.png", 1.0),
 ('STAGE 5 CLOSE PLAN', [[wo('A dated path')],[co('to signed.')]], 'A mutual action plan with dates, so the deal never stalls in the dark.', [co('Deals stop slipping.')], f"{M}/closeplan.png", 1.0),
 ('THE HUMAN GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Proposal, quote, contract, each one parks for your approval first.', [co('Still your name on it.')], f"{M}/gate.png", 1.0),
 ('THE CLOSE', [[wo('Signed, logged')],[co('and remembered.')]], 'Signature, terms and the win written back to memory for the next deal.', [co('The desk never forgets.')], f"{M}/close.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the close playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='close the other half.',q='Where do your deals stall today?')
MARK2="claude"
