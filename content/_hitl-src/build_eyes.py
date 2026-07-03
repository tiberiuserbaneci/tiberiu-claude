#!/usr/bin/env python3
# WIRE ITS EYES - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/eyes"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your AI is blind by default.')],[co('Wire its eyes.')]])
T2.CONTENT=[
 ('THE JAR', [[wo('A brain in a jar')],[co('answers from memory.')]], "Out of the box it cannot see your market, your inbox or this morning's news.", [co('Smart and sightless.')], f"{M}/jar.png", 1.0),
 ('THE EYES', [[wo('Search built for agents,')],[co('not for humans.')]], 'Structured results instead of blue links: the difference between browsing and knowing.', [co('Sight is an install.')], f"{M}/eyes10.png", 1.0),
 ('THE CRAWL', [[wo('Any website becomes')],[co('readable data.')]], 'Competitor pages, pricing changes, job boards: crawled into briefs.', [co('The web is its territory.')], f"{M}/crawl.png", 1.0),
 ('THE WATCH', [[wo('It monitors')],[co('while you operate.')]], 'Rival launches, market moves, mention spikes: watched on triggers, reported in digests.', [co('Eyes that never blink.')], f"{M}/watch.png", 1.0),
 ('THE PROOF10', [[wo('CORTEX reads 1,284')],[co('companies live.')]], "Hiring signals, funding news, stack changes: this morning's web, not last year's training.", [co('Fresh beats trained.')], f"{M}/proof10.png", 1.0),
 ('THE DIFFERENCE', [[wo('Blind AI guesses.')],[co('Sighted AI cites.')]], 'Every claim in every brief carries its source and its date.', [co('Receipts, attached.')], f"{M}/diff10.png", 1.0),
 ('THE SETUP', [[wo('Wired in minutes,')],[co('not weekends.')]], 'The senses come connected on the desk: search, crawl, watch, all gated.', [co('Sight, preinstalled.')], f"{M}/setup10.png", 1.0),
 ('THE BAR10', [[wo('Never trust an answer')],[co('that cannot see today.')]], 'Ask yours what changed in your market this week. Watch it guess.', [co('Run that test now.')], f"{M}/bar10.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the wiring list?')]], "/home/user/tiberiu-claude/content/_hitl-src/models_clay/eyes/cta_builder.png", 0.82)
T2.CLOSE=dict(l1='Save the wiring list',l2='and give yours sight.',q='What is yours still blind to?')
MARK2="claude"
