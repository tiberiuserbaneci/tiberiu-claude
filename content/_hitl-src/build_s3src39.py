#!/usr/bin/env python3
# AN ORG CHART WITH NO GAPS - adaptare IG Scraped (s3src39) in context Ultron. Coverage-completeness
# angle: a real company org, every department box filled by a named Ultron agent, no empty seats.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src39"; LIB=T2.LIB
PREMIUM=1
TITLE="AN ORG CHART WITH NO GAPS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Every function.')],[co('One agent each.')]])
T2.CONTENT=[
 ('THE ORG', [[wo('A real company')],[co('has no empty boxes.')]], 'CEO on top, an agent in every seat below. The whole chart, filled.', [co('Zero empty seats.')], f"{M}/orgtree.png", 1.0),
 ('THE GAP', [[wo('You cover one box.')],[co('Seven sit open.')]], 'The chart most solo founders run: one seat manned, seven functions unmanned.', [co('That gap is your ceiling.')], f"{M}/gaps.png", 1.0),
 ('RESEARCH', [[wo('The research seat,')],[co('ranked overnight.')]], 'CORTEX profiles people, companies and markets into one ranked brief.', [co('Nothing missed by hand.')], f"{M}/research.png", 1.0),
 ('OUTBOUND', [[wo('Outbound that')],[co('follows up itself.')]], 'SPECTER finds the lead, writes the email, works the sequence. You just close.', [co('50 in, 7 booked.')], f"{M}/outbound.png", 1.0),
 ('DEALS', [[wo('Deals worked')],[co('all the way to close.')]], 'STRIKER runs qualify, discovery, objections, proposal and close plan.', [co('One seat, the whole board.')], f"{M}/deals.png", 1.0),
 ('MARKETING', [[wo('One brief,')],[co('every channel.')]], 'PULSE writes in your voice, AMPLIFY schedules per channel and time zone.', [co('Two seats, no calendar.')], f"{M}/marketing.png", 1.0),
 ('LEGAL', [[wo('Contracts read')],[co('and flagged for you.')]], 'COUNSEL drafts and reviews NDAs, MSAs and term sheets, flags the risk.', [co('Fix it before you sign.')], f"{M}/legal.png", 1.0),
 ('COVERAGE', [[wo('Eight functions.')],[co('One login.')]], 'Every seat filled, zero headcount. The ROUTER hires the agent, you hold the gate.', [co('Billed in cents.')], f"{M}/coverage.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the org map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='fill every box.',q='Which seat on your chart is still empty?')
MARK2="claude"
