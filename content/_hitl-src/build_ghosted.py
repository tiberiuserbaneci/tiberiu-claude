#!/usr/bin/env python3
# WHY COLD EMAILS DIE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/ghosted"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Nobody reads your cold emails.')],[co('Nobody even gets them.')]])
T2.CONTENT=[
 ('THE PATTERN', [[wo('Same writer.')],[co('Opposite results.')]], 'Some campaigns crushed. Others went to spam without a trace. Copy was never the variable.', [co('The infra was.')], f"{M}/sent.png", 1.0),
 ('MISTAKE 1', [[wo('You count opens.')],[co('Buyers count replies.')]], 'Tracking pixels hurt placement and measure vanity. Kill them.', [co('Replies or nothing.')], f"{M}/opens.png", 1.0),
 ('MISTAKE 2', [[wo('Fresh domain,')],[co('full blast.')]], 'No reputation plus max volume equals the promotions folder, forever.', [co('Reputation is earned.')], f"{M}/fresh.png", 1.0),
 ('MISTAKE 3', [[wo('One domain carries')],[co('your whole pipeline.')]], 'One bad batch burns the only asset you have. Spread the load.', [co('Four domains minimum.')], f"{M}/onedomain.png", 1.0),
 ('MISTAKE 4', [[wo('Volume spikes')],[co('kill overnight.')]], '60 then 60 then 60 beats 0 then 500. Ramps live, blasts die.', [co('Boring wins inboxes.')], f"{M}/spike.png", 1.0),
 ('MISTAKE 5', [[wo('Catch-all lists')],[co('drag everyone down.')]], 'Unverified addresses poison the batch for the verified ones.', [co('Verify or pay.')], f"{M}/catchall.png", 1.0),
 ('ULTRON', [[wo('The infra runs')],[co('by default.')]], 'Warm domains, ramped sends, watched spam rates. You never think about it.', [co('99.2% inboxed.')], f"{M}/infra.png", 1.0),
 ('THE LESSON', [[wo('Fix the road,')],[co('then the car.')]], 'Great copy on dead infra is a love letter in a locked mailbox.', [co('Infra first, always.')], f"{M}/road.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the 5 mistakes',l2='before your next batch.',q='Which one is killing you?')
MARK2="claude"
