#!/usr/bin/env python3
# THE CENTS DISCIPLINE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/tokendiet"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your AI bill is a habit,')],[co('not a price.')]])
T2.CONTENT=[
 ('THE LEAK', [[wo('The meter does not lie.')],[co('Habits inflate it.')]], 'Same tool, same work: one founder pays cents, another pays multiples.', [co('The difference is discipline.')], f"{M}/leak.png", 1.0),
 ('HABIT 1', [[wo('Clear the context')],[co('between tasks.')]], 'Dragging yesterday into today makes every answer heavier and worse.', [co('Fresh task, fresh slate.')], f"{M}/habit1.png", 1.0),
 ('HABIT 2', [[wo('Right tier,')],[co('right job.')]], 'Light for lookups, standard for daily work, deep only where judgement pays.', [co('The router does this for you.')], f"{M}/habit2.png", 1.0),
 ('HABIT 3', [[wo('Filter the noise')],[co('before it reads.')]], 'Logs, dumps and threads get summarized first, not swallowed whole.', [co('Feed it signal, not bulk.')], f"{M}/habit3.png", 1.0),
 ('HABIT 4', [[wo('Keep the memory files')],[co('short and sharp.')]], 'A lean context file beats a bloated one on both cost and quality.', [co('Trim monthly.')], f"{M}/habit4.png", 1.0),
 ('HABIT 5', [[wo('Batch the small stuff.')],[co('One run, ten items.')]], 'Ten tiny asks cost more than one structured pass.', [co('Bundle, then fire.')], f"{M}/habit5.png", 1.0),
 ('THE AUTOPILOT', [[wo('On the desk,')],[co('the discipline is default.')]], 'The router tiers every turn, contexts reset per task, spend caps sit on every flow.', [co('Cents by design, not effort.')], f"{M}/autopilot.png", 1.0),
 ('THE REFRAME', [[wo('Do not chase cheap.')],[co('Chase clean.')]], 'The habits that cut cost are the same ones that raise quality.', [co('Discipline pays twice.')], f"{M}/reframe8.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save the discipline',l2='before your next session.',q='Which habit is burning yours?')
MARK2="claude"
