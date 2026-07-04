#!/usr/bin/env python3
# ONE SKILL PER GAP - adaptare IG Scraped (s3src13) in context Ultron (generat de adapt_build.py)
# Source hook: "I replaced my $270K creative team with 7 Claude skills". Diverged from the
# content-factory bucket -> each of 7 named skills closes ONE specific gap; $270K = replaced cost.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src13"; LIB=T2.LIB
PREMIUM=1
TITLE="ONE SKILL PER GAP"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One skill')],[co('for every gap.')]])
T2.CONTENT=[
 ('THE GAPS', [[wo('A $270K team')],[co('was five gaps.')]], 'Copywriter, researcher, editor, video, VA. Five hires, five holes to fill.', [co('Now cents a brief.')], f"{M}/gaps.png", 1.0),
 ('THE VOICE', [[wo('It writes like you,')],[co('not a stranger.')]], 'Extracts your cadence and vocabulary, then bans the words you never use.', [co('98% style match.')], f"{M}/voice.png", 1.0),
 ('THE RESEARCH', [[wo('One brief in,')],[co('31 sources out.')]], 'An autonomous agent fans a question into market, rivals and reviews on its own.', [co('Runs while you step away.')], f"{M}/research.png", 1.0),
 ('THE MEMORY', [[wo('A Claude that')],[co('remembers you.')]], 'ICP, pricing, past drafts, brand voice. One core every skill pulls from.', [co('Nothing starts from zero.')], f"{M}/memory.png", 1.0),
 ('THE AUDIO', [[wo('Any doc becomes')],[co('a narrated episode.')]], 'Turns a memo into narrated audio or a podcast. No mic, no booking, no editor.', [co('Brief in, voice out.')], f"{M}/audio.png", 1.0),
 ('THE VIDEO', [[wo('Video with')],[co('no editor.')]], 'Scenes described in text, composed into finished video by code, not a timeline.', [co('Rendered, not clicked.')], f"{M}/video.png", 1.0),
 ('THE WRITER', [[wo('Research to draft,')],[co('end to end.')]], 'One chain: research feeds the outline, the outline feeds a draft in your voice.', [co('Draft ready, your style.')], f"{M}/writer.png", 1.0),
 ('THE INTEL', [[wo('Their ads,')],[co('on your desk.')]], 'Scans rival ad libraries live and pulls the angle they are running right now.', [co('The market, watched.')], f"{M}/ads.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the 7 skills?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='close every gap.',q='Which gap would you close first?')
MARK2="claude"
