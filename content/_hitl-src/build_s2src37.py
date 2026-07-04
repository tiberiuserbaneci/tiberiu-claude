#!/usr/bin/env python3
# THE NIGHT SHIFT - adaptare IG/TikTok Scraped in context Ultron (s2src37)
# Reframe of "How I built Claude Code into a Content Machine" -> one overnight Ultron GTM run.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src37"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
TITLE="THE NIGHT SHIFT"; T2.TITLE=TITLE
T2.COVER=dict(head=[[wo('I gave Ultron one instruction')],[co('before bed.')]])
T2.CONTENT=[
 ('THE INSTRUCTION', [[wo('One line')],[co('before bed.')]], 'Plain English, typed once. Ultron runs the whole shift while you sleep.', [co('No dashboards.')], f"{M}/kickoff.png", 1.0),
 ('THE CREW', [[wo('Seven agents')],[co('clocked in.')]], 'CORTEX, SPECTER, PULSE and the rest ran the shift on that one instruction.', [co('You slept through it.')], f"{M}/crew.png", 1.0),
 ('THE RESEARCH', [[wo('It ranked 40 accounts')],[co('by 3 AM.')]], 'CORTEX scored every account on fit, timing and intent, this morning\'s web.', [co('Ranked, not scraped.')], f"{M}/research.png", 1.0),
 ('THE OUTBOUND', [[wo('A full sequence')],[co('written by dawn.')]], 'SPECTER drafted the three-touch outreach, personalised per account.', [co('Ready to send.')], f"{M}/outbound.png", 1.0),
 ('THE PRICE', [[wo('The whole night')],[co('cost 12 cents.')]], 'Pay per token. An agency charges thousands a month to do far less.', [co('Cents, not retainers.')], f"{M}/cost.png", 1.0),
 ('THE CONTENT', [[wo('Three posts drafted')],[co('in your voice.')]], 'PULSE sampled your real posts and wrote the week ahead while you were out.', [co('Sounds like you.')], f"{M}/content.png", 1.0),
 ('THE GATE', [[wo('Nothing sent')],[co('without your tap.')]], 'Every draft parks in a morning queue. One tap approves, one tap kills.', [co('Still your call.')], f"{M}/gate.png", 1.0),
 ('THE MORNING', [[wo('You woke up')],[co('to it done.')]], 'Research ranked, outreach written, posts drafted, all before your coffee.', [co('While you slept.')], f"{M}/summary.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the overnight setup?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and give Ultron',l2='one instruction tonight.',q='What would you wake up to?')
MARK2="claude"
