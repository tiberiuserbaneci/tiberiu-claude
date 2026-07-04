#!/usr/bin/env python3
# THE JOB PICKS THE AGENT - adaptare IG Scraped (hype vs value, best tool per job) in context Ultron.
# Reframe: nu tu alegi tool-ul/modelul; jobul se ruteaza singur la agentul care il detine.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src22"; LIB=T2.LIB
PREMIUM=1
TITLE="THE JOB PICKS THE AGENT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop picking the tool.')],[co('The job picks the agent.')]])
T2.CONTENT=[
 ('THE MAP', [[wo('You pick a tool per job.')],[co('The router picks the agent.')]], 'Seven founder jobs, seven agents, one router that reads the work and assigns it.', [co('You never pick.')], f"{M}/matrix.png", 1.0),
 ('CODE', [[wo('Coding is not a tool.')],[co('It is a shipped PR.')]], 'Describe the fix in plain English. SENTINEL builds it, tests it, ships it.', [co('Tested before you look.')], f"{M}/sentinel.png", 1.0),
 ('RESEARCH', [[wo('Ten tabs, or one')],[co('ranked brief.')]], 'People, companies and markets profiled and scored into a single page.', [co('Ranked, not scattered.')], f"{M}/cortex.png", 1.0),
 ('WRITING', [[wo('It drafts the post.')],[co('In your voice.')]], 'Sampled from your real posts, banned words enforced on every draft.', [co('Your cadence, kept.')], f"{M}/pulse.png", 1.0),
 ('OUTBOUND', [[wo('One persona in.')],[co('A sequence out.')]], 'Cold email, follow-ups and break-up, timed and personalized per contact.', [co('Multi-step, not one blast.')], f"{M}/specter.png", 1.0),
 ('DEALS', [[wo('It qualifies, then')],[co('plans the close.')]], 'Discovery, objection handling, proposal and a close plan per deal.', [co('From lead to won.')], f"{M}/striker.png", 1.0),
 ('PUBLISH', [[wo('Made once, posted')],[co('everywhere on time.')]], 'Each asset reformatted per channel and fired at its best local hour.', [co('Right channel, right hour.')], f"{M}/amplify.png", 1.0),
 ('LEGAL', [[wo('It reads the contract')],[co('and flags the risk.')]], 'Drafts and reviews NDAs, MSAs and term sheets, marks the danger.', [co('Signed with eyes open.')], f"{M}/counsel.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and', l2='let the job route itself.', q='Which job are you still doing by hand?')
MARK2="claude"
