#!/usr/bin/env python3
# MARKETING AS A COMMAND PALETTE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/twentyplays"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your marketing department')],[co('is now a command palette.')]])
T2.CONTENT=[
 ('THE PALETTE', [[wo('Twenty plays,')],[co('one line each.')]], 'Blog factory, repurpose engine, tone cloning, hook generator: commands, not campaigns.', [co('Marketing became typing.')], f"{M}/palette.png", 1.0),
 ('PLAY /BLOG', [[wo('An SEO post')],[co('in one command.')]], 'Keyword in, structured draft out, in your voice, ranked before review.', [co('The factory floor.')], f"{M}/playblog.png", 1.0),
 ('PLAY /REPURPOSE', [[wo('One article becomes')],[co('eight platforms.')]], 'Posts, tweets, carousel scripts, newsletter: the matrix runs itself.', [co('Nothing dies as one format.')], f"{M}/playrep.png", 1.0),
 ('PLAY /SEQUENCE', [[wo('The funnel emails,')],[co('written to stage.')]], 'Describe the stage; five to seven emails land with CTAs, parked.', [co('The nurture, automated.')], f"{M}/playseq.png", 1.0),
 ('PLAY /AUDIT', [[wo('Competitor content,')],[co('gutted for gaps.')]], 'URLs in, angles and frequencies out, the unclaimed spaces flagged.', [co('Attack maps on demand.')], f"{M}/playaudit.png", 1.0),
 ('PLAY /HEADLINE', [[wo('Ten headlines scored')],[co('before one ships.')]], 'Emotion, clarity, curiosity: graded against the boring rules.', [co('No gut launches.')], f"{M}/playhead.png", 1.0),
 ('THE DIFFERENCE10', [[wo('Tools give you features.')],[co('The palette gives you plays.')]], 'Each command is a whole workflow with your voice and your gate inside.', [co('Plays, not prompts.')], f"{M}/diff10b.png", 1.0),
 ('THE MONDAY', [[wo('The marketing Monday')],[co('runs before coffee.')]], 'Plan, draft, repurpose, audit, queue: five commands, one hour, gated.', [co('The department, typed.')], f"{M}/monday10.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the palette',l2='and run play one.',q='Which play replaces your Monday?')
MARK2="strip"
